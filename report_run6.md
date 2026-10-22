# Run 6 (must-have framework ranking) - Resume_Pipeline_3_4_9c_6.zip, from Resume_Pipeline_3_4_9c_5.zip (input unchanged)
Flag `must_framework_v349c` (default true, 45 flags). Template a3aaddd9 (unchanged), master b6ee9793, bank 914805e9. Details: details/run6_full128.txt, details/run6_gate16.txt.

## Rule
A language / framework that the posting REQUIRES - an unhedged qualification line ("experience in", "proficiency",
"knowledge of", "required", "years of"...), not a responsibility, a "Stack:" list, a "helpful / not mandatory / plus /
preferred" line, "one of / at least N of the following / such as / or similar" alternatives, a list of 3+ technologies
or "X or Y" - and has exactly ONE primary project becomes rank 1, only if that project is already one of the three
(the project set never changes). Primary = the project's stack names the term AND leads with it or its identity /
headline evidence names it. Reviewed against master evidence: React, Django, DRF -> LaunchOps ("Django REST and React
onboarding platform"); Java ("Java 25" leads the stack), Spring Boot -> LedgerFlow; C -> Pintos; PyTorch -> Fraud;
Python (4 projects), JavaScript, Go: none. Terms pointing to different projects decide nothing.

## Results
- GATE16 (Run 5 baseline re-run from _5.zip = Run 5 outputs): flag on 16/16 PASS, exit 0, one page, spare 10.54-10.77pt;
  only ebsco_sde1 changes (LaunchOps rank 1: "0-3 years of professional experience in React"). Flag off: 16/16 byte-identical.
  Other GATE16 files differ only by the new report.json key must_framework_v349c.
- Full 128 (rule on): 128/128 exit 0; 126 PASS + 2 expected stops; one page; spare 10.51-10.77pt.
  Project set / rank 1 / order changed: 2/126 (limit 12): ebsco_sde1 (React -> LaunchOps), bti ("Working knowledge of
  Java and Python" -> LedgerFlow). Project sets unchanged everywhere.
- Gate correction (attempt 2): the first full run's detection promoted 7; review found 5 false musts (acme_cloud, ixl
  "one of / or a similar language"; audit02 "helpful but not mandatory"; quora, vindexa "Stack:" / "Frontend:" lists)
  and bti's line was a responsibility. Detection was tightened; the 23 fixtures where either detection finds a must term
  were rerun with the final code (all PASS, exit 0); elsewhere only report.json must_framework_v349c can differ.
- Inherited full-128 failures in the verified Run 5 ZIP (not visible in GATE16), fixed under their own flags:
  - assetwatch (data_v349c, since Run 1): required "Agentic AI" was counted from the unprinted coursework list before
    Run 1; now a required posting term the page does not show joins Skills (AI/ML line, 6 Skills lines, run 4 rule).
  - vindexa (layout_v349c, since Run 4): spare 10.4pt; when the fallback page also misses the buffer, step 3 now tries one
    slot from the higher-ranked projects too (as v3.4.9b did): 2/2/2.
  With the Run 6 flag off, these two differ from Run 5 (FAIL -> PASS); all other fixtures equal Run 5.
## Checks
bank_check 120 variants / 0 failing. selftest_v349b ALL PASS (44). selftest_v348b 77 pass, 3 FAIL (hash lock in
the instructions file: unresolved, deferred to Run 9). Determinism: the first-version full run reproduced its own GATE16 run 16/16 byte for byte; the final GATE16 differs from
the full-run copies only in report.json must_framework_v349c (macys, ust_software_engineer: old detection entries).
