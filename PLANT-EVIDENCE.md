# Plant evidence for the Application sections

Built 19 October 2026 from `git show origin/main:plant/index.html` and `git show origin/main:results/index.html`.
Machine-readable output: `plant-evidence.json`. Figures: `plant/PL01` to `plant/PL09`, with 420 px copies in `thumbs/plant/`.

Nothing in `model.json`, `additions.json`, `raw/`, `upload/`, `modelling/` or `collections/` was touched.

## The chain

No part was ever applied to a plant. Every plant trial applied one of three things:

1. a 0.22 µm-filtered culture supernatant from *Bacillus subtilis* WB800 secreting a protectant, sprayed onto agar plates (three sprays, 0.536 mL);
2. the same material diluted into hydroponic root solution at 1/40 to 1/100;
3. a commercial reference product, CH Bio peptide, or exogenous trehalose — neither of which is one of our cargoes.

So the chain for any claim runs: part encodes cargo → cargo was secreted by *B. subtilis* WB800 → a preparation of that culture was sprayed or dosed → the run showed something. The plant page never records which cassette produced which batch, so the fourth link stops at the cargo. It never reaches a coding variant, a secretion peptide, or an expression module.

## Tiers

The tier describes the chain. How much the chain carries is in `summary`, `what_it_cannot_say` and the `read_state` field added alongside each tier.

| cargo | tier | read_state | figures |
|---|---|---|---|
| AcdS | indirect via strain | two heat runs readable; both salinity runs confounded | 6 |
| BoPep4 | indirect via strain | hydroponic salt and heat readable at 1/40 only; the agar set is unscored | 4 |
| LEA14 | indirect via strain | applied once, charted, never scored — no outcome | 0 |
| LightCircuit | not tested | no plant trial | 0 |

`LEA14` is tiered **indirect via strain**, not **not tested**, because a preparation really was sprayed on plants in agar salinity set 11. It carries no figures and no claim, because that set has never been scored. If a reader only looks at the tier they will be misled, which is why `read_state` exists and why the Application sentence for all six LEA14 parts says the outcome does not exist.

`PL09` (the TB-medium dilution control) is listed under both AcdS and BoPep4. It is the same file and the same legend in both.

## The correction this run forces

Four parts — `BBa_26SG0NQQ`, `BBa_26D5AX7S`, `BBa_26FSZTWM`, `BBa_269A97I7` — currently carry Application text reading:

> A full ccaSR construct with [LEA14 / BoPep4] as Module 4 was not built. The constitutive […] version lets us assess its behavior in the system, **and it also helped plants under salinity stress**, without duplicating the work […]

The "was not built" sentence is honest and must be kept. The bolded clause must not be.

- For **LEA14** it is unsupported outright. The one AtLEA14 plant trial is agar salinity set 11, which the wiki itself calls charted and not yet written up. There is no AtLEA14 figure, table or outcome sentence anywhere on the plant page. Strike the clause.
- For **BoPep4** it is over-general. One dilution, 1/40, in one unreplicated hydroponic run, kept plants green through 100 mM NaCl; 1/60, 1/80 and 1/100 gave nothing, and the agar set is unscored. Replace the clause with a cargo-level statement that names the preparation, the single working dilution and the absence of replication.

This is recorded as `corrections_required` in the JSON.

## Withdrawn numbers

| number | where it appears | what was done |
|---|---|---|
| pH 7 = 75% of ACC deaminase activity | `plant/index.html`, Hydroponics → buffer control, cited to reference [19], given as the reason for running pH 5.7 and pH 7 arms | Left out of every legend and summary. PL09 uses that figure's panels but describes only the dilution series and the two pH values as the chart labels them (pH 5.7, pH 7.1). |
| efficacy figure of 0.58 | not found on either page | nothing to exclude |
| 7.3-hour effect window | not found on either page; the plant page's timing language is in days throughout (pre-, co- and post-treatment one day apart) | nothing to exclude |

## Figures pulled

| file | source on origin/main | cargo |
|---|---|---|
| `PL01_AcdS_agar-heat-plates.png` | `assets/img/plant/r17-accdheat-plates.webp` | AcdS |
| `PL02_AcdS_agar-heat-chlorophyll.png` | `assets/img/plant/r17-accdheat-readouts.webp` | AcdS |
| `PL03_AcdS_hydro-heat-rack-before.png` | `assets/img/plant/h18-heat-rack-before.webp` | AcdS |
| `PL04_AcdS_hydro-heat-rack-after.png` | `assets/img/plant/h18-heat-rack-after.webp` | AcdS |
| `PL05_AcdS_hydro-heat-readouts.png` | `assets/img/plant/h18-accdheat-readouts.webp` | AcdS |
| `PL06_BoPep4_hydro-salt-rack.png` | `assets/img/plant/h18-bopepsal-rack.webp` | BoPep4 |
| `PL07_BoPep4_hydro-salt-readouts.png` | `assets/img/plant/h18-bopepsal-readouts.webp` | BoPep4 |
| `PL08_BoPep4_hydro-heat-readouts.png` | `assets/img/plant/h18-bopepheat-readouts.webp` | BoPep4 |
| `PL09_vehicle_hydro-TB-dilution-readouts.png` | `assets/img/plant/h18-bsub-readouts.webp` | AcdS + BoPep4 |

