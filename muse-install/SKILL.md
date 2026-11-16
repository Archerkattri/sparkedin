# Sparkedin

- Sparkedin is thirteen LinkedIn skills that execute through your tools. Each one lives in its own file under `skills/` beside this file.

- Match the user's request to one command below, read that command's `SKILL.md` first, then follow it. Never act from this router alone.

- Run the humanizer scripts with `muse.exec` before you show the user any LinkedIn text. The scripts live at `skills/sp-human/humanize.py` and `skills/sp-human/detect.py` and need Python 3 with no extra packages.

## Run a command

- Read the sub-skill file at `skills/<command>/SKILL.md` before you do anything for that command. The file holds the full method.

- Follow the sub-skill file for what to ask, what to write, what to check and what to send.

- Execute through the host tools when the user says go. The approval flow is the gate. No caps live in the skill.

- Log what you posted or sent to `<profile>/log.md` with the date and the first line, so `sp-audit` has a history to work from.

## The commands

- `/sp-post` writes a LinkedIn post from one idea with three hook options and one full draft. Read `skills/sp-post/SKILL.md`.

- `/sp-comment` writes comments on other people's posts in one of nine types. Read `skills/sp-comment/SKILL.md`.

- `/sp-reply` drafts replies to the comments under the user's own post, triaged first. Read `skills/sp-reply/SKILL.md`.

- `/sp-profile` scores a LinkedIn profile out of 100 and rewrites what lost points. Read `skills/sp-profile/SKILL.md`.

- `/sp-plan` builds the week on LinkedIn and writes `<profile>/plan.md`. Read `skills/sp-plan/SKILL.md`.

- `/sp-human` strips the machine fingerprint out of a draft and scores it on five checks. Read `skills/sp-human/SKILL.md`.

- `/sp-carousel` builds a document post as slide copy and a PDF. Read `skills/sp-carousel/SKILL.md`.

- `/sp-repurpose` turns one long asset into a week of posts. Read `skills/sp-repurpose/SKILL.md`.

- `/sp-dm` writes the invite note, the first message and the two follow-ups. Read `skills/sp-dm/SKILL.md`.

- `/sp-outreach` runs a whole outreach campaign: picks the path first, then writes the note, the DM, the thank-you and the two follow-ups, and tracks every target. Read `skills/sp-outreach/SKILL.md`.

- `/sp-inbox` triages the LinkedIn inbox and drafts the replies worth sending. Read `skills/sp-inbox/SKILL.md`.

- `/sp-audit` audits what the user already published and finds what worked. Read `skills/sp-audit/SKILL.md`.

- `/sp-stats` pulls the user's own LinkedIn posts and engagement into local JSON and builds a dashboard. Experimental. Read `skills/sp-stats/SKILL.md`.

## Voice and profile

- Read the user's voice from memory first, then from `<profile>/voice.md` when it exists. Never invent a voice.

- The profile directory on Muse is `~/workspace/linkedin/`. It holds `voice.md`, `log.md` and `plan.md`.

- Never invent a metric, client or outcome under the user's name. When a draft needs a number the user has not given, leave `{{your number}}` in it and flag it.

## Available connectors

- Use `browser.browse` for LinkedIn in the user's own Chrome through the Muse for Chrome extension, or the cloud browser when the user has not chosen one.

- Use the GitHub connector at `/opt/hatch/connectors/github/CONNECTOR.md` for the Sparkedin repo itself.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
