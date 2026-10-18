# Figure map — wiki images to registry slots

Images are on `origin/main` under `wiki/assets/img/`. **Upload the file without the `-w800` suffix** — those are the 800 px card copies from the 8 Oct image pass, not the originals.

| part | registry slot | image on origin/main | wiki caption says | registry text says |
|---|---|---|---|---|
| `BBa_26SG0NQQ` | experiment Fig 1 | `results/pp-gel-prod-csn-lea14.webp` | 735 bp, 1 of 1 colony, sequenced | [1302 bp], [735 bp], [BsaI-HFv2 enzyme], [X], [ampicillin] |
| `BBa_26D5AX7S` | experiment Fig 1 | `results/pp-gel-prod-samyq-lea14.webp` | 1,423 bp, 2 of 7, clone 1 | [1287 bp], [1423 bp], [BsaI-HFv2 enzyme], [X], [ampicillin] |
| `BBa_26CXI09X` | experiment Fig 1 | `results/pp-gel-prod-csn-accd.webp` | no numbers in wiki caption | [1145 bp], [1863 bp], [7767 bp], [BsaI-HFv2 enzyme], [ampicillin] |
| `BBa_26XVQ3FS` | experiment Fig 1 | `results/pp-gel-prod-samyq-accd.webp` | 1,984 bp, 4 of 8, clone 2 | [1848 bp], [1984 bp], [BsaI-HFv2 enzyme], [ampicillin] |
| `BBa_269A97I7` | experiment Fig 1 | `results/pp-gel-prod-bopep4-21.webp` | 678 bp, 1 of 11, clone 14 | [678 bp], [906 bp], [BsaI-HFv2 enzyme], [ampicillin] |
| `BBa_26IA55UY` | experiment Fig 1 | `results/pp-gel-prod-bopep4-22.webp` | 678 bp, 4 of 5, clone 5 | [678 bp], [906 bp], [BsaI-HFv2 enzyme], [ampicillin] |
| `BBa_26XZYM10` | experiment Fig 1 | `results/pp-gel-m1.webp` | 1,145 bp, 3 of 3, clone 1 | [1660 bp], [1721 bp], [BsaI-HFv2 enzyme], [ampicillin] |
| `BBa_261XH2RS` | experiment Fig 1 | `results/pp-gel-m2.webp` | 1,602 bp, 1 of 3 | [1602 bp], [1723 bp], [60 °C], [X], [pGEM-T Easy], [pSTK-1B] |
| `BBa_26BDO8AQ` | experiment Fig 1 | `results/pp-gel-m3.webp` | 1,442 bp, 2 of 4, clone 2 | [1174 bp], [1442 bp], [60 °C], [BsaI-HFv2 enzyme], [XXXX bp], [marker to be confirmed], [pSTK-1C-sfGFP] |
| `BBa_26Q3LKZU` | experiment Fig 1 | `results/pp-gel-m4-csn.webp` | 1,588 bp, 2 of 6, clone 3 | [1588 bp], [1788 bp], [BsaI-HFv2 enzyme], [X], [ampicillin] |
| `BBa_26DE5E2Q` | experiment Fig 1 | `results/pp-gel-m4-samyq.webp` | 1,420 bp, 7 of 16, clone 2 | [1420 bp], [1588 bp], [1773 bp], [BsaI-HFv2 enzyme], [X], [ampicillin] |
| `BBa_2654HAF3` | experiment Fig 1 | `results/pp-gel-sys-csn.webp` | 632 bp, 3 of 3, clones 3 and 5 | — |
| `BBa_2654HAF3` | experiment Fig 2 | `results/pp-pcr-sys-csn.webp` | cross-module, clone 2 | — |
| `BBa_26U8UTMH` | experiment Fig 1 | `results/pp-pcr-sys-samyq.webp` | cross-module, 3 of 3, clone 1 | — |
| `BBa_2654HAF3` | characterisation Fig 1 | `results/lpa-wb-timecourse.webp` | ABDI, green 100/12/2% + red 100% | — |
| `BBa_26U8UTMH` | characterisation Fig 1 | `results/lpa-wb-13-16h.webp` | ABDQ, 13 and 16 h, G vs R | — |
| `BBa_26U8UTMH` | characterisation Fig 2 | `results/lpa-wb-overnight.webp` | ABDQ, overnight then 3/6/8 h | — |
| `BBa_26CXI09X` | characterisation Fig 1 | `results/wb-260802-accd-fractionation.webp` | P1/P2/S, 2 Aug 2026 | — |

## Band sizes: wiki caption vs registry placeholder

- `BBa_26SG0NQQ` — wiki 735 bp matches the registry text ✓
- `BBa_26D5AX7S` — wiki 1423 bp matches the registry text ✓
- `BBa_26XVQ3FS` — wiki 1984 bp matches the registry text ✓
- `BBa_269A97I7` — wiki 678 bp matches the registry text ✓
- `BBa_26IA55UY` — wiki 678 bp matches the registry text ✓
- `BBa_261XH2RS` — wiki 1602 bp matches the registry text ✓
- `BBa_26BDO8AQ` — wiki 1442 bp matches the registry text ✓
- `BBa_26Q3LKZU` — wiki 1588 bp matches the registry text ✓
- `BBa_26DE5E2Q` — wiki 1420 bp matches the registry text ✓
- `BBa_26XZYM10` — wiki says **1145 bp**, registry text has ['1660 bp', '1721 bp'] ⚠
- `BBa_2654HAF3` — wiki says **632 bp**, registry text has no bp value ⚠

## Still missing

- `BBa_26XVQ3FS` characterisation — its legend promises a Western for the constitutive **SamyQ-AcdS 2.1** construct (`Fig. X`, unnumbered). The only constitutive ACCD blot on the wiki is the Csn fractionation one already assigned to `BBa_26CXI09X`. Either it is panel (B) of that same blot, or the image does not exist.
- `BBa_26FSZTWM` experiment Fig 1 — the caption is a **sequencing** result, not a gel. No sequencing-trace figure found on results or engineering.
- Two `Clone 1 was sequence-verified and used downstream` captions (`BBa_26CXI09X`, `BBa_26XVQ3FS`) also want sequencing traces, not gels.
- The 5 parts with no documentation at all still have nothing: `BBa_26A4MT29`, `BBa_26OSLRE4`, `BBa_26V6CPEV`, `BBa_26YHOQCL`, `BBa_26Z8FHTR`.