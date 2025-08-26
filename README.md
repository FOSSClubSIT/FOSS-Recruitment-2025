# FOSS Recruitment — Contribution Round

Welcome! 🎉 This is the **hands-on round** for FOSS recruitment.  
Instead of a typical interview, you’ll complete a **24-hour open-source style project**.

---

## Process
1. Attend the 1-hour Git/GitHub session.
2. Fork this repo or create a branch from `main` in your fork.

4. Add your project under:
   ```
   projects/lastname_firstname/
   ```
5. Inside your folder, include:
   - `README.md` (problem, features, run instructions)
   - Your project files (src/, docs/, etc.)
   - Optional (NO NEED FOR FRESHERS): `.env.example`
6. Commit & push, Open a PR to **`main`** within 24 hours.

## Rules
- Use of AI tools is allowed and encouraged, but:
  - You must list all AI tools used in your project’s README.
  - We will not judge you for using AI code.
  - Evaluation will focus on idea, workflow, implementation, and thought process — not just the code.

- Work solo — no copy-pasted or team projects.
- Keep commits clean & meaningful.
- Do not modify files outside your own submission folder (`projects/lastname_firstname/`).
- Large binaries or secrets are not allowed.


### 🚨 Instant Disqualification If:
1. **Seeking help from anyone** except:
   - FOSS Core team
   - Recruitment Round 1 In-Charge (Abshiek)
2. **Modifying or deleting any file outside your own folder** under `projects/lastname_firstname/`

## API Usage Policy
- APIs are **optional** (not mandatory).  
- If you use one:
  - Include the integration **code** in your submission.
  - Provide a `.env.example` file (no real keys).
  - Your project must run in **offline mode by default** with sample/mock data.
  - Document offline vs. online steps in your README.
- Reviewers will test your project **offline only**.

## Evaluation
You will be judged on:
- Git usage & PR hygiene
- Code quality
- Documentation & clarity
- Creativity
- Completion within 24h

See [`EVALUATION.md`](./EVALUATION.md) for details.

## Tips & Tricks

- If you are a fresher or new to coding — do not worry about giving a “perfect” project.  
  Focus on **completing something functional** within the 24 hours. Completion matters more than perfection.
- Start small, then improve — a working minimal project is better than a broken big idea.
- Document everything — even 2–3 lines about why you did something shows clarity of thought.
- Commit often — don’t push one giant commit at the end. It helps show your workflow.
- Test offline mode thoroughly — reviewers will only run your project offline.
- Use clear folder structure — e.g., `src/`, `docs/`, `sample_output/`.
- Add screenshots or demo output if possible — visuals help us quickly understand your project.
- If using APIs, cache responses into `sample_output/` and default to offline mode.
- Don’t be afraid to use AI tools — just remember to list them in your README.
- Time management — 24 hours sounds long, but plan:  
  - 2–3 hours: brainstorming & setup  
  - 12–14 hours: coding & implementation  
  - 4–5 hours: documentation & polishing
