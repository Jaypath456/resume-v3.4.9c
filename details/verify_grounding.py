"""Independent check of each specific closing: every word of the responsibility that is not a generic verb/quality word
(the pipeline's V349C_GENERIC list) must appear as a whole word in the cited evidence, assembled here from master.json
(proof sentence + evidence item text + claim atoms, or the named Experience bullets; employer names removed)."""
import sys, json, re, glob, importlib.util
O, S = sys.argv[1], sys.argv[2]
sys.argv = ["x"]; sp = importlib.util.spec_from_file_location("rp", S + "/resume_pipeline_v3_2.py"); rp = importlib.util.module_from_spec(sp); sp.loader.exec_module(rp)
m = json.load(open(S + "/master.json")); proofs = m["cover_letter_bank"]["closing_proofs"]; plainp = m["cover_letter_bank"]["plain_v349c"]["proofs"]
PROJ = {"ledger": "ledgerflow", "launchops": "launchops", "ripple": "ripple", "pintos": "pintos", "tailor": "tailor_pipeline", "fraud": "fraud", "goingonce": "goingonce"}
ALIAS = {"fraud.graphsage_result": "fraud.graphsage", "fraud.edge_ablation_result": "fraud.edge_ablation", "launchops.ownership": "launchops.workflow"}
EXPRX = {"exp.thesis_heartbeat": r"\bheartbeat\b", "exp.thesis_review": r"\bpull requests?\b", "exp.datamaven_access": r"\bVPC\b", "exp.datamaven": r"\bEC2\b",
         "exp.hein": r"\bCrossRef\b|\bHeinOnline\b", "exp.godigital": r"\bETL workflow\b", "exp.thesis_iot": r"\bIoT\b", "exp.thesis_backend": r"\bIoT\b|\bWebSocket\b",
         "exp.thesis_client": r"\bclient meetings\b|\bhealthcare platform\b"}
def evidence(k):
    t = [proofs.get(k, ""), plainp.get(k, "")]
    if k.startswith("exp."):
        t += [b for e in m["experience"] for b in e["bullets"] if re.search(EXPRX.get(k, "^$"), b)]
    else:
        e = m["projects"][PROJ[k.split(".")[0]]]["evidence_items"].get(ALIAS.get(k, k), {}); t += [e.get("text", "")] + list(e.get("claim_atoms") or [])
    s = " ".join(t)
    for e in m["experience"]: s = s.replace(re.sub(r"\s*\(.*?\)", "", e["organization"]).strip(), " ")
    return s.lower()
def base(w):
    w = re.sub(r"(ies)$", "y", w); w = re.sub(r"(?<=[a-z]{3})(es|s)$", "", w) if not w.endswith(("ss", "us", "sis")) else w
    w = re.sub(r"(?<=[a-z]{3})(ing|ed)$", "", w); return w.rstrip("e")
bad = 0; rows = []
for f in sorted(glob.glob(O + "/*/out/report.json")):
    c = (json.load(open(f)).get("cover_letter") or {}).get("closing") or {}
    if not c or c.get("family"): continue
    ev = evidence(c["proof"]); evw = {base(x) for x in re.findall(r"[a-z0-9][a-z0-9+#-]*", ev)}
    miss = []
    for w in re.findall(r"[A-Za-z][A-Za-z0-9+#/-]*", c["responsibility"]):
        w = w.lower().strip("-/")
        if w in rp.V349C_GENERIC or len(w) < 2: continue
        if w in ev.split() or base(w) in evw or re.search(r"(?<![a-z])" + re.escape(w.replace("-", "[- ]?")) + r"(?![a-z])", ev): continue
        miss.append(w)
    bad += bool(miss)
    rows.append(f"{f.split('/')[-3]:16} {'OK ' if not miss else 'BAD'} '{c['responsibility']}' <- {c['proof']} {('missing ' + str(miss)) if miss else ''}\n      evidence: {ev[:220]}")
print("\n".join(rows)); print(f"GROUNDING: {len(rows) - bad}/{len(rows)} specific closings supported by their cited evidence")
