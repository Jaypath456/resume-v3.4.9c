# Run 7 (grounded closings) - Resume_Pipeline_3_4_9c_7.zip, from Resume_Pipeline_3_4_9c_6.zip (input unchanged)
Flag `closing_v349c` (default true, 46 flags). Template a3aaddd9 (unchanged), master 67374c53, bank 914805e9. 4 files differ
from _6: pipeline, master.json (flag only), selftest_v349b, selftest_v348b (flag count / off lists). Details: details/run7_gate16.txt.

## Rule
A closing "I want to {responsibility} {where}, {connector} {proof}." keeps its responsibility only when every specific word
of it appears in the proof's own master evidence (closing proof text; that project's evidence item text, claim atoms, terms,
stack, tags; for an Experience proof that job's bullets and evidence anchors). Generic verbs / qualities / nouns ("build",
"design", "scalable", "software", "platform") are not claims. An unsupported responsibility is set aside and the next is
tried (up to 8). With none supported, the role-family closing is used; its proof must demonstrate the family claim too,
and the family claim itself must appear in master evidence (otherwise general_swe). Changed FINAL definition: _v344_closing.

## Changed closings (GATE16: 5/16; evidence rows in details/run7_gate16.txt)
- alml_engineer: "optimize models for latency, accuracy, and scalability ... building on my fraud model's edge-type ablation"
  -> "I want to apply careful, baseline-checked model evaluation to your team's machine learning work." Unsupported:
  optimize, latency, accuracy, scalability. Family claim evidence: Fraud project (tags "model evaluation", "ML"; baselines).
- doordash_mdx: "build ML infrastructure in production including feature engineering and feature stores ... LLM engine's
  provider failover" -> same data_science_ml family closing (DoorDash's). Unsupported: infrastructure, feature, stores.
- elevenlabs: "design and build generic resource and permissioning services ... LaunchOps ... owner and prerequisites"
  -> "I want to keep systems healthy at ElevenLabs." Unsupported: resource. Evidence: Thesis heartbeat / IoT monitoring
  bullets (none of the proofs the picker offered demonstrates the claim, so no proof clause).
- figure: "integrate, debug, and validate updates on real robot hardware ..." -> "I want to design, implement, and test
  features for the robot software platform at Figure, building on the locking and memory-access checks I wrote in C for
  Pintos." Unsupported: integrate, validate, updates. Kept responsibility is generic verbs + "robot software platform"
  (embedded kind) with the Pintos safety evidence.
- zoro_fullstack: "build scalable infrastructure and customer-facing solutions ... Go live-quiz service" -> "I want to ship
  reliable features with the team at Zoro, building on LedgerFlow, where a GitHub Actions CI workflow runs every automated
  test." Unsupported: infrastructure. Evidence: ledger.ci (94 tests in CI, confirmed 2026-10-15).

## Gates (GATE16, baseline = _6.zip re-run, identical to Run 6 outputs)
- Flag on: 16/16 PASS, exit 0, one US Letter page, spare 10.54-10.77pt. Letters differ only in the closing sentence (5/16);
  resume .tex, tracker_row.json, outreach.json byte-identical 16/16. Other differing files: report.json / resolved_plan.json /
  judge_packet.md / quality_v33.json closing fields only. Unsupported claims after the rule: 0/16.
- Flag off: 16/16 byte-identical to Run 6 (every output file; timings ignored).
- Determinism: the 5 changed closings were the same text in the two flag-on runs before and after the last code edit.
## Checks
bank_check 120 variants / 0 failing. selftest_v349b ALL PASS (46). selftest_v348b 77 pass, 3 FAIL (hash lock in the
instructions file, deferred to Run 9). Not run (as instructed): all 128 fixtures.
