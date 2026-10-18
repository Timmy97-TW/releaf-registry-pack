# Collection documentation — Light-sensing circuit

GEMS-Taiwan 2026. One entry per registry documentation type, each delimited by `---` and headed with the type name, so that a single entry can be pasted into the collection editor at a time.

**Members.** The four Level 1 transcription units and Level 0 parts that make up the CcaSR light-sensing chassis:

| part | title | role |
| --- | --- | --- |
| [BBa_26XZYM10](https://registry.igem.org/parts/bba-26xzym10) | PtagC+RBS-Ho1:pcyA-L3S2P21 | Module 1, PCB production |
| [BBa_26A4MT29](https://registry.igem.org/parts/bba-26a4mt29) | PtagC+RBS | promoter and RBS of Module 1 |
| [BBa_261XH2RS](https://registry.igem.org/parts/bba-261xh2rs) | PliaG-RBS0-ccaS-m3-B0015 | Module 2, light sensing |
| [BBa_26BDO8AQ](https://registry.igem.org/parts/bba-26bdo8aq) | Pveg-RBS0-ccaR-B0015 | Module 3, signal transduction |

**Members shared with the Protectant modules collection.** The two light-responsive output cassettes and the two assembled Level 2 systems:

| part | title |
| --- | --- |
| [BBa_26Q3LKZU](https://registry.igem.org/parts/bba-26q3lkzu) | PcpcG2-veg-EEBD-RBS0-Csn-AcdS-Histag-B0015 |
| [BBa_26DE5E2Q](https://registry.igem.org/parts/bba-26de5e2q) | PcpcG2-veg-EEBD-RBS0-SamyQ-AcdS 2.1-Histag-B0015 |
| [BBa_2654HAF3](https://registry.igem.org/parts/bba-2654haf3) | ccaSR-Csn-AcdS-Histag |
| [BBa_26U8UTMH](https://registry.igem.org/parts/bba-26u8utmh) | ccaSR-SamyQ-AcdS 2.1-Histag |

Two further parts, EEBD-RBS0 ([BBa_26V6CPEV](https://registry.igem.org/parts/bba-26v6cpev)) and RBS0 ([BBa_26OSLRE4](https://registry.igem.org/parts/bba-26oslre4)), are used by both collections and are documented under **Protectant modules**.

**If the registry does not allow a part in two collections.** Put the four hybrids — BBa_26U8UTMH, BBa_2654HAF3, BBa_26DE5E2Q, BBa_26Q3LKZU — in this collection, since the light switch is what distinguishes them, and leave BBa_26V6CPEV and BBa_26OSLRE4 in **Protectant modules**, which has the larger claim on them.

**What this document is for.** The Registry Rules say documentation that applies to a group of parts belongs to the collection and should not be copied onto each part. Everything below was previously repeated across the member parts. Each part keeps only what is intrinsic to it: its own sequence, its own expected band sizes, its own gels and blots, and its own clone numbers.

**Division of labour with the other collection.** To avoid moving the duplication up a level rather than removing it, the shared Level 0 and Level 1 cloning method, the Level 1 cycling conditions, the backbone and insert primers, the screening practice and the immunodetection and ELISA methods are written once in the **Protectant modules** collection. This document carries what is specific to the light circuit: the switch logic, the light-module primers, the Level 2 assembly, and the LPA illumination schedules.

---

# Design

## What the collection is

The light-sensing circuit is the CcaSR green/red two-component system of *Synechocystis* sp. PCC 6803, adapted to *Bacillus subtilis* and rebuilt so that light is the only input. It is carried as four Level 1 transcription units that are combined into one Level 2 plasmid, after which *B. subtilis* can sense a light signal and respond to it on its own.

The chain runs in this order:

1. **Module 1, PCB production** ([BBa_26XZYM10](https://registry.igem.org/parts/bba-26xzym10)): PtagC+RBS ([BBa_26A4MT29](https://registry.igem.org/parts/bba-26a4mt29)) – *ho1:pcyA* ([BBa_K4354012](https://registry.igem.org/parts/bba-k4354012)) – L3S2P21 (BBa_K2675031). Ho1 converts endogenous heme to biliverdin IXα and PcyA reduces biliverdin IXα to phycocyanobilin (PCB). Fusing the two enzymes into a single coding sequence raises PCB production about 80-fold (Castillo-Hair et al., 2019), keeps the module compact and keeps the two activities stoichiometrically matched.
2. **Module 2, light sensing** ([BBa_261XH2RS](https://registry.igem.org/parts/bba-261xh2rs)): PliaG (BBa_K823000) – RBS0 ([BBa_26OSLRE4](https://registry.igem.org/parts/bba-26oslre4)) – *ccaS-m3* (BBa_K3317069) – B0015 (BBa_B0015). CcaS binds PCB through its GAF domain and is made in a green-light-sensitive ground state with low autokinase activity.
3. **Module 3, signal transduction** ([BBa_26BDO8AQ](https://registry.igem.org/parts/bba-26bdo8aq)): Pveg (BBa_K143012) – RBS0 – *ccaR* (BBa_K5431017) – B0015. CcaR is the response regulator cognate to CcaS.
4. **Module 4, light-responsive expression**: PcpcG2-veg (BBa_254UKC9E) – EEBD-RBS0 ([BBa_26V6CPEV](https://registry.igem.org/parts/bba-26v6cpev)) – a signal-peptide–protectant–6x Histag fusion – B0015. The two built versions are [BBa_26Q3LKZU](https://registry.igem.org/parts/bba-26q3lkzu) (Csn-AcdS-Histag) and [BBa_26DE5E2Q](https://registry.igem.org/parts/bba-26de5e2q) (SamyQ-AcdS 2.1-Histag).

Modules 1 to 3 are a reusable chassis; only Module 4 defines the output.

## How the circuit works

Holo-CcaS is produced in a green-light-sensitive ground state with low autokinase activity, with a photostate absorbance maximum at 535 nm. Absorption of a green photon switches CcaS to a red-light-sensitive active state with high autokinase activity, with a photostate absorbance maximum at 672 nm. The active kinase transfers a phosphoryl group from ATP to a conserved histidine in its own kinase domain, and from there to a conserved aspartate on CcaR. Phosphorylated CcaR binds the operator region of the PcpcG2 promoter and activates transcription from it. Red light reverts CcaS to the ground state and de-activates PcpcG2 transcription, probably through CcaS-mediated dephosphorylation of CcaR (Castillo-Hair et al., 2019; Hirose et al., 2008).

The 535 nm and 672 nm figures are absorbance maxima of the CcaS photostates (Hirose et al., 2008). They are distinct from the illumination used in the published characterisation, which was delivered by a Light Plate Apparatus with 520 nm green and 660 nm red LEDs (Castillo-Hair et al., 2019).

In the original description of the pathway, autophosphorylation of the CcaS histidine kinase domain is up-regulated by green light, and CcaS then phosphorylates CcaR, which induces *cpcG2* expression (Hirose et al., 2008).

## Dependence on the PCB module

CcaS is photoactive only as a holoprotein with PCB bound to its GAF domain, and *B. subtilis* does not make PCB natively. Module 2 therefore has no function on its own, and the circuit works only with all four modules on the same plasmid. Heme is an endogenous substrate in *B. subtilis*, so the PCB module needs no added precursor; ferredoxin is required as the electron donor for PcyA.

## Pveg versus PcpcG2-veg: which promoter sits where, and why

Four different promoters are used across the circuit, and the choice on each module is deliberate.

| module | promoter | character | why this one |
| --- | --- | --- | --- |
| 1, PCB production | PtagC+RBS | constitutive promoter and RBS in one part | shorter in base pairs than Pveg plus RBS0, which makes Level 2 cloning easier and cuts down repeated sequence; the plasmid was already amplified in our collection |
| 2, light sensing | PliaG | weak constitutive σA promoter | keeps CcaS inside the range that the PCB supply can load |
| 3, transduction | Pveg | strong constitutive | high, continuous CcaR, so light is the only input |
| 4, output | PcpcG2-veg | light-responsive, activated by phosphorylated CcaR | the switch itself |

**Why constitutive promoters on the sensor and the regulator.** The published system expresses *ccaS* from the xylose-inducible PxylA promoter and *ccaR* from the IPTG-inducible Phy-spank promoter (Castillo-Hair et al., 2019), so the levels of both proteins are set by chemical inducers (Haller et al., 2025). Our bioreactor is intended to run on light alone, without xylose or IPTG dosing, so we replaced both inducible promoters with constitutive ones. This substitution is our own design decision and is not part of the published system.

**Why a weak promoter on the sensor.** Castillo-Hair et al. (2019) found that output falls again at high CcaS levels, probably because PCB becomes limiting and the resulting apo-CcaS has phosphatase activity. A weak promoter keeps CcaS inside the range where the PCB supplied by Module 1 can be loaded onto it. PliaG is the promoter of the *liaG* gene of *B. subtilis*, described in the Registry as a weak constitutive promoter and characterised as part of the Bacillus BioBrick Box, whose constitutive promoters span more than three orders of magnitude (Radeck et al., 2013).

**Why a strong promoter on the regulator.** Pveg gives high, continuous expression, and Castillo-Hair et al. (2019) report that of all the cyanobacterial genes in their study *ccaR* was the only one that did not initially suffer from poor expression. Expressing CcaR constitutively also means its level no longer tracks an inducer, so it becomes a fixed property of the strain.

**How PcpcG2-veg was engineered.** The output promoter was adapted to *B. subtilis* in stages by Castillo-Hair et al. (2019). The starting point was PcpcG2-172, the *E. coli*-optimised truncation of Schmidl et al. (2014), which removes an unwanted transcriptional start site. In *B. subtilis* it was weak. Swapping the original −10 hexamer for the *B. subtilis* consensus sequence, to improve σA RNA polymerase recruitment, gave PcpcG2-hy and about three times more output. Replacing the proximal region, meaning the sequence following the −10 hexamer, with that of the strong constitutive promoters PrpsD and Pveg gave the chimeras PcpcG2-rpsD and PcpcG2-veg; those two swaps are reported as increasing output transcription by 22- and 44-fold, and PcpcG2-veg was selected for its superior activity.

The values below are from Castillo-Hair et al. (2019), measured in *B. subtilis* PY79 by calibrated flow cytometry with an sfGFP reporter. They are not our measurements.

| Output promoter | Induced output (MEFL) | Uninduced output (MEFL) |
| --------------- | --------------------- | ----------------------- |
| PcpcG2-172      | 555 ± 65              | not reported            |
| PcpcG2-hy       | 1470 ± 110            | not reported            |
| PcpcG2-rpsD     | 32,400 ± 2800         | 174 ± 23                |
| PcpcG2-veg      | 64,000 ± 7600         | 378 ± 38                |

Two limits of that engineering matter for reading the parts. The −35 box was left untouched, and only the −10 hexamer and the proximal region downstream of it were changed, because the CcaR operator region had to be kept intact. We chose PcpcG2-veg as the output promoter for the same reason it was selected in the published work, its higher output.

**Why constitutive counterparts of the output cassette exist.** The constitutive Pveg versions of the Module 4 cassette give the maximal secretion and production of the same cargo without the light switch, so the light-controlled module has something to be compared against. Those parts are documented in the **Protectant modules** collection.

## Why the miniaturised sensor variant

We used *ccaS-m3* in place of full-length *ccaS*. It is a miniaturised variant of *ccaS*, corresponding to mini-CcaS#3 of Nakajima et al. (2016), in which the L1 linker and the two PAS domains are deleted and the GAF and histidine kinase domains are joined through a shortened linker. The miniaturised variants remove the two PAS domains, whose function in CcaS is not known, and several of them regulate gene expression better than the wild-type kinase.

Castillo-Hair et al. (2019) tested *ccaSm3* and *ccaSm10* in *B. subtilis* PY79 and reported that both increased dynamic range about ten-fold, to 71 ± 12-fold for *ccaSm3* and 62 ± 12-fold for *ccaSm10*; the two were not statistically different in *B. subtilis* (p = 0.49) and *ccaSm10* gave lower overall output, so the system containing *ccaSm3* was named *B. subtilis* CcaSR v1.0. The same PAS deletions applied in the *E. coli* CcaSR v2.0 context gave a v3.0 sensor four times less leaky, with a dynamic range of nearly 600-fold and no deleterious effect on green light sensitivity or response dynamics (Ong & Tabor, 2018). We took *ccaS-m3* as the better-supported choice on both counts, low background and high dynamic range.

## Why the blocking device sits only on the output module

EEBD-RBS0 is on Module 4 and absent from Modules 1 to 3, because of the cargo. The EEBD is an *Escherichia coli* expression-blocking device: a B0015 double terminator between two recombination sites, which stops transcription reaching the coding sequence while a construct is being assembled and propagated in *E. coli*, and so prevents unwanted expression and the production of proteins that would be toxic to the cloning host.

ACC deaminase is a secreted enzyme carried on a Sec signal peptide, and expression during cloning in *E. coli* risks unwanted protein production and loss of the construct. CcaS and CcaR, by contrast, have nothing to act on in *E. coli*, which has neither PCB nor a PcpcG2 promoter. Placing the device in front of the protectant coding sequence keeps the cassette silent through the *E. coli* steps, and the same EEBD-RBS0 part supplies the RBS for that coding sequence.

## Reuse of standard parts, and the recombination risk it carries

Pveg, RBS0 and B0015 are reused across our modules, which keeps every cassette in the same SubtiToolKit format and makes the Level 2 assembly straightforward (Caro-Astorga et al., 2025). The cost is that the Level 2 system carries several copies of the same promoter, RBS and terminator sequence, which creates a risk of homologous recombination between modules in the assembled circuit. We accepted this at Level 1, and sequence verification of the full Level 2 construct is the check on it. Module 1 uses PtagC+RBS in place of Pveg and RBS0 partly for the same reason.

B0015 is a high-efficiency double transcriptional terminator that stops RNA polymerase continuing past the coding sequence and prevents transcriptional read-through into downstream modules. L3S2P21 on Module 1 is a strong synthetic intrinsic (Rho-independent) terminator from the library of Chen et al. (2013), which ends transcription and limits read-through into neighbouring units. RBS0 is the ribosome binding site, which sets translation initiation of the downstream coding sequence.

## The main design risk: background activation of CcaR

In the published v0.1 system, adding IPTG alone, which raised CcaR without any green light, increased sfGFP output up to 40-fold, probably because CcaR can be phosphorylated by a small-molecule donor such as acetyl phosphate (Castillo-Hair et al., 2019). The amount of CcaR in the cell therefore sets how much output the circuit gives in the dark, and a constitutive promoter fixes that background.

Dark-state and red-light output must be measured in our strain and reported alongside the green-light output; a fold-change quoted without a measured background would not be meaningful. **These measurements have not yet been made.** If the background proves too high, the correction is a weaker promoter or a weaker RBS on Module 3.

## Why optogenetic control at all

Our original plan was to release engineered rhizobacteria that sensed stress themselves, which limits the usable stressors, and crops also differ in their thresholds. Heat stress in *Arabidopsis* starts at about 30–37 °C, whereas peanut tolerates about 35–40 °C. Using light as the only input lets the user program thresholds per crop through a microcontroller-based sensor, without redesigning the genetic circuit.

## About

* **Biosafety level:** S1
* **Target organism:** *Bacillus subtilis* WB800
* **Main purpose of use:** green/red light-controlled expression and secretion of a protectant protein in *B. subtilis*
* **Potential application:** controlling the release of plant-growth-promoting protectants with green and red light

## References

1. Hirose, Y., Shimada, T., Narikawa, R., Katayama, M., & Ikeuchi, M. (2008). Cyanobacteriochrome CcaS is the green light receptor that induces the expression of phycobilisome linker protein. *Proceedings of the National Academy of Sciences, 105*(28), 9528–9533. [https://doi.org/10.1073/pnas.0801826105](https://doi.org/10.1073/pnas.0801826105)
2. Nakajima, M., Ferri, S., Rögner, M., & Sode, K. (2016). Construction of a miniaturized chromatic acclimation sensor from cyanobacteria with reversed response to a light signal. *Scientific Reports, 6*, Article 37595. [https://doi.org/10.1038/srep37595](https://doi.org/10.1038/srep37595)
3. Ong, N. T., & Tabor, J. J. (2018). A miniaturized *Escherichia coli* green light sensor with high dynamic range. *ChemBioChem, 19*(12), 1255–1258. [https://doi.org/10.1002/cbic.201800007](https://doi.org/10.1002/cbic.201800007)
4. Castillo-Hair, S. M., Baerman, E. A., Fujita, M., Igoshin, O. A., & Voigt, C. A. (2019). Optogenetic control of *Bacillus subtilis* gene expression. *Nature Communications, 10*, Article 3099. [https://doi.org/10.1038/s41467-019-10906-6](https://doi.org/10.1038/s41467-019-10906-6)
5. Haller, D. J., Castillo-Hair, S. M., & Tabor, J. J. (2025). Optogenetic control of *B. subtilis* gene expression using the CcaSR system. In A. Baumschlager (Ed.), *Optogenetics* (Methods in Molecular Biology, Vol. 2840, pp. 1–17). Humana. [https://doi.org/10.1007/978-1-0716-4047-0_1](https://doi.org/10.1007/978-1-0716-4047-0_1)
6. Radeck, J., Kraft, K., Bartels, J., Cikovic, T., Dürr, F., Emenegger, J., Kelterborn, S., Sauer, C., Fritz, G., Gebhard, S., & Mascher, T. (2013). The Bacillus BioBrick Box: generation and evaluation of essential genetic building blocks for standardized work with *Bacillus subtilis*. *Journal of Biological Engineering, 7*(1), 29. [https://doi.org/10.1186/1754-1611-7-29](https://doi.org/10.1186/1754-1611-7-29)
7. Schmidl, S. R., Sheth, R. U., Wu, A., & Tabor, J. J. (2014). Refactoring and optimization of light-switchable *Escherichia coli* two-component systems. *ACS Synthetic Biology, 3*(11), 820–831. [https://doi.org/10.1021/sb500273n](https://doi.org/10.1021/sb500273n)
8. Chen, Y.-J., Liu, P., Nielsen, A. A. K., et al. (2013). Characterization of 582 natural and synthetic terminators and quantification of their design constraints. *Nature Methods, 10*(7), 659–664.
9. Caro-Astorga, J., Rogan, M., Malcı, K., Ming, H., Debenedictis, E., James, P., & Ellis, T. (2025). SubtiToolKit: A bioengineering kit for *Bacillus subtilis* and Gram-positive bacteria. *Trends in Biotechnology, 43*(6), 1446–1469. [https://doi.org/10.1016/j.tibtech.2025.02.004](https://doi.org/10.1016/j.tibtech.2025.02.004)
10. Fernández, S., Ayora, S., & Alonso, J. C. (2000). *Bacillus subtilis* homologous recombination: Genes and products. *Research in Microbiology, 151*(6), 481–486.
11. BBa_K823000
12. BBa_K143012
13. BBa_B0015
14. BBa_K4354012
15. BBa_K2675031

---

# Experiment

The Level 0 entry cloning, the Level 1 Golden Gate reaction, the Level 1 cycling conditions, the backbone sequencing primers and the screening practice are common to every part in both collections and are written once in the **Protectant modules** collection, *Experiment*. This entry carries what is specific to the light circuit.

## Which Level 1 vector each module went into

Each module was built and sequence-verified as a Level 1 transcription unit in a SubtiToolKit Level 1 vector before Level 2 assembly (Caro-Astorga et al., 2025). The four positions are fixed by the vector:

| module | part | Level 1 vector |
| --- | --- | --- |
| 1, PCB production | BBa_26XZYM10 | pSTK-1A-sfGFP |
| 2, light sensing | BBa_261XH2RS | pSTK-1B-sfGFP |
| 3, transduction | BBa_26BDO8AQ | pSTK-1C-sfGFP |
| 4, output | BBa_26Q3LKZU, BBa_26DE5E2Q | pSTK-1D-sfGFP |

Each module was assembled from its Level 0 parts in the order promoter, RBS, CDS, terminator, by Golden Gate with BsaI-HFv2, T4 DNA ligase and T4 DNA ligase buffer. The reactions were transformed into *E. coli* DH5α, positive clones were identified by colony PCR and sent for sequencing, and verified clones went forward to the Level 2 assembly in pSTK-EXP2.

## Light-module primers

Each insert primer carries a 5′ ATATAT spacer, a BpiI site (GAAGAC) for Level 0 entry cloning, and a BsaI site (GGTCTC) for Level 1 assembly. The inner BsaI overhangs are TATG, incorporating the start codon, at the 5′ end and TGTC at the 3′ end, which sets the coding-sequence position and allows fusion to the downstream terminator.

| Primer name | Primer sequence (5′ to 3′) |
| ----------- | ------------------------------------------------------------------ |
| Ho1 F       | ATATATGAAGACATCTGAGGTCTCATATGTCAGTAAATTTAGCATCA                    |
| pcyA R      | ATATATGAAGACATGAGGGGTCTCATGTCTTACTGGATGACATCAAA                    |
| ccaS F      | ATA TAT GAA GAC ATC TGA GGT CTC ATA TGG GAA AAT TTT TAA TTC CAA TT |
| ccaS R      | ATA TAT GAA GAC ATG AGG GGT CTC ATG TCT TAA GCT CGA GGC AAA TGG T  |
| ccaR F      | ATA TAT GAA GAC ATC TGA GGT CTC ATA TGA GAA TTC TTT TAG TGG AGG AT |
| ccaR R      | ATA TAT GAA GAC ATG AGG GGT CTC ATG TCC TAG TTT TTC CCT TGG CAC AA |
| pSTK-seq F  | agtgccacctgacgtctaagaaacc                                          |
| pSTK-seq R  | tctttcctgcgttatcccctgattc                                          |

The *ccaS-m3* and *ccaR* coding sequences were each amplified as a single amplicon from a synthesised fragment and cloned into an entry vector before Level 1 assembly: pGEM-T Easy for *ccaR*, and `[pGEM-T Easy]` for *ccaS-m3*, which is not corroborated elsewhere in the record and is still bracketed on that part.

## Level 2 assembly

The four sequence-verified Level 1 units were combined in a single Golden Gate reaction into the pSTK-EXP2 Level 2 vector, in the order Module 1 – Module 2 – Module 3 – Module 4. Two vector-to-insert ratios were tested, 1:5 and 1:7. The reaction was transformed into *E. coli* DH5α, clones were screened by colony PCR with primers specific to each module and sequence-verified, and the verified plasmid was electroporated into *B. subtilis* 168 and WB800 at 2.1–2.3 kV.

* **Vector:** pSTK-EXP2 (Level 2 vector)
* **Assembly method:** Golden Gate, BsmBI
* **Vector-to-insert ratios tested:** 1:5 and 1:7

| Temperature | Time   | Cycles    |
| ----------- | ------ | --------- |
| 42 °C       | 5 min  | 45 cycles |
| 16 °C       | 5 min  |           |
| 55 °C       | 10 min | 1 cycle   |
| 80 °C       | 20 min | 1 cycle   |

## Verifying a Level 2 construct

Colonies from the Level 2 transformation were screened by colony PCR with primers specific to each module, and the products were run on an agarose gel alongside a DNA ladder. A colony was a positive candidate only if it gave a band of the expected size for the modules. Positive candidates were then sequenced to confirm that all four modules are correct and in the right order. Every module was checked, because one module being positive does not verify the state of the others. Confirmed constructs were electroporated into *B. subtilis* and grown into liquid culture to start functional runs in the LPA.

| Primer      | Sequence                       |
| ----------- | ------------------------------ |
| L2-pcyA-F   | GCG AAG CAT GGG CAG AAA GA     |
| L2-ccaSm3 R | GCG TTC TTG GTT TTG TCT GTG CC |
| L2-ccaSm3 F | GGG AAC AGG ACT CGG TTT AAT GG |
| L2-ccaR R   | CCA GCG GCA AAT CAT CCT CC     |
| L2-ccaR F   | GGT CCA TGG CAT TGG GTA TCG    |
| L2-SamyQ R  | GAA CGA AAC TGT CCG CTT TCG TT |

The three junctions screened with these primers have expected sizes of 375 bp (Ho1:pcyA forward with CcaSm3 reverse), 632 bp (CcaSm3 forward with CcaR reverse) and 441 bp (CcaR forward with ACCD reverse).

---

# Characterisation

The immunodetection and ELISA methods are common to both collections and are written once in the **Protectant modules** collection, *Characterisation*. This entry carries the illumination and sampling schedules, and the circuit-level reading of the results.

## The Light Plate Apparatus

Functional runs were done in a Light Plate Apparatus (LPA). Cultures carrying an assembled Level 2 construct were grown under green light, which is expected to activate output, or under red light, which served as the repressing control. Intensity is set as a percentage of full output.

Three schedules were run across the two Level 2 constructs:

| construct | light | sampling |
| --- | --- | --- |
| ccaSR-Csn-AcdS-Histag (ABDI) in WB800 | green 100%, green 12%, green 2%, red 100% | before exposure (0 h), then 2, 4, 6 and 8 h |
| ccaSR-SamyQ-AcdS 2.1-Histag (ABDQ) | green 100% and red 100% | 13 h and 16 h after exposure |
| ccaSR-SamyQ-AcdS 2.1-Histag (ABDQ), secondary regulation | dark overnight (16 h), then green 100% | 3, 6 and 8 h after the light was turned on |

Samples from the 13 h and 16 h run were read twice, by Western blot and by anti-His ELISA on the same four samples, with two samples a side.

## What the runs establish, and what they do not

Immunodetection of a His-tagged cargo reports presence and apparent size, not enzymatic activity. Activity assays for ACC deaminase are still planned, so none of the LPA runs measures the function of the secreted enzyme.

Dark-state and red-light output in our strain still need to be measured and reported alongside green-light output. Until they are, a fold-change for the circuit would not be meaningful. See *Design*, "The main design risk: background activation of CcaR".

## The apparent size of ACC deaminase is not settled

Four different sizes for the same cargo appear across the parts in this collection and the constitutive cassettes, and they have not been reconciled:

| figure | where it comes from |
| --- | --- |
| about 35 kDa | predicted monomer |
| about 37 kDa | observed in the culture supernatant of the constitutive Pveg constructs, read as consistent with the predicted size of the secreted enzyme |
| 41 kDa | the purified recombinant enzyme of Hontzeas et al. (2004), which carries neither a cleaved signal peptide nor a His tag |
| roughly 63 to 75 kDa, and between the 75 and 100 kDa markers | observed on the Level 2 LPA blots |

ACC deaminase can also form a homodimer of about 70 kDa, so the high bands may be the dimer. That is a possibility we plan to test, not a result. The 41 kDa figure and the 37 kDa band have not been compared directly.

---

# Application

## What the collection is for

The circuit exists to release plant-protective proteins only when and where they are needed. Modules 1 to 3 are a reusable light-sensing chassis and only Module 4 defines the output, so any protectant cassette can in principle be placed behind PcpcG2-veg.

Two complete systems were assembled and are documented as parts:

* **ccaSR-Csn-AcdS-Histag** ([BBa_2654HAF3](https://registry.igem.org/parts/bba-2654haf3)): produces and secretes ACC deaminase on the Csn signal peptide under green/red light control.
* **ccaSR-SamyQ-AcdS 2.1-Histag** ([BBa_26U8UTMH](https://registry.igem.org/parts/bba-26u8utmh)): the same output on the SamyQ signal peptide, with the recoded *acdS* 2.1 coding sequence.

Each carries four Level 1 transcriptional units on a single plasmid: PCB production, the sensor kinase CcaS-m3, the response regulator CcaR, and the output cassette that secretes ACC deaminase under green light. Because *B. subtilis* does not make PCB, the circuit works only with all four together.

## Why light is the input

Crops differ in their stress thresholds, so a strain that sensed stress itself would have to be redesigned for each stressor and each crop. With light control, a user sets thresholds per crop through a microcontroller-based sensor that switches the light, without redesigning the genetic circuit. Replacing the published inducible promoters with constitutive ones also means no inducer dosing is required. This is the role the circuit plays in our bioreactor.

## No full circuit was built with LEA14 or BoPep4

A full ccaSR construct with LEA14 or with BoPep4 as Module 4 was not built. The constitutive versions of those cassettes let their behaviour be assessed without repeating the assembly, because the two ACC deaminase systems above already serve as the proof of concept for the circuit. Those cassettes are documented in the **Protectant modules** collection.

---

# Discussion

## Use in plant protection

A secreted ACC deaminase lowers stress ethylene around roots, so it could be used as part of a plant-growth-promoting bioprotectant. Light as the only input is a practical advantage over circuits that sense stress themselves, for the reason given under *Application*.

## A modular platform for other protectants

Modules 1 to 3 form a reusable light-sensing chassis, and only Module 4 defines the output. The three cargo families we carry could each sit there:

* **AcdS** lowers ethylene levels. This is the version built and tested in the full circuit.
* **LEA14** protects cellular structures under environmental stress. The light-responsive Module 4 with LEA14 was not built; the constitutive version was characterised instead to see how it would behave in the whole system, and it also protects plants facing salinity stress.
* **BoPep4**, a broccoli plant elicitor peptide, activates plant defence responses.

Our constitutive constructs, which use Pveg in place of the light switch, give the maximal secretion and production of each protectant and serve as the benchmark for the light-controlled version.

## Beyond our project

Replacing the xylose-inducible and IPTG-inducible promoters of the published CcaSR system (Castillo-Hair et al., 2019) with constitutive ones means no inducer dosing is required. Other teams can reuse the four-module Level 2 plasmid for any secreted protein by exchanging the output cassette, which makes light-controlled secretion in *B. subtilis* usable beyond plant protection — for other enzymes or peptides that should be produced on demand.

## What is not yet shown

Three things are open and should be read as open.

**Light dependence of the SamyQ system is not demonstrated.** For ccaSR-Csn-AcdS-Histag, signal rose with time under green 100%, 12% and 2%, but not in an ordered way across intensities: green 2% was faint until 6 h, while green 12% at 8 h gave the strongest signal of the green lanes. For ccaSR-SamyQ-AcdS 2.1-Histag, band intensities were similar across all lanes at 13 h and 16 h, so ACC deaminase was produced steadily and at comparable levels under both wavelengths under the conditions tested; the anti-His ELISA on the same four samples put green above red each time, 12.9 against 11.8 µg/mL at 13 h and 12.5 against 12.1 µg/mL at 16 h, with two samples a side and ranges that overlap. In the overnight run, ACC deaminase was present at all three time points at similar levels. A statement that output rose under green light but not under red is supported for the Csn system and not for the SamyQ system, and should not be made for both.

**Background is unmeasured.** Dark-state and red-light output have not been measured in our strain, for the reasons under *Design*.

**Recombination risk is accepted, not excluded.** The repeated promoter, RBS and terminator sequences in the Level 2 plasmid create a risk of homologous recombination between modules. Sequence verification of the full construct is the only check applied so far.

---

# Values still bracketed

Unresolved placeholders inside the text above, kept bracketed because nothing in the record corroborates them:

| value | where it came from | why it is still open |
| --- | --- | --- |
| `[pGEM-T Easy]` | BBa_261XH2RS, Experiment — the Level 0 entry vector for *ccaS-m3* | not corroborated anywhere; BBa_26BDO8AQ names pGEM-T Easy unbracketed for *ccaR*, which is the only reason to expect it here |

Placeholders that stay on the individual parts — expected band sizes, clone numbers, the Level 1 antibiotic marker, the BsaI-HFv2 catalogue form — are listed in `per-part-cuts.md`.
