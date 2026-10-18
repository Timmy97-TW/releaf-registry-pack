# Bracketed band sizes — what the sequences can settle

19 Oct 2026. Covers the 43 unresolved `\[N bp]` values in `model.json` (the other 27 blockers are strains, markers, enzymes, temperatures and clone numbers). Sources used: the `part.sequence` of each part in `raw/`, the primer tables in the staged text, and nothing else. No wiki captions were used, so none of this depends on the nine values the figure map already corroborated.

## Counts

| Verdict | Rows |
|---|---|
| Confirms | 6 |
| Contradicts | 19 |
| Cannot be determined | 17 |
| No value stated (`\[XXXX bp]`) | 1 |
| **Total** | **43** |

The 6 confirmations are 3 distinct values (each appears twice on its page). The 19 contradictions are 13 distinct values. The 17 undeterminable ones are all colony-PCR totals that run from a primer in the insert into vector sequence that is not in these records.

## Method

**Primers.** Every amplification primer in these tables is built as `ATATAT` spacer + `GAAGAC` (BpiI) + 6 nt + `GGTCTC` (BsaI) + 1 nt + 4 nt BsaI overhang + annealing region. The annealing region was found by taking the longest 3' suffix of the primer that occurs in the part's own sequence (forward) or whose reverse complement occurs in it (reverse). The split is unambiguous for all 18 primers tested: the next base 5' of the match never pairs. Both forward primers used here (`Csn F`, `SamyQ F`, and `Ho1 F`, `ccaS F`, `ccaR F`) carry a 25–26 nt tail; the reverse primers (`ACCD R`, `LEA R`, `LEA14 R`, `BoPep R`, `pcyA R`, `ccaS R`, `ccaR R`) carry a 28–29 nt tail. Amplicon = forward tail + template span from the first base of the forward annealing region to the last base of the reverse annealing region + reverse tail.

**Insert lengths.** The composites in this pack are exact concatenations of their sub-parts, with no scars, so each sub-part's position inside a composite was found by exact substring match. That gives the element lengths the brackets are claiming:

| Element | Length | How it was measured |
|---|---|---|
| Pveg | 97 bp | positions 1–97 in all 8 Pveg parts, identical sequence, `EEBD-RBS0` starts at 98 |
| PliaG | 121 bp | `BBa_261XH2RS` 1–121, `RBS0` (`BBa_26OSLRE4`) matches at 122–154 |
| PtagC+RBS | 100 bp | `BBa_26A4MT29` matches `BBa_26XZYM10` at 1–100 exactly |
| EEBD-RBS0 | 303 bp | `BBa_26V6CPEV` matches at 98–400 in all 7 EEBD composites |
| RBS0 | 33 bp | `BBa_26OSLRE4` matches at 98–130 in `BBa_26BDO8AQ` |
| B0015 | 129 bp | terminal 129 bp of every composite, identical sequence |
| Csn signal peptide | 108 bp | `BBa_26NXOP7S` 1–108; `AcdS` (`BBa_26MA70QI`) matches at 109–1119 |
| SamyQ signal peptide | 93 bp | `BBa_26J0GJGZ`, `BBa_26TOGLX3`, `BBa_26PX0UGH` all 1–93 with the cargo matching at 94 |
| 6x Histag | 18 bp | the 21 bp after each cargo, minus the 3 bp stop |

**The team's `Insert:` convention.** On the three Level 0 pages whose stated insert length is self-consistent, the number equals the sum of the three named elements with the stop codon excluded (`576 = 108 + 450 + 18`, `561 = 93 + 450 + 18`, `1122 = 93 + 1011 + 18`). That convention is used below for the `Insert:` bullets. The deposited part is 3 bp longer in each case, so for the three contradicting insert rows the stated value disagrees under either convention.

## Worked example 1 — the band on BBa_26CXI09X is 1195 bp, not 1145

This is the only unresolved colony-PCR band whose two primers both sit inside the insert, so it needs no vector sequence. The page says: "screened by colony PCR with Csn F and ACCD R primers flanking the CDS insertion site … A correct band runs at the expected size \[1145 bp]".

