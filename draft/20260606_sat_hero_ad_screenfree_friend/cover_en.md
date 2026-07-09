<!-- engine-override: PROMPT_ENGINE_DETAIL_FLOOR + BUBABU_PIXAR_LOCK reason: AI HYPERREAL 8K ad - photoreal cover, EN-audience headline (baked Latin). Brand-break, Archil sign-off before publish. -->

# COVER (EN AUDIENCE · HYPERREAL 8K) - Bubabu Hero Ad «Screen-Free Friend»

> English-language cover. Same photoreal hero as `cover.md`; headline baked in ENGLISH (Latin - NB2 renders Latin reliably). Cast = the primary child (`child_ref.png`). **Archil sign-off before publish.**
> Sony A1 / 85mm / Portra / 8K. No price. No character name as text.

---

## DESIGN CONCEPT
Warm photoreal domestic poster on the BOND. A child, lit and delighted, reaches for the real Bubabu plush; the cold tablet lies face-down and forgotten on the rug (the "screen off" signal). Late-afternoon window light, creamy bokeh. 0.3s read: *"the kid chose the owl over the screen."* Mid-action - the reach, not the finished hug.

**Palette:** muted butter-cream + oatmeal + warm amber, grey hoodie, a single cyan note from Bubabu's goggles. Warm earthy, zero blue/navy dominant (FB-safe).

## CENTRAL HEADLINE (baked, English Latin)
- **Main:** `A FRIEND WITH NO SCREEN` - chunky rounded, warm cream + soft dark drop shadow.
- **Sub:** `talks in a hundred languages` - smaller, warm cream/amber (benefit, from the VO).
- **Brand:** tiny `BUBABU.GE` (warm-cream pill + deep-magenta text), bottom-center-safe.
- **NO price, NO character name.**

**EPIC anchor:** PARADOX (a friend with no screen) + concrete benefit subline.

## TYPOGRAPHY STACK (≥1 FILL-bucket mandatory)
- **TY-FILL = WARM-CREAM SOLID + soft amber inner-glow** in the headline letters.
- **TY-A = CHUNKY ROUNDED WEIGHT** · **TY-B = SOFT DARK DROP SHADOW.**
- Visual-language: *"big chunky soft-rounded warm-cream English headline with a soft dark drop shadow; a smaller warm-cream line beneath; a tiny warm-cream pill wordmark bottom-center."*

---

## IMAGE PROMPT - PHOTOGRAPH LAYER (NB2 v3.2 image SPEC, PRIMARY = baked English text)

**Refs uploaded:** `child_ref.png` + `1.jpeg` + `2.jpeg` (Bubabu, NEVER `3.jpeg`).

```json
{"schema_version":"PROMPT_ENGINE_v3.0","schema_kind":"image","scene_id":"screenfree_cover_en","user_intent":"Photoreal poster: a delighted child reaches for the Bubabu plush while the tablet lies face-down; baked English headline.","meta":{"aspect_ratio":"9:16","quality":"ultra_photorealistic","seed":80951,"guidance_scale":6.2},"sequence_logic":{"shot_type":"portrait_poster","color_grading":{"palette_driver":"warm domestic naturalism, golden late-afternoon, muted butter-cream and amber, Kodak Portra skin science, creamy bokeh","lut_simulation":"Kodak Portra 400","contrast":"flat_log"},"temporal_effects":"freeze_frame"},"subjects":[{"id":"child","character_dna":{"bone_structure":"delicate","persistent_features":["child about six, warm eyes, dark-brown hair, real pores, individual hair strands","catchlight in the eyes","match child_ref.png face exactly"],"heritage":"real child, photoreal, face shown, from child_ref.png"},"spatial_layout":{"coordinates":{"x":-0.2,"y":-0.05,"z_index":2},"visual_weight":0.55},"appearance":{"age":"young child","expression":"delighted, eyes lit and bright, a happy reach toward the plush","clothing":[{"item":"grey hooded long-sleeve and soft joggers","fabric":"cotton fleece","weathering":"worn"}]},"interaction":{"target_id":"bubabu","action":"reaching toward the plush, eyes bright","emotional_state":"delighted"}},{"id":"bubabu","character_dna":{"bone_structure":"delicate","persistent_features":["real plush owl toy, photoreal short-pile fabric with visible fibers and seams","matte printed cyan-turquoise goggle fabric, NOT illuminated","black felt triangular beak, closed; match 1.jpeg + 2.jpeg 1:1"],"heritage":"real Bubabu plush product, match 1.jpeg + 2.jpeg exactly"},"spatial_layout":{"coordinates":{"x":0.35,"y":0.25,"z_index":2},"visual_weight":0.45},"appearance":{"age":"n/a plush","expression":"sitting warm in focus on the rug, beak closed","clothing":[]},"interaction":{"target_id":"child","action":"sitting on the rug as the child reaches for it","emotional_state":"n/a"}},{"id":"tablet","character_dna":{"bone_structure":"delicate","persistent_features":["kids tablet with chunky rubber bumper case","lying face-down on the rug, screen hidden","smudged back casing"],"heritage":"real kids tablet, screen-off signal"},"spatial_layout":{"coordinates":{"x":-0.05,"y":0.5,"z_index":1},"visual_weight":0.18},"appearance":{"age":"n/a","expression":"face-down, dark and forgotten on the rug","clothing":[]},"interaction":{"target_id":"child","action":"lying face-down, set aside","emotional_state":"n/a"}}],"scene":{"location":"a warm real living room, late-afternoon window light, soft rug","mise_en_scene":{"narrative_clutter":["soft area rug","a low wooden shelf with books","a knitted throw blanket","a potted plant by the window","creamy bokeh highlights","dust motes in the window beam"],"world_state":"new"},"lighting_advanced":{"color_temperature":5200,"type":"cinematic","volumetric_fog":0.1}},"technical":{"camera":{"model":"Sony A1","lens":"Sony GM 85mm f/1.4","aperture":"f/1.8"},"material_science":{"roughness_global":0.55,"subsurface_scattering":true,"reflections":"ray_traced"}},"text_rendering":{"enabled":true,"text":"A FRIEND WITH NO SCREEN / talks in a hundred languages / BUBABU.GE","placement":"big chunky soft-rounded warm-cream English headline 'A FRIEND WITH NO SCREEN' across the upper third with a soft dark drop shadow; a smaller warm-cream English line 'talks in a hundred languages' just beneath; a tiny warm-cream pill 'BUBABU.GE' bottom-center-safe. No other text."},"advanced":{"negative_prompt":["cartoon","3d render","CGI","anime","Pixar","plastic skin","waxy skin","glowing goggles","open beak","realistic live owl","second plush","tablet screen visible","oversaturated HDR","face morphing","character name text","price text","garbled letters","watermark","blurry"],"hdr_mode":true}}
```

