# Contributing

Thanks for helping improve Gift Finder.

## What is useful

- **Real conversations that went badly.** Open an issue with what you asked, what the skill did, and what you expected. Remove personal details first.
- **Better refinement questions** for a gift category (Step 4 in `SKILL.md`).
- **New special situations**, such as an occasion or constraint the skill handles poorly.

## Making a change

1. Fork the repository and create a branch.
2. Edit `skills/gift-finder/SKILL.md`. Keep it under 500 lines and explain the reason behind any new instruction, so the agent can apply it with judgement.
3. Run the check:

   ```bash
   python3 scripts/validate.py
   ```

4. Try the skill on at least two different requests, one detailed and one vague, and describe the results in your pull request.
5. If behaviour changes, bump `version` in `SKILL.md`, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, and add a line to `CHANGELOG.md`.

## Principles to keep

- Few questions. Every question must change the outcome.
- Stated interests outrank age and gender.
- No invented products, prices or links, and no affiliate links.
