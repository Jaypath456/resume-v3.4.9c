# Run 2 (page_v349c) - BLOCKED, not a checkpoint. Draft: Resume_Pipeline_3_4_9c_2_DRAFT.zip (from _1.zip)
Flag `page_v349c` (default true, 40 flags). Template dadca8c0, master 6e3f855e, bank 914805e9; 3 files differ from _1.
Implemented: Standard reference preamble (NewGrad spacing lines on new-grad pages), \rolegap after name, \hspace separators,
two-line Education (coursework under the Master's line), no Certifications & Awards (awards, hackathon evidence and the
heading leave the loaded master; bank variants naming 1st Place / Copart / Cloud Practitioner are not selectable), 10.5pt buffer.
## GATE16 vs Run 1 baseline (_1.zip, re-run: identical to the Run 1 flag-on outputs)
- Flag off: 16/16 byte-identical to Run 1. Flag on: 16/16 PASS builds, 1 page, spare >= 10.5pt (min 10.8, ebsco_sde1).
- Letters, tracker rows, outreach: 0/16 changed. Grep (1st Place, Copart, Cloud Practitioner): 0 resumes.
- GATE FAIL 6/16: content outside header/geometry/Education/removed section changed. Two causes, isolated by experiment:
  A. left/right 0.4in (narrower line; with 0.3in these pass): Skills line loses an item - akamai_se Parallel Processing,
     audible Event-Driven Architecture, elevenlabs ETL, macys REST APIs; giga_swe GoingOnce bullet negotiate.a -> determ.a
     (+ Claude API in Tools).
  B. NewGrad reference spacing on new-grad pages (with Standard spacing these pass): figure 3/3/3 -> 3/3/2 (RIPPLE
     Claude Code bullet; Tools changes), macys 3/2/2 -> 3/2/1 (Pintos bullet) to keep the 10.5pt spare.
- ebsco_sde1 (Run 1 exception): the nine-course coursework line is back, spare 10.8pt; its Run 2 gate row passes.
## Not done (stopped at the gate)
No _2.zip checkpoint, no selftests, no commit to build/v349c, Run 3 not started. Run 1 exceptions unchanged:
selftest_v348b 3 hash-lock failures deferred to Run 9 (not passed).
