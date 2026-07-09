# META - Bubabu "WHERE TO BUY" outro endplate

<!-- engine-override: SOCIAL_ENGINE reason: this meta.md is production notes, not social copy - the Georgian lines are the USER-VERBATIM editor overlay text (locations) that must ship exactly as written; no social post exists in this folder -->

**What this is:** one reusable end-card scene. Render ONCE → save master → append at the end of EVERY Bubabu episode / ad before export. Locks the endplate slot from SKIN_IDENTITY (was "to be locked Phase B").

## Build once (operator steps)

1. **Image:** paste IMAGE SPEC from `video.md` into Nano Banana 2, upload `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg`. Check: beak closed, no goggle glow, `BUBABU.GE` on the podium plate rendered clean (retry if letters garbled - Latin usually renders fine).
2. **Video:** paste VIDEO SPEC into Veo 3.1 with the rendered image as first frame → 8 sec clip.
3. **TTS:** one Gemini TTS run per `voiceover.md` (Charon Storytime) → `bubabu_outro_vo_ka.mp3` (+ EN for EN masters).
4. **Editor (CapCut):** extend the last frame freeze so the card holds ~12 sec total → add text overlays (below) → lay VO → export `bubabu_outro_master_ka.mp4` (+ `_en`).

## Editor text overlay (NEVER baked - long Mkhedruli garbles in render)

Placement: clean upper third of the frame, above Bubabu. Two lines, user text VERBATIM:

```
თბილისი მოლი მე-3 სართული, კვების სივრცეში
გალერია თბილისი, მე-3 სართული, ლიფტის მიმდებარედ
```

- Font: Noto Sans Georgian, Mkhedruli lowercase (never Mtavruli), white fill + soft deep-cyan drop shadow - matches Candy Pop skin.
- Line 1 pops in at ~0.8s (with VO cue B01), line 2 at ~4.5s (cue B02). Soft scale-pop entrance, no slide.
- At ~8.5s (cue B03) the baked `BUBABU.GE` podium plate gets a gentle editor glow-pulse or 105% scale-pop - the "site" beat points at the wordmark instead of a third text line.
- EN master: same two KA lines stay (locations are physical-Georgia info), VO carries EN.

## Per-episode usage

- Append master AFTER the episode's final story scene (after the SKU handoff landing). Hard cut in, no transition.
- Episode music: let the episode's Lyria tail ring out under the card OR duck it to -22 dB; VO on top at standard mix (VO peak -3 dB above foley, per SKILL composite order). No separate outro music needed - the music-box chime SFX from the Veo render carries it.
- Concat per `bible/FFMPEG_DEFAULTS.md`: `libx264 -preset medium -crf 18 -pix_fmt yuv420p` + `aac 192k`, local merge.

## Locks respected

- No price anywhere (locations CTA allowed per `memory/reference_bubabu_retail_locations.md` - location ≠ price).
- BUBABU.GE uppercase Latin everywhere written; spoken KA = «ბუბაბუ წერტილი ჯი».
- Beak closed, static camera, rigid body, no goggle glow, refs 1.jpeg+2.jpeg, no 3.jpeg heart-eyes.
- No Cyrillic anywhere; KA on-screen text = editor overlay only.

## Calibration

Format checks pass (validator green with documented overrides - DETAIL_FLOOR photoreal fields omitted per bubabu Pixar-lock; CINEMA lives in SPEC JSON). Render + wordmark legibility + KA native check = pending operator test. KA glue verb «ბუბაბუს იპოვით» needs user confirm.
