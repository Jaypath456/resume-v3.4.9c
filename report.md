# Run 5 (adaptive spacing) - Resume_Pipeline_3_4_9c_5.zip, from Resume_Pipeline_3_4_9c_4.zip (input unchanged)
Flag `spacing_v349c` (default true, 44 flags). Template a3aaddd9 (unchanged), master 91442d55, bank 914805e9; 4 files differ from _4.
- After the page is decided and validated, t in [0,1] is binary-searched in 9 steps (lo 0, hi 1, mid accepted when one
  page with >= 10.5pt unrounded spare; ties accepted) and the largest accepted t is kept: divider 0.2->1.0em / 0.25->0.8em,
  rolegap 3->10pt, section skip 0.2->0.7em / 0.1->0.6ex, itemsep 0->1.5pt. Margins untouched. report.json: spacing_v349c.
- Run 4 defect found and fixed: _4.zip ends every layout build with "KeyError: 0" after all outputs are written (16/16,
  exit code 1; outputs complete). Fix in _v349c_fit (layout attempts log only in layout_v349c); outputs unchanged.
## GATE16 vs Run 4 baseline (_4.zip re-run: identical outputs). Rows: details/run5_gate16.txt
- Flag off: 16/16 byte-identical to Run 4. Flag on: 16/16 PASS, no tracebacks, one US Letter page, spare 10.54-10.77pt.
- Resume text identical to Run 4 (PDF text, whitespace removed) 16/16; .tex differs only in the 4 spacing lengths;
  letters, tracker rows, outreach, resolved plans unchanged 16/16.
- t: min 0.324 (doordash_mdx), median 0.416, max 0.629 (cardinal, figure). Per page: akamai 0.412, allergan 0.539,
  alml 0.348, audible 0.426, cardinal 0.629, doordash 0.324, ebsco 0.420, elevenlabs 0.412, figure 0.629, giga 0.516,
  macys 0.342, meritore 0.412, nvidia 0.531, umich 0.336, ust 0.412, zoro 0.420. (Run 2 Standard spacing = t 0.32.)
## Diagnostic only (no shipped change): details/run5_margin_spacing_diagnostic.json
- NewGrad reference spacing (t >= 0.527) fits on 4/16 (allergan, cardinal, figure, nvidia_infra; giga_swe 0.516 just short).
- 0.4in side margins at each page's t: content and 10.5pt kept on 12/16; akamai_se, audible, elevenlabs, macys lose a
  Skills item (same 4 as the Run 2 draft). Geometry stays 0.3in until separately approved.
## Checks
- bank_check: 120 variants, 0 failing. selftest_v349b: ALL PASS (44). selftest_v348b: 77 pass, 3 FAIL - "hash lock
  lists" pipeline / master / template: unresolved, deferred to Run 9. Selftest edits: flag count 44, spacing_v349c in off lists.
## Carried forward
Run 2 deviations (0.3in margins, Standard spacing baseline); Run 4 approved exception (cardinal Skills). Not run: 128 fixtures.