### FALLBACK (clean-photo path)
Same SPEC with `"text_rendering":{"enabled":false,...}` → render clean → assemble the English lines + BUBABU.GE pill in CapCut/AE.

## EDITOR-OVERLAY ASSEMBLY (fallback)
1. clean photoreal render · 2. headline `A FRIEND WITH NO SCREEN` warm-cream + shadow, upper third, ≥220px · 3. sub `talks in a hundred languages` warm-cream ~90px · 4. `BUBABU.GE` warm-cream pill + magenta, bottom-center.

## TYPOGRAPHY HIERARCHY
| Layer | Text | Treatment | Color | Function |
|---|---|---|---|---|
| Headline | `A FRIEND WITH NO SCREEN` | chunky rounded + warm-cream FILL + shadow | warm cream | paradox hook |
| Sub | `talks in a hundred languages` | rounded medium | warm cream/amber | benefit |
| Brand | `BUBABU.GE` | warm-cream pill | magenta `#FF1F8F` | the one Latin element |

## SELF-CHECK SCORECARD
| # | Check | Verdict |
|---|---|---|
| 1 | 0.3-sec readable | ✅ kid chose the owl over the screen |
| 2 | Mid-action | ✅ the reach + tablet face-down |
| 3 | Curiosity gap | ✅ photo shows kid+plush+dead tablet, headline says "no screen" |
| 4 | Contrast vs FB blue UI | ✅ warm butter-cream/amber |
| 5 | One focal ≤3 elements | ✅ child face focal; plush + tablet secondary |
| 6 | Face emotion named | ✅ delight (lit eyes) |
| 7 | Mobile text ≥220px | ✅ chunky + shadow upper third |
| 8 | Safe zone | ✅ headline upper third, brand above caption rail |
| 9 | Style match | ✅ photoreal Portra matches the video |
| 10 | No banned | ✅ no name-text, no price, no glow on plush, tablet screen hidden |
| **FILL** | ≥1 FILL-bucket | ✅ warm-cream FILL + amber lift |
| **EPIC** | anchor | ✅ PARADOX + benefit |
**Score: 10/10 → ship (after Archil sign-off).**

## A/B/C/D VARIANTS
- **B - HUG CLOSE** (child hugging the plush) · **C - SPLIT** (cold tablet-glow face vs warm plush face) · **D - PLUSH HERO** (plush in focus, reaching hand behind). Trigger A 48h → <1.5% CTR → B → C → D.

## PLATFORM CROPS + CHANNEL
9:16 (TT/IG Reels/YT) · 1:1 (IG feed) · 4:5 (FB). Bubabu official + Axiom Smart + Bubabu Smart Gifts only.

## Calibration
- L1/L2 - VERIFIED (photoreal baked-English SPEC, self-check, A-D, crops). L3 render PENDING (child matches child_ref.png). L4 + Archil sign-off PENDING.
