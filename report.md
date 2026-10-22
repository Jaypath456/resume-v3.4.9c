# Run 3 (Thesis, coursework) - Resume_Pipeline_3_4_9c_3.zip, from Resume_Pipeline_3_4_9c_2.zip (input unchanged)
Flags `thesis_v349c`, `coursework_v349c` (independent, default true, 42 flags). Template a3aaddd9, master b5dbde69, bank 914805e9 unchanged; 5 files differ from _2.
- Thesis: first bullet = approved variant I (Agile/Scrum, reviewed and merged team pull requests; both in master's Thesis evidence) by default; variant E (requirements first) only when a role line asks for requirements work or 2+ role lines name stakeholders / business users / clients. Mentor bullet = the one-line text given.
- Coursework: new-grad pages only; 1 point per listed term in the title + role lines; top 3 (ties: table order) when 2+ courses score; one line under the Master's line. Interpretation: with exactly 2 matches the third course is the next in table order (giga_swe: Algorithms, score 0).
- Content decisions (bullets, slots) are made with run 3 flags off, as in run 2; the kept attempt is retried first with the coursework line allowed.
## GATE16 vs Run 2 baseline (_2.zip re-run: identical to the Run 2 outputs)
- Flag on: 16/16 PASS; resumes differ only in Thesis bullets and the coursework line; ranking and bank selections identical; letters, tracker rows, outreach byte-identical; one US Letter page; spare >= 10.5pt (min 16.0 figure).
- Thesis: variant I on 13/16, E on 3 (akamai_se "translate requirements", allergan "gather and clarify requirements", ust_software_engineer business requirements + stakeholders). Mentor bullet one line on 16/16.
- Coursework: 6/6 new-grad pages - allergan (Data Models, OS, Algorithms), cardinal (Data Models, Project Dev, OS), figure (OS, Security, Project Dev), giga_swe (OS, Data Intensive, Algorithms), macys (OS, Project Dev, Data Models), nvidia_infra (OS, Data Intensive, Algorithms); 3 courses on one rendered line each. Standard pages: none.
- Flags off: both off = Run 2 byte-identical 16/16. thesis off: differs from Run 2 only in coursework, from flag-on only in Thesis (16/16). coursework off: differs from Run 2 only in Thesis, from flag-on only in coursework (16/16).
## ebsco_sde1 (inherited Run 1 failure)
- RESOLVED by the new rule: ebsco_sde1 is a standard (not new-grad) page, so no coursework line is shown; spare 34.3pt. The nine-course two-line problem cannot recur: the line is now at most 3 courses on one line (checked on all 6 pages that show it).
## Checks
- bank_check: 120 variants, 0 failing. selftest_v349b: ALL PASS (44). selftest_v348b: 77 pass, 3 FAIL - "hash lock lists" pipeline / master / template: unresolved, deferred to Run 9 (instructions not edited).
- Selftest edits: flag count 42; thesis_v349c / coursework_v349c added to flag-off lists that compare with older baselines.
- Not run: all 128 fixtures, selftests v341-v349a.
## Carried forward
Run 2 deviations stay (0.3in side margins, Standard spacing on new-grad pages; not an exact Trial2 match). Run 5: assess restoring airiness without losing content or the 10.5pt buffer.
