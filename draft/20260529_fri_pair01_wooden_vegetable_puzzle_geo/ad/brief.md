# Brief - pair01 Ad (Wooden Vegetable Puzzle GE)

## Pair identity

| Field | Value |
|-------|-------|
| Pair slug | `20260529_fri_pair01_wooden_vegetable_puzzle_geo` |
| Companion cartoon | `../cartoon/` (same pair-folder, sibling subfolder) |
| Cartoon ship date | 2026-05-29 fri (even-day) |
| **Ad ship date** | **2026-05-30 sat (odd-day) - next-day pull from cartoon** |
| Pair role | First Smart Gifts paired SKU - locks ad-format template for the whole series |

## SKU

| Field | Value |
|-------|-------|
| Catalog ID | `4860129139038` |
| EN name | Wooden Vegetable Matching Puzzle (Georgian) |
| GE label on product | ფაზლი |
| Price (operator-only - NEVER in customer-facing content) | 24 ₾ |
| In stock | 8 |
| Flag | none - ad can publish to FB / IG / TT / YouTube immediately |
| Retail zone | Educational Smart Gifts |
| Age tier | 3-6 (core early-learning) |
| Reference photo | `./sku_ref.jpg (in this pair-folder root)` |

## Ad concept

**3-scene Mode B re-render (per SKILL.md pair pipeline §Smart Gifts Pair Pipeline, expanded 2026-05-30).** Cartoon scene 07 (Bubabu lifts puzzle, KEY FRAME) provided the original visual anchor, but ad expanded to 3 scenes for product-reveal arc: JOY-HOP REVEAL → THEMATIC PLAY → POSSESSION HOLD. Each scene = paired NB2 image SPEC + Veo img2vid video SPEC (cartoon-style scene-block). All 3 scenes upload `1.jpeg` + `2.jpeg` + `sku_ref.jpg` to NB2 (mandatory).

