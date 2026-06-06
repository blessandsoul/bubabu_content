# Meta — Storeroom Reveal Teaser

## Production identity

| Field | Value |
|-------|-------|
| **Slug** | `20260528_thu_teaser_storeroom_reveal` |
| **Type** | Standalone brand-launch teaser (NOT a cartoon+ad pair — no specific catalog SKU featured) |
| **ADV mode version applied** | v4 (Smart Gifts pivot integration) |
| **Series role** | EP00 / canon-establisher for the new Bubabu Smart Gifts pipeline. Locks SKIN_IDENTITY for every future paired SKU episode. |
| **Folder structure** | Single flat folder (legacy ADV pattern). NOT pair-folder — no `cartoon/` + `ad/` subfolders since there is no companion ad for a teaser. |
| **Status** | DRAFT in `agents/bubabu/draft/`. Awaits user «выложил» before move to `content/`. |
| **Paired ad** | NONE (teaser stands alone) |

## Variant declaration (SKIN_VARIANTS axis per ADV v4 SKIN_SYSTEM)

| Axis | Variant chosen | Why |
|------|----------------|-----|
| Music mood | **M1 bedtime-warm** (C major, 72 BPM) | Teaser sets brand-bell baseline — M1 = the bell's home key |
| Palette | **P1 butter-cream warm** | Locks the series-skin palette for every later episode |
| Narrator register | **N1 lullaby** (closer to whisper Charon Storytime) | Tease + promise feels best as intimate bedside-whisper |
| Cold-open | **O1 cloud-tree descent** (Scene 1 wide cloud-tree at dusk) | Origin canon anchor — establishes the world before any SKU enters |

## §H seasonal opt-in

NONE. Teaser is evergreen-launch, not tied to a calendar window. First pair episode (post-teaser) may opt into §H for June 1 Children's Day if launch lands in that window.

## SKU featured

NONE (teaser shows wrapped wonder-bundles only, no specific catalog SKU named or visually identifiable). First paired SKU episode (post-teaser) will identify the first SKU in its `meta.md`.

## Channels (publish-time)

| Channel | Format | Status |
|---------|--------|--------|
| Bubabu official Facebook | 9:16 video + facebook.md body + first comment | Primary launch |
| Bubabu official Instagram Reels | 9:16 video + IG caption (same body) | Day-1 |
| Bubabu official TikTok | 9:16 video + TT caption (same body, shorter hashtag set) | Day-1 |
| Bubabu official YouTube Shorts | 9:16 video + EN title + EN description | Day-1 |
| Axiom Smart corporate | 16:9 derivative + share post | Day-2 |
| BoG co-promo | Pending Archil sign-off | Hold |
| Andrew Altair personal / aiNOW agency | **NEVER** without explicit Archil approval (memory L0 reference_andrew_personal_vs_ainow_brand_split) | Forbidden default |

## Render queue

