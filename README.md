# Academic Paper Translator

A Codex skill for translating complete English academic papers into polished Simplified Chinese DOCX files.

## Features

- Generates a full Chinese edition and a paragraph-aligned English–Chinese edition.
- Preserves equations, tables, citation numbering, and the original English reference list.
- Translates figure titles, captions, legends, and semantic labels inside figures.
- Keeps original and localized figures together in the bilingual edition.
- Adds WPS-compatible citation navigation and clickable DOI links.
- Applies quality gates for paragraph alignment, figures, references, and DOCX integrity.

## Installation

Copy this repository to:

```text
~/.codex/skills/translate-academic-papers
```

On Windows, the typical location is:

```text
C:\Users\<username>\.codex\skills\translate-academic-papers
```

The repository root contains `SKILL.md`.

## Usage

> Use Academic Paper Translator to translate this English paper. Generate a full Chinese DOCX and a paragraph-aligned English–Chinese DOCX. Translate all figure labels in place and preserve equations and references.

## Repository layout

- `SKILL.md` — core workflow
- `agents/openai.yaml` — Codex UI metadata
- `references/` — translation, figure, performance, output, and QA standards
- `scripts/` — citation linking, navigation validation, and timing helpers

## Links

- [ClawHub listing](https://clawhub.ai/fangmingqi2005-create/skills/translate-academic-papers)

## Privacy and copyright

Only process papers the user is authorized to access. Do not publish source papers or translated copyrighted content without permission.

## License

MIT. See [LICENSE](LICENSE).
