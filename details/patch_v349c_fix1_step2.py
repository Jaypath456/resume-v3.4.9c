"""v3.4.9c fix1, step 2 (evidence matching only), applied on top of patch_v349c_fix1.py.
- The cited evidence is the proof sentence and, for a project proof, its evidence item's text and claim atoms; for an
  Experience proof, the Experience bullets that proof names. Job titles, employer names, evidence-anchor notes, tags and
  keyword labels are not evidence.
- A responsibility word matches only a whole evidence word with the same base form (plural / -ing / -ed / final -e
  removed): "internal" no longer matches "interviewed". Compounds match as the whole term (or a listed spelling), else
  every specific part of 4+ letters as a whole word."""
import sys, pathlib
P = pathlib.Path(sys.argv[1]); s = P.read_text(encoding="utf-8")
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:100], s.count(a)); s = s.replace(a, b)

old_corpus = s[s.index("def v349c_proof_corpus(key: str, master: dict[str, Any]) -> str:"):s.index("def v349c_closing_unsupported(")]
rep(old_corpus, '''def v349c_proof_corpus(key: str, master: dict[str, Any]) -> str:
    """The evidence a closing proof cites (lower case). fix1: the proof sentence; for a project proof, its evidence item's
    text and claim atoms; for an Experience proof, the Experience bullets the proof names. Job titles, employer names,
    evidence-anchor notes, tags and keyword labels are not evidence."""
    proofs = (master.get("cover_letter_bank") or {}).get("closing_proofs") or {}
    parts = [str(proofs.get(key, ""))]
    if key.startswith("exp."):
        rx = V349_EXP_PROOF.get(key)
        for r in master.get("experience") or []:
            parts += [str(b) for b in r.get("bullets") or [] if rx and re.search(rx, str(b))]
    else:
        p = (master.get("projects") or {}).get(V349C_PROOF_PROJECT.get(key.split(".")[0], ""), {})
        e = (p.get("evidence_items") or {}).get(v349_proof_eid(key), {})
        parts += [str(e.get("text", ""))] + [str(x) for x in list(e.get("claim_atoms") or [])]
    cor = " ".join(parts)
    for r in master.get("experience") or []:   # employer names are not evidence ("Thesis Mumbai Tech" is not "tech")
        org = re.sub(r"\\s*\\(.*?\\)", "", str(r.get("organization", ""))).strip()
        if org:
            cor = cor.replace(org, " ")
    return cor.lower()


''')

_w0 = s.index("def v349c_word_in(w: str, cor: str) -> bool:")
old_word = s[_w0:s.index("def v349c_family_unsupported(", _w0)]
rep(old_word, '''def v349c_lemma(w: str) -> str:
    """Base form for whole-word matching: plural, -ing, -ed and a final -e removed ("automated" = "automate")."""
    w = w.lower().strip("'’")
    w = w[:-2] if w.endswith(("'s", "’s")) else w
    for suf, sub in (("ies", "y"), ("sses", "ss"), ("xes", "x"), ("ches", "ch"), ("shes", "sh"), ("s", "")):
        if w.endswith(suf) and not (suf == "s" and w.endswith(("ss", "us", "sis"))) and len(w) - len(suf) >= 3:
            w = w[:-len(suf)] + sub
            break
    for suf in ("ing", "ed"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[:-len(suf)]
            if len(w) > 3 and w[-1] == w[-2] and w[-1] not in "aeiousl":
                w = w[:-1]
            if w.endswith("i"):
                w = w[:-1] + "y"
            break
    return w[:-1] if w.endswith("e") and len(w) > 3 else w


def v349c_corpus_words(cor: str) -> set[str]:
    return {v349c_lemma(t) for t in re.findall(r"[a-z0-9][a-z0-9+#]*(?:-[a-z0-9+#]+)*", cor)}


def v349c_word_in(w: str, cor: str) -> bool:
    """A responsibility word is in the cited evidence as a whole word with the same base form ("APIs" = "API";
    "internal" is not "interviewed"), as one of the listed spellings, or, for a compound, as the whole term ("low-level")
    or with every specific part of 4+ letters ("customer-facing" needs "customer")."""
    words = v349c_corpus_words(cor)
    has = lambda t: re.search(r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])", cor) is not None
    if w in V349C_EQUIV:
        return any(has(e) for e in V349C_EQUIV[w])
    if "-" in w or "/" in w:
        if any(has(v) for v in (w, w.replace("-", " "), w.replace("-", ""))):
            return True
        parts = [p for p in re.split(r"[-/]", w) if p and p not in V349C_GENERIC and p not in V349C_COMPOUND_TAIL]
        return bool(parts) and all(len(p) >= 4 and v349c_lemma(p) in words for p in parts)
    return v349c_lemma(w) in words


''')

old_map = s[s.index("def v349c_support_map(c: str, eid: str, kind: str, master: dict[str, Any]) -> dict[str, str]:"):s.index("def v349c_grounded_closing(")]
rep(old_map, '''def v349c_support_map(c: str, eid: str, kind: str, master: dict[str, Any]) -> dict[str, str]:
    """For the report: each specific word of the responsibility and the evidence words that show it (whole words)."""
    cor = v349c_proof_corpus(eid, master)
    toks = re.findall(r"[a-z0-9][a-z0-9+#]*(?:-[a-z0-9+#]+)*", cor)
    out = {}
    for mm in re.finditer(r"[A-Za-z][A-Za-z0-9+#/-]*", c):
        w = mm.group(0).lower().strip("-/")
        if w in V349C_GENERIC or len(w) < 2:
            continue
        parts = [w] if not ("-" in w or "/" in w) else [p for p in re.split(r"[-/]", w) if p and p not in V349C_GENERIC and p not in V349C_COMPOUND_TAIL]
        hits = [t for p in parts for t in toks if v349c_lemma(t) == v349c_lemma(p) or t == w]
        out[w] = ", ".join(dict.fromkeys(hits)) if hits else ("spelling: " + "/".join(V349C_EQUIV.get(w, ())) if w in V349C_EQUIV else "whole term")
    return out


''')
s = s.replace("# proof evidence shows every specific word (v349c_closing_unsupported),", "# cited evidence shows every specific word as a whole word (v349c_closing_unsupported, v349c_word_in),", 1)
P.write_text(s, encoding="utf-8"); print("ok")
# role-family quality adjectives: one list for the selector and the claim check ("dependable" like "careful")
s = P.read_text(encoding="utf-8")
a = 'V349C_FAMILY_QUALITY = {"apply", "careful", "trustworthy", "grow", "they"}'
assert s.count(a) == 1
s = s.replace(a, 'V349C_FAMILY_QUALITY = {"apply", "careful", "trustworthy", "grow", "they", "dependable"}   # fix1: "dependable" is a quality, as the selector reads it')
P.write_text(s, encoding="utf-8"); print("ok 2")
