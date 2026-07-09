# Meta - «Parent Rescue» (Bubabu 9-scene story-ad)

## Identity
| Field | Value |
|-------|-------|
| Slug | `20260606_sat_parent_rescue` |
| Type | **standalone hero story-ad** (sells the Bubabu owl itself, NOT a catalog SKU) |
| Paired cartoon / ad | none (not a SKU-pair) |
| Distinct from | the sibling 4-scene `20260606_sat_hero_ad_screenfree_friend` (this is the longer 9-beat story variant) |
| Ship date | 2026-06-06 (sat) draft · publish date TBD by user |
| Status | DRAFT in `agents/bubabu/draft/`. Moves to `content/` only after the user confirms it is published. |
| Deliverable | PROMPT PACKAGE - user renders in Veo 3.1 + records KA VO + generates Lyria + composites. Claude does NOT render. |

## SKU / price (operator-internal only)
| Field | Value |
|-------|-------|
| Product | Bubabu hero unit (AI owl, Axiom Smart) |
| Retail zone | Hero Bubabu |
| Age tier | family / kids 3-12 |
| Price | **operator-internal only - lives on the current BUBABU.GE listing / shop sheet. NEVER in any customer-facing file (no price number written in this package by design).** |

## Deviations logged (deliberate, scoped to this ad)
1. **9 scenes** (not the locked 3-scene REVEAL/PLAY/HOLD ad) - justified by the user's explicit 9-beat story.
2. **First-person mother voiceover, voice Sulafat** (warm female), NOT Charon Storytime brand-narrator - the testimonial POV needs the mother's own voice. Charon canon unchanged; a Charon third-person alt cut is available if the client prefers brand consistency.
3. **Humans on screen** (mother + 3 kids) - the zero-human locked ad never does this. Awake, daytime, clothed; no bed/nightwear/sleeping.
4. **HYPERREAL 8K render replaces Pixar** (user request: hyperreal 8K + replace Pixar, 2026-06-06) - `video.md` + `cover.md` are photoreal (Sony A1 / Kodak Portra / creamy bokeh). Children shown ONLY from-behind / faces hidden (photoreal child face trips the safety filter); mother's photoreal face carries the emotion; Bubabu = photoreal plush. Magic (flight + wonder-light) kept at accepted risk - **probe-render S1 + S3 first.** Breaks the Bubabu Pixar render-lock → **needs Archil sign-off before publish.** Pixar version in git history. `voiceover.md` / `audio.md` / `post.md` unchanged.

## Render queue
| Asset | Tool | Refs uploaded | Status |
|-------|------|---------------|--------|
| S1 image (chaos - humans only, NO Bubabu) | NB2 v3.2 | (generated; save as human-ref plate) | DRAFT SPEC in `video.md` S1 |
| S2 image (Bubabu on cloud-tree sees the home) | NB2 v3.2 | `1.jpeg` + `2.jpeg` | DRAFT SPEC in `video.md` S2 |
| S3 image (flies in through curtains, freeze) | NB2 v3.2 | `1.jpeg` + `2.jpeg` + human-ref plate | DRAFT SPEC in `video.md` S3 |
| S4 image (CU mom relief) | NB2 v3.2 img2img | S3 last frame + human-ref plate | DRAFT SPEC in `video.md` S4 |
| S5 image (story circle, wonder-light) | NB2 v3.2 | `1.jpeg` + `2.jpeg` + human-ref plate | DRAFT SPEC in `video.md` S5 |
| S6 image (coffee calm) | NB2 v3.2 img2img | S5 last frame + `1.jpeg` + `2.jpeg` + human-ref plate | DRAFT SPEC in `video.md` S6 |
| S7 image (kids laugh) | NB2 v3.2 img2img | S6 last frame + `1.jpeg` + `2.jpeg` + human-ref plate | DRAFT SPEC in `video.md` S7 |
| S8 image (mom on phone, recommend) | NB2 v3.2 | `1.jpeg` + `2.jpeg` + human-ref plate | DRAFT SPEC in `video.md` S8 |
| S9 image (calm play resolve) | NB2 v3.2 img2img | S8 last frame + `1.jpeg` + `2.jpeg` + human-ref plate | DRAFT SPEC in `video.md` S9 |
| S1-S9 videos | Veo 3.1 v3.2 | each scene image as source frame | DRAFT SPECs in `video.md` |
| Cover (baked Georgian headline + BUBABU.GE pill) | NB2 v3.2 baked-text | `1.jpeg` + `2.jpeg` + human-ref plate | DRAFT SPEC in `cover.md` |
| Narrator VO (Sulafat, 8 cues + S8 separate take) | Gemini TTS Studio | - | DRAFT in `voiceover.md` |
| Music (Lyria 3, ~80s) | Lyria 3 Pro | - | DRAFT in `audio.md` |
| Post copy (EN body + first comment) | manual | - | DRAFT in `post.md` |
| KA voiceover (`voiceover_geo.md`) | USER produces verbatim | EN draft | PENDING USER |
| KA post (`post_geo.md`) | USER produces verbatim | EN draft | PENDING USER |
| KA cover headline confirm | USER confirms native form | `cover.md` proposed | PENDING USER |