| Asset | Tool | Refs uploaded | Status |
|-------|------|---------------|--------|
| Scenes 1, 3, 5-7, 11-14 image prompts (Bubabu visible) | Nano Banana 2 | `1.jpeg` + `2.jpeg` mandatory | DRAFT prompt ready |
| Scenes 2, 4, 6, 8-10 image prompts (Bubabu off-frame or close-detail-shelf) | Nano Banana 2 | `1.jpeg` + `2.jpeg` for any Bubabu-visible portion | DRAFT prompt ready |
| Scene 12 + Scene 13 image prompts (Bubabu with bundle/star) | Nano Banana 2 | `1.jpeg` + `2.jpeg` | DRAFT prompt ready |
| Scene 14 image prompt (Bubabu at branch edge, paper-glider, guiding star) | Nano Banana 2 | `1.jpeg` + `2.jpeg` | DRAFT prompt ready |
| Video clips per scene | Veo 3.1 (img2vid from scene's photo) | Photo from previous step | DRAFT prompt ready |
| Voiceover audio | Gemini TTS (Charon Storytime preset) | FULL SCRIPT block from voiceover.md | DRAFT script ready |
| Music | Lyria 3 Pro (TIMESTAMP primary, DESCRIPTIVE fallback) | — | DRAFT prompt ready |
| Cover | Nano Banana 2 baked-text PRIMARY | `1.jpeg` + `2.jpeg` | DRAFT prompt ready |
| KA voiceover (`voiceover_ka.md`) | **USER produces verbatim** (per memory `feedback_bubabu_no_ai_ka_verse_or_prose`) | EN draft from voiceover.md | **PENDING USER** |
| KA SRT (`speech_ka.srt`) | Generated AFTER KA voiceover finalized (Phase 2) | KA voiceover.md from user | PENDING |

## Pre-render checklist

- [ ] User reviews voiceover.md EN draft and approves tone
- [ ] User produces voiceover_ka.md (KA verbatim)
- [ ] Charon Storytime narrator audition gate (R1) — 3-take test passes
- [ ] Nano Banana 2 renders Scene 1 first as character-reference anchor for all other scenes
- [ ] Scene 7 (chest-lid lift) and Scene 13 (Bubabu tucks bundle) — these are the most rendering-fragile beats — generate first iteration, review for goggle-glow drift before rendering remaining scenes
- [ ] Lyria 3 generates audio master — librosa verification (R2) asserts brand-bell C5-E5-G5-E5 motif at intro 0-1s AND outro 1:17-1:18 (bookend lock)
- [ ] Cover renders with baked Mkhedruli OR EN headline — pre-publish grep for Cyrillic look-alikes if KA chosen
- [ ] Editor concatenates cartoon clips, syncs Charon voiceover, ducks Lyria music to -22 dB under VO, adds foley
- [ ] Andrew reviews final master before Archil sign-off
- [ ] Archil sign-off for series-skin lock (this teaser sets SKIN_IDENTITY for the whole Smart Gifts series)
- [ ] Post-publish: monitor watch-rate at 25 sec, 50 sec, 75 sec marks. Hold rate above 60% at 50 sec = teaser working.

## Post-publish actions

1. After 48h, log view counts + watch% to `agents/bubabu/results.md` (create file).
2. Update `wiki/performance/format_rankings.md` with teaser performance vs other Bubabu content.
3. **If teaser hits ≥20K views:** lock SKIN_IDENTITY into `agents/bubabu/series_skin_smart_gifts.md`, proceed to first paired SKU (recommend `magnetic_balls_rainbow` per design doc).
4. **If teaser hits <5K views:** reflection-engine pass — likely missed audience signal, revise hook/cover before first pair ships.
5. Move `agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/` → `agents/bubabu/content/` on user «выложил».

## Calibration

- L1 FORMAT — VERIFIED at write time (all 8 files present, grep gates pass per SKILL.md spec).
- L2 SPEC-CONFORMANCE — VERIFIED (voiceover.md FULL SCRIPT block + Lyria 3 format + Bubabu cover override + SOCIAL_ENGINE v2.1 EN body + SLOP_FILTER re-audit + CHARACTER_BLOCK verbatim across files).
- L3 GENERATOR-CONVERGENCE — PENDING render. The hardest convergence test is Scene 7 chest-lid-lift (gold light pouring up onto Bubabu without triggering body-glow / goggle-glow). If first 3 renders all show body-glow drift, regenerate with stronger NEGATIVE bans or split into Scene 7a (closed lid) + Scene 7b (open lid) two-pass composite.
- L4 VIEWER-TEST — PENDING audience response after publish. Success metric: ≥60% watch-rate at 50 sec + organic comments mentioning «storeroom» / «chest» / «soon» / «what gift» = canon planted.

**Allowed claim now:** «Format + spec checks pass. Outcome pending render + viewer test.»
**Forbidden claim:** «Done / shipped / works / ready» — outcome unverified.

## Phase 3 audit log — 2026-05-28

User caught 4 issues in first-draft review:

### Issue 1 — `[pause]` / `[pause longer]` markers inside FULL SCRIPT block
**Problem:** Gemini TTS reads `[pause]` literally as a word, not as silence.
**Fix:** Stripped all `[pause]` and `[pause longer]` from voiceover.md + voiceover_geo.md. Natural punctuation + ellipses carry pacing now.
**Status:** FIXED.

### Issue 2 — Scene-count + VO-sync verification
**Result:** PASS — 14 cues / 14 scenes / 14 `> VOICEOVER:` lines, all verbatim matched (re-checked post-rewrite via Bash grep).

### Issue 3 — PHOTO_VIDEO_FIDELITY noun drift (4 violations + 2 borderline)
**Problem:** video prompts introduced nouns not present in matching photo prompts — generator would have «додумывал» (drifted into hallucination).
**Fixes applied** to `video.md`:
- Scene 02 photo: added «soft clouds drift slowly across the frame edges».
- Scene 05 photo: added «dust motes drifting slowly in the warm amber light inside the storeroom».
- Scene 06 photo: added «dust motes catching the chest's amber seam-light, drifting slowly in the warm air».
- Scene 07 photo: added «dust motes visible in the gold light pouring up from the chest».
- Scene 10 photo: added «dust motes drifting slowly in the soft gold backlight».
- Scene 14 photo: added «a gentle pre-dawn air movement very slightly stirs the leaves on the branch and the ribbons on the paper-glider boat».
**Status:** FIXED. Re-audit pending grep verification (see «Verification grep gates» below).

### Issue 4 — Voiceover text felt telegraphic
**Problem:** Too many short fragments («Below the clouds... children are waiting.» / «Tonight he opens it. Shelves carved from the tree itself. Rows of small wonders.») broke the warm-bedtime-grandmother flow Bubabu's voice needs.
**Fix:** Rewrote all 14 EN cues + FULL SCRIPT block + word count line. Added connective tissue, removed B11's soft negation-correction («These are not ordinary toys» = §1 SLOP form), preserved 14-beat structure + meaning.
**Word count:** 132 → 174 EN words. Final video estimate: ~82-87 sec (was ~75-78), still inside ADV 60-90 sec window. Optional B04/B11 trim available if user wants tighter.
**video.md** sync: all 14 `> VOICEOVER:` lines + VOICEOVER-TO-CLIP MAP beat-text column + timing column updated to match new cues.
**Status:** FIXED.

### KA translation (voiceover_geo.md)
**Status:** STALE — current voiceover_geo.md was generated from the pre-rewrite EN cues. User produces fresh KA verbatim translation from the new EN cues per memory `feedback_bubabu_no_ai_ka_verse_or_prose` (agent never auto-translates Bubabu KA prose). Old KA cues to discard, new ones to write.

### Verification grep gates (post-rewrite)

Run these to confirm fixes landed:
- `grep "dust motes" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/video.md` — should hit photo prompts AND video prompts in Scenes 5, 6, 7, 10, 11 (was: only Scene 11 photo + 4 video prompts). Now expect: 5 photo + 4 video = 9 hits min.
- `grep "These are not ordinary" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/voiceover.md` — should be EMPTY (B11 rewritten).
- `grep "\[pause" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/voiceover.md` — should be EMPTY.
- `grep "carved by hand" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/voiceover.md` — should HIT (new B11 phrase).
- `grep -c "^### Cue B" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/voiceover.md` — should = 14.
- `grep -c "^> VOICEOVER:" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/video.md` — should = 14.
- `grep "soft clouds drift" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/video.md` — should HIT Scene 2 photo.
- `grep "pre-dawn air movement" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/video.md` — should HIT Scene 14 photo.

## Phase 4 audit log — 2026-05-29

User listened to KA voiceover (Storeroom Reveal teaser KA cues) and rejected the body-style: «отныне давай без троеточий и всякого говна тольк о предложения цельные длинные! рассказ! запомни все контенты так нужно без ТТС енджайна».

### Issue 5 — Ellipsis (`...`) used as breath-pause throughout cue bodies
**Problem:** B02 / B05 / B07 / B12 / B14 contained `...` breath-pauses that read as broken / staccato / amateur when voiced. Bubabu brand voice is warm grandmother bedtime story — must FLOW.
**Fix:** Universal Bubabu rule promoted to `bible/BUBABU_SCRIPT_ENGINE.md` §BS (v1.4 2026-05-29) + memory `feedback_bubabu_no_ellipsis_complete_sentences_only` [L0]. ALL Bubabu content (voiceover / video VOICEOVER lines / facebook / cover headline / KA translation) bans `...` anywhere from now on.

### Issue 6 — Inline TTS bracket directives in cue bodies
**Problem:** Every cue prefixed with `[low, warm, settled in]` / `[hushed reveal]` / `[tender, slow]` etc. User: «без ТТС енджайна» — pure storytelling text only, no stage directions.
**Fix:** Same §BS law. All `[bracket]` directives stripped from cue bodies. Tone direction now lives ONLY in AUDIO PROFILE field of TTS Settings table at top of voiceover.md (Charon Storytime preset handles macro tone; per-cue specific moments referenced by quoted phrase in AUDIO PROFILE notes, never as inline bracket).

### Issue 7 — Sentence fragments + telegraphic phrasing
**Problem:** «Below the clouds. Children waiting.» / «Tonight he opens it. Shelves carved. Rows of wonders.» — broken bullet-rhythm not bedtime-story flow.
**Fix:** All 14 cues rewritten as complete long flowing sentences linked by commas + em-dashes only. Average cue length 16.1 words (was 12.4 in Phase 3, was 9.4 in initial draft). Sentences read as one continuous warm grandmother bedtime story.

### Fixes applied to teaser

- `voiceover.md` AUDIO PROFILE: rewrote tone directions to reference per-cue moments by quoted phrase (not bracket prefix). Added «slow and continuous — no broken fragments» pacing note.
- `voiceover.md` 14 cues: stripped all `...` ellipses + all `[bracket]` directives + rewrote as complete long flowing sentences. Cue B14 «Soon... very soon... a child somewhere will wake up... and find...» → «Very soon, a child somewhere will wake up and find Bubabu's first gift waiting on the windowsill.» (3 ellipses removed, one complete sentence).
- `voiceover.md` FULL SCRIPT block: collapsed into one continuous flowing paragraph (was 14 fragmented lines with blank-line breaks). Reads as one TTS run with natural sentence-rhythm.
- `voiceover.md` word count: 174 → 226 EN words. Duration estimate ~1:35-1:45 master (was ~1:25). Above ADV 60-90s soft ceiling — accepted per user directive «цельные длинные» (the flowing-prose rule fundamentally adds words; user prefers story over tight duration).
- `voiceover.md` audit checklist: added §BS BODY-STYLE entry, marked complete.
- `video.md` all 14 `> VOICEOVER:` lines: synced verbatim to new cues (zero `...`, zero brackets).
- `video.md` VOICEOVER-TO-CLIP MAP: beat-text column + timing column updated to new cues + new durations.

### KA translation (`voiceover_geo.md`)
**Status:** STALE — KA cues were translated from Phase 3 EN body (which had `...` and `[brackets]`). User produces FRESH KA verbatim translation from the new Phase 4 EN cues per memory `feedback_bubabu_no_ai_ka_verse_or_prose`. KA translation MUST also honor §BS — zero `...` and zero `[brackets]` in KA cue bodies. Lang agent next pass needs the §BS rule fed in.

### Verification grep gates (Phase 4)

- `grep "\.\.\." agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/voiceover.md` — should be EMPTY (was 14 hits across cues).
- `grep -E "^\[.*\]" agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/voiceover.md` (cue body lines) — should be EMPTY (was 14 bracket-prefixed cues).
- `grep "\.\.\." agents/bubabu/draft/20260528_thu_teaser_storeroom_reveal/video.md` — should be EMPTY in VOICEOVER lines (atmospheric mentions in prompt body OK).
- `grep -c "^### Cue B" voiceover.md` — should still = 14.
- `grep -c "^> VOICEOVER:" video.md` — should still = 14.
- `grep "Bubabu knows that the time has come" voiceover.md` — should HIT (new B12 phrase).
- `grep "Very soon, a child somewhere" voiceover.md` — should HIT (new B14 phrase, no ellipses).

## Pre-pivot reference

Pre-pivot Bubabu content + early ADV EP01 production work archived at `_archive/bubabu/20260528_pre_smart_gifts_pivot/` per pivot decision 2026-05-28. Do NOT consult those files for format reference — they used a different production model (single-product cartoons without paired ads, no storeroom canon, R5 churchkhela exception). This teaser establishes the NEW canon.

## File inventory (8 files in this folder)

| File | Role | Status |
|------|------|--------|
| `brief.md` | Concept + arc + goal + format spec | ✅ written |
| `character.md` | Bubabu IDENTITY_BLOCK verbatim + mood-state declarations | ✅ written |
| `voiceover.md` | Gemini TTS Charon Storytime, 14 cues + FULL SCRIPT block | ✅ written |
| `video.md` | 14 scenes paired PHOTO+VIDEO prompts + VOICEOVER-TO-CLIP MAP + audit | ✅ written |
| `audio.md` | Lyria 3 Pro 8-section spec + brand-bell lock + librosa verification spec | ✅ written |
| `cover.md` | Baked-text Pixar candy-pop hero + 4 A/B/C/D variants + series-skin lock | ✅ written |
| `facebook.md` | SOCIAL_ENGINE v2.1 EN body 745 chars + first-comment debate-bait + SLOP_FILTER re-audit | ✅ written |
| `meta.md` | this file | ✅ written |