`BBa_26CXI09X` is 1669 bp and decomposes exactly as `Pveg(97) + EEBD-RBS0(303) + Csn-AcdS-Histag(1140) + B0015(129)`.

- `Csn F` = `ATATATGAAGACATCTGAGGTCTCAT | ATGAAAATCAGTATGCAAAAAGCA`. Tail 26 nt. The 24 nt annealing region occurs once, at **401–424** (the first base of the Csn start codon is 401).
- `ACCD R` = `ATATATGAAGACATGAGGGGTCTCATGTC | TTAATGATGATGATGATGAT`. Tail 29 nt. The reverse complement of the 20 nt annealing region, `ATCATCATCATCATCATTAA`, occurs once, at **1521–1540**, ending on the last base of the stop codon.
- Template span = 1540 − 401 + 1 = **1140 bp**.
- Amplicon = 26 + 1140 + 29 = **1195 bp**.

1145 bp is 50 bp short of that and is also the band the wiki caption gives for Module 1 (`BBa_26XZYM10`), which is where it probably came from. The figure caption on the same page gives `\[7767 bp]` for the same gel, which is plasmid-scale and cannot be a product of these two primers in this orientation.

## Worked example 2 — the Pveg composite inserts are all ~194 bp too long

Take `BBa_26SG0NQQ`, "Composite insert: Pveg – EEBD-RBS0 – Csn-LEA14-Histag – B0015, \[1302 bp]".

The deposited sequence is 1111 bp and splits with no remainder:

- `Pveg` 1–97 (97 bp; byte-identical to positions 1–97 of the other seven Pveg parts, and it carries a `TTGACA` −35 and a `TATAAT` −10, so it is a complete promoter, not a fragment)
- `EEBD-RBS0` 98–400 (303 bp; exact match to `BBa_26V6CPEV`)
- `Csn-LEA14-Histag` 401–982 (582 bp; exact match to `BBa_26ZQ1T72`, whose `Csn F` site starts at its own position 4)
- `B0015` 983–1111 (129 bp)

97 + 303 + 582 + 129 = 1111. So the composite insert is **1111 bp**, not 1302.

The same subtraction on the other six Pveg and PliaG composites shows one systematic cause rather than six separate slips. The stated value needs a promoter of 288–295 bp where the deposited parts carry 97 bp:

| Part | Stated | Deposited | Promoter implied by the stated value |
|---|---|---|---|
| `BBa_269A97I7` | 906 | 712 | 291 bp |
| `BBa_26IA55UY` | 906 | 712 | 291 bp |
| `BBa_26D5AX7S` | 1287 | 1093 | 291 bp |
| `BBa_26CXI09X` | 1863 | 1669 | 291 bp |
| `BBa_26XVQ3FS` | 1848 | 1654 | 291 bp |
| `BBa_26FSZTWM` | 910 | 712 | 295 bp |
| `BBa_26SG0NQQ` | 1302 | 1111 | 288 bp |

## Worked example 3 — BBa_26NXOP7S has Csn, not SamyQ

`BBa_26NXOP7S` ("Insert: Csn signal peptide – AcdS – 6x Histag, \[1122 bp]") is 1140 bp. `AcdS` (`BBa_26MA70QI`, 1011 bp) matches at 109–1119, so the signal peptide is 1–108 and the tag plus stop is 1120–1140. `Csn F` anneals at 1–24, confirming the Csn start codon at position 1.

108 + 1011 + 18 = **1137 bp** under the team's convention, 1140 bp with the stop codon. The stated 1122 is the value from `BBa_26TOGLX3`, which has the 93 bp SamyQ peptide in place of the 108 bp Csn one (93 + 1011 + 18 = 1122). The 15 bp difference is the peptide difference.

## Every row

