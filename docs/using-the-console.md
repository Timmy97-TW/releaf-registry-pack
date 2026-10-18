# Using the console

`console.html` is a single file. Open it in a browser straight from the folder — no server, no build. It needs `thumbs/`, `upload/` and `modelling/` sitting beside it, because the image paths are relative.

Across the top: the four tabs, the person selector, and a ring showing how much of the current queue is ticked off.

## The four tabs

**Queue** is the one to work from. It shows a single step at a time out of 115, in the order they should be done, with the part name, its tier and family, and the staged text behind a copy button. A line under the step title says what kind of step it is:

| | |
|---|---|
| section (83) | Open the existing entry on the registry page and replace its body with this. |
| image (18) | Upload the named file from `upload/`, then paste its legend. |
| draft (5) | Create a new entry of that type and paste this in. |
| fix (5) | A confirmed defect on a live page. Find the first line, replace it with the second. |
| decision (4) | A caption whose figure does not exist. A judgement call, not a paste. |

**Parts** lists all 33 parts, tier A first, each with every section and figure that belongs to it and a link that opens that part on the registry. Use it to see one part whole, or to jump back to something already done. Parts in the BoPEP4, AcdS or LEA14 families also carry a fold of modelling figures whose legends are already written — optional, for the Design section, none of them required.

**Figures** is the contact sheet: the 18 wet-lab figures that have a slot waiting, then the 43 modelling figures grouped by family. Click any thumbnail to see it full size. The thumbnails in `thumbs/` are 420 px copies for the screen; the file to upload is always the one in `upload/`.

**Decisions** collects everything that needs settling once instead of at the keyboard, in three groups: the bracketed values nothing corroborates, the confirmed defects on live pages, and the captions with no possible image. Each has its own tick box, kept separately from the queue.

## Keyboard

On the Queue tab:

| key | |
|---|---|
| `←` `→` | previous step, next step |
| `C` | copy the step's text |
| `D` | mark done and move to the next step |
| `U` | undo the tick you just made — it steps back one first if the step on screen is not ticked |

They are off on the other three tabs, off while the cursor is in a text field, and off when a modifier key is held, so browser shortcuts still behave. Every key has a button next to it in the step, if that is easier.

## Two people at once

Top right: **Both**, **A**, **B**. The 115 steps are already dealt out — 59 to person A across 17 parts, 56 to person B across 16 — and the split is by part, so a registry page belongs to one person for the whole session. Each person picks their own letter before starting and leaves it there. Two people on **Both** will sooner or later open the same registry page at the same time, and the registry editor keeps whichever save landed last.

The ring and the "n of m done" line follow the selector, so on **A** they count only person A's work.

## Progress is local

Ticks live in that browser's own storage, under the key `releaf-registry-v2`. Three consequences worth knowing before you start:

- Nothing syncs. Person A's ticks are invisible to person B, and both are invisible on any other machine.
- Reopening the file on the same browser restores where you stopped. A different browser, a private window, or cleared site data starts at zero.
- The ticks are a bookmark, not a record. What counts as done is what is saved on the registry page.

Say out loud which parts are finished, or keep a shared list, if anyone needs to know the state of the whole set.
