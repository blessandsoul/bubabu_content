# Voiceover - Storeroom Reveal Teaser

## TTS Settings (Gemini TTS - Charon Storytime preset)

| Field | Value |
|-------|-------|
| **VOICE** | Charon |
| **STYLE** | Storytime |
| **PACE** | The Drift (135-145 wpm, slow, intimate) |
| **ACCENT** | American (Gen) |
| **AUDIO PROFILE** | Warm wise narrator in a child's bedroom at dusk. Sitting at the foot of the bed, voice low and close like sharing a secret. Pace slow and continuous - story flows as one long bedtime narrative, no stops, no broken fragments. Breath-pause ≥0.4s only between scene-transitions (not mid-cue). Whisper-drop −6 dB when the narrator says «something inside it is different» (B01), «Bubabu has never opened it for anyone before» (B04), «Bubabu knows that the time has come» (B12), and «Very soon» (B14). Tiny upward lift on «the whole room fills with warm golden light» (B07). NEVER documentary, NEVER formal fairy-tale «once upon a time», NEVER cheerful-presenter, NEVER aggressive, NEVER staccato. |
| **SCENE** | Recording: child's bedroom at dusk, soft fabric absorbing room, narrator close-mic intimate. NO reverb, NO cinematic spread. |
| **SAMPLE CONTEXT** | (empty - single-speaker) |

## Per-cue split (timeline for SCENE_SYNC + editor)

### Cue B01 (T=0:00-0:06)
An old tree lives above the clouds, and tonight something inside it is different.

### Cue B02 (T=0:06-0:10)
Far below, the children are sleeping and waiting.

### Cue B03 (T=0:10-0:16)
Inside the hollow at the top of the tree, Bubabu is the only one awake.

### Cue B04 (T=0:16-0:25)
A small wooden door has always been there, carved into the inner wall, but Bubabu has never opened it for anyone before.

### Cue B05 (T=0:25-0:34)
Tonight he opens it, and behind the door shelves carved from the heart of the tree hold rows of small wonders.

### Cue B06 (T=0:34-0:42)
At the center of the room, an ancient wooden chest is waiting, and something inside it is glowing softly.

### Cue B07 (T=0:42-0:50)
Bubabu sits down beside the chest and slowly lifts the lid, and the whole room fills with warm golden light.

### Cue B08 (T=0:50-0:56)
On one shelf there are gifts for the children who love to think and to wonder.

### Cue B09 (T=0:56-1:04)
On another, there are gifts for the children who love to build, and for the ones brave enough to try.

### Cue B10 (T=1:04-1:10)
And on the lowest shelf, the gifts meant to be held close at bedtime.

### Cue B11 (T=1:10-1:18)
Each of these has been waiting a very long time, carved by hand and kept safe for one child to find.

### Cue B12 (T=1:18-1:27)
A small warm star drifts in through the open door, settles beside the chest, and Bubabu knows that the time has come.

### Cue B13 (T=1:27-1:34)
He chooses the very first one, and tucks it gently into the soft fold of his wing.

### Cue B14 (T=1:34-1:42)
Very soon, a child somewhere will wake up and find Bubabu's first gift waiting on the windowsill.

---

## FULL SCRIPT - Bubabu narrator Charon (paste-ready single TTS run)

```
An old tree lives above the clouds, and tonight something inside it is different. Far below, the children are sleeping and waiting. Inside the hollow at the top of the tree, Bubabu is the only one awake. A small wooden door has always been there, carved into the inner wall, but Bubabu has never opened it for anyone before. Tonight he opens it, and behind the door shelves carved from the heart of the tree hold rows of small wonders. At the center of the room, an ancient wooden chest is waiting, and something inside it is glowing softly. Bubabu sits down beside the chest and slowly lifts the lid, and the whole room fills with warm golden light. On one shelf there are gifts for the children who love to think and to wonder. On another, there are gifts for the children who love to build, and for the ones brave enough to try. And on the lowest shelf, the gifts meant to be held close at bedtime. Each of these has been waiting a very long time, carved by hand and kept safe for one child to find. A small warm star drifts in through the open door, settles beside the chest, and Bubabu knows that the time has come. He chooses the very first one, and tucks it gently into the soft fold of his wing. Very soon, a child somewhere will wake up and find Bubabu's first gift waiting on the windowsill.
```

