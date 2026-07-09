# Meta - pair01 Cartoon (Wooden Vegetable Puzzle GE)

## Production identity

| Field | Value |
|-------|-------|
| **Slug** | `20260529_fri_pair01_wooden_vegetable_puzzle_geo` |
| **Pair number** | **01** (first post-pivot Smart Gifts pair - locks SKIN_IDENTITY for the whole series) |
| **Cartoon date** | 2026-05-29 fri (even-day) |
| **Paired ad date** | 2026-05-30 sat (odd-day, in `../ad/` subfolder) |
| **ADV mode version** | v4 (Smart Gifts pivot integration) |
| **Series role** | EP01 - locks SKIN_IDENTITY for every later paired SKU episode |
| **Folder structure** | Pair-folder: `agents/bubabu/draft/20260529_fri_pair01_wooden_vegetable_puzzle_geo/{cartoon/, ad/}` |
| **Status** | DRAFT in `agents/bubabu/draft/`. Awaits user «выложил» before move to `content/`. |
| **Paired ad** | `../ad/` (same parent folder, sibling subfolder) |

## SKU featured

| Field | Value |
|-------|-------|
| Catalog ID | `4860129139038` |
| EN name | Wooden Vegetable Matching Puzzle (Georgian) |
| GE label on product | ფაზლი |
| Price | 24 ₾ |
| In stock | 8 |
| Flag | none (clean - ad can publish to FB/IG/TT immediately after render) |
| Retail zone | Educational Smart Gifts |
| Age tier | 3-6 (core early-learning) |
| Spark | Curiosity (cyan `#5BC0DE`) |
| Mood-state | Curious (head tilt 8-12°, eyes wide on SKU, wing-tip extending) |
| Reference photo | `./sku_ref.jpg (in this pair-folder root)` |

## SKIN_VARIANTS declaration (per ADV mode v4 SKIN_SYSTEM)

