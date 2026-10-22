"""v3.4.9c fix1 (targeted repair) on the v3.4.9c release pipeline.
Fix 1 (closing_v349c): the grounded closing searches every on-page proof for each posting responsibility (the release
checked only the one proof the v3.4.4 picker offered), splits coordinated responsibilities ("implement X and review Y"),
matches plurals / front-end / back-end / full-stack spellings, refuses vague fragments, and gives a role-family closing a
supporting on-page proof when one exists. Every specific word must still appear in the cited proof's own evidence.
Fix 2 (closing_v349c / letters_plain_v349c): the letter kept in the plan for every page decision is the run 6 letter
(composed with closing_v349c off); the grounded closing is chosen only for the written letter."""
import sys, pathlib
P = pathlib.Path(sys.argv[1]); s = P.read_text(encoding="utf-8")
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:100], s.count(a)); s = s.replace(a, b)

# --- matching: plurals, spellings, compounds (helper used only with closing_v349c on) -------------------------------
rep('''    cor = v349c_proof_corpus(key, master)
    out = []
    for mm in re.finditer(r"[A-Za-z][A-Za-z0-9+#/-]*", resp):
        w = mm.group(0).lower().strip("-/")
        if w in V349C_GENERIC or len(w) < 2 or any(i in covered for i in range(mm.start(), mm.end())):
            continue
        stem = w[:5] if len(w) > 5 else w
        if not re.search(r"(?<![a-z])" + re.escape(stem), cor):
            out.append(w)
    return out
''', '''    cor = v349c_proof_corpus(key, master)
    out = []
    for mm in re.finditer(r"[A-Za-z][A-Za-z0-9+#/-]*", resp):
        w = mm.group(0).lower().strip("-/")
        if w in V349C_GENERIC or len(w) < 2 or any(i in covered for i in range(mm.start(), mm.end())):
            continue
        if not v349c_word_in(w, cor):   # v3.4.9c fix1: plurals, front-end / back-end / full-stack spellings, compounds
            out.append(w)
    return out


V349C_EQUIV = {"frontend": ("front end", "front-end", "frontend"), "front-end": ("front end", "front-end", "frontend"),
               "backend": ("back end", "back-end", "backend"), "back-end": ("back end", "back-end", "backend"),
               "full-stack": ("full stack", "full-stack", "fullstack"), "fullstack": ("full stack", "full-stack", "fullstack")}   # spellings only
V349C_COMPOUND_TAIL = {"powered", "based", "driven", "facing", "level", "grade", "ready", "oriented"}


def v349c_word_in(w: str, cor: str) -> bool:
    """A responsibility word is in the proof's evidence: the same word or its singular ("APIs" -> "API"), one of the
    listed spellings, or, for a compound, the whole term or each specific part of 4+ letters ("customer-facing")."""
    if w in V349C_EQUIV:
        return any(e in cor for e in V349C_EQUIV[w])
    if "-" in w or "/" in w:   # the whole term ("low-level", "ai-powered"), else every specific part of 4+ letters
        if any(v in cor for v in (w, w.replace("-", " "), w.replace("-", ""))):
            return True
        parts = [p for p in re.split(r"[-/]", w) if p and p not in V349C_GENERIC and p not in V349C_COMPOUND_TAIL]
        return bool(parts) and all(len(p) >= 4 for p in parts) and all(v349c_word_in(p, cor) for p in parts)
    n = w[:-3] + "y" if w.endswith("ies") and len(w) > 4 else (w[:-1] if w.endswith("s") and not w.endswith("ss") and len(w) > 3 else w)
    stem = n[:5] if len(n) > 5 else n
    return bool(re.search(r"(?<![a-z])" + re.escape(stem), cor))
''')

