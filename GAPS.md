# Registry pull — 33 parts, 19 Oct 2026

Pulled from `api.registry.igem.org/v1` (public, unauthenticated). Raw JSON per part in `raw/`, one row per part in `inventory.csv`.

Every documentation body is **raw Markdown** — what is in `value` is exactly what the registry editor holds, so it round-trips by copy-paste with no conversion.

## Coverage

| | design | experiment | characterisation | application | discussion | docs | images |
|---|---|---|---|---|---|---|---|
| light (4) | 3/4 | 3/4 | 0/4 | 3/4 | 0/4 | 9 | 3 |
| hybrid (4) | 4/4 | 4/4 | 2/4 | 4/4 | 2/4 | 16 | 6 |
| protectant (23) | 21/23 | 14/23 | 2/23 | 20/23 | 1/23 | 58 | 10 |
| shared (2) | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 | 0 | 0 |

## What is missing

**5 parts have no documentation at all:** `BBa_26A4MT29` (PtagC+RBS), `BBa_26OSLRE4` (RBS0), `BBa_26V6CPEV` (EEBD-RBS0), `BBa_26YHOQCL` (Bopep4 (15-23)), `BBa_26Z8FHTR` (Pveg-EEBD-RBS0-SamyQ-Bopep4-Histag (9-23)-B0015)

**All 4 characterisation entries are a figure legend with no figure** — 0 images between them. These are the Western blots:

- `BBa_2654HAF3` — 144 words, 0 images — **Fig.1. Western blot of wild-type ACCD in *Bacillus subtilis* WB800 carrying CcaSR under diffe…
- `BBa_26CXI09X` — 141 words, 0 images — **Fig. 1. Western blot analysis of constitutive ACC deaminase expression in *Bacillus subtilis*…
- `BBa_26U8UTMH` — 150 words, 0 images — **Fig.1. Level 2 optogenetic control of His-tagged ACC deaminase expression (ABDQ).** Cells wer…
- `BBa_26XVQ3FS` — 63 words, 0 images — **Fig. X. Western blot analysis of constitutive ACC deaminase-2.1-Histag expression in *Bacillu…

**5 figure captions have no image above them:**

- `BBa_26CXI09X` [experiment] Figure 1 — *** **Colony PCR of pSTK-EXP1-Pveg-EEBD-RBS0-Csn-AcdS-Histag…
- `BBa_26CXI09X` [experiment] Figure 2 — *** **Clone 1 was sequence-verified and used downstream.**…
- `BBa_26FSZTWM` [experiment] Figure 1 — Sequencing of pSTK-EXP1-Pveg-EEBD-RBS0-SamyQ-BoPep4-Histag-B…
- `BBa_26XVQ3FS` [experiment] Figure 1 — *** **Colony PCR of pSTK-EXP1-Pveg-EEBD-RBS0-SamyQ-AcdS 2.1-…
- `BBa_26XVQ3FS` [experiment] Figure 2 — *** **Clone 1 was sequence-verified and used downstream.**…

**118 unfilled `[bracket]` placeholders, 44 distinct, live on public pages.** Most frequent:

- `[168 / WB800]` × 19
- `[ampicillin]` × 10
- `[BsaI-HFv2 enzyme]` × 10
- `[X]` × 7
- `[177 bp]` × 4
- `[536 bp]` × 4
- `[678 bp]` × 4
- `[1122 bp]` × 4
- `[GenBank sequence CP103783.1]` × 3
- `[1588 bp]` × 3
- `[60 °C]` × 2
- `[1602 bp]` × 2

The 19 `[168 / WB800]` all resolve to **WB800** (settled 7 Oct). The ~20 distinct `[N bp]` values are expected-band sizes that need computing from the sequences, which we now have.

## Two things that are not defects

The `-sfGFP` suffix on vector names (`pSTK-0C-sfGFP`, `pSTK-1A/1B/1C/1D-sfGFP`, `pSTK-EXP1-sfGFP`, `pSTK-EXP2-sfGFP`) is the SubtiToolKit dropout-cassette naming, used consistently across all 33 parts — not a copy-paste leftover. The only wrinkle is that the same vector is sometimes written with the suffix and sometimes without, which is worth normalising.

No two of the 33 sequences are identical, so neither draft duplicates an existing part and both are documentable. Version families share a length but differ in sequence: 69 bp (BoPep4 / 2.1 / 2.2), 183 bp (SamyQ-BoPep4 / 2.1 / 2.2), 450 bp (LEA14 / 2.1), 712 bp (three Pveg-SamyQ-BoPep4 cassettes), 1011 bp (AcdS / 2.1).

Neither draft exposes a sequence to anonymous callers; everything else does.
