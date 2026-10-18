# Collection documentation — Protectant modules

GEMS-Taiwan 2026. One entry per registry documentation type, each delimited by `---` and headed with the type name, so that a single entry can be pasted into the collection editor at a time.

**Members.** The cargo coding sequences, the signal-peptide fusions, the constitutive expression cassettes, and the two shared Level 0 elements that carry them.

Cargo coding sequences:

| part | title |
| --- | --- |
| [BBa_26MA70QI](https://registry.igem.org/parts/bba-26ma70qi) | AcdS |
| [BBa_262YYNPV](https://registry.igem.org/parts/bba-262yynpv) | AcdS 2.1 |
| [BBa_26LTB0W1](https://registry.igem.org/parts/bba-26ltb0w1) | LEA14 |
| [BBa_26IN6G1D](https://registry.igem.org/parts/bba-26in6g1d) | LEA14 2.1 |
| [BBa_265CD14Z](https://registry.igem.org/parts/bba-265cd14z) | BoPep4 |
| [BBa_26LYCBW0](https://registry.igem.org/parts/bba-26lycbw0) | BoPep4 2.1 |
| [BBa_26ERHWWI](https://registry.igem.org/parts/bba-26erhwwi) | Bopep4 2.2 |
| [BBa_26YHOQCL](https://registry.igem.org/parts/bba-26yhoqcl) | Bopep4 (15-23) |

Signal-peptide fusions:

| part | title |
| --- | --- |
| [BBa_26NXOP7S](https://registry.igem.org/parts/bba-26nxop7s) | Csn-AcdS-Histag |
| [BBa_26TOGLX3](https://registry.igem.org/parts/bba-26toglx3) | SamyQ-AcdS 2.1-Histag |
| [BBa_26ZQ1T72](https://registry.igem.org/parts/bba-26zq1t72) | Csn-LEA14-Histag |
| [BBa_26J0GJGZ](https://registry.igem.org/parts/bba-26j0gjgz) | SamyQ-LEA14 2.1-Histag |
| [BBa_26ILD3SO](https://registry.igem.org/parts/bba-26ild3so) | SamyQ-BoPep4-Histag |
| [BBa_26PX0UGH](https://registry.igem.org/parts/bba-26px0ugh) | SamyQ-BoPep4 2.1-Histag |
| [BBa_267B69E3](https://registry.igem.org/parts/bba-267b69e3) | SamyQ-BoPep4 2.2-Histag |

Constitutive expression cassettes:

| part | title |
| --- | --- |
| [BBa_26CXI09X](https://registry.igem.org/parts/bba-26cxi09x) | Pveg-EEBD-RBS0-Csn-AcdS-Histag-B0015 |
| [BBa_26XVQ3FS](https://registry.igem.org/parts/bba-26xvq3fs) | Pveg-EEBD-RBS0-SamyQ-AcdS 2.1-Histag-B0015 |
| [BBa_26SG0NQQ](https://registry.igem.org/parts/bba-26sg0nqq) | Pveg-EEBD-RBS0-Csn-LEA14-Histag-B0015 |
| [BBa_26D5AX7S](https://registry.igem.org/parts/bba-26d5ax7s) | Pveg-EEBD-RBS0-SamyQ-LEA14 2.1-Histag-B0015 |
| [BBa_26FSZTWM](https://registry.igem.org/parts/bba-26fsztwm) | Pveg-EEBD-RBS0-SamyQ-BoPep4-Histag-B0015 |
| [BBa_269A97I7](https://registry.igem.org/parts/bba-269a97i7) | Pveg-EEBD-RBS0-SamyQ-BoPep4 2.1-Histag-B0015 |
| [BBa_26IA55UY](https://registry.igem.org/parts/bba-26ia55uy) | Pveg-EEBD-RBS0-SamyQ-BoPep4 2.2-Histag-B0015 |
| [BBa_26Z8FHTR](https://registry.igem.org/parts/bba-26z8fhtr) | Pveg-EEBD-RBS0-SamyQ-Bopep4-Histag (9-23)-B0015 |

Shared Level 0 elements:

| part | title |
| --- | --- |
| [BBa_26V6CPEV](https://registry.igem.org/parts/bba-26v6cpev) | EEBD-RBS0 |
| [BBa_26OSLRE4](https://registry.igem.org/parts/bba-26oslre4) | RBS0 |

**Members shared with the Light-sensing circuit collection.** The two light-responsive output cassettes, [BBa_26Q3LKZU](https://registry.igem.org/parts/bba-26q3lkzu) and [BBa_26DE5E2Q](https://registry.igem.org/parts/bba-26de5e2q), and the two assembled Level 2 systems, [BBa_2654HAF3](https://registry.igem.org/parts/bba-2654haf3) and [BBa_26U8UTMH](https://registry.igem.org/parts/bba-26u8utmh), are cargo-carrying modules as well as light-controlled ones.

**If the registry does not allow a part in two collections.** Keep EEBD-RBS0 and RBS0 here, and put the four hybrids in **Light-sensing circuit**, since the light switch is what distinguishes them.

**What this document is for.** The Registry Rules say documentation that applies to a group of parts belongs to the collection and should not be copied onto each part. Everything below was previously repeated across the member parts. Each part keeps only what is intrinsic to it: its own sequence, its own codon changes and predicted scores, its own expected band sizes, its own gels and blots, and its own clone numbers.

**Division of labour with the other collection.** The switch logic of the light circuit, the Level 2 assembly and the LPA illumination schedules are written once in the **Light-sensing circuit** collection. This document carries the shared Level 0 and Level 1 cloning method, the cycling conditions, the primers, the screening practice, the protein-detection methods and the plant work.

---

# Design

## What the collection is

A Protectant Module constitutively expresses a candidate stress-mitigation protein and allows its secretion and detection to be assessed. Each module is a composite transcription unit with four elements, in this order: the constitutive promoter Pveg, the ribosome binding site EEBD-RBS0, a translational fusion of a Sec-dependent signal peptide with a protectant coding sequence and a 6x Histag, and the terminator B0015.

The collection holds that cassette at every level of assembly: the bare cargo coding sequences, the signal-peptide fusions built from them, and the complete constitutive cassettes. Its light-responsive counterparts, which replace Pveg with PcpcG2-veg, are documented in the **Light-sensing circuit** collection.

## The SubtiToolKit architecture

Every part in both collections is built in the SubtiToolKit (STK) format of Caro-Astorga et al. (2025), with the kit provided by [Dr Joaquín Caro-Astorga](https://www.google.com/search?kgmid=%2Fg%2F11jg8gn6cr&q=Dr.+Joaqu%C3%ADn+Caro-Astorga). The format has three levels.

| level | what it holds | vector |
| --- | --- | --- |
| Level 0 | a single element: promoter, RBS, coding sequence or terminator | pSTK-0C-sfGFP, or pGEM-T Easy for entry cloning |
| Level 1 | one complete transcription unit: promoter, RBS, CDS, terminator | pSTK-EXP1-sfGFP (expression shuttle); pSTK-1A/1B/1C/1D-sfGFP (cloning) |
| Level 2 | four Level 1 units on one plasmid | pSTK-EXP2 |

The `-sfGFP` suffix is part of the vector name, not a leftover: each of these vectors carries a superfolder green fluorescent protein cassette flanked by Type IIS restriction sites, which serves as a visual selection marker. Cells containing the empty vector fluoresce green, while successful insertion of the target fragment replaces the sfGFP sequence and gives white, non-fluorescent colonies.

Holding the format constant has a purpose beyond convenience. Because every cassette uses the same promoter, the same ribosome binding site and the same terminator, a difference in output between two cargoes, or between the two signal peptides, reflects the cargo rather than the strength of transcription or the rate of translation initiation.

## The shared elements

* **Pveg** (BBa_K143012): a constitutive bacterial promoter originally derived from *Bacillus subtilis*, which drives continuous transcription without requiring external induction.
* **EEBD-RBS0** ([BBa_26V6CPEV](https://registry.igem.org/parts/bba-26v6cpev)): a composite element containing a synthetic ribosome binding site with expression-enhancing nucleotide context to improve translation initiation efficiency, preceded by a blocking device. See the next section.
* **RBS0** ([BBa_26OSLRE4](https://registry.igem.org/parts/bba-26oslre4)): the ribosome binding site itself, which sets translation initiation of the downstream coding sequence. It is used alone on the light-circuit modules and as the translation-initiation half of EEBD-RBS0 here.
* **B0015** (BBa_B0015): a high-efficiency double transcriptional terminator that stops RNA polymerase continuing past the protectant coding sequence, preventing transcriptional read-through into downstream modules.
* **6x Histag**: fused to the protectant and followed by a stop codon, which allows the protein to be detected and purified. On the short BoPep4 peptide the tag is what makes detection possible at all: the mature peptide is 23 residues, too short to detect without it.

**Open point on the tag.** The part names put the Histag at the C-terminus, and the fusion descriptions for AcdS and LEA14 say it is fused at the C-terminus followed by a stop codon. The BoPep4 fusion descriptions say it is fused N-terminally to the peptide, while the BoPep4 Application text says the C-terminus. The record disagrees with itself here and one reading needs to be adopted before this entry is published.

## Why the blocking device, and why it sits here

The EEBD is an *Escherichia coli* expression-blocking device: a B0015 double terminator between two recombination sites. While a construct is being assembled and propagated in *E. coli*, the terminator stops transcription reaching the coding sequence, which prevents unwanted gene expression and the production of a protein that would be toxic to the cloning host.

It sits on the protectant modules and is absent from the light-sensing and transduction modules, because of the cargo. A protectant is a secreted protein carried on a Sec signal peptide, and expression during cloning in *E. coli* risks unwanted protein production and loss of the construct. CcaS and CcaR, by contrast, have nothing to act on in *E. coli*, which has neither phycocyanobilin nor a PcpcG2 promoter. Placing the device in front of the protectant coding sequence keeps the cassette silent through the *E. coli* steps, and the same EEBD-RBS0 part then supplies the RBS for that coding sequence.

## Csn versus SamyQ, and why both are carried

Two Sec-dependent signal peptides are used across the collection, and both are carried on purpose.

* **Csn**: the N-terminal Sec-dependent signal peptide of *B. subtilis* chitosanase (gene *csn*), which directs the protein to the secretion pathway and is cleaved off during export.
* **SamyQ** ([BBa_K1074014](https://registry.igem.org/parts/bba-k1074014)): the N-terminal signal peptide of the *amyQ* gene, which encodes a highly efficient α-amylase natively found in *B. subtilis* and related lineages such as *Bacillus amyloliquefaciens*.

Csn and SamyQ were selected as candidates to determine which offers higher secretion efficiency. Carrying both, on the same cargo and in the same cassette format, is what makes that comparison possible: Csn-AcdS-Histag and SamyQ-AcdS 2.1-Histag, and Csn-LEA14-Histag and SamyQ-LEA14 2.1-Histag, are matched pairs.

**Status of the comparison.** It is not yet readable. Both constitutive ACC deaminase constructs were reported as a clear band at approximately 37 kDa in the culture supernatant, and the one constitutive blot has two lanes labelled S whose distinction was not documented. Comparing Csn with SamyQ is listed as a future direction, not a result.

## Why these three cargo families

**ACC deaminase (AcdS).** ACC deaminase hydrolyses 1-aminocyclopropane-1-carboxylate, the precursor of the plant stress hormone ethylene, and so lowers the ethylene levels that inhibit plant growth under stress (Glick et al., 1998; Hontzeas et al., 2004; Shah et al., 1998). The cloned gene can be expressed in *Escherichia coli*, which lets that bacterium grow on ACC as its sole nitrogen source, and both *E. coli* and *Pseudomonas* spp. strains transformed with it gain the ability to promote root elongation in canola seedlings (Hontzeas et al., 2004).

The coding sequence is that of *Pseudomonas putida* (*Arthrobacter siderocapsulatus*) strain UW4, taken from UniProt Q5PWZ8. A soluble recombinant enzyme from that strain has been cloned, expressed and purified: it has a molecular weight of 41 kDa and shows selectivity and high activity towards ACC, with K(M) = 3.4 ± 0.2 mM and k(cat) = 146 ± 5 min⁻¹ at pH 8.0 and 22 °C. Activity is optimal at pH 8.0, declines sharply to essentially nothing below pH 6.5, tapers off more gradually at higher pH, and is lost above pH 10 (Hontzeas et al., 2004).

**Open point on the accession.** Three identifiers appear for this sequence across the parts: UniProt Q5PWZ8, GenBank CP053102.1, and `[GenBank sequence CP103783.1]`, which is cited as the *Bacillus subtilis* subsp. *subtilis* str. 168 genome. One source accession needs to be adopted for the *acdS* sequence and the other two separated out or dropped.

**LEA14.** LEA proteins are small, partially folded, hydrophilic proteins that stabilise membranes and isolate ions to prevent water loss, and they keep other proteins from aggregating when water is withdrawn (Goyal et al., 2005; Hundertmark et al., 2008; Mertens et al., 2018). LEA14 from *Arabidopsis thaliana*, gene *At1g01470.1* of the LEA_2 subgroup, is an intrinsically disordered protein of this family (Singh et al., 2005), and its overexpression raises salt-stress tolerance in *A. thaliana* (Jia et al., 2014). We selected it as a protectant cargo on the expectation that a secreted copy can help stabilise plant cell membranes under drought, salinity, heat and osmotic stress.

**BoPep4.** BoPep4 is a 23-residue mature plant elicitor peptide from broccoli (*Brassica oleracea* var. *italica*), sequence GILIGSKKRPREPHSSGKPGGHN. It works through auxin and abscisic acid signalling crosstalk to raise salt-stress tolerance in broccoli, lowering the Na⁺/K⁺ ratio and promoting leaf wax and cutin accumulation (Wang, A., et al., 2022). It also enhances plant salt tolerance by improving glucosinolate metabolism (Li et al., 2026).

## The 5′ recoding pipeline

The mRNA secondary structure around the ribosome binding site and the start codon influences translation initiation in bacteria, independently of the encoded protein sequence. Synonymous codons at the 5′ end of a coding sequence change how the mRNA folds near the binding site, and that folding can either hide or expose the Shine-Dalgarno sequence and the start codon.

Following Castillo-Hair et al. (2019), our design pipeline treated the first 15 codons of each cargo coding sequence as an editable region. ViennaRNA 2.7.2 (Lorenz et al., 2011) generated and folded tens of thousands of synonymous variants in the RS-inclusive 236-nt 5′ window — residual recombination site, MF001 RBS, spacer, SamyQ open reading frame, and the first 90 nt of the coding sequence — scoring the mean base-pair unpaired probability across the 15 nt following the ATG and across the MF001 Shine-Dalgarno core (AAGGAGG), and combining the two into a balance score. The codon adaptation index of each variant was also scored against *B. subtilis* 168 codon usage (Kazusa DNA Research Institute, n.d.).

We worked to a usability threshold of roughly 0.50 on each accessibility score, against an Ho1 reference baseline of 0.681. Rather than applying Castillo's rule, which prioritises low GC content and A over U, the pipeline folded and checked every candidate individually. The Castillo-rule control for each cargo is recorded on that cargo's own part.

The encoded protein sequence is unchanged in every variant. **These scores are predictions. Translation initiation from these cassettes has not been measured.**

Variants taken forward, with the predicted figures as recorded:

| variant | codons changed of 15 | start+15 accessibility | SD-core accessibility | balance score | CAI, *B. subtilis* 168 |
| --- | --- | --- | --- | --- | --- |
| AcdS wild type | — | 0.563 | 0.088 | 0.651 | 0.85 |
| AcdS 2.1 | 12 | 0.773 | 0.203 | 0.976 | 0.75 |
| LEA14 wild type | — | 0.538 | 0.357 | 0.895 | 0.85 |
| LEA14 2.1 | 6 | 0.669 | 0.307 | 0.976 | 0.81 |
| BoPep4 wild type | — | 0.396 | 0.067 | 0.462 | 0.87 |
| BoPep4 2.1 | 9 | 0.497 | 0.634 | 1.131 | 0.77 |
| BoPep4 2.2 | 8 | 0.432 | 0.658 | 1.090 | 0.77 |

**Why three BoPep4 versions.** Wild-type BoPep4 was the weakest starting point of the whole construct series, with start+15 accessibility 0.396 and Shine-Dalgarno core accessibility 0.067, both below the usability threshold and below the Ho1 baseline, which is why this cargo had the most to gain. The three BoPep4 cassettes all use the SamyQ signal peptide and differ only in the first 15 codons, so they are the one place in our part set where the effect of 5′ recoding can be read on its own, with everything else held fixed. The untouched copy is kept as the baseline for the recoded versions and for the mutant and truncated peptides.

**Why 2.2 as well as 2.1.** The two solutions divide the gain differently. BoPep4 2.1 changed nine codons and reached start+15 0.497 with a Shine-Dalgarno core of 0.634, for a balance of 1.131; BoPep4 2.2 changed eight codons and reached start+15 0.432 with a Shine-Dalgarno core of 0.658, for a balance of 1.090. BoPep4 2.2 therefore gains more access at the Shine-Dalgarno core and less at the start codon, and we carry both so that the two can be compared at the bench.

## Why constitutive counterparts exist at all

We built the constitutive Pveg version of each cassette in addition to the light-sensing construct because it shows the maximal secretion and protein production rate without the light switch. These versions can be applied to plants and characterised directly by Western blot, which shows whether the constructs work under the most favourable conditions, and they give the light-controlled modules something to be compared against.

## About

* **Biosafety level:** S1
* **Target organism:** *Bacillus subtilis* WB800
* **Main purpose of use:** constitutive expression and secretion of a candidate stress-mitigation protein in *B. subtilis*
* **Potential application:** plant-growth-promoting and plant-protecting bioprotectants — lowering plant ethylene levels under stress (AcdS), protecting cellular structures and maintaining cellular stability under environmental stress (LEA14), and enhancing plant salt-stress tolerance (BoPep4)

Seven of the constitutive cassettes still carry the target organism as "*Bacillus subtilis* (168 / WB800)" on the part. The strain was settled as WB800 and those fields should be brought into line.

## References

1. UniProt Consortium. (n.d.). *Q5PWZ8*. UniProt. Retrieved October 18, 2026, from [UniProt entry Q5PWZ8](https://www.uniprot.org/uniprotkb/Q5PWZ8/entry)
2. Hontzeas, N., Zoidakis, J., Glick, B. R., & Abu-Omar, M. M. (2004). Expression and characterization of 1-aminocyclopropane-1-carboxylate deaminase from the rhizobacterium *Pseudomonas putida* UW4: A key enzyme in bacterial plant growth promotion. *Biochimica et Biophysica Acta, 1703*(1), 11–19. [https://doi.org/10.1016/j.bbapap.2004.09.015](https://doi.org/10.1016/j.bbapap.2004.09.015)
3. Shah, S., Li, J., Moffatt, B. A., & Glick, B. R. (1998). Isolation and characterization of ACC deaminase genes from two different plant growth-promoting rhizobacteria. *Canadian Journal of Microbiology, 44*(9), 833–843. [https://doi.org/10.1139/w98-074](https://doi.org/10.1139/w98-074)
4. Glick, B. R., Penrose, D. M., & Li, J. (1998). A model for the lowering of plant ethylene concentrations by plant growth-promoting bacteria. *Journal of Theoretical Biology, 190*(1), 63–68. [https://doi.org/10.1006/jtbi.1997.0532](https://doi.org/10.1006/jtbi.1997.0532)
5. Goyal, K., Walton, L. J., & Tunnacliffe, A. (2005). LEA proteins prevent protein aggregation due to water stress. *Biochemical Journal, 388*(1), 151–157. [https://doi.org/10.1042/bj20041931](https://doi.org/10.1042/bj20041931)
6. Hundertmark, M., Hincha, D. K., & Thalhammer, A. (2008). LEA (late embryogenesis abundant) proteins and their encoding genes in *Arabidopsis thaliana*. *BMC Genomics, 9*, Article 118. [https://doi.org/10.1186/1471-2164-9-118](https://doi.org/10.1186/1471-2164-9-118)
7. Jia, F., Qi, S., Li, H., Liu, P., Li, P., Wu, C., Zheng, C., & Huang, J. (2014). Overexpression of late embryogenesis abundant 14 enhances *Arabidopsis* salt stress tolerance. *Biochemical and Biophysical Research Communications, 454*(4), 505–511. [https://doi.org/10.1016/j.bbrc.2014.10.136](https://doi.org/10.1016/j.bbrc.2014.10.136)
8. Mertens, J., Aliyu, H., & Cowan, D. A. (2018). LEA proteins and the evolution of the WHy domain. *Applied and Environmental Microbiology, 84*(15), Article e00539-18. [https://doi.org/10.1128/AEM.00539-18](https://doi.org/10.1128/AEM.00539-18)
9. Singh, S., Cornilescu, C. C., Tyler, R. C., Cornilescu, G., Tonelli, M., Lee, M. S., & Markley, J. L. (2005). Solution structure of a late embryogenesis abundant protein (LEA14) from *Arabidopsis thaliana*, a cellular stress-related protein. *Protein Science, 14*(10), 2601–2609. [https://doi.org/10.1110/ps.051579205](https://doi.org/10.1110/ps.051579205)
10. Wang, A., Guo, J., Wang, S., Zhang, Y., Lu, F., Duan, J., Liu, Z., & Ji, W. (2022). BoPEP4, a C-terminally encoded plant elicitor peptide from broccoli, plays a role in salinity stress tolerance. *International Journal of Molecular Sciences, 23*(6), Article 3090. [https://doi.org/10.3390/ijms23063090](https://doi.org/10.3390/ijms23063090)
11. Li, R., Liu, M., Hu, X., Li, J., Pang, Q., Yan, X., Li, J., & Ji, W. (2026). Broccoli plant elicitor peptide BoPep4 enhances plant salt tolerance by improving glucosinolate metabolism. *Plant Science, 364*, 112954.
12. Wang, J. W., Squire, H. J., Goh, N. S., Ni, H. M., Lien, E., Wong, C., González-Grandío, E., & Landry, M. P. (2023). Delivered complementation in planta (DCIP) enables measurement of peptide-mediated protein delivery efficiency in plants. *Communications Biology, 6*(1), Article 829. [https://doi.org/10.1038/s42003-023-05191-5](https://doi.org/10.1038/s42003-023-05191-5)
13. Castillo-Hair, S. M., Baerman, E. A., Fujita, M., Igoshin, O. A., & Voigt, C. A. (2019). Optogenetic control of *Bacillus subtilis* gene expression. *Nature Communications, 10*, Article 3099. [https://doi.org/10.1038/s41467-019-10906-6](https://doi.org/10.1038/s41467-019-10906-6)
14. Lorenz, R., Bernhart, S. H., Höner zu Siederdissen, C., Tafer, H., Flamm, C., Stadler, P. F., & Hofacker, I. L. (2011). ViennaRNA Package 2.0. *Algorithms for Molecular Biology, 6*, Article 26. [https://doi.org/10.1186/1748-7188-6-26](https://doi.org/10.1186/1748-7188-6-26)
15. Kazusa DNA Research Institute. (n.d.). Codon usage database: *Bacillus subtilis* subsp. *subtilis* str. 168 (taxid:1423). [https://www.kazusa.or.jp/codon/](https://www.kazusa.or.jp/codon/)
16. Caro-Astorga, J., Rogan, M., Malcı, K., Ming, H., Debenedictis, E., James, P., & Ellis, T. (2025). SubtiToolKit: A bioengineering kit for *Bacillus subtilis* and Gram-positive bacteria. *Trends in Biotechnology, 43*(6), 1446–1469. [https://doi.org/10.1016/j.tibtech.2025.02.004](https://doi.org/10.1016/j.tibtech.2025.02.004)
17. BBa_K143012
18. BBa_K1074014
19. BBa_B0015
20. Deng, L. (2022). *Bacillus subtilis subsp. subtilis str. 168 chromosome, complete genome* `[GenBank sequence CP103783.1]`. GenBank. National Center for Biotechnology Information. [https://www.ncbi.nlm.nih.gov/nucleotide/CP103783.1](https://www.ncbi.nlm.nih.gov/nucleotide/CP103783.1)

---

# Experiment

This is the shared cloning workflow for every part in both collections. The Level 2 step that applies only to the two assembled systems is in the **Light-sensing circuit** collection, *Experiment*.

## Step 1 — Level 0 entry cloning of the signal-peptide fusion

Each signal-peptide–protectant–Histag coding sequence was amplified by PCR as a single amplicon from a synthesised fragment and cloned into an entry vector, to make the Level 0 entry step reliable before the Golden Gate reactions. The ligation was transformed into *E. coli* strain DH5α, and positive clones were identified by colony PCR and sent for sequencing to confirm the insert before use in the subsequent Golden Gate reactions.

* **Annealing temperature:** 60 °C
* **Template:** synthesised fragment
* **Entry vectors used:** pSTK-0C-sfGFP (chloramphenicol resistance, sfGFP dropout) for most fusions; pGEM-T Easy (ampicillin resistance, blue/white screening) for the Csn-AcdS-Histag fusion, screened with the T7 and SP6 primers that flank its insertion site

Each insert primer carries a 5′ ATATAT spacer, a BpiI site (GAAGAC) for Level 0 entry cloning, and a BsaI site (GGTCTC) for Level 1 assembly. The inner BsaI overhangs are TATG, incorporating the start codon of the signal peptide, at the 5′ end and TGTC at the 3′ end, which sets the coding-sequence position and allows fusion to the downstream terminator.

**Exception.** The wild-type SamyQ-BoPep4 cassette was built differently. SamyQ-BoPep4-Histag ([BBa_26ILD3SO](https://registry.igem.org/parts/bba-26ild3so)) was incorporated directly into Pveg-EEBD-RBS0-SamyQ-BoPep4-Histag-B0015 ([BBa_26FSZTWM](https://registry.igem.org/parts/bba-26fsztwm)) by de novo gene synthesis of the whole cassette, so there is no Level 0 entry step and no amplification of the coding-sequence fusion for it, and the SamyQ F and BoPep R primers were not needed.

## Step 2 — Level 1 Golden Gate assembly

The Level 0 parts — promoter, EEBD-RBS0 or RBS0, the signal-peptide fusion, and B0015 — were combined in a single Golden Gate reaction with BsaI (BsaI-HFv2), T4 DNA ligase buffer and T4 DNA ligase, in the order promoter, RBS, CDS, terminator. The reaction was transformed into *E. coli* DH5α, positive clones were identified by colony PCR and sent for sequencing, and verified clones were electroporated into *B. subtilis*.

The Level 1 vector depends on what the unit is for: pSTK-EXP1-sfGFP, the expression shuttle, for the constitutive cassettes that are expressed directly; pSTK-1A, -1B, -1C or -1D-sfGFP, the cloning vectors, for units destined for a Level 2 assembly.

| Temperature | Time   | Cycles    |
| ----------- | ------ | --------- |
| 37 °C       | 5 min  | 45 cycles |
| 16 °C       | 5 min  |           |
| 37 °C       | 10 min | 1 cycle   |
| 80 °C       | 20 min | 1 cycle   |

## Primers

Protectant insert primers:

| Primer name | Primer sequence (5′ to 3′) |
| ----------- | ------------------------------------------------------------------ |
| Csn F       | ATA TAT GAA GAC ATC TGA GGT CTC ATA TGA AAA TCA GTA TGC AAA AAG CA |
| SamyQ F     | ATA TAT GAA GAC ATC TGA GGT CTC ATA TGA TTC AAA AAC GAA AGC GGA C  |
| ACCD R      | ATA TAT GAA GAC ATG AGG GGT CTC ATG TCT TAA TGA TGA TGA TGA TGA T  |
| LEA R       | ATA TAT GAA GAC ATG AGG GGT CTC ATG TCT TAA TGA TGA TGA TGA TGA T  |
| BoPep R     | ATA TAT GAA GAC ATG AGG GGT CTC ATG TCA TGA TGA TGA TGA TGA TG     |

ACCD R and LEA R are the same sequence under two names, which is why the LEA14 cassettes are recorded in places as amplified with ACCD R.

Backbone and sequencing primers:

| Primer name | Primer sequence (5′ to 3′) |
| ----------- | --------------------------------- |
| pSTK-EXP-seq F | atagtcgatcggttcatcattcaccaaatca |
| pSTK-EXP-seq R | ctcactcattaggcaccccagg          |
| pSTK-seq F     | agtgccacctgacgtctaagaaacc       |
| pSTK-seq R     | tctttcctgcgttatcccctgattc       |

Colony screens on the Level 0 entry vector used the fusion's forward primer with the STK R primer that flanks the insertion site; screens on the Level 1 vector used either the fusion primers or the backbone primers above.

## Step 3 — Verification

Colonies from the transformation were screened by colony PCR with primers flanking the insertion site, and the products were run on an agarose gel alongside a DNA ladder to assess cloning success. A correct band runs at the expected size, which for a Level 0 entry screen is the length of the insert plus the vector sequence between the priming sites, and for a Level 1 screen is the length of the insert plus the vector sequence between the backbone priming sites. A band at that size confirms that a fragment of the correct length was ligated into the vector at the expected position. Colonies producing a single, clean band at that size were taken as positive candidates.

Positive candidates were then sequenced, to confirm that the insert is free of mutations and that the promoter, blocking device, RBS, protectant coding sequence and terminator are correct and correctly ordered. Clones with a verified sequence were used for the next Golden Gate reaction, or for expression experiments in the case of the pSTK-EXP1 constitutive cassettes.

Each part records its own expected band sizes, how many colonies gave that band, and which clone was taken forward. Those numbers stay on the parts, as does every expected-size placeholder that is still bracketed.

---

# Characterisation

This is the shared protein-detection method. The LPA illumination and sampling schedules for the light-controlled constructs are in the **Light-sensing circuit** collection, *Characterisation*.

## Immunodetection

Expression and secretion were assessed by Western blot of culture samples, detected with a mouse monoclonal anti-Histag primary antibody against the C-terminal 6x Histag on the fusion. A molecular weight ladder was run alongside; lane M is the marker. On the fractionation blot the ladders span 28–180 kDa on both sides of the gel, and the exposure was six minutes.

**What a blot settles and what it does not.** Immunodetection reports the presence of the tagged protein and its apparent size. It does not report enzymatic activity. Activity assays for ACC deaminase are still planned, so no blot in this collection measures the function of the secreted enzyme.

## Fractionation

To separate secreted protein from protein retained in the cell, cultures were split into three fractions:

| fraction | what it is |
| --- | --- |
| P1 | total pellet |
| P2 | soluble pellet |
| S | culture supernatant |

A band appearing only in the supernatant lanes is read as secretion. The one fractionation blot in the record is a single blot with no loading control, and it has two lanes labelled S whose distinction was not documented. That is why the Csn versus SamyQ comparison cannot yet be read off it.

## Purification

Purification of His-tagged ACC deaminase was followed on a blot of the eluted fractions, S1 to S4, which correspond to different concentrations of imidazole buffer: `[25 mM, 100 mM, 150 mM and 250 mM]`. Those concentrations are not corroborated elsewhere in the record and are still bracketed.

## Bioreactor time course

Production and secretion in the bioreactor were followed by sampling two sides of the membrane: the lumen side, as a cell lysate fraction and a culture medium fraction, and the shell side, as a culture medium fraction. Samples were taken at t = 14, 16, 18, 20, 22, 24, 40, 42 and 44 h, to assess expression, secretion efficiency and diffusion across the membrane.

## Anti-His ELISA

Where a quantitative figure was wanted, an anti-His ELISA was run on the same culture samples as the blot, with two samples a side, and reported as a concentration in µg/mL. The ELISA is a second read of the same material rather than an independent experiment, and with two samples a side the ranges can overlap; where they do, the difference should not be reported as a difference. The figures themselves belong to the construct they were measured on and stay on that part.

## The apparent size of ACC deaminase is not settled

Four sizes for the same cargo appear across the collection and have not been reconciled: about 35 kDa as the predicted monomer; about 37 kDa in the culture supernatant of the constitutive Pveg constructs, read as consistent with the predicted size of the secreted enzyme; 41 kDa for the purified recombinant enzyme of Hontzeas et al. (2004), which carries neither a cleaved signal peptide nor a His tag; and bands running from roughly 63 to 75 kDa and between the 75 and 100 kDa markers on the Level 2 blots, which may be the approximately 70 kDa homodimer. The 41 kDa and 37 kDa forms have not been compared directly, and the dimer reading is a possibility we plan to test rather than a result.

## Plant work

The constitutive cassettes are the versions intended to go to plants: they give the maximal secretion and production of each protectant, and the protein they secrete can be applied to plants for functional testing. The constitutive LEA14 and BoPep4 cassettes were carried for this reason in place of light-responsive Module 4 versions, and both are recorded as having helped plants under salinity stress, which is the only plant readout in the part record.

**The design of the plant trials is not in this pack.** Species, dose, application method, duration, replication and controls are not recorded in the registry documentation for any of these parts, and nothing here should be read as describing them. Until the trial design is written down, the only defensible statement at collection level is the one above: that the constitutive cassettes are the ones applied to plants, and that salinity stress is the condition under which an effect was reported. A method for measuring peptide-mediated protein delivery efficiency in plants is cited on the LEA14 parts (Wang, J. W., et al., 2023) but is not reported as having been used.

---

# Application

## What the collection is for

These parts are the payload of a stress-responsive optogenetic bioreactor for precision plant protection. A Protectant Module constitutively expresses a candidate stress-mitigation protein and lets its secretion and detection be evaluated, using the constitutive promoter Pveg, the ribosome binding site EEBD-RBS0 and the terminator B0015. The light-responsive modules, which replace Pveg with PcpcG2-veg so that the same cargo is released on demand, are in the **Light-sensing circuit** collection.

## How the parts build on each other

Each cargo runs up the same ladder, so a reader can find any part's place in one table instead of on twenty pages.

| cargo | coding sequence | signal-peptide fusion | constitutive cassette | light-responsive cassette | Level 2 system |
| --- | --- | --- | --- | --- | --- |
| AcdS, wild type | BBa_26MA70QI | BBa_26NXOP7S (Csn) | BBa_26CXI09X | BBa_26Q3LKZU | BBa_2654HAF3 |
| AcdS 2.1 | BBa_262YYNPV | BBa_26TOGLX3 (SamyQ) | BBa_26XVQ3FS | BBa_26DE5E2Q | BBa_26U8UTMH |
| LEA14, wild type | BBa_26LTB0W1 | BBa_26ZQ1T72 (Csn) | BBa_26SG0NQQ | not built | not built |
| LEA14 2.1 | BBa_26IN6G1D | BBa_26J0GJGZ (SamyQ) | BBa_26D5AX7S | not built | not built |
| BoPep4, wild type | BBa_265CD14Z | BBa_26ILD3SO (SamyQ) | BBa_26FSZTWM | not built | not built |
| BoPep4 2.1 | BBa_26LYCBW0 | BBa_26PX0UGH (SamyQ) | BBa_269A97I7 | not built | not built |
| BoPep4 2.2 | BBa_26ERHWWI | BBa_267B69E3 (SamyQ) | BBa_26IA55UY | not built | not built |
| BoPep4 (15-23) | BBa_26YHOQCL | not built | not built | not built | not built |
| BoPep4 (9-23) | — | — | BBa_26Z8FHTR | not built | not built |

EEBD-RBS0 ([BBa_26V6CPEV](https://registry.igem.org/parts/bba-26v6cpev)) and RBS0 ([BBa_26OSLRE4](https://registry.igem.org/parts/bba-26oslre4)) sit in the same position in every row.

## Why no full circuit was built for LEA14 or BoPep4

A full ccaSR construct with LEA14 or with BoPep4 as Module 4 was not built. The constitutive versions let the behaviour of those cargoes be assessed, and they also helped plants under salinity stress, without duplicating the assembly work, because the two ACC deaminase Level 2 systems already serve as the proof of concept for the circuit.

## What each cargo is for

* **AcdS**: lowering plant ethylene levels under stress, as a component of plant-growth-promoting bioprotectants.
* **LEA14**: protecting cellular structures and maintaining cellular stability under environmental stress conditions.
* **BoPep4**: enhancing plant salt-stress tolerance, as a component of plant-protecting bioprotectants.

---

# Discussion

## What the data mean

ACC deaminase is expressed in *B. subtilis* and secreted into the culture medium, so the construct works under optimal, constitutive conditions. Yield in the bioreactor was low, so there is room to improve it.

## Limitations

Western blots show presence and apparent size, not enzymatic activity, and activity assays are still planned. Pveg, EEBD-RBS0 and B0015 are reused across modules, which creates a risk of homologous recombination in the full circuit; sequence verification of the assembled construct is the only check applied so far.

The Csn versus SamyQ comparison that the matched pairs were built to support has not yet been made: both constitutive ACC deaminase constructs give a band at about 37 kDa, and the two supernatant lanes on the one fractionation blot were not labelled distinguishably.

The 5′ recoding scores are predictions from a folding model. Translation initiation from the recoded cassettes has not been measured, so the ranking of wild type, 2.1 and 2.2 is a prediction to be tested, not a result.

## Future directions

Improve yield through promoter strength and codon optimisation; measure ACC deaminase activity directly rather than inferring it from a band; compare Csn with SamyQ on a blot where the two lanes are distinguishable; and read the three BoPep4 cassettes against each other at the bench to test whether the predicted balance scores track measured output.

---

# Values still bracketed

Unresolved placeholders inside the text above, kept bracketed because nothing in the record corroborates them:

| value | where it came from | why it is still open |
| --- | --- | --- |
| `[25 mM, 100 mM, 150 mM and 250 mM]` | BBa_26CXI09X, Characterisation — the imidazole concentrations for purification fractions S1–S4 | not corroborated anywhere |
| `[GenBank sequence CP103783.1]` | BBa_26CXI09X, BBa_26MA70QI and BBa_26NXOP7S, Design — the fourth reference | not corroborated anywhere, and it names the *B. subtilis* 168 genome rather than the *P. putida acdS* source |

Placeholders that stay on the individual parts — expected band sizes, clone numbers, the Level 1 antibiotic marker, the BsaI-HFv2 catalogue form — are listed in `per-part-cuts.md`.