# --- the grounded selector -----------------------------------------------------------------------------------------
block = r'''# ===========================================================================
# v3.4.9c fix1 (2026-10-23): targeted repair. Fix 1, closing_v349c: v349c_grounded_closing tries every posting
# responsibility (and the two halves of a coordinated one) against every on-page proof; it keeps the first pair whose
# proof evidence shows every specific word (v349c_closing_unsupported), whose wording is a real responsibility
# (v349c_meaningful) and whose proof does not repeat the letter. Otherwise the role-family closing, with an on-page proof
# that shows the family claim when one exists. Fix 2: compose_bank_cover_letter keeps the run 6 letter (closing_v349c
# off) in the plan for page decisions; the grounded closing goes only into the written letter.
# ===========================================================================
V349C_VAGUE = {"best", "results", "great", "amazing", "awesome", "impactful", "innovative", "cutting-edge", "breakthrough", "world-class",
               "excellent", "exceptional", "outstanding", "expected", "things", "stuff", "life", "needs", "value", "success", "goals",
               "impact", "mission", "vision", "ideas", "opportunities", "initiatives", "efforts", "part", "takes", "difference", "future",
               "excellence", "passion", "growth", "career", "journey", "culture", "environment", "fun", "others", "everything",
               "anything", "something", "responsibilities", "tasks", "duties", "assignments", "custom", "tailored", "key", "various",
               "modern", "latest", "next-generation", "state-of-the-art", "transformational", "meaningful", "exciting"}
V349C_AUX = {"are", "is", "be", "was", "were", "will", "can", "should", "must", "may", "been", "being"}


def v349c_meaningful(c: str) -> bool:
    """A real responsibility, not a vague fragment: at least one specific content word after the leading verbs (not
    generic, not vague), no auxiliary verb straight after them ("engineer are expected") and no question word ("build
    or integrate, how")."""
    words = [w.lower().strip("-/") for w in re.findall(r"[A-Za-z][A-Za-z0-9+#/-]*", c)]
    if any(w in ("how", "what", "why", "whatever", "whether") for w in words):
        return False
    toks = c.split()
    i = 0
    while i < len(toks) and (_v344_base_verb(toks[i]) or toks[i].lower().rstrip(",") in ("and", "or", "help")):
        i += 1
    if i < len(toks) and toks[i].lower().rstrip(",") in V349C_AUX:
        return False
    spec = [p for w in words[i:] for p in re.split(r"[-/]", w)
            if p and p not in V349C_GENERIC and p not in V349C_VAGUE and p not in _V344_STOP and p not in V349C_COMPOUND_TAIL and len(p) >= 3]
    return bool(spec)


def v349c_splits(c: str) -> list[tuple[str, bool]]:
    """The responsibility and, for "X and <verb> Y", each half that is a responsibility of its own ((text, is_head))."""
    out = [(c, False)]
    for mm in re.finditer(r",? and ", c):
        head, tail = c[:mm.start()].strip().rstrip(","), c[mm.end():].strip()
        if tail.split() and _v344_base_verb(tail.split()[0]):
            if len(head.split()) >= 3:
                out.append((head, True))
            if len(tail.split()) >= 3:
                out.append((tail, False))
    return list(dict.fromkeys(out))


def v349c_kind_of(c: str, eid: str) -> str:
    return next((k for k, rx, eids in _V344_KINDS if eid in eids and rx.search(c)), "")


def v349c_closing_pool(plan: dict[str, Any], master: dict[str, Any], body: str, plain: bool) -> list[str]:
    """On-page proofs: every project on the page (plain letters) or the projects the letter names, and Experience."""
    pool = _v344_proof_pool(plan, master, "" if plain else body)
    if _v347_on("proof_on_page_v349"):
        on_page = v349_page_evidence(plan, master)
        pool = [e for e in pool if v349_proof_eid(e) in on_page]
    return pool


def v349c_support_map(c: str, eid: str, kind: str, master: dict[str, Any]) -> dict[str, str]:
    """For the report: each specific word of the responsibility and the evidence text that shows it."""
    cor = v349c_proof_corpus(eid, master)
    rx = next((x[1] for x in _V344_KINDS if x[0] == kind), None)
    out = {}
    for mm in re.finditer(r"[A-Za-z][A-Za-z0-9+#/-]*", c):
        w = mm.group(0).lower().strip("-/")
        if w in V349C_GENERIC or len(w) < 2:
            continue
        if rx is not None and rx.search(mm.group(0)):
            out[w] = f"proof kind {kind}"
            continue
        n = w.split("-")[0] if "-" in w else w
        n = n[:-1] if n.endswith("s") and not n.endswith("ss") and len(n) > 3 else n
        hit = re.search(r"(?<![a-z])" + re.escape(n[:5] if len(n) > 5 else n), cor)
        out[w] = cor[max(0, hit.start() - 30):hit.end() + 40].strip() if hit else "(spelling list)"
    return out


def v349c_grounded_closing(plan: dict[str, Any], master: dict[str, Any], raw_jd: str, company_ref: str, body: str, budget: int = 30,
                           plain: bool = False, accept=None, exclude: set[str] | None = None) -> tuple[str, dict[str, Any]]:
    bank = master.get("cover_letter_bank", {})
    proofs = bank.get("closing_proofs", {})
    ptext = (lambda k: (bank.get("plain_v349c") or {}).get("proofs", {}).get(k, "")) if plain else (lambda k: str(proofs.get(k, "") or ""))
    where = _v344_where(company_ref)
    low = str(body).lower()
    pool = v349c_closing_pool(plan, master, body, plain)
    co = company_ref if where.startswith("at ") else ""
    tried, seen = 0, set()
    for resp, line in closing_candidates(raw_jd, plan, master, body):
        for cut in _v344_cuts(resp):
            for c, head in v349c_splits(cut):
                if c in seen or (exclude and c in exclude):
                    continue
                seen.add(c)
                if not _v344_resp_ok(c, plan, master, low) or (not head and not _v345_clause_end_ok(c, line)) or not v349c_meaningful(c):
                    continue
                if plain and v349c_resp_plain(c, master):
                    continue
                tried += 1
                order = [e for k in _v344_kind_order(c) for e in k[2]] + pool
                for eid in dict.fromkeys(e for e in order if e in pool):
                    pt = ptext(eid)
                    if not pt:
                        continue
                    kind = v349c_kind_of(c, eid)
                    if v349c_closing_unsupported(c, eid, "", master):   # every specific word in the proof's own evidence (no kind shortcut)
                        continue
                    conn = _v344_connector(c, company_ref, pt)
                    sent = _v343_fix_dots(f"I want to {c} {where}, {conn} {pt}.")
                    if len(sent.split()) > min(budget, 30) or closing_problems(sent, co) or (accept is None and closing_repeats_letter(pt, body)):
                        continue   # with accept (plain letters) the repeat check runs on the written letter, not on body
                    info = {"rule": "v3.4.9c fix1", "responsibility": c, "jd_line": line, "proof": eid, "proof_kind": kind, "_proof": pt, "connector": conn,
                            "closing_v349c": {"selector": "every on-page proof", "candidates_tried": tried, "evidence": v349c_support_map(c, eid, "", master)}}
                    if accept is None or accept(sent, info):
                        return sent, info
    # no supported specific closing: the role-family closing, with an on-page proof that shows its claim when one exists
    fam = str(plan.get("role_family", ""))
    fc = bank.get("family_closing", {})
    tmpl = fc.get(fam, "build dependable, well-tested software with the team at {company}")
    if v349c_claim_in_master(re.sub(r"\s+", " ", tmpl.replace("{company}'s", " ").replace("{company}", " ")), master):
        tmpl = fc.get("general_swe", "build dependable, well-tested software with the team at {company}")
    poss = company_ref + ("'" if company_ref.endswith("s") else "'s")
    what = tmpl.replace("{company}'s", poss).replace("{company}", company_ref)
    if company_ref in ("your team", "your client"):
        what = what.replace("with the team at your team", "with your team").replace("at your client", "for your client")
    general = fc.get("general_swe", "build dependable, well-tested software with the team at {company}")
    for tm in dict.fromkeys((tmpl, general)):   # the family's claim, then the general claim, each only with a proof that shows it
        wh = tm.replace("{company}'s", poss).replace("{company}", company_ref)
        if company_ref in ("your team", "your client"):
            wh = wh.replace("with the team at your team", "with your team").replace("at your client", "for your client")
        claim = re.sub(r"\s+", " ", tm.replace("{company}'s", " ").replace("{company}", " ")).strip()
        order = [e for k in _v344_kind_order(claim) for e in k[2]] + pool
        for eid in dict.fromkeys(e for e in order if e in pool):
            pt = ptext(eid)
            kind = v349c_kind_of(claim, eid)
            bad = [w for w in v349c_closing_unsupported(re.sub(r"(?i)\bmachine learning\b", "ML", claim), eid, "", master) if w not in V349C_FAMILY_QUALITY | {"dependable"}]
            if not pt or bad:
                continue
            conn = _v344_connector(wh, company_ref, pt)
            sent = _v343_fix_dots(f"I want to {wh}, {conn} {pt}.")
            if len(sent.split()) > min(budget, 30) or closing_problems(sent, co) or (accept is None and closing_repeats_letter(pt, body)):
                continue
            info = {"rule": "v3.4.9c fix1", "responsibility": "", "proof": eid, "proof_kind": kind, "_proof": pt, "connector": conn, "family": True,
                    "closing_v349c": {"selector": "role-family (no supported responsibility)" + ("" if tm == tmpl else ", general claim"), "candidates_tried": tried,
                                      "evidence": v349c_support_map(claim, eid, "", master)}}
            if accept is None or accept(sent, info):
                return sent, info
    sent = _v343_fix_dots(f"I want to {what}.")
    return sent, {"rule": "v3.4.9c fix1", "responsibility": "", "proof": "", "proof_kind": "", "_proof": "", "connector": _v344_connector(what, company_ref),
                  "family": True, "closing_v349c": {"selector": "role-family, no proof shows its claim", "candidates_tried": tried}}


'''
anchor = 'V349B_FLAGS = ("bank_format_v349b"'
rep(anchor, block + anchor)

