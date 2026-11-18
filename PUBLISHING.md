# Publishing checklist

Everything here assumes the GitHub account `toxx663` and the repository name `gift-finder`. If you use another name, search and replace `toxx663/gift-finder` across the repository first.

## 1. Publish on GitHub

```bash
cd gift-finder
python3 scripts/validate.py

git init -b main
git add -A
git commit -m "Release gift-finder v1.1.0"

gh repo create toxx663/gift-finder --public --source . --push \
  --description "Agent skill that finds well-researched gifts: short interview, category shortlist, live product research, three concrete picks."

gh repo edit toxx663/gift-finder \
  --add-topic agent-skills --add-topic agent-skill --add-topic claude-skills \
  --add-topic claude-code --add-topic claude-code-plugin --add-topic skill-md \
  --add-topic gift-ideas

git tag v1.1.0
git push origin v1.1.0
```

Pushing the tag runs the release workflow, which attaches `gift-finder.zip` to a GitHub release. That zip is what people upload in the Claude apps.

## 2. Check that it installs

```bash
npx skills add toxx663/gift-finder --list
```

In Claude Code:

```
/plugin marketplace add toxx663/gift-finder
/plugin install gift-finder@toxx663-skills
```

Then run `/gift-finder` once with a vague request and once with a detailed one.

## 3. List it in skill directories

Directory rules change often. Check each site's current submission page before relying on the notes below.

| Directory | How a skill gets listed |
|---|---|
| skills.sh | Built around `npx skills add owner/repo`. Your page lives at `skills.sh/toxx663/gift-finder`. Listing is driven by installs through the CLI; if the page does not appear, look for an index request option on the site. |
| skillsmp.com | Indexes public GitHub repositories that contain a `SKILL.md`. Usually no action needed beyond a public repo and topics. |
| agentskill.sh | Has a submit form: paste the GitHub repository URL and it imports every `SKILL.md`. |
| Awesome lists on GitHub (for example `awesome-claude-skills`) | Open a pull request adding one line, following that list's contributing rules. |

## 4. Listing copy

Use these when a form asks for them.

**Name:** Gift Finder

**Slug:** `gift-finder`

**Tagline (under 60 characters):** Well-researched gifts in a five-minute conversation

**Short description (under 160 characters):**
Asks a few quick questions, suggests gift categories, then researches the one you pick and returns three concrete products with prices and buy links.

**Long description:**
Gift Finder turns "what should I get them?" into a short guided conversation. It asks who the gift is for, what they enjoy and what you want to spend, never repeating a question you already answered. It then proposes four to six concrete gift categories. Pick one and it asks the one or two questions that decide which product is best, researches independent tests and reviews on the web, checks current prices and availability in your country, and returns three picks: best overall, best value and a wildcard. Each pick comes with the reason it fits, an honest trade-off and a direct buy link on Amazon or another shop that delivers to you. Choose one and it runs a final check: compatibility with what the person already owns, colour or size, and anything missing from the box. No invented products, no affiliate links.

**Category:** Lifestyle / Shopping / Personal

**Tags:** gifts, gift-ideas, shopping, recommendations, product-research, personal-assistant

**Requirements:** Web search

**License:** MIT

**Install command:** `npx skills add toxx663/gift-finder`

## 5. Releasing an update

1. Edit `skills/gift-finder/SKILL.md`.
2. Bump the version in `SKILL.md`, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (the validator fails if they differ).
3. Add an entry to `CHANGELOG.md`.
4. Commit, then `git tag vX.Y.Z && git push origin main vX.Y.Z`.
