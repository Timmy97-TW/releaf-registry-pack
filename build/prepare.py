#!/usr/bin/env python3
"""steps.json -> console-data.json

Two jobs:

1. Bake the 15 confirmed defect corrections into the staged section bodies.
   Before this, every `fix` step pointed at a string that the staged section
   text still carried uncorrected, so pasting a section re-introduced the
   defect the next step then asked you to repair by hand. Baked in, one paste
   lands the corrected body and the fix becomes a note rather than an action.

2. Annotate each step for the console: a bucket (required / optional /
   decision), a minute estimate, and character spans to highlight -- amber for
   a value still in brackets, green for text the bake changed.
"""
import json, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = json.loads((ROOT / "steps.json").read_text(encoding="utf-8"))
STEPS, CARDS = D["steps"], D["cards"]

# ---------------------------------------------------------------- bake fixes

def bake(text, find, repl, old_spans):
    """Replace every occurrence. Returns the new text, the spans of what was
    inserted, and the earlier spans moved to where they now sit."""
    out, spans, cuts, at, shift = [], [], [], 0, 0
    while True:
        j = text.find(find, at)
        if j < 0:
            out.append(text[at:])
            break
        out.append(text[at:j])
        out.append(repl)
        spans.append([j + shift, j + shift + len(repl)])
        cuts.append((j, len(repl) - len(find)))
        shift += len(repl) - len(find)
        at = j + len(find)
    moved = [[a + sum(d for j, d in cuts if j < a),
              b + sum(d for j, d in cuts if j < b)] for a, b in old_spans]
    return "".join(out), spans + moved

# the four "unsupported claim" corrections sit mid-sentence as
# ", and <clause>," -- a clause, not a token, so the comma pair goes with it
def clause_rule(find, fix):
    if fix == "— delete the clause —":
        return ", and " + find + ",", ","
    return ", and " + find + ",", ", and " + fix + ","

bodies = {}          # (part, type) -> section/draft step
for s in STEPS:
    if s["kind"] in ("section", "draft"):
        bodies[(s["part"], s["type"])] = s

baked = unbaked = 0
for s in STEPS:
    if s["kind"] != "fix":
        continue
    sec = bodies.get((s["part"], s["type"]))
    note = {"find": s["find"], "fix": s["fix"], "why": s["why"], "label": s["label"]}
    if sec is None:
        s["baked"] = False
        unbaked += 1
        continue
    find, repl = s["find"], s["fix"]
    if repl == "— delete the clause —" or find == "it also helped plants under salinity stress":
        cf, cr = clause_rule(find, repl)
        if cf in sec["text"]:
            find, repl = cf, cr
    if find not in sec["text"]:
        s["baked"] = False
        unbaked += 1
        continue
    sec["text"], spans = bake(sec["text"], find, repl, sec.get("fixmarks", []))
    sec.setdefault("fixed", []).append(note)
    sec["fixmarks"] = spans
    s["baked"] = True
    baked += 1

# word counts move with the baked text
for s in STEPS:
    if s["kind"] in ("section", "draft") and s.get("fixed"):
        s["words"] = len(s["text"].split())

# ------------------------------------------------- brackets, buckets, timing

BUCKET = {"section": "req", "draft": "req", "image": "req",
          "model": "opt", "plant": "opt", "noimage": "dec", "fix": "note"}

def minutes(s):
    if s["kind"] in ("section", "draft"):
        m = 1.5 + s.get("words", 300) / 420.0 + (1.5 if s["kind"] == "draft" else 0)
    elif s["kind"] == "image":
        m = 2.5
    elif s["kind"] == "model":
        m = 2.0
    elif s["kind"] == "plant":
        m = 2.5
    else:
        m = 0.0
    return round(m, 2)

for s in STEPS:
    s["id"] = s["part"] + ":" + str(s["i"])
    s["bucket"] = BUCKET[s["kind"]]
    s["min"] = minutes(s)
    marks = []
    for a, b in s.pop("fixmarks", []):
        if b - a >= 3:           # a one-character mark is noise, not a change you can see
            marks.append([a, b, "fix"])
    for tok, _why in (s.get("blockers") or []):
        needle = "\\[" + tok + "]"
        at = 0
        txt = s.get("text", "")
        while True:
            j = txt.find(needle, at)
            if j < 0:
                break
            marks.append([j, j + len(needle), "brk"])
            at = j + len(needle)
    if marks:
        marks.sort()
        # drop any overlap so the renderer can walk them in one pass
        clean, end = [], -1
        for a, b, k in marks:
            if a >= end:
                clean.append([a, b, k]); end = b
        s["marks"] = clean

# order within a part: text first, then wet-lab figures, then the optional
# library, then the judgement calls -- the order you actually work a page in
RANK = {"section": 0, "draft": 0, "image": 1, "model": 2, "plant": 3, "noimage": 4, "fix": 5}
STEPS.sort(key=lambda s: (D["order"].index(s["part"]), RANK[s["kind"]], s["i"]))

# ------------------------------------------------------------------- numbers

def n(pred):
    return sum(1 for s in STEPS if pred(s))

req = [s for s in STEPS if s["bucket"] == "req"]
opt = [s for s in STEPS if s["bucket"] == "opt"]
counts = {
    "parts": len(D["order"]),
    "required": len(req),
    "optional": len(opt),
    "decisions": n(lambda s: s["bucket"] == "dec"),
    "sections": n(lambda s: s["kind"] == "section"),
    "drafts": n(lambda s: s["kind"] == "draft"),
    "images": n(lambda s: s["kind"] == "image"),
    "fixes_baked": baked,
    "fixes_manual": unbaked,
    "brackets": sum(len(s.get("blockers") or []) for s in STEPS),
    "req_A": n(lambda s: s["bucket"] == "req" and s["who"] == "A"),
    "req_B": n(lambda s: s["bucket"] == "req" and s["who"] == "B"),
    "min_A": round(sum(s["min"] for s in req if s["who"] == "A")),
    "min_B": round(sum(s["min"] for s in req if s["who"] == "B")),
    "min_opt": round(sum(s["min"] for s in opt)),
    "disputed": len(D["disputes"].get("disputed", [])),
    "suspect": len(D["disputes"].get("suspect_sequence", [])),
    "drafts_parts": sum(1 for c in CARDS.values() if c.get("status") == "draft"),
}
D["meta"] = {"built": datetime.date.today().isoformat(), "counts": counts}

out = ROOT / "build" / "console-data.json"
out.write_text(json.dumps(D, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("baked", baked, "fixes;", unbaked, "left manual")
print(json.dumps(counts, indent=2))
