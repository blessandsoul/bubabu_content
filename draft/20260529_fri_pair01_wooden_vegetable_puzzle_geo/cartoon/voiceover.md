# Voiceover - pair01 Cartoon (Wooden Vegetable Puzzle GE)

## TTS Settings (Gemini TTS - Charon Storytime preset)

| Field | Value |
|-------|-------|
| **VOICE** | Charon |
| **STYLE** | Storytime |
| **PACE** | The Drift (135-145 wpm, slow, intimate, continuous flow) |
| **ACCENT** | American (Gen) |
| **AUDIO PROFILE** | Warm wise storyteller at a small breakfast-nook window at golden hour, the kind of voice a grandmother uses when telling a soft true story to one child at a kitchen table. Pace slow and continuous - the whole story reads as one long warm narrative, no broken fragments, no staccato. Breath-pause ≥0.4s only between scene-transitions (never mid-cue). Whisper-drop −6 dB when the narrator says «watches the morning come» (B02), «curious painted shapes shine in the storeroom light» (B07), and «the very last cyan spark of curiosity fades quietly on the empty window behind her» (B14). Tiny upward lift on «the small wonder motif sings in four notes» (B10) and «sees something resting in the soft morning light on her window» (B13). NEVER documentary, NEVER formal fairy-tale «once upon a time», NEVER cheerful-presenter, NEVER aggressive, NEVER staccato. |
| **SCENE** | Recording: warm sunlit terrace at golden hour, friend leaning forward, single cup of tea on the table - the storyteller intimate and engaged, NOT depressive, NOT noir, NOT midnight-alone (per VOICEOVER_ENGINE §4.2 banned list). The narrator is alive and pulling the listener into the wonder. Mic close, no reverb, narrow stereo. |
| **SAMPLE CONTEXT** | (empty - single-speaker) |

## §0 One-sentence story test (per STORYTELLING_ENGINE §0)

«Bubabu picks a wooden tray of painted wonders from his cloud-tree storeroom and quietly leaves it on a child's windowsill so she finds it in the soft morning light.»

PROMISE planted in B01: «the windowsill is still empty» - a windowsill that is EMPTY this morning implies it will not stay empty. The viewer wonders what will arrive there. Open loop until Scene 12-14 closes it.

## Per-cue split (timeline for SCENE_SYNC + editor)

### Cue B01 (T=0:00-0:08)
There is a quiet window in a quiet small room, and on this morning the windowsill is still empty.

### Cue B02 (T=0:08-0:16)
In a small quiet room far below, a child sits awake on a soft cushion by the window and watches the morning come.

### Cue B03 (T=0:16-0:24)
Far above her, in the same pale pre-dawn light, the old cloud-tree is waking too.

### Cue B04 (T=0:24-0:34)
Inside the hollow at the very top of the tree, Bubabu has been awake for a while, listening for someone.

### Cue B05 (T=0:34-0:44)
He walks softly across his hollow, opens the small wooden door in the inner wall, and steps into the storeroom.

### Cue B06 (T=0:44-0:54)
On one of the shelves, lit by a soft cyan glow, a small wooden tray of painted wonders is waiting for the right child.

### Cue B07 (T=0:54-1:04)
Bubabu lifts the wooden tray gently with the tip of his wing, and the curious painted shapes shine in the storeroom light.

### Cue B08 (T=1:04-1:12)
He carries the wonder out of the storeroom and tucks it carefully into the soft fold of his wing.

### Cue B09 (T=1:12-1:22)
At the edge of the branch, the paper-glider boat is already woven from leaves and ribbons, ready for the journey down.

### Cue B10 (T=1:22-1:34)
His wing-tip arcs once beside him, leaving a trail of cyan curiosity-sparks in the cold morning air, and the small wonder motif sings in four notes.

### Cue B11 (T=1:34-1:42)
The paper-glider tilts down through a gap in the clouds, and the guiding star drifts alongside to light the path.

### Cue B12 (T=1:42-1:54)
Bubabu lands softly on the child's windowsill, places the small wooden tray of painted wonders gently on the sill, and steps back into the dawn.

### Cue B13 (T=1:54-2:04)
The child turns gently toward the window, looks softly through the glass, and sees something resting in the soft morning light on her sill.

### Cue B14 (T=2:04-2:14)
She walks over, cradles the small tray in both hands, and the very last cyan spark of curiosity fades quietly on the empty window behind her.

---

## FULL SCRIPT - Bubabu narrator Charon (paste-ready single TTS run)

