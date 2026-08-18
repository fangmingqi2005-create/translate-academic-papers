# Performance budget

Use exactly one monotonic request-to-delivery clock. Start it when the user request arrives, before any commentary, skill/reference reading, file inspection, dependency loading, or tool call. A standard paper is at most 20 pages, 120 source blocks, and 6 main figures; its hard deadline is 180 seconds. A paper exceeding any threshold is long; its hard deadline is 300 seconds. The deadline includes every tool wait, Image 2 queue, retry, validation, render, and final-response preparation.

Store `started_at`, `deadline_at`, and `cache_state` once. Every command or external request receives `deadline_at - now - 20 seconds` as its maximum timeout. Never start work whose expected duration exceeds the remaining allowance.

## Phase targets

- Request setup, skill loading, acquire, parse, and map source once: by 20% of total budget.
- Dispatch all batched translation and independent figure jobs: by 40%.
- Finish translation and figure processing: by 70%.
- Build both DOCX files and add links: by 85%.
- Structural checks and final response: final 15%, with at least 20 seconds reserved.

Overlap translation and independent figure processing where tools permit. Do not serialize independent Image 2 edits. Submit translation blocks in batches of 20-40 stable IDs with an unambiguous machine-readable response shape; reject a batch if IDs or counts differ, then retry only that batch once.

Prefer deterministic in-image text replacement for simple charts whose semantic text consists only of known axis titles, legends, or labels and whose text bounds can be identified without touching data marks. Use Image 2 for complex raster figures, schematics, or unsafe deterministic edits. Dispatch all independent Image 2 calls concurrently and permit at most one targeted retry per figure.

## Single-pass and cache rules

- Parse the PDF or authoritative HTML once and retain one canonical source map for both outputs.
- Key text cache entries by SHA-256 of source text plus translation-policy version and terminology-ledger version.
- Key figure cache entries by SHA-256 of source image plus label map plus image-edit prompt version.
- Reuse an entry only after its prior acceptance record passes the current validation rule.
- Build both document variants from the same in-memory records in one process.
- Patch a local defect and rerun its validator; do not restart extraction or translation.

## Deadline behavior

At 40%, fail fast if mapping is incomplete or jobs are not dispatched. At 70%, stop optional typography refinement and prohibit restarting extraction, translation, or the complete build. At 90%, stop regeneration and run only deterministic packaging, existence, counts, pairing, media, bookmark, hyperlink, and XML checks. Perform at most one render pass when the renderer is already available; do not spend the deadline discovering or installing a renderer.

If an external translator or image service does not return before the hard deadline, terminate the attempt, retain valid partial cache entries, and label the result as a timed-out draft. Never claim that the deadline was met by excluding external service wait time.

## Reporting

Report wall-clock seconds from receipt of the user's request through final delivery. Never substitute a substage measurement such as translation-only, rebuild-only, or cache-only time. Label the run:

- `cold-cache`: no accepted translation or figure-edit cache was reused;
- `warm-cache`: at least one accepted cached translation or figure was reused.

Do not compare a warm-cache result with a cold-cache target without naming it explicitly. If the true request-receipt timestamp is unavailable, state that exact timing could not be proven; do not invent a shorter duration.