All taken from the originals, not the `-w800` card copies, and converted webp → png with no edits.

Every legend was written against the panel, not against the page prose. Where the two disagree, the panel wins — see "Where the wiki text runs ahead of its own panels" below.

## Not used, and why

Everything below is on the plant page or the results page and was deliberately left out of the Application package.

**Not our cargoes.**

- All trehalose work — pre-tests (sets 1–3) and official sets 4, 5, 6, including the dose-response and the 8.7× chlorophyll result at 100 mM NaCl. Exogenous sugar, not a part.
- All CH Bio peptide work — agar set 7 (three trials), the hydroponic salinity and heat pre-tests, the heat-on-agar comparison on the results page. A commercial product whose active components were not disclosed to the team; the results page says so itself and warns the reader not to read it as evidence for ACC deaminase. Using it would be the easiest and worst over-claim available.

**Our cargo, but the run cannot be read.**

- `r17-exp8-plates.webp` and `r17-exp8-readouts.webp` — agar ACC deaminase salinity pre-test, set 8. Contamination occupied the plates and the team suspects the protectant itself was contaminated during filtering. The plant page reads this set as "minimal rescue"; the results page reads the same design as pre-treatment reaching 3.3× the control. Two live pages disagree about one contaminated pre-test. Nothing that contradicts itself on the wiki belongs in a permanent Registry claim.
- `r17-exp9-readouts.webp` — agar ACC deaminase salinity, official set 9. Confounded by the TB medium.
- `h18-accdsal-rack.webp` and `h18-accdsal-readouts.webp` — hydroponic ACC deaminase salinity. Prof. Peng pointed out after the run that the TB-medium concentration was not fixed, so raising the ACCD dose raised the vehicle dose with it. The team records this as preliminary data and not a reading of ACC deaminase under salt. Honouring that.
- `s18-accdsal-pots.webp` — soil ACC deaminase at three timings under 300 mM NaCl. The pots have not been scored; the page says so.
- `r18-bopep-sal-plates.webp` and `r18-bopep-sal-readouts.webp` — agar BoPEP4 salinity, set 10. Charted; the page states explicitly that no conclusion is drawn from it.
- `r18-lea14-sal-readouts.webp` — agar AtLEA14 salinity, set 11. Same: charted, not scored. This is the only AtLEA14 plant figure in existence, and including it would invite exactly the claim the page refuses to make. A legend for it could not state n or what to read off the panel, which is the test every legend here had to pass.

**Real data, but not cargo evidence.**

- `results/fig-salinity-dose-response.webp` and `plant/fig-salladder-day6-panel.webp` — the salt ladder, 74.95 → 1.36 mm root length across 0–150 mM NaCl, nine seedlings per group. The best-controlled plant measurement the team has, and it characterises the assay, not a part. Worth citing on the plant page; it belongs in no part's Application section.
- Hydroponic prototypes 1 to 5, the three overview workflow drawings, the two timeline drawings, the six process-step photographs, and all outreach and classroom photographs. Method and narrative.
- `d-260815-model-sketch.webp` and the dry-lab collaboration material. Modelling, and the 1.67 mL-per-three-sprays dose figure there is described by the team as "a dose that worked rather than the smallest that works".

## Where the wiki text runs ahead of its own panels

Found while writing the legends. Not corrected here — this package only reads `origin/main` — but the Application text must not inherit either error.

1. **Hydroponic ACC deaminase heat run** (`h18-accdheat-readouts.webp`). The page says "The 1/40, 1/60 and 1/80 ACCD groups held higher fresh weights and higher chlorophyll contents than the controls […] The 1/100 ACCD group came out close to the 1/40 WB800 group, both below the other treatments." The chlorophyll half is right. The fresh-weight half is backwards: under heat those three groups sit at about 0.014–0.015 g, below the 1/40 WB800 vehicle control at about 0.018 g, and 1/100 ACCD is the heaviest group on the panel at about 0.019 g. PL05's legend states the disagreement instead of repeating the sentence.
2. **Agar ACC deaminase heat run** (`r17-accdheat-readouts.webp`). The results page says chlorophyll and fresh weight for this set are "still being analysed"; the plant page has both, charted. The plant page is the later and fuller source and was used, but the Application text should not cite the results page's framing of this run.
3. **BoPEP4 salinity** (`h18-bopepsal-readouts.webp`). "Highest fresh weight and the highest chlorophyll content per plant" at 1/40 is correct on those two panels. On the third panel, relative chlorophyll, the medium-only control is the highest salt-stressed group, above 1/40 BoPEP4. PL07's legend says so.
