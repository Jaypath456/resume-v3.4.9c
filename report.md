# Run 2 (page) - Resume_Pipeline_3_4_9c_2.zip, from Resume_Pipeline_3_4_9c_1.zip (input unchanged)
Flag `page_v349c` (v347_flags, default true, 40 flags). Template 1bdb13f9, master 2e55c1c9, bank 914805e9 unchanged; 5 files differ from _1.
- Done: Standard reference preamble; \rolegap after the name line; \hspace{0.5em}|\hspace{0.5em} separators; Education on two lines (coursework under the Master's line); no Certifications & Awards (awards, hackathon evidence and the heading leave the loaded master at run time; bank variants naming 1st Place / Copart / Cloud Practitioner are not selectable; a build fails if one renders); 10.5pt buffer.
- APPROVED DEVIATIONS (Jay 2026-10-22), not an exact match to the Trial2 visual spec: (1) left/right margins 0.3in, not 0.4in; (2) Standard reference spacing on new-grad pages too, not the NewGrad spacing. Reason: with them 6/16 GATE16 pages lost Skills items or bullets (blocked draft, branch wip/v349c-run2-page-blocked).
- Content lock: the Letter fit runs on the run 1 page first and the new page starts at the attempt it kept, so the freed space never adds bullets (it had added slots on allergan, giga_swe, nvidia_infra).
- Education "\textit{}" kept on both dates, as in the references.
## GATE16 vs Run 1 baseline (_1.zip re-run: identical to the Run 1 flag-on outputs)
- Flag off: 16/16 byte-identical to Run 1 (timestamps/durations ignored).
- Flag on: 16/16 PASS, one US Letter page each, spare >= 10.5pt on all (min 10.8 ebsco_sde1, max 62.1).
- Experience, Projects and Skills sections, ranking, display order, bank selections and resolved skills: identical on 16/16.
- Letters, tracker rows, outreach: byte-identical on 16/16. Grep 1st Place / Copart / Cloud Practitioner: 0 resumes.
- report.json only: skills_text_hash, free_space_pt, letter_fit attempt logs (start at the run 1 choice); judge_packet.md, quality_v33.json, tex_sha256.txt follow the page.
## ebsco_sde1 (inherited Run 1 failure)
- Coursework line is back with all nine courses (2 lines), spare 10.8pt >= 10.5pt; a permitted Education change. Run 3 must still apply the top-3 rule.
## Checks
- bank_check: 120 variants, 0 failing. selftest_v349b: ALL PASS (44). selftest_v348b: 77 pass, 3 FAIL - "hash lock lists" pipeline / master / template: unresolved, deferred to Run 9 (instructions not edited).
- Selftest edits: flag count 40; page_v349c added to flag-off lists that compare with older baselines; v349b format checks read the run 1 template (page_v349c off).
- Not run: all 128 fixtures, selftests v341-v349a.
## Run 5 note
Assess whether more airiness (0.4in margins, NewGrad spacing) can return without losing content or the 10.5pt buffer; margins stay 0.3in until then.
