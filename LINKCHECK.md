# Cross-reference check — 19 Oct 2026

Scope: the `staged` body of all 83 sections across the 33 parts in `model.json`.

Found 143 Markdown links to `registry.igem.org/parts/`, 224 bare `BBa_…` mentions, and 40 distinct
part ids between them. Every one of the 40 was fetched from
`GET https://api.registry.igem.org/v1/parts/slugs/{slug}` and cached, so every "real title" and
"status" below is API-verified rather than taken from `model.json`.

## Counts

| Class | Occurrences | Distinct defects | Parts affected |
|---|---|---|---|
| Dead link | 0 | 0 | — |
| Mismatched link | 3 | 2 | BBa_2654HAF3, BBa_26U8UTMH, BBa_26XVQ3FS |
| Id/URL disagreement | 4 | 1 | BBa_2654HAF3, BBa_26U8UTMH, BBa_26XZYM10 |
| Broken Markdown | 1 | 1 | BBa_261XH2RS |
| Link to a `draft` part | 0 | 0 | — |

Four further occurrences are label typos where the link target is correct; they are listed
separately below rather than counted as mismatches.

## Dead link

None. All 40 distinct ids returned HTTP 200 with a part record. The seven ids that appear only as
bare text and are never linked (`BBa_254UKC9E`, `BBa_B0015`, `BBa_K143012`, `BBa_K2675031`,
`BBa_K3317069`, `BBa_K5431017`, `BBa_K823000`) all exist and are published too.

## Mismatched link

### BBa_2654HAF3 — design

> `ccaS-m3 ([BBa\_26OSLRE4](https://registry.igem.org/parts/bba-26oslre4))- B0015 (BBa\_B0015). `

The visible name is *ccaS-m3*, but `BBa_26OSLRE4` is **RBS0** (API-verified, published). The same
sentence already carries RBS0's own correct citation a few words earlier
(`RBS0  (BBa\_26OSLRE4)-`), so the id has been repeated onto the wrong element.

Correct target: `https://registry.igem.org/parts/bba-k3317069` — `BBa_K3317069`, title `ccaSm3*`,
published. Corroborated by BBa_261XH2RS's own design text, which writes `*ccaS-m3* (BBa\_K3317069)`.

### BBa_26U8UTMH — design

> `ccaS-m3 ([BBa\_26OSLRE4](https://registry.igem.org/parts/bba-26oslre4))- B0015 (BBa\_B0015). `

Identical defect, identical correct target. The Light Sensing paragraph is duplicated verbatim
between BBa_2654HAF3 and BBa_26U8UTMH, so the error travelled with it.

### BBa_26XVQ3FS — design

> `SamyQ-AcdS 2.1-Histag (**[BBa\_26NXOP7S](https://registry.igem.org/parts/bba-26nxop7s)**):** a translational fusion of `

The visible name is *SamyQ-AcdS 2.1-Histag*, but `BBa_26NXOP7S` is **Csn-AcdS-Histag**
(API-verified, published) — the Csn-signal-peptide sibling, not the SamyQ one.

Correct target: `https://registry.igem.org/parts/bba-26toglx3` — `BBa_26TOGLX3`, title
`SamyQ-AcdS 2.1-Histag`, published. The titles match exactly.

All three of these were flagged in advance and are confirmed. The sweep found no additional
mismatches: every other link's surrounding name matches its target's real title, and the numbered
module labels (`1. PCB production`, `2. Light Sensing`, `4. Light responsive`, `2. Transduction`,
`1. SamyQ signal peptide`, and the `AcdS` / `BoPep4` / `LEA14` variant headings) plus the generic
descriptor `the protectant CDS fusion` were all checked individually and are legitimate.

Two cases look like mismatches to a pattern match but are not. In BBa_2654HAF3 design,
`Csn– AcdS – 6xHis ([BBa\_26NXOP7S]…)` sits inside a longer `PcpcG2-veg – EEBD – RBS0 – … – B0015`
module description; the citation attaches to the fusion element, which really is Csn-AcdS-Histag.
BBa_26U8UTMH design has the same shape with `SamyQ– AcdS 2.1– 6xHis ([BBa\_26TOGLX3]…)`, also
correct.

### Label typos — link target is right, visible name is wrong

These are not wrong-target errors, so they are listed apart. In each case the URL points at exactly
the part the sentence means; the name beside it is misspelled.

| Part | Section | Quoted text | What is wrong |
|---|---|---|---|
| BBa_269A97I7 | experiment | `SamyQ-BoPep 2.1-Histag ([BBa\_26PX0UGH](https://registry.igem.org/parts/bba-26px0ugh))` | Real title is `SamyQ-BoPep4 2.1-Histag`; the `4` is dropped from BoPep4 |
| BBa_26IA55UY | experiment | `SamyQ-BoPep 2.2-Histag ([BBa\_267B69E3](https://registry.igem.org/parts/bba-267b69e3))` | Real title is `SamyQ-BoPep4 2.2-Histag`; same dropped `4` |
| BBa_26IN6G1D | application | `* **Pveg-EEBD-RBS0-SamyQ-LEA14-Histag 2.1-B0015** ([<u>BBa\_26D5AX7S</u>](https://registry.igem.org/parts/bba-26d5ax7s))` | Real title is `Pveg-EEBD-RBS0-SamyQ-LEA14 2.1-Histag-B0015`; the `2.1` sits after `Histag` instead of after `LEA14` |
| BBa_26J0GJGZ | application | same string | same |