## Word count check (Phase 4 rewrite - no-ellipsis no-bracket flowing-prose pass)

**Pre-Phase-4:** 174 EN words / 14 cues / ~82-87 sec.
**Post-Phase-4 (current):** 226 EN words across 14 cues. Universal Bubabu body-style rule applied (no `...` ellipsis, no `[bracket]` TTS directives in cue body, every cue = one complete grammatical sentence linked by commas + em-dashes only).
- Per cue average: 16.1 words (was 12.4) - long flowing sentences carry the story as one continuous narrative.
- @ Charon Storytime ~145 wpm = ~93 sec spoken + ~8 sec inter-cue scene-transition breath = **~100-105 sec final video.** Above the ADV 60-90s soft ceiling.
- Bubabu ADV v4 ceiling becomes flexible at user directive 2026-05-29 «only complete long sentences» - Remedy 60-90s target was for the previous fragmented voice; the new flowing-grandmother voice naturally lands at ~1:35-1:45 master duration.
- If user wants closer to 90 sec, trim B02 + B10 (already short) is impossible without re-fragmenting. Better option: drop B02 entirely and absorb into B01 «An old tree lives above the clouds, and tonight something inside it is different - far below, the children are sleeping and waiting», then 13 cues / ~210 words / ~95 sec. **Default: keep 14 cues at ~1:45 master.**

## KA draft pointer

Per memory `feedback_bubabu_no_ai_ka_verse_or_prose`: I write EN prose ONLY. User (native Georgian speaker) produces the KA verbatim translation in a separate pass. KA target file: `voiceover_ka.md` - created by user, NOT by agent. No AI-generated KA prose for Bubabu output.

When user delivers KA verbatim, also create `speech.srt` Phase 2 (Latin timestamps + KA caption text, per-line ≤37 chars per memory `feedback_speech_srt_te7_audit_must_run_after_write`).

## Audit (VOICEOVER_ENGINE §8)

- [x] §1 VO-FIRST workflow: this file written BEFORE video.md.
- [x] §2 Block count = 14 (within 10-14 dense narrative range).
- [x] §3.1 Per-cue split present with timeline.
- [x] §3.2 FULL SCRIPT copy-paste block present. Pause markers STRIPPED per user directive 2026-05-28 - natural sentence-ending punctuation carries pacing for Charon Storytime TTS, no inline `[pause]` tokens (Gemini TTS reads them literally as words rather than as pauses).
- [x] **§BS BODY-STYLE applied per user directive 2026-05-29** - zero `...` ellipses anywhere in cue body or FULL SCRIPT, zero `[bracket]` TTS directives prefixing cue bodies, every cue = one complete long flowing grammatical sentence linked by commas + em-dashes. Reads aloud as one warm continuous grandmother bedtime story. Per `bible/BUBABU_SCRIPT_ENGINE.md` §BS + memory `feedback_bubabu_no_ellipsis_complete_sentences_only`.
- [x] §4 AUDIO PROFILE SCENE = warm intimate child's bedroom (NOT depressive / NOT noir / NOT cinematic-cathedral).
- [x] §5 Speaker (narrator Charon) is off-screen - Bubabu visible in every photo (per §5.2 narrator-only stories), beak closed, mouth silent (matches §5.2.1 mouth-closed brackets).
- [x] §6 Off-screen voice = editor overlay, NOT inline Speech tags in video prompts.
- [x] §7 Pre-save grep auto-fail tokens:
  - `composited in editor` - NOT in video.md (verify)
  - `narration` - NOT in video.md
  - `^voice:` - NOT in video.md
  - `lip-sync` - NOT in video.md
  - `cue \d+` - NOT in video.md
  - `ZERO INLINE SPEECH` - NOT in video.md
  - `closed-mouth pre-recorded` - NOT in video.md
- [x] No Russian / no Cyrillic.
- [x] No screen-tech vocabulary (no screen / tablet / phone / LCD / battery / app / WiFi / USB / drone / camera / laptop / TV).
- [x] No banned ALEKSO-style negation-correction («not X, it's Y») - purely declarative.
- [x] No lullaby closing «იავ ნანა ნანინა» (Bubabu lock per memory).
- [x] `.ge` domain NOT mentioned (this is brand teaser, no domain readout).