| Part | Section | Bracketed | Computed | Verdict | Reason |
|---|---|---|---|---|---|
| `BBa_261XH2RS` | experiment | 1723 bp | 1693 bp | Contradicts | Deposited composite = PliaG(121) + RBS0(33) + ccaS-m3(155–1564, 1410) + B0015(129) = 1693; stated value needs a 151 bp PliaG |
| `BBa_267B69E3` | experiment | 177 bp | 180 bp | Contradicts | SamyQ(1–93) + BoPep4 2.2(94–162) + Histag(163–180) = 180; part is 183 with the stop |
| `BBa_267B69E3` | experiment | 177 bp | 180 bp | Contradicts | Same value repeated in the verification sentence |
| `BBa_267B69E3` | experiment | 536 bp | — | Cannot be determined | Total runs from `SamyQ F` into pSTK-0C; `STK R` is not in the primer table and the pSTK-0C sequence is not in these records |
| `BBa_267B69E3` | experiment | 536 bp | — | Cannot be determined | Same total repeated in the Figure 1 caption |
| `BBa_269A97I7` | experiment | 906 bp | 712 bp | Contradicts | Pveg(97) + EEBD-RBS0(303) + CDS(401–583) + B0015(129) = 712 |
| `BBa_26BDO8AQ` | experiment | XXXX bp | 964 bp | No value stated | Nothing to test; deposited composite = Pveg(97) + RBS0(33) + ccaR(131–835) + B0015(129) = 964 |
| `BBa_26BDO8AQ` | experiment | 1174 bp | 964 bp | Contradicts | Same composite insert as the row above, written as the insert term of the 1442 bp total |
| `BBa_26CXI09X` | experiment | 1863 bp | 1669 bp | Contradicts | Pveg(97) + EEBD-RBS0(303) + Csn-AcdS-Histag(401–1540) + B0015(129) = 1669 |
| `BBa_26CXI09X` | experiment | 1145 bp | 1195 bp | Contradicts | `Csn F` (tail 26, anneals 401–424) to `ACCD R` (tail 29, anneals 1521–1540): 26 + 1140 + 29. Worked example 1 |
| `BBa_26CXI09X` | experiment | 7767 bp | 1195 bp | Contradicts | Figure caption for the same `Csn F` + `ACCD R` gel; 7767 bp is plasmid-scale, not an amplicon of this pair |
| `BBa_26D5AX7S` | experiment | 1287 bp | 1093 bp | Contradicts | Pveg(97) + EEBD-RBS0(303) + CDS(401–964) + B0015(129) = 1093 |
| `BBa_26DE5E2Q` | experiment | 1773 bp | — | Cannot be determined | The deposited 2602 bp still contains the vector's sfGFP dropout (PcpcG2-veg 1–190, sfGFP 191–916, B0015 917–1045, then EEBD-RBS0), so it is not the assembled insert and the promoter's 5' boundary cannot be trusted |
| `BBa_26DE5E2Q` | experiment | 1588 bp | — | Cannot be determined | `CDS SamyQ F` (anneals 1349) to `pSTK-seq R`, which lies in pSTK-1D; that sequence is absent. Note the verification sentence on the same page gives 1420 bp for this gel |
| `BBa_26FSZTWM` | experiment | 910 bp | 712 bp | Contradicts | Pveg(97) + EEBD-RBS0(303) + SamyQ-BoPep4-Histag(401–583) + B0015(129) = 712 |
| `BBa_26IA55UY` | experiment | 906 bp | 712 bp | Contradicts | Same decomposition as `BBa_269A97I7`; the two differ only in the BoPep4 variant |
| `BBa_26J0GJGZ` | experiment | 561 bp | 561 bp | Confirms | SamyQ(1–93) + LEA14 2.1(94–543) + Histag(544–561) = 561; `SamyQ F` anneals 1–23, `LEA14 R` 545–564 |
| `BBa_26J0GJGZ` | experiment | 561 bp | 561 bp | Confirms | Same value repeated in the verification sentence |
| `BBa_26J0GJGZ` | experiment | 770 bp | — | Cannot be determined | Total runs into pSTK-0C; `STK R` not listed, vector sequence absent |
| `BBa_26J0GJGZ` | experiment | 770 bp | — | Cannot be determined | Same total repeated in the Figure 1 caption |
| `BBa_26NXOP7S` | experiment | 1122 bp | 1137 bp | Contradicts | Csn(1–108) + AcdS(109–1119) + Histag(1120–1137) = 1137. Worked example 3 |
| `BBa_26NXOP7S` | experiment | 1122 bp | 1137 bp | Contradicts | Same value repeated in the verification sentence |
| `BBa_26NXOP7S` | experiment | 1372 bp | — | Cannot be determined | T7 and SP6 are not in the primer table and the pGEM-T Easy sequence is not in these records |
| `BBa_26NXOP7S` | experiment | 1372 bp | — | Cannot be determined | Same total repeated in the Figure 1 caption |
| `BBa_26PX0UGH` | experiment | 177 bp | 180 bp | Contradicts | SamyQ(1–93) + BoPep4 2.1(94–162) + Histag(163–180) = 180; part is 183 with the stop |
| `BBa_26PX0UGH` | experiment | 177 bp | 180 bp | Contradicts | Same value repeated in the verification sentence |
| `BBa_26PX0UGH` | experiment | 536 bp | — | Cannot be determined | Total runs from `SamyQ F` into pSTK-0C; `STK R` not listed, vector sequence absent |
| `BBa_26PX0UGH` | experiment | 536 bp | — | Cannot be determined | Same total repeated in the Figure 1 caption |
| `BBa_26Q3LKZU` | experiment | 1788 bp | — | Cannot be determined | Deposited 2617 bp carries the same un-dropped sfGFP cassette as `BBa_26DE5E2Q` (190 + 726 + 129 + 303 + 1140 + 129); the 190 bp it holds upstream of sfGFP would give 1762 bp, but that 5' boundary is not reliable |
| `BBa_26SG0NQQ` | experiment | 1302 bp | 1111 bp | Contradicts | Pveg(97) + EEBD-RBS0(303) + Csn-LEA14-Histag(401–982) + B0015(129) = 1111. Worked example 2 |
| `BBa_26TOGLX3` | experiment | 1122 bp | 1122 bp | Confirms | SamyQ(1–93) + AcdS 2.1(94–1104) + Histag(1105–1122) = 1122; `SamyQ F` anneals 1–23, `ACCD R` 1106–1125 |
| `BBa_26TOGLX3` | experiment | 1122 bp | 1122 bp | Confirms | Same value repeated in the verification sentence |
| `BBa_26TOGLX3` | experiment | 1331 bp | — | Cannot be determined | Total runs into pSTK-0C; `STK R` not listed, vector sequence absent |
| `BBa_26TOGLX3` | experiment | 1331 bp | — | Cannot be determined | Same total repeated in the Figure 1 caption |
| `BBa_26XVQ3FS` | experiment | 1848 bp | 1654 bp | Contradicts | Pveg(97) + EEBD-RBS0(303) + SamyQ-AcdS 2.1-Histag(401–1525) + B0015(129) = 1654 |
| `BBa_26XZYM10` | experiment | 1660 bp | 1655 bp | Contradicts | PtagC+RBS(1–100) + Ho1:pcyA(101–1594, `Ho1 F` anneals from 100, `pcyA R` stop at 1592–1594) + L3S2P21(1595–1655) = 1655 |
| `BBa_26XZYM10` | experiment | 1660 bp | 1655 bp | Contradicts | Same value repeated in the verification sentence |
| `BBa_26XZYM10` | experiment | 1721 bp | — | Cannot be determined | `Ho1 F` to `pSTK-seq R`, which lies in pSTK-1A; that sequence is absent. The stated arithmetic (insert + 61 bp of vector) is also wrong in shape, because `Ho1 F` anneals 100 bp inside the insert, so the product cannot contain PtagC+RBS |
| `BBa_26XZYM10` | experiment | 1721 bp | — | Cannot be determined | Same total repeated in the Figure 1 caption |
| `BBa_26ZQ1T72` | experiment | 576 bp | 576 bp | Confirms | Csn(4–111) + LEA14(112–561) + Histag(562–579) = 576; `Csn F` anneals 4–27, `LEA R` 563–582. The deposited part is 582 bp: an extra `ATG` at 1–3 and the stop at 580–582 |
| `BBa_26ZQ1T72` | experiment | 576 bp | 576 bp | Confirms | Same value repeated in the verification sentence |
| `BBa_26ZQ1T72` | experiment | 811 bp | — | Cannot be determined | Total runs from `Csn F` into pSTK-0C; `STK R` not listed, vector sequence absent |
| `BBa_26ZQ1T72` | experiment | 811 bp | — | Cannot be determined | Same total repeated in the Figure 1 caption |

