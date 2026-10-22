# Run 4 (layout) - Resume_Pipeline_3_4_9c_4.zip, from Resume_Pipeline_3_4_9c_3.zip (input unchanged)
Flag `layout_v349c` (default true, 43 flags). Template a3aaddd9 (unchanged), master b906ba00, bank 914805e9; 4 files differ from _3.
- New-grad pages: 3/2/2 project slots (6/4/4 lines), a subset of the reference page's slots chosen on the shipped page;
  slot choices that lose the fewest page technologies (bank jd_terms) first; the letter must stay the reference letter.
- Fit fallback per page only (no global trims): (1) coursework line, (2) Skills filler, (3) one bullet slot.
- Skills: at most 5 lines; a 6th only when every item needing it is named in the posting. Python first on the
  Languages line for AI/ML postings (role family ai_llm / data_science_ml).
- Go Digital: unchanged rule (hidden on new-grad pages except data / fintech / compliance); no project-set conflict.
## GATE16 vs Run 3 baseline (_3.zip re-run: identical to Run 3 outputs). Rows: details/run4_gate16.txt
- Flag off: 16/16 byte-identical to Run 3. Flag on: 16/16 PASS, one US Letter page, spare >= 10.5pt (min 21.4 doordash_mdx).
- Project set, rank 1, project order, Fit: unchanged 16/16. Letters, tracker rows, outreach: unchanged 16/16.
- Differences (all fit-phase "fits", no fallback used):
  - allergan: LaunchOps 3 -> 2 slots (new-grad 3/2/2).
  - cardinal: LaunchOps 3 -> 2 slots; APPROVED EXCEPTION (Jay 2026-10-22, option 1): Skills lose "Django REST
    Framework" - not named in the posting, its only bullet (launchops.workflow.c) left with the slot.
  - figure: LedgerFlow 3 -> 2, RIPPLE 3 -> 2 slots (3/3/3 -> 3/2/2).
  - nvidia_infra: RIPPLE 3 -> 2 slots.
  - giga_swe: Languages line Python first (ai_llm posting).
- No page needed coursework / Skills-filler / slot fallback; no 6th Skills line on any page.
## Checks
- bank_check: 120 variants, 0 failing. selftest_v349b: ALL PASS (44). selftest_v348b: 77 pass, 3 FAIL - "hash lock
  lists" pipeline / master / template: unresolved, deferred to Run 9 (instructions not edited).
- Selftest edits: flag count 43; layout_v349c added to flag-off lists that compare with older baselines.
## Carried forward
Run 2 deviations (0.3in side margins, Standard spacing on new-grad pages). Not run: all 128 fixtures.
