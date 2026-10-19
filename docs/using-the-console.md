# Using the console

`console.html` is a single file. Open it in a browser straight from the folder — no server, no build. It needs `thumbs/`, `upload/`, `plant/` and `modelling/` sitting beside it, because the image paths are relative.

Across the top: the four tabs, the lane selector, how much time is left, and a ring for the lane you are in.

## Work one registry page at a time

The Queue is built around the thing that actually costs time: opening a registry part page. So it gives you **one part per screen, with every step for that part on it**. Open the part once with the blue button in the bar, work down the card, then press `→` for the next part.

A step collapses to a single ticked line as soon as you finish it, so the screen shrinks as you go and what is left is always at the top of what remains.

The strip of 33 cells above the part bar is the whole set: filled means finished, outlined is where you are. Click any cell to jump. `skip to the next unfinished` does what it says.

## The step kinds

| | |
|---|---|
| section (83) | Open that entry on the registry, select its whole body, paste over it. |
| draft (5) | The entry does not exist yet. Add it, then paste. |
| figure (18) | **Download the file** from the step, upload it inside that entry, then paste the legend under it as a bold paragraph. |
| optional (25) | Modelling figures for Design, plant figures for Application. Hidden until you ask for them at the foot of the part. |
| judgement call (4) | A caption whose figure does not exist. Nothing to paste; decide and move on. |

### The fifteen defects are already in the pastes

Fifteen things are wrong on the live pages — three wrong cross-reference links, four `share.google` shorteners, an unclosed bracket, three title typos, and four claims about salinity the plant data does not support. **Every one of them is corrected inside the staged text.** Pasting the section repairs the page; there is no separate find-and-replace step any more. Each affected step says `n fixes baked in` and lists what changed, and the inserted words are marked green in the text so you can see them.

### Brackets are marked where they are

Seventy values could not be corroborated and are still in brackets. They are marked amber in the text, exactly where they sit, and listed under the step. Decide them before you paste or leave them bracketed — but do not invent one at the keyboard. The Decisions tab holds all seventy in one list.

## Keyboard

The Queue is meant to be driven from the keyboard.

| key | |
|---|---|
| `return` | copy this step and tick it, then move to the next one |
| `j` `k` | next / previous step on this part |
| `→` `←` | next / previous part |
| `o` | open this part on the registry |
| `f` | download the figure for this step |
| `x` | tick or untick without copying |
| `u` | undo the last tick |
| `g` | go to the first part still unfinished |
| `/` or `⌘K` | jump to a part by id, title, tier or family |
| `1`–`4` | Queue, Board, Figures, Decisions |
| `?` | the list above, on screen |

They are off while the cursor is in a text field and when a modifier is held, so browser shortcuts still behave. Every key has a button beside it in the step.

`return` ticks the step as it copies. The tick is a bookmark for where you are, not a claim that the registry saved — if a paste goes wrong, press `u`.

## The other three tabs

**Board** is the status surface: both lanes, how many parts are finished, how long is left, and a row per part you can click to go there. It also holds the handoff tools — see below.

**Figures** is the contact sheet. The 18 wet-lab figures with a slot waiting, each with a download link, then the 43 modelling figures grouped by family. The thumbnails in `thumbs/` are screen copies; the file to upload is always the full one.

**Decisions** collects everything that wants settling once rather than at the keyboard: the seventy bracketed values, the two deposits that look like the pre-assembly vector, the fourteen numbers the sequences dispute, the design-history questions, the captions with no possible image, and the record of the fifteen corrections the pastes now carry.

## Two people at once

Top right: **A**, **B**, **Both**. The work is dealt out by part, so a registry page belongs to one person for the whole session — 55 steps to A across 17 parts, 51 to B across 16, about two hours each. Pick your letter before you start and leave it there. Two people on **Both** will sooner or later open the same page at the same time, and the registry keeps whichever save landed last.

Rename a lane on the Board if "A" and "B" are not the names you use.

## Time left

The header shows how many steps remain and how long they should take. It starts from the staged estimate and switches to **your own measured pace** once you have ticked a few — median gap between ticks, with breaks over fifteen minutes ignored. If the number says you will not finish, turn the optional figures off and keep to the 106 required steps.

## Progress is local

Ticks live in that browser's own storage, under the key `releaf-registry-v2`. Nothing syncs: A's ticks are invisible to B, and both are invisible on another machine. Reopening the file on the same browser puts you back on the first part you had not finished.

On the Board, under **Handoff and backup**:

- **Copy a progress code** — a string holding every tick. Paste it on the other machine to merge.
- **Paste a progress code** — merges, never erases; two lanes can be combined at the end.
- **Copy a status report** — plain text, one line per part, for the team chat.
- **Clear all ticks** — this browser only, and it asks first.

The ticks are a bookmark, not a record. What counts as done is what is saved on the registry page.
