# NOTES v3.4.9c (2026-10-22)

Built from Resume_Pipeline_3_4_9b.zip in nine runs, each a verified, pushed checkpoint (Resume_Pipeline_3_4_9c_1.zip ...
_8.zip, branch build/v349c). Deliverables: Resume_Pipeline_3_4_9c.zip, this file, CHANGES.md, golden_report.md,
report_v349c.md (repository root).

## Result
- 128 fixtures (all nine flags on): exit 0 on 128/128; 126 PASS on one US Letter page with 10.51-10.77pt unrounded spare,
  plus the 2 expected stops. Grep gates clean on every resume and letter.
- All nine flags off: GATE16 byte-identical to the unmodified v3.4.9b outputs (16/16).
- Selftests v341-v349b all pass (14 files); bank_check 120/0; golden_check 12/12; score_all resume 9.96 / letter 9.98.
- audit_v344 exits 1: role-family closings 69.0% (cap 10%), the cost of the Run 7 grounding rule; 30 of its 31 repeat lines
  are proof-less family closings. Not changed (see Deviations 6).
- Letters 127-160 words; tracker rows and outreach identical to Run 6 everywhere; resumes identical to Run 6 except vindexa.

## The nine flags (master.json v347_flags, default true; false restores the previous behaviour for that change)
| Flag | Run | What it does |
|---|---|---|
| data_v349c | 1 (+6) | Education "August 2025 -- December 2026"; the nine listed courses; Agentic AI a skill, not coursework; "We won 1st place." out of the letter bank; a required posting term the page does not show joins Skills |
| page_v349c | 2 | Standard reference layout; no Certifications & Awards section; content kept from the run 1 page |
| thesis_v349c | 3 | Thesis lead bullet variant I (E for requirements postings); mentoring line |
| coursework_v349c | 3 | new-grad pages only, one line, top 3 courses by posting terms |
| layout_v349c | 4 (+6) | new-grad 3/2/2 slots; per-page fit fallback; Skills <= 5 lines; Python first on AI/ML postings |
| spacing_v349c | 5 | spacing grows while one page keeps >= 10.5pt spare; margins fixed at 0.3in |
| must_framework_v349c | 6 | a required language / framework with one primary project already on the page makes it rank 1 |
| closing_v349c | 7 | closing responsibility must be in its proof's master evidence; else role-family closing |
| letters_plain_v349c | 8 | three plain paragraphs, 120-160 words, one achievement, no tools / digits / we-our-us |
All nine off: GATE16 equals the unmodified v3.4.9b outputs byte for byte (the version label reads v3.4.9b then).

## Deviations and exceptions (approved by Jay unless marked)
1. Side margins 0.3in, not the Trial2 0.4in (approved 2026-10-22).
2. Standard reference spacing on every page, not the NewGrad spacing (approved 2026-10-22); Run 5 lets spacing grow only
   while the page keeps 10.5pt spare (t 0.32-0.63 on GATE16). The template is not an exact match of Trial2; no claim is made
   that it is.
3. Cardinal exception (approved, option 1): a Skills item may disappear when its only bullet leaves with the 3/2/2 slot
   reduction (cardinal loses "Django REST Framework", not named in the posting).
4. Letters (Run 8, my reading): digits in the posting's own role title or company name are allowed, because the letter
   must name the position ("Macy's 2027 Tech Early Careers - Software Engineer"). The internship sentence keeps its
   wording ("... is expected in December 2026, and I can start work in February 2027."), as instructed.
5. Letter word count: 120-154 body words, so the whole letter with greeting and sign-off stays <= 160.
6. Run 7 makes most closings fall back to the role-family closing (87/126 = 69%, v3.4.9b 13/126): a responsibility stays
   only when its proof's evidence shows every specific word. audit_v344's 10% line and its repeat check (which reads a
   proof-less closing as a proof) were not changed, so the audit exits 1. Loosening the support check (e.g. synonyms)
   would bring specific closings back; that is a decision for Jay.

## Run notes
- Run 1: ebsco_sde1's nine-course line did not fit (fixed by Run 3's top-3 rule; ebsco is a standard page and shows none).
- Run 4: "KeyError: 0" after outputs were written (exit 1) - fixed in Run 5.
- Run 6: two inherited full-128 failures found and fixed under their own flags (assetwatch: Agentic AI; vindexa: spare
  10.4pt). First must detection promoted 7 projects, 5 wrongly; the tightened rule promotes 2 (ebsco_sde1, bti).
- Run 7: 5 GATE16 closings changed (alml_engineer, doordash_mdx, elevenlabs, figure, zoro_fullstack).
- Run 8: page decisions read the letter (fit steps that compare letters; "every letter number is on the resume"), so the
  Run 7 letter stays in the plan until the letter is written; with that, resumes are identical to Run 7.
- Run 9: the three selftest_v348b "hash lock lists" failures (deferred since Run 1) are resolved by the new hash lock.
  The first full 128 run of the release code found plain-letter defects that GATE16 and the 20 extra Run 8 fixtures did
  not show, all fixed under letters_plain_v349c and rerun on all 128:
  - laminar: the opening "I am applying for the Jr. Machine Learning (ML) Developer role ..." was cut at "Jr." (role
    missing, exit 2); twitch: 118 words (a third project's plain description now fills a letter still under 120);
    "Another project is fraud detection models ..." now reads "In another project, I built fraud detection models ...".
  - Hooks: tool names used as adjectives or objects stayed in, so hooks fell back to cut phrases ("build features end")
    or a generic sentence (cobalt, dominos, sparkline). The hook is now de-tooled ("React dashboards" -> "dashboards",
    "use Python" -> "write code", "with Java and Spring Boot" leaves) and must pass the pipeline's own posting test
    (hook test or 3+ content words from one responsibility line); cut phrases ending on a dangling word are refused.
  - Tool names: common industry tools Jay does not list (Swift, Kotlin, TypeScript, ...) now count (ios_randstad named
    Swift); concepts in Jay's skills pool (Concurrency, Operating Systems, ...) do not.
  - report.json ranking_v349.rank kept the pre-promotion order after a Run 6 must-have promotion (ebsco_sde1, bti), so
    golden_check read the wrong rank1; it now shows the final ranking (report only).
  - score_all: 15 letters for postings that require AI coding tools had lost that evidence (the plain rules forbid
    "Claude Code"); they now say "An AI coding assistant helped me write RIPPLE, and I checked its work with its full test
    suite." (master evidence). Short letters describe a second / third project before using the courtesy sentence.
  - Found, not changed: vindexa's resume differs from Run 6 (GoingOnce 3 bullets, LaunchOps 1 fewer). Its page needs the
    fit step that keeps a trimmed page only when the letter stays the same, and Run 7 changed its closing; Run 7's
    "resumes identical" gate held on GATE16 but this full-128 case differs (still one page, 10.5pt spare). Run 8 changes
    no resume.

## Migration
Paste the new instructions (7,574 characters) and re-upload the 7 Sources (4 changed). Expect hash PASS: pipeline
b04aa71d | master 019e5b87 | bank 914805e9 | template a3aaddd9 | context md b43948bf. No tracker change. Rollback of one
change: set its flag false in master.json (needs a rehash; master.json is hash-locked).
