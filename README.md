# Academic Paper Translator

A Codex skill for translating complete English academic papers into polished Simplified Chinese DOCX files.

## Features

- Generates a full Chinese edition and a paragraph-aligned English–Chinese edition.
- Preserves equations, tables, citation numbering, and the original English reference list.
- Translates figure titles, captions, legends, and semantic labels inside figures.
- Requires an actual Image2 edit for every raster figure containing semantic English; captions and translation panels do not count.
- Keeps original and localized figures together in the bilingual edition.
- Adds WPS-compatible citation navigation and clickable DOI links.
- Starts immediately from a supplied paper and uses resumable source-ID translation state without asking setup questions.
- Renders DOCX files through installed Microsoft Word or WPS on Windows; LibreOffice is not required.
- Applies hard quality gates for paragraph alignment, Image2 hashes, figure pairing, references, navigation, and rendered-page integrity.
- Uses no arbitrary translation time limit; verified quality takes priority.

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

> Use Academic Paper Translator now. Without asking setup questions, completely translate this English paper. Deliver an Image2 Chinese-only DOCX and a paragraph-aligned English–Chinese DOCX, preserve equations and English references, add WPS Ctrl+click citation jumps and DOI links, render every page through Word/WPS, and repair all validation failures before returning the files.

## Citation navigation and literature lookup

In Microsoft Word or WPS Writer, hold **Ctrl** and click a citation number with the **left mouse button** to jump to its reference entry. Hold **Ctrl** and left-click a DOI to open its official DOI page. Some installations are configured for single-click hyperlinks and do not require Ctrl.

If a hyperlink does not open, press **Ctrl + F** and search for the DOI, exact title, author surname, or reference number. Use lawful sources such as publisher pages, PubMed Central, institutional subscriptions, preprints, and author manuscripts.

## Example

See [Figure-interior localization and reference navigation](examples/figure-localization.md), based on Figure 1 of Yazdanpanah et al. (2026), PNAS, https://doi.org/10.1073/pnas.2513856123. The repository also includes a real accepted Image2 heatmap pair and its hash-backed audit record under `examples/`.

## Repository layout

- `SKILL.md` — core workflow
- `agents/openai.yaml` — Codex UI metadata
- `references/` — translation, figure, performance, output, and QA standards
- `scripts/` — resumable translation pipeline, Word/WPS rendering, citation linking, Image2 manifests, media replacement, contact sheets, and final validation
- `examples/` — source-grounded usage examples

## Links

- [ClawHub listing](https://clawhub.ai/fangmingqi2005-create/skills/translate-academic-papers)

## Privacy and copyright

Only process papers the user is authorized to access. Do not publish source papers or translated copyrighted content without permission.

## License

MIT. See [LICENSE](LICENSE).

