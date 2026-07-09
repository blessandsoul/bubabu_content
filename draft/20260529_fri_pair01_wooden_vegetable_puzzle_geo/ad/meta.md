# Meta - pair01 Ad (Wooden Vegetable Puzzle GE)

## Pair identity

| Field | Value |
|-------|-------|
| Pair slug | `20260529_fri_pair01_wooden_vegetable_puzzle_geo` |
| Paired cartoon | `../cartoon/` (same pair-folder, sibling subfolder) |
| Cartoon ship date | 2026-05-29 fri |
| **Ad ship date** | **2026-05-30 sat** (next-day pull, odd-day cadence) |
| Ad production mode | **B re-render across 3 scenes** (NB2 redraws Bubabu + puzzle on neutral butter-cream background, drops cartoon storeroom context, expanded to 3-scene reveal → play → hold arc per user directive 2026-05-30) |
| Ad file format | **Cartoon-style dual SPEC scene-block** in single `video.md` (3 paired NB2 image SPEC + Veo video SPEC). Former separate `image.md` MERGED into `video.md` 2026-05-30. |
| Ad voiceover | **Charon Storytime soft emotional explainer** in `voiceover.md` (3 cues, 41 EN words, ~19 sec). Off-screen narrator composited in editor over silent Veo + foley. ZERO price/CTA in narration (per user directive «без цены, просто объясни почему игрушка классная»). Added 2026-05-30. |
| Status | DRAFT in `agents/bubabu/draft/`. Awaits user «выложил pair01». |

## SKU featured (same as cartoon)

| Field | Value |
|-------|-------|
| Catalog ID | `4860129139038` |
| EN name | Wooden Vegetable Matching Puzzle (Georgian) |
| Price (operator-only - NEVER in customer-facing content per 2026-05-31 rule) | 24 ₾ |
| Retail zone | Educational Smart Gifts |
| Age tier | 3-6 |
| Flag | none - clean for publish |

## Channels (publish-time)

| Channel | Asset | Schedule |
|---------|-------|----------|
| Bubabu official Facebook | Scene 3 POSSESSION HOLD static image render + `post.md` body + first comment | Saturday 15:00 Tbilisi |
| Bubabu official Instagram feed (1:1) | Scene 3 POSSESSION HOLD static image cropped to 1:1 + `post.md` caption | Sat 15:00 Tbilisi |
| Bubabu official Instagram Reels (9:16) | All 3 scenes montage video (~15 sec) + `post.md` caption | Sat 15:00 Tbilisi |
| Bubabu official TikTok | Scene 1 JOY-HOP (3 sec hook) → Scene 2 PLAY (6 sec) → Scene 3 HOLD (4 sec) = ~13 sec total + `post.md` (tighter hashtags) + pinned first comment | Sat 15:30 Tbilisi |
| Bubabu official YouTube Shorts | All 3 scenes montage video + EN title `Bubabu Smart Gifts pair01 — Curious` | Sat 16:00 Tbilisi |
| Axiom Smart corporate | Scene 3 static 16:9 derivative | Sun (day after) |
| BoG co-promo | pending Arčil sign-off | Hold |
| Andrew Altair personal / aiNOW | **NEVER** without explicit Arčil approval | Forbidden |

## Render queue

