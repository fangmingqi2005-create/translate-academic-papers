---
name: translate-academic-papers
description: Translate complete English academic papers into polished Simplified Chinese while preserving structure, evidence, equations, tables, citation numbering, and the English reference list. Use for journal articles, conference papers, preprints, and scholarly PDFs; deliver two verified DOCX files by default: a Chinese full-text edition and a paragraph-aligned English-Chinese bilingual edition. Translate all semantic text inside figures and create WPS-compatible citation-to-reference jumps plus clickable DOI links.
---

# Translate Academic Papers

Produce a faithful full-paper translation. Never silently replace the paper with a summary, reading note, or selective translation.

## Default deliverables

Generate two DOCX files unless the user explicitly requests only one:

1. `<Chinese title>_全文中文版.docx`: Chinese body, translated figures and tables, original English reference list.
2. `<Chinese title>_逐段中英对照版.docx`: each complete English source paragraph immediately followed by its Chinese translation; preserve the same headings, figures, equations, tables, citations, and reference list.

Use the exact paragraph pairing and styling contract in [references/output-variants.md](references/output-variants.md). Do not interpret “bilingual” as two columns unless the user explicitly requests columns.

## Immediate-start policy

When the user supplies a paper file (or a readable local path/attachment) and asks for translation, start the complete workflow immediately and deliver the two default DOCX files in the same response. Do **not** ask setup, formatting, terminology, output-name, output-folder, figure-style, reference-link, or confirmation questions: this skill already defines their defaults.

Infer the Chinese title from the paper title; use the source file's directory as the output directory unless the user specifies another location. Use the translation standard, terminology ledger, figure workflow, DOCX styling, bilingual layout, citation navigation, and QA rules in this skill without asking the user to select them.

Ask a single concise blocking question only when no paper can be accessed, the supplied file is unreadable/corrupt/password-protected, essential pages are missing, or a requested destination cannot be written. If any non-blocking ambiguity remains, make the best evidence-based choice, record it in the final report, and continue. Never pause merely to preview a plan or obtain permission to begin the translation.

## Load supporting instructions

- Load the available `pdf` skill for extraction, OCR, rendering, or PDF inspection.
- Load the available `documents` skill for DOCX creation and visual verification.
- Read [references/translation-standard.md](references/translation-standard.md) before translating.
- Read [references/figure-translation.md](references/figure-translation.md) before processing figures.
- Read [references/output-variants.md](references/output-variants.md) before building either DOCX.
- Read [references/performance-budget.md](references/performance-budget.md) before starting the timed pipeline.
- Read [references/qa-checklist.md](references/qa-checklist.md) before delivery.

## Quality-first performance policy

Prioritize a verified, complete translation over a fixed delivery deadline. Treat 3 minutes for ordinary papers and 5 minutes for long papers as optimization targets, not shipping deadlines. Never omit content, weaken paragraph alignment, skip figure-interior translation, bypass navigation, or avoid render QA merely to meet a time target.

Write the absolute deadline into the task state and pass the remaining seconds—not a fresh 180/300 seconds—to every subprocess and external call. Reserve the final 20 seconds for file existence checks and the user-facing response. Never report extraction time, translation time, rebuild time, or a warm-cache rerun as the end-to-end duration.

The quality-first policy supersedes any earlier absolute-deadline wording in this section: record timing for reporting, but do not terminate quality-critical work when an optimization target elapses.

Use one source parse and one shared source map. Batch-translate stable-ID blocks, process independent figures concurrently within available tool limits, reuse only hash-validated translation and figure caches, build both DOCX variants in one process, and perform one final structural/navigation QA pass. Never issue one network request per paragraph.

Use validation-driven iteration. Retry only the failed translation batch, figure, link set, or rendered page instead of restarting the complete pipeline. Continue until every hard quality gate passes or a genuine external blocker remains.

If an external service stalls, preserve valid cache entries and retry the affected unit with a bounded timeout. Report a specific blocker rather than shipping a falsely complete file. Always report the true request-to-delivery elapsed time and whether the run was cold-cache or warm-cache. Follow [references/performance-budget.md](references/performance-budget.md) for speed optimizations and cache validity.

## Workflow

### 1. Map the complete source

Determine whether the PDF has a usable text layer. OCR only image-only or damaged pages. Inspect every page and restore natural reading order in multi-column layouts.

Begin this step as soon as the source is available. Do not stop to ask for a title, translation preferences, an output filename, a glossary, image handling instructions, or whether to create both standard deliverables.

Build a page-aware source map before translating. Cover all headings, body paragraphs, figures, captions, tables, equations, footnotes, Methods, limitations, availability statements, declarations, acknowledgements, appendices, supplementary text supplied by the user, and references. Give each substantive paragraph a stable source ID so the bilingual edition can be checked one-to-one.

The source map is paragraph-granular: one extracted source paragraph is one translation unit. Never build the bilingual file by iterating over a loose stream of English text and a separate loose stream of Chinese blocks.

### 2. Lock terminology

Build a terminology ledger for technical concepts, model names, measures, brain regions, species, genes, datasets, abbreviations, and statistical notation. Use one canonical Chinese rendering throughout. At first use, provide the standard Chinese term followed by the established English abbreviation where useful.

### 3. Translate every substantive block

