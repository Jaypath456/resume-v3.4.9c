# Run 8 (plain letters) - Resume_Pipeline_3_4_9c_8.zip, from Resume_Pipeline_3_4_9c_7.zip (input unchanged)
Flag `letters_plain_v349c` (default true, 47 flags). Template a3aaddd9 (unchanged), master 99ea650e (flag + new
cover_letter_bank.plain_v349c), bank 914805e9. 4 files differ from _7: pipeline, master.json, selftest_v349b, selftest_v348b
(flag count / off lists). Details: details/run8_gate16.txt.

## Rule
The letter is rebuilt in exactly three paragraphs, 120-154 body words (<= 160 with greeting and sign-off), from
master.json cover_letter_bank.plain_v349c, sentences that restate master evidence in everyday words:
- P1: the Run 7 opening sentence (position and company), then the plan hook as the posting connection. A closing phrase
  that only lists tools is dropped ("... adjusters across the country with Java and Spring Boot." -> "... across the
  country."), and "REST APIs" becomes "APIs". If the hook still names a tool or has a digit, a posting responsibility
  is used instead.
- P2: the letter's Experience item (descriptive) and the rank #1 project. At most one concrete achievement: the project's
  result, or its plain description when the closing proof is itself a result. A second project (described, no result)
  or a short courtesy sentence fills the letter to 120 words.
- P3: the graduation sentence (full-time: "I graduate in December 2026 and can start work in February 2027.";
  internships keep their Run 7 sentence), the relocation clause when the Run 7 letter had one, then the Run 7 closing.
  The closing keeps the same responsibility, proof and connector; only the proof is reworded plainly (no tools, no
  digits). A closing responsibility that names a tool or has a digit is re-picked for the plain letter, with the same
  grounding rules.
- Never: tool or library names, hackathon or certification words, standalone we/our/us. No digits except in the
  graduation sentence and in the posting's own role title or company name (deviation: e.g. "Macy's 2027 Tech Early
  Careers - Software Engineer", which is the position name the letter must include).
- Validators added: v349c_plain_letter (all rules above), three-paragraph count and the data/ML Experience anchor on the
  plain letter, start clause checked in paragraph 3. The Run 7 letter stays in the plan until build_cover_letter writes
  the plain one. So every page decision (the fit steps that compare letters; "every letter number is on the resume") sees
  the Run 7 letter, and the Run 7 letter checks still run on it.
  Found in testing: with the plain letter in the plan, audit01 and ixl got different resumes. This is fixed, and resumes
  now match Run 7.

## Gates (GATE16; baseline = _7.zip re-run, identical to Run 7 outputs 16/16)
- Flag on: 16/16 PASS, exit 0, one US Letter page, spare 10.54-10.77pt. Letter gate 16/16 (details file).
  Body 121-144 words, at most one achievement, plan hook used 16/16. Resume .tex, tracker_row.json and outreach.json
  are byte-identical to Run 7 16/16 (no tracker or outreach change). Other files that differ hold letter fields only.
  Closing logic changed 1/16: cardinal ("develop and maintain Java and Spring Boot applications" names tools ->
  general_swe family closing, proof ledger.chaos_runs).
- Flag off: 16/16 byte-identical to Run 7 (every output file; timings ignored).
- Extra (not required): 20 edge fixtures (agency / unnamed company / missing title / internship / data-ML / SDET /
  systems / support): exit 0 20/20, letter gate 20/20, resumes = Run 6/7, spare >= 10.51pt.
## Checks
bank_check 120 variants / 0 failing. selftest_v349b ALL PASS (47). selftest_v348b 77 pass, 3 FAIL (hash lock in the
instructions file, deferred to Run 9). Not run (as instructed): all 128 fixtures.

## Five complete sample letters (GATE16, flag on)

**akamai_se** (experience proof in the closing)
```text
Dear Hiring Manager,

I am applying for the Software Engineer role at Akamai Technologies. I want to help build the API endpoints, configuration management, and customer-facing features that developers use on the Akamai Inference Cloud.

At Thesis Mumbai Tech, I led a team of four through healthcare software projects, from client meetings and early prototypes to finished features. I also built LedgerFlow, a payment system that never recorded a payment twice, even when I crashed its parts on purpose. Another project is LaunchOps, an employee onboarding app that guides HR, IT, managers, and new employees through their tasks.

I graduate in December 2026 and can start work in February 2027. I want to build and maintain customer-facing platform features at Akamai Technologies, drawing on the live device-data feed I built at Thesis Mumbai Tech. Thank you for considering my application.

Sincerely,
Jay Niketan Pathare
```

**figure** (internship sentence kept; course project result)
```text
Dear Hiring Manager,

I am applying for the Embedded Software Engineering Intern, Platform role at Figure. I want to help build and improve the core software infrastructure that keeps Figure's robot fleet running safely through every update.

At Thesis Mumbai Tech, I built a live feed that carried readings from infant warming devices into a healthcare platform for real-time monitoring. For a course, I wrote the part of a teaching operating system that runs user programs, and my version passes all of its tests.

My Master's in Computer Science at the University at Buffalo is expected in December 2026, and I can start work in February 2027. I am open to relocating. I want to design, implement, and test features for the robot software platform at Figure, building on the locking and memory checks I wrote for a teaching operating system. Thank you for considering my application.

Sincerely,
Jay Niketan Pathare
```

**macys** (role title with a digit (exempt); relocation clause)
```text
Dear Hiring Manager,

I am applying for the Macy's 2027 Tech Early Careers - Software Engineer role. I want to contribute to clearly defined projects for Macy's connected commerce technology, which serves millions of customers.

At Data Maven, I set up cloud servers and databases and limited who could reach them. I also built LedgerFlow, a payment system that never recorded a payment twice, even when I crashed its parts on purpose. Another project is LaunchOps, an employee onboarding app that guides HR, IT, managers, and new employees through their tasks.

I graduate in December 2026 and can start work in February 2027. I am open to relocating. I want to build dependable, well-tested software with the team at Macy's, drawing on LedgerFlow, where every automated test runs whenever the code changes. Thank you for considering my application.

Sincerely,
Jay Niketan Pathare
```

**elevenlabs** (role-family closing, no proof)
```text
Dear Hiring Manager,

I am applying for the Full-Stack Engineer (Backend Leaning) - Platform Engineering role at ElevenLabs. I want to build the core platform foundations that every ElevenLabs product builds on, so users, workspaces and permissions stay correct and secure.

At Thesis Mumbai Tech, I reviewed my teammates' code, mentored new hires, and restored services when a monitor caught a failure. I also built LaunchOps, an employee onboarding app where the server stops people from changing tasks that are not theirs. Another project is LedgerFlow, a payment ledger made of two services that pass events to each other.

I graduate in December 2026 and can start work in February 2027. I want to keep systems healthy at ElevenLabs. Thank you for considering my application.

Sincerely,
Jay Niketan Pathare
```

**cardinal** (hook tool list dropped; closing re-picked (tools))
```text
Dear Hiring Manager,

I am applying for the Software Engineer role at Cardinal Insurance. I want to build claims processing applications used by adjusters across the country.

At Data Maven, I set up cloud servers and databases and limited who could reach them. I also built LedgerFlow, a payment ledger made of two services that pass events to each other. Another project is LaunchOps, an employee onboarding app that guides HR, IT, managers, and new employees through their tasks.

I graduate in December 2026 and can start work in February 2027. I want to build dependable, well-tested software with the team at Cardinal Insurance, drawing on LedgerFlow, which kept every balance correct even when I crashed its parts on purpose. Thank you for considering my application.

Sincerely,
Jay Niketan Pathare
```