## Contradictions

These are the 13 distinct values now on public registry pages that the parts' own sequences dispute.

1. `BBa_26SG0NQQ` composite insert: page says **1302 bp**, sequence gives **1111 bp**.
2. `BBa_269A97I7` composite insert: **906 bp** against **712 bp**.
3. `BBa_26IA55UY` composite insert: **906 bp** against **712 bp**.
4. `BBa_26FSZTWM` composite insert: **910 bp** against **712 bp**.
5. `BBa_26D5AX7S` composite insert: **1287 bp** against **1093 bp**.
6. `BBa_26CXI09X` composite insert: **1863 bp** against **1669 bp**.
7. `BBa_26XVQ3FS` composite insert: **1848 bp** against **1654 bp**.
   (1 to 7 are one fault: each needs a 288–295 bp Pveg where all eight Pveg parts carry 97 bp.)
8. `BBa_261XH2RS` composite insert: **1723 bp** against **1693 bp**, needing a 151 bp PliaG where the part carries 121 bp.
9. `BBa_26BDO8AQ` insert: **1174 bp** against **964 bp**.
10. `BBa_26XZYM10` composite insert: **1660 bp** against **1655 bp** (appears twice).
11. `BBa_26NXOP7S` insert: **1122 bp** against **1137 bp** (appears twice). The stated number belongs to `BBa_26TOGLX3`, which carries the 93 bp SamyQ peptide in place of the 108 bp Csn one.
12. `BBa_26PX0UGH` and `BBa_267B69E3` insert: **177 bp** against **180 bp** (twice on each page).
13. `BBa_26CXI09X` colony PCR: **1145 bp** in the verification text and **7767 bp** in the Figure 1 caption, against **1195 bp** computed from the `Csn F` and `ACCD R` annealing positions. These two also disagree with each other, for the same gel.