# --- the run 7 wrapper uses the grounded selector (written run 7 letters, letters_plain_v349c off) -------------------
a = s[s.index('''    if _v347_on(V349C_CLOSING_FLAG) and not V349C_CTX.get("closing_inner"):   # v3.4.9c run 7: grounded responsibility'''):
      s.index('''    if _v347_on("proof_on_page_v349") and V349_CTX.get("sib") is None:   # v3.4.9a fix 7b''')]
rep(a, '''    if _v347_on(V349C_CLOSING_FLAG) and not V349C_CTX.get("closing_inner"):   # v3.4.9c run 7 / fix1: grounded responsibility
        V349C_CTX["closing_inner"] = True
        try:
            return v349c_grounded_closing(plan, master, raw_jd, company_ref, body, budget, plain=False, exclude=set(exclude_resp or ()))
        finally:
            V349C_CTX["closing_inner"] = False
''')

# --- Fix 2: the plan keeps the run 6 letter; the written letter gets the grounded closing ---------------------------
rep('''    if v349c_plain_on() and not V349C_CTX.get("plain_inner"):   # v3.4.9c run 8: the plain three-paragraph letter
        V349C_CTX["plain_inner"] = True
        try:
            failures = compose_bank_cover_letter(plan, master, raw_jd)
        finally:
            V349C_CTX["plain_inner"] = False
        if plan.get("_cover_letter_mode") != "bank" or not plan.get("cover_letter_paragraphs"):
            return failures
''', '''    closing_on = _v347_on(V349C_CLOSING_FLAG)
    if (v349c_plain_on() or closing_on) and not V349C_CTX.get("plain_inner"):   # v3.4.9c run 8 / fix1 (written letter apart)
        V349C_CTX["plain_inner"] = True
        try:
            _V347_FLAGS[V349C_CLOSING_FLAG] = False   # fix1: page decisions see the run 6 letter (closing_v349c off)
            failures = compose_bank_cover_letter(plan, master, raw_jd)
        finally:
            _V347_FLAGS[V349C_CLOSING_FLAG] = closing_on
            V349C_CTX["plain_inner"] = False
        if plan.get("_cover_letter_mode") != "bank" or not plan.get("cover_letter_paragraphs"):
            return failures
        if not v349c_plain_on():   # fix1, closing_v349c with run 7 letters: compose the written letter again, then restore the plan
            snap = deepcopy(plan)
            V349C_CTX["plain_inner"] = True
            try:
                out_fail = compose_bank_cover_letter(plan, master, raw_jd)
                out = {"paragraphs": list(plan.get("cover_letter_paragraphs") or []), "closing_info": dict(plan.get("_v342_closing") or {})}
            finally:
                V349C_CTX["plain_inner"] = False
                plan.clear()
                plan.update(snap)
            plan["_v349c_out"] = dict(out, before=list(plan["cover_letter_paragraphs"]))
            return failures + [f for f in out_fail if f not in failures]
''')
rep('''    if v349c_plain_on() and isinstance(plan.get("_v349c_plain"), dict) and plan["_v349c_plain"].get("paragraphs"):   # v3.4.9c run 8
        plan["cover_letter_paragraphs"] = list(plan["_v349c_plain"]["paragraphs"])
        plan["_v342_closing"] = dict(plan["_v349c_plain"]["closing_info"])
''', '''    if v349c_plain_on() and isinstance(plan.get("_v349c_plain"), dict) and plan["_v349c_plain"].get("paragraphs"):   # v3.4.9c run 8
        plan["cover_letter_paragraphs"] = list(plan["_v349c_plain"]["paragraphs"])
        plan["_v342_closing"] = dict(plan["_v349c_plain"]["closing_info"])
    elif not v349c_plain_on() and isinstance(plan.get("_v349c_out"), dict) and plan["_v349c_out"].get("paragraphs"):   # fix1: run 7 letters
        plan["cover_letter_paragraphs"] = list(plan["_v349c_out"]["paragraphs"])
        plan["_v342_closing"] = dict(plan["_v349c_out"]["closing_info"])
''')
rep('''    if v349c_plain_on() and isinstance(plan.get("_v349c_plain"), dict):   # v3.4.9c run 8: compare the run 7 letter
        txt = "\\n".join(plan["_v349c_plain"].get("before") or [])
''', '''    _pl = plan.get("_v349c_plain") if v349c_plain_on() else plan.get("_v349c_out")
    if isinstance(_pl, dict):   # v3.4.9c run 8 / fix1: compare the letter the page was chosen for (the run 6 letter)
        txt = "\\n".join(_pl.get("before") or [])
''')
rep('''    _pl = ((globals().get("_V33_CTX") or {}).get("plan") or {}).get("_v349c_plain") if v349c_plain_on() else None''',
    '''    _pp = (globals().get("_V33_CTX") or {}).get("plan") or {}
    _pl = _pp.get("_v349c_plain") if v349c_plain_on() else _pp.get("_v349c_out")   # fix1: also the run 7 written letter''')