## Id/URL disagreement

One defect, four occurrences: the id `BBa_K2675031` is always labelled correctly but always linked
to a Google share-link shortener instead of a registry part URL. There is no slug in the URL at all,
so there is nothing for the id to agree with.

| Part | Section | Quoted text |
|---|---|---|
| BBa_2654HAF3 | design | `-L3S2P21 ([<u>**BBa\_K2675031**</u>](https://share.google/pocPiJukHq9mm39e5)). Ho1 converts heme to b` |
| BBa_26U8UTMH | design | `-L3S2P21 ([<u>**BBa\_K2675031**</u>](https://share.google/pocPiJukHq9mm39e5)). Ho1 converts heme to b` |
| BBa_26XZYM10 | design | `L3S2P21 (**[<u>**BBa\_K2675031**</u>](https://share.google/pocPiJukHq9mm39e5)**):** a strong synthetic` |
| BBa_26XZYM10 | design (reference list) | `4. [<u>**BBa\_K2675031**</u>](https://share.google/pocPiJukHq9mm39e5)` |

Correct target: `https://registry.igem.org/parts/bba-k2675031` — `BBa_K2675031`, title
`L3S2P21 Terminator`, published, API-verified. The share.google URL itself was **not** followed, so
where it actually resolves is unverified; the id in the label was verified against the API
independently.

No other id/URL disagreement exists. All 143 registry links were compared id-against-slug and every
one agrees; every URL also matches the canonical `https://registry.igem.org/parts/<lowercase-slug>`
shape, with no uppercase slugs, no underscores, no trailing slashes and no query strings.

## Broken Markdown

### BBa_261XH2RS — experiment

> `Assembly method: Golden Gate, \[BsaI-HFv2 enzyme` + newline + `* Thermal cycle:`

An unresolved bracket placeholder with no closing `]`. This is the only unbalanced bracket in all 83
sections — every other `\[…]` placeholder in the pack closes properly. Because the `[` is escaped,
a CommonMark renderer shows it as a literal `[` rather than swallowing the rest of the section, but
the reader still sees a stray bracket, and a more permissive renderer could pair it with the `]` of
the `![](…)` image further down the same section and eat roughly 1,600 characters of DETAILS,
Verification and primer-table content.

Fix: close it, as `\[BsaI-HFv2 enzyme]`. Note the part's own Design section states the assembly
enzyme unbracketed ("Golden gate assembly with BsaI-HFv2"), so the value is corroborated even though
resolving it is a separate editorial call.

No other malformed link syntax was found: no nested `[` inside any label, no unclosed `](`, no `](`
without an opening bracket, and no bare parenthesised registry URL missing its label.

## Links to draft parts

None. All 40 linked or mentioned ids came back `status: "published"`.

`model.json` holds two draft parts — `BBa_26YHOQCL` (`Bopep4 (15-23)`) and `BBa_26Z8FHTR`
(`Pveg-EEBD-RBS0-SamyQ-Bopep4-Histag (9-23)-B0015`). Both were fetched and both are confirmed
`draft` by the API, but neither is linked to or even mentioned in any staged body, so no reader-facing
link can look broken on their account. Both also have no sections of their own.

## Minor, cosmetic

Not defects in any of the four classes; noted because they are in the same sentences.

- Missing space before a link: BBa_262YYNPV application has `after[<u>BBa\_26XZYM10</u>](…)`,
  `,[<u>BBa\_261XH2RS</u>](…)` and `and[<u>BBa\_26BDO8AQ</u>](…)`. BBa_26MA70QI and BBa_26TOGLX3
  application carry the same three links with the space moved inside the label instead
  (`after[ <u>BBa\_26XZYM10</u>]`). BBa_26NXOP7S application has the same sentence spaced correctly,
  which is the version to copy.
- Stray space before a closing parenthesis: `ho1:pcyA ([<u>**BBa\_K4354012**</u>](https://registry.igem.org/parts/bba-k4354012) )`
  in BBa_2654HAF3 design and BBa_26U8UTMH design.

## Method

Links were matched as `[label](https://registry.igem.org/parts/<slug>)` over `staged` only, with
escaped underscores normalised (`BBa\_26ZQ1T72` → `BBa_26ZQ1T72`) and slugs lowercased before
comparison. Because every one of the 143 registry links carries the part id as its label, with the
human-readable name sitting in the text just before the opening parenthesis, the mismatch check
compares that preceding name against the API title, and each non-matching candidate was then read in
context by hand. Non-registry Markdown links were swept separately for BBa ids, which is how the
share.google case surfaced. Each id was fetched once, cached to disk, with 3.5 s between calls and
escalating backoff on 429; no 429 was hit.