## Two things found on the way

**The pSTK-0C totals cannot all be right.** The four `\[N bp]` totals on the Level 0 pages all use the same vector and the same reverse primer, so each should be its insert plus one constant. The constants implied are 180 bp (`BBa_26J0GJGZ`, 770 − 26 − 564), 180 bp (`BBa_26TOGLX3`, 1331 − 26 − 1125), 206 bp (`BBa_26ZQ1T72`, 811 − 26 − 579) and 327 bp (`BBa_26PX0UGH` and `BBa_267B69E3`, 536 − 26 − 183). If 180 bp is the real figure, the two 536 bp totals should be near 389 bp. This is not a calculation, because `STK R` and the vector are both missing, but the 536 bp pair is the odd one out by a wide margin.

**One already-resolved pair looks wrong.** The two pSTK-EXP1 colony PCRs that used both backbone primers give the same vector contribution independently: `BBa_26D5AX7S` 1423 − 1093 = 330 bp and `BBa_26XVQ3FS` 1984 − 1654 = 330 bp. On that footing the 678 bp quoted for `BBa_269A97I7` and `BBa_26IA55UY` is impossible, since their insert alone is 712 bp and the page also says backbone primers. Those two values are outside the scope of this pass (both were treated as corroborated by a wiki caption), but they are worth a second look before the freeze.

**Sequence deposits to check.** `BBa_26Q3LKZU` and `BBa_26DE5E2Q` both carry 855 bp that the stated composition does not mention: an sfGFP coding sequence at 191–916 followed by a B0015 at 917–1045, sitting between the promoter and `EEBD-RBS0`. That is the pSTK dropout cassette Golden Gate is supposed to replace, so these two deposited sequences are almost certainly the pre-assembly vector map rather than the finished construct. Their composite-insert brackets cannot be checked until the sequences are fixed.