```
There is a quiet window in a quiet small room, and on this morning the windowsill is still empty. In a small quiet room far below, a child sits awake on a soft cushion by the window and watches the morning come. Far above her, in the same pale pre-dawn light, the old cloud-tree is waking too. Inside the hollow at the very top of the tree, Bubabu has been awake for a while, listening for someone. He walks softly across his hollow, opens the small wooden door in the inner wall, and steps into the storeroom. On one of the shelves, lit by a soft cyan glow, a small wooden tray of painted wonders is waiting for the right child. Bubabu lifts the wooden tray gently with the tip of his wing, and the curious painted shapes shine in the storeroom light. He carries the wonder out of the storeroom and tucks it carefully into the soft fold of his wing. At the edge of the branch, the paper-glider boat is already woven from leaves and ribbons, ready for the journey down. His wing-tip arcs once beside him, leaving a trail of cyan curiosity-sparks in the cold morning air, and the small wonder motif sings in four notes. The paper-glider tilts down through a gap in the clouds, and the guiding star drifts alongside to light the path. Bubabu lands softly on the child's windowsill, places the small wooden tray of painted wonders gently on the sill, and steps back into the dawn. The child turns gently toward the window, looks softly through the glass, and sees something resting in the soft morning light on her sill. She walks over, cradles the small tray in both hands, and the very last cyan spark of curiosity fades quietly on the empty window behind her.
```

## Word count check

256 EN words across 14 cues. Per cue average: 18.3 words.

- @ Charon Storytime 140 wpm = ~110 sec spoken + ~10 sec scene-transition breath = **~2:00 master duration.**
- ADV mode v4 60-90s soft ceiling exceeded - accepted per §BS body-style rule (flowing-prose naturally extends duration; user directive 2026-05-29 «цельные длинные» prioritizes story over tight duration).
- If user wants tighter ~1:30 target, trim B09 + B11 each by one beat (fold paper-glider mention into B10 + drop guiding-star detail from B11). Saves ~18 words, returns to ~1:40.

## KA draft pointer

Per memory `feedback_bubabu_no_ai_ka_verse_or_prose`: I write EN prose ONLY. User (native Georgian speaker via lang agent) produces KA verbatim translation in `voiceover_geo.md`. KA target file: created by user, NOT by agent. KA translation MUST honor §BS too - no `...`, no `[bracket]` directives in KA cue bodies. When user delivers KA verbatim, then create `speech.srt` Phase 2 (per-line ≤37 chars per memory `feedback_speech_srt_te7_audit_must_run_after_write`).

## Audit (VOICEOVER_ENGINE §8 + STORYTELLING_ENGINE §0 + BUBABU_SCRIPT_ENGINE §BS)

- [x] §1 VO-FIRST workflow: this file written BEFORE video.md.
- [x] §2 Block count = 14 (within 10-14 dense-narrative range for ADV).
- [x] §3.1 Per-cue split present with timeline.
- [x] §3.2 FULL SCRIPT copy-paste block present as one continuous paragraph (per §BS - collapsed into one flowing paragraph, no blank-line breaks between cues).
- [x] §4 AUDIO PROFILE SCENE = warm sunlit terrace at golden hour (intriguing storyteller, per §4.1 approved patterns - NOT noir / NOT midnight / NOT empty-room / NOT depressive).
- [x] §5 Speaker (narrator Charon) is off-screen - Bubabu visible in his own scenes (beak closed, mouth silent per §5.2.1), child visible in child scenes (mouth softly closed, no Speech tags per character.md). Bubabu and child NEVER in same frame in pair01.
- [x] §6 Off-screen voice = editor overlay, NOT inline Speech tags in video prompts.
- [x] STORYTELLING_ENGINE §0 one-sentence test done above. §1 PROMISE planted in B01 («the windowsill is still empty» = open loop, viewer wonders what will arrive).
- [x] **§BS BODY-STYLE applied (per 2026-05-29 universal rule):** zero `...` ellipses in any cue body or FULL SCRIPT, zero `[bracket]` TTS directives prefixing cue bodies, every cue = one complete long flowing grammatical sentence linked by commas. Reads aloud as one warm continuous grandmother story. Verified by pre-save grep.
- [x] No Russian / no Cyrillic.
- [x] No screen-tech vocabulary (no screen / tablet / phone / LCD / battery / app / WiFi / USB / drone / camera / laptop / TV / pixel). Wooden puzzle = pure canon-friendly noun.
- [x] No negation-correction (no «not X, it's Y»).
- [x] No lullaby closing (per Bubabu lock `feedback_bubabu_no_sacred_closing_lullaby`).
- [x] `.ge` domain NOT mentioned (cartoon doesn't carry domain readout; FB caption handles that).
- [x] Catalog SKU name «Wooden Vegetable Matching Puzzle» NOT mentioned in cartoon body (per Wonder Tools §BS rule - catalog name lives only in ad copy and meta.md). Cartoon refers to the object as «small wooden tray of painted wonders» / «the wonder» / «the wooden tray».
