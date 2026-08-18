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

## Citation navigation and literature lookup

In Microsoft Word or WPS Writer, hold **Ctrl** and click a citation number with the **left mouse button** to jump to its reference entry. Hold **Ctrl** and left-click a DOI to open its official DOI page. Some installations are configured for single-click hyperlinks and do not require Ctrl.

If a hyperlink does not open, press **Ctrl + F** and search for the DOI, exact title, author surname, or reference number. Use lawful sources such as publisher pages, PubMed Central, institutional subscriptions, preprints, and author manuscripts.

## Example

See [Figure-interior localization and reference navigation](examples/figure-localization.md), based on Figure 1 of Yazdanpanah et al. (2026), PNAS, https://doi.org/10.1073/pnas.2513856123.

## Repository layout

- `SKILL.md` — core workflow
- `agents/openai.yaml` — Codex UI metadata
- `references/` — translation, figure, performance, output, and QA standards
- `scripts/` — citation linking, navigation validation, and timing helpers
- `examples/` — source-grounded usage examples

## Links

- [ClawHub listing](https://clawhub.ai/fangmingqi2005-create/skills/translate-academic-papers)

## Privacy and copyright

Only process papers the user is authorized to access. Do not publish source papers or translated copyrighted content without permission.

## License

MIT. See [LICENSE](LICENSE).
