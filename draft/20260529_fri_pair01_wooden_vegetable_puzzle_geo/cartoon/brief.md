# Brief - pair01 Cartoon (Wooden Vegetable Puzzle GE)

## Pair identity

| Field | Value |
|-------|-------|
| Slug | `20260529_fri_pair01_wooden_vegetable_puzzle_geo` |
| Pair number | **01** (first post-pivot Smart Gifts pair - locks SKIN_IDENTITY for the whole series) |
| Cartoon day | **2026-05-29 fri** (even-day cadence - chëtnyy: cartoon) |
| Ad day | **2026-05-30 sat** (nechëtnyy: ad in `ad/` subfolder) |

## SKU featured

| Field | Value |
|-------|-------|
| Catalog ID | `4860129139038` |
| EN name | Wooden Vegetable Matching Puzzle (Georgian) |
| GE label on product | ფაზლი |
| Price | 24 ₾ |
| In stock | 8 |
| Flag | none (clean - can publish ad to FB/IG/TT immediately after render) |
| Reference photo | `./sku_ref.jpg (in this pair-folder root)` |
| Photo description | (intentionally NOT described in this brief - generator MUST use uploaded `sku_ref.jpg` as sole visual source of truth per `feedback_no_sku_appearance_dump_when_ref_uploaded` memory. Operator confirms uploaded photo present in pair-folder root before render. Catalog name + price live in retail copy / ad caption only - never re-describe SKU appearance in any prompt-bound text.) |
| Retail zone | Educational Smart Gifts |
| Age tier | 3-6 (core early-learning category) |

## Spark + Mood + Variant declaration (per ADV mode v4 SKIN_SYSTEM)