| Axis | Variant chosen | Why |
|------|----------------|-----|
| Music mood | **M2 adventure-bright** (D/G major, 100-130 BPM - pair01 uses 108 BPM D major) | Curiosity-discovery beat lifts brighter than teaser bedtime. Rotation honored (teaser had M1). |
| Palette | **P2 sunlit-meadow green-amber** | Matches puzzle's painted vegetables + Bubabu cyan goggle accent. Rotation honored (teaser had P1). |
| Narrator register | **N2 storyteller (default warmth)** | Slightly more energy than teaser's N1 lullaby - Curious arc earns brighter narration. |
| Cold-open | **O2 in-room arrival** (Scene 1 = empty windowsill in child's bedroom) | Rotation honored (teaser had O1 cloud-tree descent). |

## §H seasonal opt-in

NONE. pair01 is evergreen-launch, not tied to a calendar window. June 1 Children's Day overlay could be opted in for pair02-04 if launch lands in that window.

## Channels (publish-time)

| Channel | Format | Status |
|---------|--------|--------|
| Bubabu official Facebook | 9:16 video + facebook.md body + first comment | Primary launch (Sun 20:30 Tbilisi) |
| Bubabu official Instagram Reels | 9:16 video + IG caption (same FB body) | Day-1 (Sun 20:30) |
| Bubabu official TikTok | 9:16 video + same facebook.md body (operator trims to 5-6 tightest hashtags at paste time) + first comment | Sun 20:00 Tbilisi (slightly before FB) |
| Bubabu official YouTube Shorts | 9:16 video + KA title «ფაზლი - ბუბაბუ ჭკვიანი საჩუქრები pair01» (user produces KA verbatim per memory rule) + EN description | Day-1 (Sun 20:30) |
| Axiom Smart corporate | 16:9 derivative + share post | Day-2 (Mon) |
| BoG co-promo | Pending Arčil sign-off | Hold |
| Andrew Altair personal / aiNOW agency | **NEVER** without explicit Arčil approval (memory L0 `reference_andrew_personal_vs_ainow_brand_split`) | Forbidden default |

## Render queue

| Asset | Tool | Refs uploaded | Status |
|-------|------|---------------|--------|
| Scene 01 image (no Bubabu, no SKU) | Nano Banana 2 | none | DRAFT SPEC ready |
| Scene 02 image (child only, FIRST child render = anchor for 13+14) | Nano Banana 2 | none (first child render) | DRAFT SPEC ready |
| Scene 03 image (cloud-tree only, no Bubabu) | Nano Banana 2 | none | DRAFT SPEC ready |
| Scene 04 image (Bubabu in hollow, FIRST Bubabu render = anchor for all later Bubabu scenes) | Nano Banana 2 | `1.jpeg` + `2.jpeg` mandatory | DRAFT SPEC ready |
| Scene 05 image (Bubabu + open door + storeroom) | Nano Banana 2 | `1.jpeg` + `2.jpeg` + Scene 04 reference | DRAFT SPEC ready |
| Scene 06 image (Bubabu + Curiosity shelf + puzzle - FIRST Bubabu+SKU render = anchor for 07-12) | Nano Banana 2 | `1.jpeg` + `2.jpeg` + `sku_ref.jpg` + Scene 04 reference | DRAFT SPEC ready |
| Scene 07 image (Bubabu lifts puzzle - KEY FRAME for ad reuse) | Nano Banana 2 | `1.jpeg` + `2.jpeg` + `sku_ref.jpg` + Scene 06 reference | DRAFT SPEC ready - **most-critical render of the pair** |
| Scene 08 image (Bubabu carries puzzle out) | Nano Banana 2 | same + Scene 06 reference | DRAFT SPEC ready |
| Scene 09 image (Bubabu at branch edge with puzzle, paper-glider) | Nano Banana 2 | same + Scene 04 reference for Bubabu pose | DRAFT SPEC ready |
| Scene 10 image (R4 wing-arc spark mechanic) | Nano Banana 2 | same | DRAFT SPEC ready - **goggle-glow risk: verify NEGATIVE bans work** |
| Scene 11 image (paper-glider descent through clouds) | Nano Banana 2 | same | DRAFT SPEC ready |
| Scene 12 image (Bubabu places puzzle on sill - alternate ad key frame) | Nano Banana 2 | same + Scene 01 windowsill reference | DRAFT SPEC ready |
| Scene 13 image (child wakes, sees puzzle on sill) | Nano Banana 2 | Scene 02 child reference + `sku_ref.jpg` | DRAFT SPEC ready |
| Scene 14 image (child cradles puzzle, cyan spark fades) | Nano Banana 2 | Scene 02 child reference + `sku_ref.jpg` | DRAFT SPEC ready |
| Video clips per scene | Veo 3.1 (img2vid from each scene's image) | Photo from previous step | DRAFT SPEC ready |
| Voiceover audio | Gemini TTS (Charon Storytime preset) | FULL SCRIPT block from voiceover.md | DRAFT script ready |
| Music | Lyria 3 Pro (TIMESTAMP primary, DESCRIPTIVE fallback) | - | DRAFT prompt ready |
| Cover | Nano Banana 2 baked-text PRIMARY | `1.jpeg` + `2.jpeg` + `sku_ref.jpg` | DRAFT SPEC ready |
| KA voiceover (`voiceover_ka.md`) | **USER produces verbatim** (per memory `feedback_bubabu_no_ai_ka_verse_or_prose`) | EN draft from voiceover.md | **PENDING USER** |
| KA SRT (`speech_ka.srt`) | Generated AFTER KA voiceover finalized (Phase 2) | KA voiceover.md from user | PENDING |

## Pre-render checklist

- [ ] User reviews voiceover.md EN draft and approves tone (especially after §BS rewrite - confirm flow reads as one warm grandmother bedtime story)
- [ ] User produces voiceover_geo.md KA verbatim translation per memory rule (KA also honors §BS - no `...` no `[bracket]`)
- [ ] Charon Storytime narrator audition gate (R1) - 3-take test passes
- [ ] Nano Banana 2 renders Scene 04 first as Bubabu-character-anchor for all other Bubabu scenes
- [ ] Nano Banana 2 renders Scene 02 first as child-character-anchor for Scenes 13 + 14
- [ ] Nano Banana 2 renders Scene 06 SECOND as Bubabu+SKU pairing anchor for Scenes 07-12
- [ ] Scene 07 (Bubabu lifts puzzle - ad key frame) - generate first iteration, review for: goggle-glow drift, second-puzzle hallucination, character drift vs Scene 04 anchor, asymmetric-wing-lock honored (right wing engaged with puzzle, left wing frozen)
- [ ] Scene 10 (R4 wing-arc spark) - most rendering-fragile beat - generate first iteration and verify NEGATIVE bans worked: NO glow on body, NO goggle illumination, NO cyan reflection on fur, particles stay BESIDE Bubabu not ON him
- [ ] Lyria 3 generates audio master - librosa verification (R2) asserts brand-bell D5-F#5-A5-F#5 motif at intro 0-3s AND outro 2:09-2:14 (bookend lock - identical timbre to teaser brand bell, only motif transposed)
- [ ] Cover renders with baked Mkhedruli OR EN headline - pre-publish grep for Cyrillic look-alikes if KA chosen
- [ ] Editor concatenates cartoon clips, syncs Charon voiceover, ducks Lyria music to -22 dB under VO, adds foley per video.md sfx_cues
- [ ] Andrew reviews final master before Arčil sign-off
- [ ] Arčil sign-off for SKIN_IDENTITY lock (this pair sets the canon for the whole Smart Gifts series)
- [ ] Post-publish: monitor watch-rate at 60 sec, 90 sec, 120 sec marks. Hold rate above 50% at 90 sec = pair format working.

## Post-publish actions

1. After 48h, log view counts + watch% to `agents/bubabu/results.md` (create file if missing).
2. Update `wiki/performance/format_rankings.md` with pair01 cartoon performance vs Storeroom Reveal teaser baseline.
3. **If pair01 cartoon hits ≥10K views:** lock SKIN_IDENTITY into `agents/bubabu/series_skin_smart_gifts.md`, lock brand-bell motif-transposition table into `agents/bubabu/series_brand_bell.md`, proceed to pair02 (recommend next SKU: `wooden_world_flags_puzzle` for Educational rotation OR `magic_painting_board_pink` to test Wonder Tools reframing).
4. **If pair01 cartoon hits <3K views:** reflection-engine pass - likely missed audience signal, revise hook/cover/voiceover before pair02 ships. Common failure modes to check: Bubabu mascot mode not landing emotionally / handoff-while-child-sleeps reads as too quiet / 2-minute duration too long for TikTok algorithm.
5. After paired ad (Saturday) publishes - monitor 24h conversion signal (DMs, comments on puzzle availability, bubabu.ge clicks).
6. Move `agents/bubabu/draft/20260529_fri_pair01_wooden_vegetable_puzzle_geo/` → `agents/bubabu/content/` on user «выложил pair01».

## Calibration

- L1 FORMAT - VERIFIED at write time (all 8 cartoon files present, grep gates pass, JSON SPEC schema_version markers present per Bubabu STRICT floor).
- L2 SPEC-CONFORMANCE - VERIFIED (voiceover.md §BS body-style + Lyria 3 format + Bubabu cover override baked-text + SOCIAL_ENGINE v2.1 EN body + SLOP_FILTER clean + CHARACTER_BLOCK verbatim across files + PHOTO_VIDEO_FIDELITY §1 set-equality clean per scene).
- L3 GENERATOR-CONVERGENCE - PENDING render. Highest-risk beats: Scene 07 (Bubabu lifts puzzle, ad key frame - goggle-glow + asymmetric-wing-lock most-tested), Scene 10 (wing-arc spark - anti-glow bans most-tested), Scene 13/14 (child anchor consistency vs Scene 02 anchor - face-lock between two scenes is the only intra-episode lock).
- L4 VIEWER-TEST - PENDING audience response after publish. Success metric: ≥50% watch-rate at 90 sec + organic comments mentioning «storeroom» / «painted vegetables» / «curious» / «my child would love this» = SKIN_IDENTITY lands.

**Allowed claim now:** «Format + spec checks pass. Outcome pending render + viewer test.»
**Forbidden claim:** «Done / shipped / works / ready» - outcome unverified.

## Pre-pivot reference

Pre-pivot Bubabu content + early ADV EP01 production work archived at `_archive/bubabu/20260528_pre_smart_gifts_pivot/` per pivot decision 2026-05-28. Do NOT consult those files for format reference - they used a different production model (single-product cartoons without paired ads, no storeroom canon, R5 churchkhela exception, fragmented voice with `[bracket]` directives, ellipsis breath-pauses). pair01 establishes the NEW canon.

## File inventory (this folder)

| File | Role | Status |
|------|------|--------|
| `brief.md` | Concept + SKU + spark + child + arc summary + variant declaration | ✅ written |
| `character.md` | Bubabu IDENTITY_BLOCK verbatim + per-ep child STATIC+DYNAMIC + 2-character rule + reference image attachment plan | ✅ written |
| `voiceover.md` | Gemini TTS Charon Storytime, 14 EN cues + FULL SCRIPT block + §BS body-style applied + word count + KA pointer + audit | ✅ written |
| `video.md` | 14 scenes paired NB2 image SPEC + Veo video SPEC + VOICEOVER-TO-CLIP MAP + PHOTO_VIDEO_FIDELITY §1 set-equality audit | ✅ written |
| `audio.md` | Lyria 3 Pro 8-section spec + brand-bell D-major transposition D5-F#5-A5-F#5 + librosa verification spec | ✅ written |
| `cover.md` | Bubabu candy-pop baked-text + Curious mood + SKIN_LOCK + 4 A/B/C/D variants | ✅ written |
| `facebook.md` | SOCIAL_ENGINE v2.1 EN body 810 chars + thematic-fit emoji + SLOP_FILTER clean + first-comment debate-bait - reused across FB + IG + TT + YT Shorts per `feedback_bubabu_no_tiktok_md_reuse_facebook` | ✅ written |
| `meta.md` | this file | ✅ written |
| `voiceover_geo.md` | KA verbatim translation by user via lang agent | ⏳ PENDING USER |
| `speech_ka.srt` | Phase 2 from KA voiceover | ⏳ PENDING |
