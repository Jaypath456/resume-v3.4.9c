# Run 4 (layout_v349c) - BLOCKED, not a checkpoint. Draft: Resume_Pipeline_3_4_9c_4_DRAFT.zip (from _3.zip)
Stopped: the Run 4 gate "only slot-count and Skills-order differences" failed twice (same check: Skills content).
## Implemented (draft)
- New-grad 3/2/2 slots chosen on the shipped page as a subset of the reference page's slots (letter must stay the
  reference letter); slot choices losing the fewest page technologies (bank jd_terms) first.
- Per-page fit order: coursework line, then Skills filler (page-buffer Skills trim), then one slot. No global trims.
- Skills 6th line only for posting-named items; Python first on the Languages line for ai_llm / data_science_ml.
- Go Digital rule unchanged (already hidden on new-grad pages except data / fintech / compliance; macys keeps it: analyze-data posting).
## GATE16 vs Run 3 baseline (_3.zip re-run: identical to the Run 3 outputs)
- Flag off: 16/16 byte-identical to Run 3.
- Flag on: 16/16 PASS builds; one page; spare >= 10.5pt (min 21.4 doordash_mdx). Project set, rank 1, project order,
  Fit: unchanged 16/16. Letters, tracker rows, outreach: unchanged 16/16.
- Allowed differences: slots 3/3/2 -> 3/2/2 allergan (LaunchOps), cardinal (LaunchOps), nvidia_infra (RIPPLE);
  3/3/3 -> 3/2/2 figure (LedgerFlow, RIPPLE); giga_swe Languages line Python first.
- GATE FAIL 1/16 (attempt 2): cardinal Skills lose "Django REST Framework" (not named in the posting; it was on the
  page only through LaunchOps bullet workflow.c). Of the three LaunchOps 2-slot choices, two fail the bank selection
  rules (bank_auto_selection) and one changes the letter; the kept choice drops workflow.c.
- Attempt 1 failed the same check on 3 pages (allergan Go / MongoDB / Redis / nginx; cardinal same; figure Claude Code
  -> Docker, Redis); the technology-preserving slot order fixed allergan and figure.
## Decision needed
Allow Skills items that leave with a dropped slot (not posting-named) as a slot-count consequence, or keep cardinal at 3/3/2.
Run 1-3 open items unchanged: selftest_v348b 3 hash-lock failures deferred to Run 9 (not passed). Run 5 not started.
