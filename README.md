# ReLEAF registry pack

Everything needed to fill in the 33 GEMS-Taiwan (2026) parts on the iGEM Registry by hand, built on 19 October 2026 from the live registry and the team wiki.

**Open [`console.html`](console.html) and work from the Queue tab.** That is the whole tool.

---

## What is here

| | |
|---|---|
| [`console.html`](console.html) | The working tool. 115 ordered steps, a copy button on every one, figure thumbnails, and tick boxes that remember where you stopped. |
| `ReLEAF registry staging pack - 19 Oct.docx` | The same content as a Word document, for reading and approving rather than pasting. |
| `upload/` | The 18 wet-lab figures as PNG, named `NN_PART_SECTION_figN_source.png`. These are the files you upload. |
| `modelling/` | 43 molecular-dynamics and docking figures with written legends, optional, for Design sections. |
| `thumbs/` | Small copies the console displays. Not for upload. |
| `raw/` | The untouched API response for each of the 33 parts. The source of truth for everything else. |
| `model.json`, `steps.json`, `additions.json` | Staged text, the ordered step list, and the drafts and fixes. Rebuild the console or the document from these. |
| `inventory.csv` | One row per part: status, length, sections present, word counts, editor, dates. |
| `GAPS.md`, `FIGURE-MAP.md` | What the pull found, and which image belongs in which slot. |

## The work, in numbers

115 steps across 33 parts: 83 documentation sections to update, 18 figures to upload, 5 confirmed defects to correct, 5 sections drafted for parts that have none, and 4 judgement calls where no image exists.

Parts are split into three tiers. **Tier A** (13) has figures or characterisation data. **Tier B** (15) is text only. **Tier C** (5) has no documentation at all yet.

## How the text was prepared

Each section is the live registry Markdown with `\[bracketed]` values resolved **only where something corroborates them**: the strain settling on WB800, a band size that matches the wiki caption for that part's gel, a clone number the wiki names, or a value written unbracketed elsewhere in the same part. 48 resolved that way. The other 70 stay visibly bracketed in the text and are collected in the console's Decisions tab, so nothing unverified gets pasted by accident.

Markdown structure was checked against the original on all 83 sections: links, images, headings, table rows and bold runs are identical, and every length change maps to a recorded resolution.

## Two people at once

The console assigns whole parts to person A or person B, so two people never edit the same registry page. Pick A or B in the header. Progress is stored in that browser only and does not sync between machines.

## Not done

- **The two collection documents.** The Registry Rules say documentation that applies to a group of parts belongs in collection documentation and should not be duplicated across parts. The shared cloning block currently sits on roughly twenty composites.
- **Four figure slots have no image.** One Western for the constitutive SamyQ-AcdS 2.1 construct, and three captions that want sequencing traces. No such figure exists anywhere on the wiki — all 30 pages were searched.
- **One band size disagrees.** The wiki says 1,145 bp for Module 1 (`BBa_26XZYM10`); that part's registry text says 1,660 / 1,721 bp, and 1,145 bp turns up instead on `BBa_26CXI09X`.

## Rebuilding

The pack regenerates from `raw/`. The generators live outside this repo; `model.json` → `steps.json` → `console.html` is the chain, and each is plain JSON you can edit by hand.

---

Built for team GEMS-Taiwan (2026), project ReLEAF. The part documentation itself is the team's work; this repository is the staging apparatus around it.