# --- plain letters: the grounded closing chosen against the plain letter itself ------------------------------------
a = s[s.index('''    # closing: the run 7 closing (same responsibility, proof and connector), its proof in plain words
    cl = dict(plan.get("_v342_closing") or {})'''):s.index('''    out = [_v343_fix_dots(re.sub(r"\\s+", " ", x).strip()) for x in paras()]
    return {"paragraphs": out, "closing": closing, "closing_info": dict(cl, text=closing),''')]
body_old = a
# keep the closing-off path (run 8 behaviour) and add the fix1 path; the letter body is assembled by a local function
i_p2 = a.index("    # P2: Experience (descriptive) and the rank #1 project")
closing_old = a[:i_p2]
assemble_old = a[i_p2:]
assemble_fn = "    def assemble(closing: str, cl: dict[str, Any]) -> dict[str, Any]:\n" + \
    "        pkey = str(cl.get(\"proof\") or \"\")\n        proof = (bank.get(\"proofs\") or {}).get(pkey, \"\")\n        proof_in = bool(proof) and proof in closing\n" + \
    "\n".join(("    " + ln) if ln.strip() else ln for ln in assemble_old.rstrip("\n").split("\n")) + "\n" + \
    '''        out = [_v343_fix_dots(re.sub(r"\\s+", " ", x).strip()) for x in paras()]
        return {"paragraphs": out, "closing": closing, "closing_info": dict(cl, text=closing), "proof_key": pkey if proof_in else "", "experience": ek, "project": pid,
                "achievements": int(bool(pj) and not ach_proof) + int(ach_proof), "hook_source": hook_src,
                "exempt": [x for x in (role, company) if x], "internship": intern, "relocation": reloc, "family": bool(cl.get("family"))}

    if _v347_on(V349C_CLOSING_FLAG):   # v3.4.9c fix1: the grounded closing, checked against this plain letter's own body
        ref = "your client" if "your client" in joined else ("your team" if not named else company)

        def accept(sent: str, info: dict[str, Any]) -> bool:
            res = assemble(sent, info)
            rest = " ".join(res["paragraphs"]).replace(sent, " ")
            return not closing_repeats_letter(str(info.get("_proof") or "") or sent, rest)
        sent, cl = v349c_grounded_closing(plan, master, raw_jd, ref, joined + " " + hook, 30, plain=True, accept=accept)
        return assemble(sent, cl)
'''
closing_old_indented = closing_old.replace('''    closing = _v343_fix_dots(closing)
    proof_in = bool(proof) and proof in closing
''', '''    closing = _v343_fix_dots(closing)
''')
rep(body_old, assemble_fn + closing_old_indented + "    return assemble(closing, cl)\n" + "    # (fix1: the run 8 body below is assemble())\n")
# drop the now-unreachable old tail (out = ... return {...}) that followed the replaced block
old_tail = '''    out = [_v343_fix_dots(re.sub(r"\\s+", " ", x).strip()) for x in paras()]
    return {"paragraphs": out, "closing": closing, "closing_info": dict(cl, text=closing), "proof_key": pkey if proof_in else "", "experience": ek, "project": pid,
            "achievements": int(bool(pj) and not ach_proof) + int(ach_proof), "hook_source": hook_src,
            "exempt": [x for x in (role, company) if x], "internship": intern, "relocation": reloc, "family": bool(cl.get("family"))}
'''
rep("    return assemble(closing, cl)\n    # (fix1: the run 8 body below is assemble())\n" + old_tail, "    return assemble(closing, cl)\n")
P.write_text(s, encoding="utf-8"); print("ok")