| Axis | Choice | Why |
|------|--------|-----|
| **Spark** | **Curiosity** (cyan `#5BC0DE`) | Wooden educational puzzle = learning + wondering. Cyan matches Bubabu's goggles, locks brand color into Scene 10 wing-arc trail. |
| **Mascot mood-state** | **Curious** | Head tilt 8-12° toward SKU, eyes wide on shelf object, wing-tip extending toward puzzle but not touching. |
| **Music mood (M-axis)** | **M2 adventure-bright** (D/G major, 100-130 BPM) | Curiosity-discovery beat lifts brighter than bedtime. Teaser had M1 - pair01 takes M2 (rotation rule honored). |
| **Palette (P-axis)** | **P2 sunlit-meadow green-amber** | Matches the puzzle's painted vegetables + Bubabu goggle cyan accent + Curious shelf cyan backlight. Teaser had P1 - rotation honored. |
| **Narrator register (N-axis)** | **N2 storyteller (default warmth)** | Slightly more energy than teaser's N1 lullaby - Curious arc earns brighter narration. |
| **Cold-open (O-axis)** | **O2 in-room arrival** | Teaser opened on O1 cloud-tree descent - pair01 rotates to O2 (child's room first). |

## SKIN_IDENTITY (LOCKED on this pair - propagates verbatim to every later episode)

This pair establishes the canon for every Smart Gifts cartoon+ad to follow. After pair01 ships, copy SKIN block verbatim into `agents/bubabu/series_skin_smart_gifts.md`.

- **Narrator voice cast:** Charon Storytime preset (Gemini TTS), pace 135-145 wpm, breath-pause ≥0.4s scene-transitions only (no mid-cue pauses).
- **Bubabu character block:** verbatim from `agents/bubabu/character_bubabu.md`. Refs uploaded: `1.jpeg` + `2.jpeg` (NEVER `3.jpeg` heart-eyes in pair mode).
- **Three-spark color semantics:** curiosity cyan `#5BC0DE` / kindness gold `#FFEB3B` / courage coral `#FF6B6B`.
- **Three-spark visual mechanic:** wing-arc trail BESIDE body at Scene 10 (R4) - never chest-glow, never goggle-glow, never aura.
- **Title card layout:** lower-third Bubabu silhouette + chunky cyan headline word + soft butter-cream gradient bottom - to be locked after Nano Banana render passes.
- **Endplate layout:** Bubabu seated by chest in storeroom + small «bubabu» wordmark + cyan dot indicating curiosity-spark of this episode - to be locked after render.
- **Universal closing line:** retired per Phase 2 - Smart Gifts cartoons close on the SKU handoff itself (Bubabu places gift in child's hand or on windowsill), no vocal serial-tease.
- **Motif identity:** «the wonder motif» 4-note hummable phrase **C-E-G-E**, transposable across keys per variant. Pair01 uses D-major transposition: D5-F#5-A5-F#5.

## Child profile (NEW per ep - no recurring face)

- **Name:** unnamed (origin canon - no specific names beyond the brand mascot).
- **Age:** 5 years old.
- **Appearance:** light-brown hair gently combed, soft cream daytime kid t-shirt + matching kid leggings or pants + soft cream cotton kid socks, kind face, no specific ethnicity markers (universal-child framing per origin canon). NEVER pyjamas, NEVER nightwear (moderation-safe per `feedback_bubabu_never_child_in_bed_in_nightwear`).
- **Room:** small daytime kid room with a large pale cream floor reading-nook cushion placed near the window, a small folded soft throw on a low wooden chair beside the cushion (decorative only, never on the child), soft toy on a low shelf in the corner, a small wooden picture-book shelf with colorful kid books in soft-focus, a single tall window facing east, morning blue-to-amber dawn light starting to come through. **NO bed visible anywhere in the room.**
- **Scenario:** child is already awake early on the reading-nook cushion by the window, sitting calmly cross-legged and watching the morning come. Then she turns gently toward the window-sill, sees the wooden puzzle resting in the soft dawn light, walks softly over, and cradles it in both hands.
- **Why this child:** age fits the catalog 3-6 range for the puzzle. Early-awake-by-window aligns with cartoon arc ending at dawn (Scene 14 = SKU on windowsill at first light) AND avoids the «minor + bed + nightwear + eyes-closed» CSAM-filter combo that Veo 3.1 / Nano Banana 2 / Meta ad-review reject.

## Arc (14 scenes - ADV v4 hybrid HOOK→SETUP→STOREROOM PICK→DESCEND→HANDOFF)

| Scene | Beat | Storeroom or world | SKU appears? |
|-------|------|---------------------|--------------|
| 01 | COLD OPEN - child's room at pre-dawn, empty windowsill, single guiding star outside | child world | no |
| 02 | Child awake on reading-nook cushion by window, watching the morning come (daytime clothes, NO bed, NO blanket) | child world | no |
| 03 | Cut to cloud-tree at the same pre-dawn moment | Bubabu world | no |
| 04 | Inside the hollow - Bubabu seated, awake, listening | Bubabu world | no |
| 05 | Bubabu enters the storeroom, walks past the shelves | storeroom | no |
| 06 | Close on the Curiosity shelf (cyan backlight) - wooden puzzle sits among other curious-objects | storeroom | **first SKU appearance** |
| 07 | **STOREROOM REVEAL** - Bubabu's wing-tip touches the wooden puzzle, lifts it gently | storeroom (key frame for ad) | **yes - full SKU shot** |
| 08 | **APPROACH** - Bubabu carries the puzzle out of the storeroom, tucks it into his wing-fold | storeroom→hollow | **yes - SKU carried** |
| 09 | **HANDOFF intent** - Bubabu at the cloud-tree branch edge, puzzle in wing, paper-glider boat ready | Bubabu world (transition) | **yes - SKU in wing** |
| 10 | THE SPARK - Bubabu's right wing-tip arcs beside him, cyan curiosity-particle trail dissipates outward, motif phrase plays | Bubabu world | yes (in wing) |
| 11 | DESCENT - paper-glider boat drifts down through cloud-gap, guiding star lighting the path | between worlds | yes (in wing) |
| 12 | LANDING - Bubabu lands silently on the child's windowsill at dawn, places the puzzle gently on the sill | child world | **yes - handoff complete** |
| 13 | CHILD TURNS - child on cushion turns toward window, sees the puzzle on the sill, eyes widen softly | child world | yes (on sill) |
| 14 | THE HOLD - child cradles the puzzle, soft smile, Bubabu silhouette already gone from sill, single curiosity-cyan spark fading on the empty window | child world | yes (in child's hands) |

**Scenes 7-9 are the canonical key-frame set for the next-day ad** - Bubabu in-frame holding/examining/carrying the puzzle in soft amber storeroom light. Ad reuses one of these three frames as the hero image.

## Goal

- Establish SKIN_IDENTITY for the Smart Gifts series.
- Show the full cartoon→handoff→child arc end-to-end as a template every later pair follows.
- Visualize how Wonder Tools reframing is NOT needed for this SKU (wooden puzzle = canon-friendly).
- Land the ad next-day on the puzzle in soft morning light, 24 ₾, simple one-line benefit.

## Engine compliance pre-flight

- [ ] PROMPT_ENGINE v3.2 (NB2 dual SPEC JSON) - to be applied at scene-prompt drafting in `video.md`.
- [ ] PHOTO_VIDEO_FIDELITY v1.1 - set equality {video nouns} ⊆ {photo nouns} per scene.
- [ ] VOICEOVER_ENGINE v1.0 + BUBABU_SCRIPT_ENGINE §BS (2026-05-29) - 14 cues, no `...`, no `[bracket]`, complete flowing sentences.
- [ ] CHARACTER_ENGINE v1.0 - CHARACTER_BLOCK verbatim every prompt.
- [ ] AUDIO_ENGINE §L (Lyria 3 Pro) - 8-section spec, brand bell C-E-G-E in D-major transposition.
- [ ] COVER_ENGINE + Bubabu cover override - baked-text Pixar candy-pop.
- [ ] SOCIAL_ENGINE v2.1 - English body + first-comment debate-bait + thematic-fit emoji.
- [ ] SLOP_FILTER §BS - no ellipsis, no bracket directives, complete sentences universal.
- [ ] MODERATION_ENGINE - kid-content safe vocabulary (wooden puzzle = no risk).

## File inventory (this folder)

```
cartoon/
├── brief.md            ✅ this file
├── character.md        (Bubabu identity + per-ep child)
├── voiceover.md        (Charon Storytime EN cues + FULL SCRIPT block)
├── video.md            (14 scenes paired PHOTO + VIDEO + VOICEOVER-TO-CLIP MAP)
├── audio.md            (Lyria 3 Pro 8-section + brand-bell D-major)
├── cover.md            (Bubabu candy-pop baked-text)
├── facebook.md         (SOCIAL_ENGINE v2.1 EN body + first comment — reused across FB + IG + TT + YT Shorts per `feedback_bubabu_no_tiktok_md_reuse_facebook`)
└── meta.md             (variant declaration + SKU + paired_ad pointer)

ad/                     (next-day, written 2026-05-30 sat)
├── brief.md
├── image.md
├── video.md
├── post.md
├── cover.md
└── meta.md
```

## Calibration

L1 FORMAT - verified at write time. L2 SPEC-CONFORMANCE - verified post-write across all files. L3 GENERATOR-CONVERGENCE - PENDING render (key risk: Scene 07 wing-tip on puzzle - verify no body-glow drift from cyan curiosity backlight). L4 VIEWER-TEST - PENDING after publish + audience response.