| Asset | Tool | Refs uploaded | Status |
|-------|------|---------------|--------|
| Scene 1 image (JOY-HOP REVEAL - puzzle foreground, Bubabu mid-hop apex, sunburst rays expanded) | Nano Banana 2 v3.2 | `1.jpeg` + `2.jpeg` + `sku_ref.jpg` | DRAFT SPEC ready in `video.md` SCENE 1 Image SPEC |
| Scene 1 video (rigid vertical-translate hop loop, 5 sec) | Veo 3.1 v3.2 | Scene 1 image as source frame | DRAFT SPEC ready in `video.md` SCENE 1 Video SPEC |
| Scene 2 image (THEMATIC PLAY - close on Bubabu wing-tip placing tile in slot) | Nano Banana 2 v3.2 | `1.jpeg` + `2.jpeg` + `sku_ref.jpg` | DRAFT SPEC ready in `video.md` SCENE 2 Image SPEC |
| Scene 2 video (wing-tip places tile into slot loop, 6 sec) | Veo 3.1 v3.2 | Scene 2 image as source frame | DRAFT SPEC ready in `video.md` SCENE 2 Video SPEC |
| Scene 3 image (POSSESSION HOLD - Bubabu seated cradling puzzle against chest) | Nano Banana 2 v3.2 | `1.jpeg` + `2.jpeg` + `sku_ref.jpg` | DRAFT SPEC ready in `video.md` SCENE 3 Image SPEC |
| Scene 3 video (seated micro-breath + single wing-settle, 5 sec) | Veo 3.1 v3.2 | Scene 3 image as source frame | DRAFT SPEC ready in `video.md` SCENE 3 Video SPEC |
| Ad cover with baked BUBABU SMART GIFTS brand wordmark (NO price, NO benefit subheadline - per 2026-05-31 update) | Nano Banana 2 v3.2 baked-text | `1.jpeg` + `2.jpeg` + `sku_ref.jpg` | DRAFT SPEC ready in `cover.md` |
| Voiceover audio (Charon Storytime, 3 cues, ~19 sec, FULL SCRIPT single TTS run) | Gemini TTS Studio | - | DRAFT script ready in `voiceover.md` |
| Post copy (EN body + first comment) | manual | - | DRAFT ready in `post.md` |
| KA voiceover (`voiceover_geo.md`) | USER produces verbatim | EN draft from `voiceover.md` | PENDING USER |
| KA post copy (`post_geo.md`) | USER produces verbatim | EN draft from `post.md` | PENDING USER |

## Pre-render checklist

- [ ] **Scene 1 (JOY-HOP REVEAL) image render** - NB2 with `1.jpeg` + `2.jpeg` + `sku_ref.jpg`. Verify: Bubabu mid-hop apex (rigid translate, NO body squash-stretch), puzzle visible in lower-third matching `sku_ref.jpg` 1:1, sunburst rays expanded behind, butter-cream BG clean.
- [ ] **Scene 1 video render** - Veo 3.1 img2vid from Scene 1 image. Verify: rigid vertical hop (8cm up-down), NO body squash on landing, NO ear-stretch, seamless loop.
- [ ] **Scene 2 (THEMATIC PLAY) image render** - NB2 with `1.jpeg` + `2.jpeg` + `sku_ref.jpg`. Verify: close-up of wing-tip holding one tile above its matching slot, asymmetric-wing-lock (left wing frozen), puzzle matches `sku_ref.jpg` (other tiles in their slots, one slot empty waiting), goggles matte not illuminated.
- [ ] **Scene 2 video render** - Veo 3.1 img2vid from Scene 2 image. Verify: tile lowers into slot over 2 sec, pauses, returns to start for seamless loop, tile stays GLUED to wing-tip.
- [ ] **Scene 3 (POSSESSION HOLD) image render** - NB2 with `1.jpeg` + `2.jpeg` + `sku_ref.jpg`. Verify: Bubabu seated cradling complete puzzle in wing-fold, eyes soft on puzzle, asymmetric-wing-lock (left wing relaxed at side), puzzle complete per `sku_ref.jpg` (all tiles in slots).
- [ ] **Scene 3 video render** - Veo 3.1 img2vid from Scene 3 image. Verify: static body with micro-breath only, one gentle wing-settle at second 2, no body slouch.
- [ ] All 3 scenes - verify NEGATIVE bans worked: no storeroom context, no cyan goggle illumination, no character drift, no second Bubabu, no second puzzle.
- [ ] All 3 scenes - verify Pixar render lock held: stylized geometry, NO photoreal output, toy-like proportions throughout.
- [ ] NB2 renders the ad cover (`cover.md`) with baked `BUBABU SMART GIFTS` brand wordmark in soft warm gold (NO price, NO benefit subheadline - price lives ONLY in `post.md` caption per scope extension 2026-05-31).
- [ ] **Voiceover EN approval** - user reads `voiceover.md` EN draft and confirms tone (should feel like friend explaining gift, NOT commercial announcer).
- [ ] **User produces `voiceover_geo.md`** KA verbatim translation per memory rule (§BS body-style applies to KA too - zero `...`, zero `[bracket]`).
- [ ] **Gemini TTS render** - paste `voiceover.md` FULL SCRIPT block into Gemini TTS Studio with Charon Storytime preset, AUDIO PROFILE SCENE = sunlit terrace warm storyteller. Single TTS run captures all 3 cues. Verify pace ~140 wpm + soft warm tone (NOT commercial).
- [ ] User produces `post_geo.md` KA verbatim translation (per memory rule).
- [ ] Editor cuts platform-specific lengths per Channels table above (FB = Scene 3 static / IG Reels = all 3 montage + VO + foley + optional Lyria / TT = Scene 1 hook + Scene 2 + Scene 3 + VO / YT = all 3 montage + VO).
- [ ] **Editor composite layer order:** silent Veo video tracks → foley layer (from Veo `sfx_cues`) → VO layer (Charon at -3 dB above foley peak, -22 dB below) → optional Lyria 3 brand-bell loop layer at -22 dB under foley. Mix mastered at -14 LUFS for broadcast standard.
- [ ] **Listening test:** does VO feel like warm friend explaining or like commercial? Should feel like the former. If commercial-feel → re-render Charon at lower pitch + softer pace.