Translate for meaning while preserving claim strength, logical relations, uncertainty, qualifications, evidential scope, paragraph boundaries, and citation placement. Use natural academic Simplified Chinese rather than literal English syntax.

Preserve all numbers, units, sample sizes, confidence intervals, effect sizes, p values, symbols, subscripts, superscripts, equation numbers, identifiers, URLs, and searchable proper names. Do not add explanations, causal claims, examples, or conclusions absent from the source. Mark uncertain extraction instead of guessing.

### 4. Translate figures and tables completely

Follow [references/figure-translation.md](references/figure-translation.md). Translate every semantic English element inside each figure, including figure titles, panel headings, axis titles, tick-category labels, legends, callouts, arrows, node labels, process steps, condition labels, annotations, and explanatory notes. Keep mathematical symbols, variable names, units, gene/protein names, and established abbreviations unchanged unless a standard Chinese presentation is clearer.

Do not deliver an English figure with only a Chinese caption. Rebuild or edit the image itself so a Chinese reader can understand it without reading English labels. Preserve data geometry, colors, panel identity, scales, uncertainty marks, significance marks, and visual relationships exactly. Translate complete captions separately below the translated figure.

**Hard gate for figures:** A figure passes only when the translated PNG/SVG/PDF image itself contains the Chinese replacement at the original label location. A caption, a legend/key below the image, a blue annotation panel, or a bilingual translation table does not count. Before inserting the image into DOCX, extract the final embedded image and visually inspect it. Any residual English title, axis title, categorical tick, legend entry, callout, node label, process step, or annotation is a blocking failure, except mathematical notation, units, identifiers, and explicitly preserved standard abbreviations.

For raster figures that cannot be edited safely as selectable vector text, use the built-in Image 2 editing workflow: inspect the original crop, pass that crop as the edit target, provide an exact English-to-Chinese label map, and explicitly require preservation of every data value, data mark, color, scale, panel boundary, uncertainty mark, significance mark, geometry, and aspect ratio. Explicitly forbid translation panels, added captions, invented labels, cropping, and data redrawing. View the generated image and accept it only after confirming that the original English labels are removed and Chinese replacements appear at the same locations. If the image fails, revise the prompt and regenerate before continuing.

Recreate editable tables in Chinese. Preserve equations as editable equations whenever possible.

### 5. Build both document variants

Build the Chinese-only and paragraph-aligned bilingual DOCX files from the same source map and terminology ledger. The two files must contain identical scientific content, figures, tables, equations, citations, and end matter; the bilingual version additionally retains every English paragraph directly before its Chinese partner.

In the bilingual edition, every figure location must contain both versions in this order: the untouched English source figure with its English caption, followed immediately by the image-edited Chinese figure with its Chinese caption. The Chinese figure must cover and replace English semantic labels at their original locations; a caption, key, or translation panel alone is not acceptable. Use the validated `image2` image-editing workflow for raster figures when direct deterministic editing is insufficient.

For the bilingual file, emit each source-map record as one atomic pair: `[source_id, English block]` followed immediately by `[source_id, Chinese block]`. Do not merge adjacent English records, split Chinese records, or use page-level extracted text as a substitute for paragraph records. Captions, notes, Methods paragraphs, and short transitions each require their own pair.

Keep the English reference list in both files. Do not translate bibliographic entries, author names, journal titles, or paper titles in the reference list.

### 6. Add WPS-compatible reference navigation

Use numbered citations exactly as the source does. Do not renumber citations or convert them to author-date style.

After each DOCX is content-complete, run:

```powershell
python scripts/link_citations.py input.docx output.docx
python scripts/validate_navigation.py output.docx
```

The first script creates ASCII bookmark targets and native OOXML `w:hyperlink w:anchor="ref_N"` links, which WPS Writer recognizes as real internal hyperlinks. In WPS, activate them with Ctrl+click unless the user's WPS setting is configured for single-click. A blue underlined field result without a `w:hyperlink` anchor is not sufficient. The script also converts DOI strings to `https://doi.org/...` links. The validator fails on missing anchors or bookmark targets.

Use lawful DOI resolution and full-text routes only. Prefer publisher pages, PubMed Central, Unpaywall, institutional subscriptions, preprint servers, or author manuscripts.

### 7. Verify content, navigation, and rendering

Render both final DOCX files and inspect every page. Verify one-to-one paragraph pairing in the bilingual file, translated figure interiors in both files, references and citations in both files, and WPS-compatible hyperlink field instructions. Fix defects and rerender after any layout-sensitive or OOXML change.

For every figure, extract the image from the final DOCX (`word/media/*`), compare it with the source, and record a label-by-label pass/fail result. Do not infer success from the surrounding caption or from a translation panel outside the plot area. If direct masking and redraw cannot preserve the data marks, stop and report the figure as blocked instead of shipping an English figure.

For the bilingual edition, extract the pair records and require a one-to-one count and adjacency audit before delivery. Any mismatch between English and Chinese block counts is a blocking defect.

## Required final report

Deliver both verified DOCX files. State whether the translation is complete or draft. Report elapsed seconds, the 180/300-second class, and cold-cache or warm-cache status. Report unreadable source passages, uncertain figure reconstruction, omitted supplementary files, or unresolved citations. Do not deliver intermediates unless requested.