## Editor composite layer order (mandatory)
1. Render all 9 `video.md` scenes SILENT (Veo = foley only, `speech:null`).
2. Concatenate: HARD CUTs at S1→S2, S2→S3, S4→S5, S7→S8; img2img-continuous seams elsewhere (each chained scene seeded from the prior last frame).
3. Foley layer from each scene's `sfx_cues`.
4. Narrator track (Sulafat, 8 cues) over the whole runtime at -3 dB above foley / -22 dB below VO peak.
5. S8 diegetic Georgian phone line synced to the mother's animated mouth; the narrator ducks under it.
6. Lyria 3 music bed at -22 dB (the held-breath drop at the freeze sits almost alone).
7. BUBABU.GE end-card graphic after S9 (editor layer - not generated in any scene).
8. Master -14 LUFS. Crops: 9:16 (TT/IG Reels/YT Shorts), 1:1 (IG feed), 4:5 (FB feed).

## Channels (publish-time)
| Channel | Asset | Note |
|---------|-------|------|
| Bubabu official Facebook | 4:5 cover + `post.md` body + first comment | Sat 15:00 Tbilisi |
| Bubabu official Instagram (feed 1:1 / Reels 9:16) | cover / full montage + `post.md` | Sat 15:00 Tbilisi |
| Bubabu official TikTok | full montage + `post.md` (trim hashtags) + pinned first comment | Sat 15:30 Tbilisi |
| Bubabu official YouTube Shorts | full montage + EN title | Sat 16:00 Tbilisi |
| Axiom Smart corporate | 16:9 derivative | next day |
| Andrew Altair personal / aiNOW | **NEVER** without explicit Archil approval | Forbidden |

## Pre-render checklist
- [ ] S1 rendered first; mother + 3 children saved as the human-reference plate, uploaded on S3/S5/S6/S7/S8/S9 for cross-scene human consistency.
- [ ] Every Bubabu scene uploads `1.jpeg` + `2.jpeg` (NEVER `3.jpeg`); beak black closed, goggles matte (no glow), rigid body, white body / caramel wings+feet.
- [ ] Kids awake + daytime clothes + daytime indoor in every scene; no bed/nightwear/sleeping; chaos reads comic not distressing.
- [ ] Child mouths: S1 wail / S7 laugh = open-mouth NON-VERBAL emotional shape (not word-forming). If Veo drifts to speech, regenerate with "rounded emotional mouth, not word-forming". All vocalization = foley.
- [ ] S8 mother mouth animates as talking; her KA line is composited + synced (separate take), narrator ducks; Veo S8 silent.
- [ ] Cover: confirm KA headline native form with user before locking; if Mkhedruli mis-renders 3×, use the fallback editor-overlay.
- [ ] VO: render Sulafat FULL SCRIPT + the separate S8 take; listen-test for warm-friend tone (not commercial).
- [ ] Music: render Lyria 3, verify ≤96 BPM major + the freeze-drop hinge.

## Post-publish 24-48h monitoring
- Track BUBABU.GE clicks + DM inquiries about the owl.
- Track FB/IG/TT comments - especially first-comment "what calms your kids" replies (identity-trigger engagement).
- Track watch-rate at 3s / 50% / 75% (hold-rate across the 9-beat arc).
- ≥10 organic first-comment replies + ≥50% mid-point hold = story-ad format validated.

## Calibration
- L1 FORMAT - VERIFIED (7 files present, JSON SPECs schema markers, SMALL 2/9, set-equality ∅).
- L2 SPEC-CONFORMANCE - VERIFIED (Bubabu locks per scene, price/CTA bans, deviations logged, composite order, channel restriction).
- L3 GENERATOR-CONVERGENCE - PENDING render (child-mouth drift, human cross-scene consistency, S8 KA sync, Mkhedruli cover legibility, moderation classifier).
- L4 VIEWER-TEST - PENDING publish (hold-rate, recommendation beat landing, client accepting the mom-narrator deviation).

**Allowed claim now:** «Format + spec checks pass. Outcome pending render + viewer test.»
**Forbidden claim:** «Done / shipped / works / ready.»

## File inventory (this folder)
| File | Role | Status |
|------|------|--------|
**FINAL RENDER STYLE = HYPERREAL 8K (photoreal). All 8 files below are the final set.**

| # | File | What it is | Status |
|---|------|-----------|--------|
| 1 | `brief.md` | the plan - concept, 9-scene arc, seller logic, deviations, calibration | ✅ |
| 2 | `character.md` | the cast - Bubabu plush + mother + 3 kids, canonical blocks (HYPERREAL, kids from-behind) | ✅ |
| 3 | `video.md` | the 9 scenes - paired image+video JSON SPEC per scene (HYPERREAL 8K) | ✅ |
| 4 | `voiceover.md` | the narration - first-person mother (Sulafat), 9 cues + FULL SCRIPT + S8 diegetic line | ✅ |
| 5 | `audio.md` | the music - Lyria 3 score + wonder motif + mix | ✅ |
| 6 | `cover.md` | the thumbnail - photoreal poster, baked Georgian headline + BUBABU.GE pill (NO price) | ✅ |
| 7 | `post.md` | the caption - EN body ~700 chars + first comment | ✅ |
| 8 | `meta.md` | this file - production map + render queue + composite order | ✅ |
| - | `voiceover_geo.md` | KA verbatim of voiceover (you produce) | ⏳ YOU |
| - | `post_geo.md` | KA verbatim of post (you produce) | ⏳ YOU |