## Post-publish 24-48h monitoring

- Track `bubabu.ge` clicks + DM inquiries about the puzzle.
- Track FB/IG comments - especially Georgian-vegetable-name first-comment responses (signals identity-trigger engagement).
- Track TT TikTok video watch-rate at 3 sec, 6 sec (loop completion).
- If first-comment ≥10 organic responses + watch-rate ≥60% loop-completion = pair format VALIDATED, proceed to pair02.
- If first-comment <3 responses + watch-rate <30% = reflection-engine pass on ad format before pair02.

## Calibration

- L1 FORMAT - VERIFIED at write time (5 ad files present, JSON SPECs schema_version markers present per Bubabu STRICT floor).
- L2 SPEC-CONFORMANCE - VERIFIED (cartoon hero pose Scene 07 matched in ad image SPEC, SOCIAL_ENGINE v2.1 + SLOP_FILTER + §BS body-style clean in ad post.md, cover override baked-text per Bubabu rule, paired pointers cross-reference correctly).
- L3 GENERATOR-CONVERGENCE - PENDING render. Highest-risk render: ad hero image Bubabu pose must match cartoon Scene 07 within reasonable variance (if pose drifts, ad-to-cartoon visual continuity breaks).
- L4 VIEWER-TEST - PENDING audience response 24-48h after Saturday publish.

**Allowed claim now:** «Format + spec checks pass. Outcome pending render + viewer test.»
**Forbidden claim:** «Done / shipped / works / ready» - outcome unverified.

## File inventory (this ad/ folder)

| File | Role | Status |
|------|------|--------|
| `brief.md` | Concept + SKU + 3-scene reveal→play→hold arc + Mode B reasoning + benefit + CTA | ✅ written |
| `voiceover.md` | Gemini TTS Charon Storytime - 3 cues soft emotional product explainer, ~19 sec, zero price/CTA, sells RESULT not TOOL, off-screen narrator composited in editor | ✅ written |
| `video.md` | NB2 + Veo 3.1 v3.2 dual SPEC scene-block × 3 scenes (JOY-HOP REVEAL / THEMATIC PLAY / POSSESSION HOLD). MERGED from former separate image.md 2026-05-30. FOLEY ONLY in Veo output, NO Speech: tag (narrator composited in editor). | ✅ written |
| `post.md` | EN body 623 chars + first-comment debate-bait + audit | ✅ written |
| `cover.md` | NB2 baked-text PRIMARY with `BUBABU SMART GIFTS` brand wordmark only (NO price, NO benefit subheadline - scope extended 2026-05-31, price lives ONLY in `post.md`) | ✅ written |
| `meta.md` | this file | ✅ written |
| `voiceover_geo.md` | KA verbatim translation of `voiceover.md` by user via lang agent | ⏳ PENDING USER |
| `post_geo.md` | KA verbatim translation of `post.md` by user via lang agent | ⏳ PENDING USER |

**Structure change 2026-05-30:** Former `image.md` deleted, contents merged into `video.md` as 3 scene-blocks dual SPEC per user directive «у меня все подточено под формат картун там фото промпт и видео промпт» - generation workflow now identical between cartoon + ad.