**The 3 scenes:**
1. **JOY-HOP REVEAL** (4-6 sec) - SKU center-foreground, Bubabu rigid-translates vertical hop behind in Curious-Excited sub-mood (NO body squash-stretch per SKILL §Production Rules Video #2), sunburst rays expand. Product reveal hook.
2. **THEMATIC PLAY** (5-7 sec) - close on Bubabu's right wing-tip placing one vegetable tile into its matching slot on the puzzle (Curious-Playful sub-mood). Asymmetric-wing-lock honored (left wing frozen). Audience reads «matching game» from one action.
3. **POSSESSION HOLD** (4-6 sec) - Bubabu seated, puzzle cradled in right wing-fold against chest, eyes soft on puzzle (Curious-Cozy sub-mood). Reads «this is yours».

**Three production-mode options per SKILL.md still apply per scene:**
- **Mode A frame-rip** - literal cartoon scene screenshot. Cheapest. But cartoon background competes with the SKU.
- **Mode B re-render** ← **CHOSEN for all 3 ad scenes.** NB2 redraws Bubabu + puzzle on neutral butter-cream background + sunburst rays per series-skin. Best commercial clarity.
- **Mode C cartoon-still** - fast but loses commercial framing.

**Why 3 scenes for pair01:** first pair establishes the ad-format template for ALL future SKU pairs. Three-scene reveal → play → hold arc is reusable per SKU type. Editor cuts platform-specific lengths (FB feed = Scene 3 static / IG Reels = montage all 3 / TT = Scene 1 hook + Scene 2 play / YT Shorts = montage all 3).

## Hero benefit (one line for the ad post)

**EN draft:** «A small wooden tray, painted by hand, with seven vegetables to name in Georgian - the first gift Bubabu chose for the children who love to think.»

**KA verbatim:** USER produces in `post_geo.md` (per memory `feedback_bubabu_no_ai_ka_verse_or_prose`).

## CTA approach

Soft retail CTA on first pair (no aggressive sales push - pair01 is brand-trust setup, not high-conversion push):
- «Find it on **bubabu.ge**» (per memory `.ge` domain pronunciation rule «ჯი» - handled in TTS contexts only; here written domain).
- «BUBABU.GE · Tbilisi Mall · Galleria Tbilisi» (3-channel «where to find it» signal - NO price text in caption per «про цены мы не говорим» rule, scope re-extended 2026-05-31).

Future pairs may test stronger CTAs (limited-stock counter, gift-occasion urgency). pair01 = brand-setup.

## File inventory (this ad/ folder)

```
ad/
├── brief.md            ✅ this file
├── voiceover.md        (Gemini TTS Charon Storytime — 3 cues soft emotional product explainer, sells WHY toy matters, ZERO price/CTA mentions)
├── video.md            (3 scene-blocks dual SPEC cartoon-style: JOY-HOP REVEAL / THEMATIC PLAY / POSSESSION HOLD — each scene = paired NB2 image SPEC + Veo video SPEC, FOLEY ONLY in Veo output, narrator composited in editor)
├── post.md             (caption + price + CTA — EN body per SOCIAL_ENGINE LAW 1)
├── cover.md            (FB/IG thumbnail — derived from Scene 3 POSSESSION HOLD image render)
└── meta.md             (paired_cartoon pointer + zone + age + channels)
```

**Structure change 2026-05-30:** former separate `ad/image.md` (single Mode B hero re-render) + `ad/video.md` (single 6-sec loop) MERGED into one `ad/video.md` with 3 scene-blocks dual SPEC per cartoon-style. User directive «у меня все подточено под формат картун там фото промпт и видео промпт» - operator generation workflow now identical between cartoon + ad.

**Voiceover added 2026-05-30 (same day):** former foley-only ad now ships with soft emotional Charon Storytime VO per user directive «давай со звуком и без цены а просто объясни почему игрушка классная». Off-screen narrator path (VOICEOVER_ENGINE §6 editor overlay - silent Veo render + Gemini TTS composite). 41 EN words across 3 cues, ~19 sec total. Sells RESULT (child interaction + Georgian learning + handmade lasting keepsake) not TOOL (puzzle features), zero price/CTA in narration - those stay in `post.md` overlay only.

## Engine compliance pre-flight

- [ ] PROMPT_ENGINE v3.2 - NB2 SPEC JSON for image (Bubabu STRICT floor).
- [ ] PHOTO_VIDEO_FIDELITY v1.1 - if video shipped, set equality {video nouns} ⊆ {image nouns}.
- [ ] CHARACTER_ENGINE v1.0 - CHARACTER_BLOCK verbatim from cartoon character.md.
- [ ] SOCIAL_ENGINE v2.1 - EN body + thematic-fit emoji + first-comment debate-bait (post.md).
- [ ] SLOP_FILTER §BS - no `...`, no `[bracket]`, complete flowing sentences.
- [ ] Bubabu cover override - baked-text Pixar candy-pop on ad cover.
- [ ] No screen-tech reframing needed (wooden puzzle = canon-friendly noun, also catalog name openly used in ad copy per Wonder Tools rule - ad context allows catalog name).
- [ ] Catalog SKU name «Wooden Vegetable Matching Puzzle (Georgian)» appears in ad post (NOT in cartoon body, but ad copy free to use catalog name).

## Channel restriction

Same as cartoon meta.md:
- Bubabu official IG / FB / TT / YT.
- Axiom Smart corporate.
- BoG co-promo if Arčil signs off.
- NEVER Andrew personal / aiNOW without explicit approval.

## Calibration

L1 FORMAT - verified at write time. L2 SPEC-CONFORMANCE - verified post-write. L3 GENERATOR-CONVERGENCE - PENDING render (Mode B re-render must match cartoon Bubabu pose + puzzle scale + lighting tone within reasonable variance). L4 VIEWER-TEST - PENDING audience response 24-48h after publish. Success metric: ad post comments mention puzzle / price / availability + organic FB/IG inquiries.
