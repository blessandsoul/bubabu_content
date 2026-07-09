<!-- engine-override: PROMPT_ENGINE_DETAIL_FLOOR + BUBABU_PIXAR_LOCK reason: AI HYPERREAL 8K ad - photoreal cover (matches the hyperreal video), replaces Pixar candy-pop. Brand-break, Archil sign-off before publish. -->

# COVER (HYPERREAL 8K) - Bubabu Hero Ad «Screen-Free Friend»

> ⚠️ Photoreal cover (matches `video.md`), not the Bubabu candy-pop default. **Archil sign-off before publish.**
> Quality bar = Sony A1 / 85mm / Kodak Portra / creamy bokeh / 8K. Mkhedruli lowercase only · no Cyrillic · no character name as text · no price. Georgian cast (matches the primary video.md). RU variant = swap cast → `cover_ru.md` (say the word).

---

## DESIGN CONCEPT
A warm photoreal domestic poster on the BOND. A Georgian child, fully lit and delighted, just turned to the real Bubabu plush and reaches for it; the cold tablet lies face-down and forgotten on the rug beside them (the "screen off" signal). Late-afternoon window light, dust motes, creamy bokeh. In 0.3s it reads: *"the kid chose the owl over the screen."* Mid-action - the reach, not the finished hug.

**Palette (warm domestic, FB-blue-UI safe):** muted butter-cream + oatmeal + warm amber daylight, the grey hoodie, a single cyan note from Bubabu's goggles. Warm earthy, zero blue/navy dominant.

## CENTRAL HEADLINE (baked, Mkhedruli lowercase - KA PROPOSED, user confirms native form before lock)
- **Main:** `მეგობარი ეკრანის გარეშე` - *"a friend without a screen"* - chunky rounded, warm cream with a soft dark drop shadow.
- **Sub:** `ასამდე ენაზე ელაპარაკება` - *"talks in up to a hundred languages"* - smaller, warm cream/amber (the benefit, from the VO).
- **Brand:** tiny `BUBABU.GE` (UPPERCASE Latin, warm-cream pill + deep-magenta text), bottom-center-safe.
- **NO price, NO character name `ბუბაბუ` as text.**

**EPIC anchor:** PARADOX / curiosity (a friend with no screen) + concrete benefit subline.

## TYPOGRAPHY STACK (≥1 FILL-bucket mandatory)
- **TY-FILL = WARM-CREAM SOLID + soft amber inner-glow** inside the headline letters (legible FILL on a warm photo; gradient reads muddy here).
- **TY-A = CHUNKY ROUNDED WEIGHT.**
- **TY-B = SOFT DARK DROP SHADOW** for lift off the photo.
- Visual-language for the render: *"big chunky soft-rounded warm-cream Georgian headline with a soft dark drop shadow; a smaller warm-cream Georgian line beneath; a tiny warm-cream pill wordmark bottom-center."*

---

## IMAGE PROMPT - PHOTOGRAPH LAYER (NB2 v3.2 image SPEC, PRIMARY = baked text)

**Refs uploaded:** `child_ref.png` (Georgian child turnaround) + `1.jpeg` + `2.jpeg` (Bubabu, NEVER `3.jpeg`).
**LAW:** child face shown (Georgian); Bubabu photoreal plush, beak closed, matte goggles (no glow); tablet face-down (screen hidden).

```json
{"schema_version":"PROMPT_ENGINE_v3.0","schema_kind":"image","scene_id":"screenfree_cover","user_intent":"Photoreal poster: a delighted Georgian child reaches for the real Bubabu plush while the tablet lies face-down and forgotten; baked Georgian headline.","meta":{"aspect_ratio":"9:16","quality":"ultra_photorealistic","seed":80950,"guidance_scale":6.2},"sequence_logic":{"shot_type":"portrait_poster","color_grading":{"palette_driver":"warm domestic naturalism, golden late-afternoon, muted butter-cream and amber, Kodak Portra skin science, creamy bokeh","lut_simulation":"Kodak Portra 400","contrast":"flat_log"},"temporal_effects":"freeze_frame"},"subjects":[{"id":"child","character_dna":{"bone_structure":"delicate","persistent_features":["real Georgian child about six, soft Caucasian features, warm brown eyes, dark-brown hair, olive-warm skin, real pores","catchlight in the eyes, individual hair strands","match child_ref.png face exactly"],"heritage":"real Georgian child, photoreal, face shown, from child_ref.png"},"spatial_layout":{"coordinates":{"x":-0.2,"y":-0.05,"z_index":2},"visual_weight":0.55},"appearance":{"age":"young child","expression":"delighted, eyes lit and bright, a happy reach toward the plush","clothing":[{"item":"grey hooded long-sleeve and soft joggers","fabric":"cotton fleece","weathering":"worn"}]},"interaction":{"target_id":"bubabu","action":"reaching toward the plush, eyes bright","emotional_state":"delighted"}},{"id":"bubabu","character_dna":{"bone_structure":"delicate","persistent_features":["real plush owl toy, photoreal short-pile fabric with visible fibers and seams","matte printed cyan-turquoise goggle fabric, NOT illuminated","black felt triangular beak, closed; match 1.jpeg + 2.jpeg 1:1"],"heritage":"real Bubabu plush product, match 1.jpeg + 2.jpeg exactly"},"spatial_layout":{"coordinates":{"x":0.35,"y":0.25,"z_index":2},"visual_weight":0.45},"appearance":{"age":"n/a plush","expression":"sitting warm in focus on the rug, beak closed","clothing":[]},"interaction":{"target_id":"child","action":"sitting on the rug as the child reaches for it","emotional_state":"n/a"}},{"id":"tablet","character_dna":{"bone_structure":"delicate","persistent_features":["kids tablet with chunky rubber bumper case","lying face-down on the rug, screen hidden","smudged back casing"],"heritage":"real kids tablet, screen-off signal"},"spatial_layout":{"coordinates":{"x":-0.05,"y":0.5,"z_index":1},"visual_weight":0.18},"appearance":{"age":"n/a","expression":"face-down, dark and forgotten on the rug","clothing":[]},"interaction":{"target_id":"child","action":"lying face-down, set aside","emotional_state":"n/a"}}],"scene":{"location":"a warm real living room, late-afternoon window light, soft rug","mise_en_scene":{"narrative_clutter":["soft area rug","a low wooden shelf with books","a knitted throw blanket","a potted plant by the window","creamy bokeh highlights","dust motes in the window beam"],"world_state":"new"},"lighting_advanced":{"color_temperature":5200,"type":"cinematic","volumetric_fog":0.1}},"technical":{"camera":{"model":"Sony A1","lens":"Sony GM 85mm f/1.4","aperture":"f/1.8"},"material_science":{"roughness_global":0.55,"subsurface_scattering":true,"reflections":"ray_traced"}},"text_rendering":{"enabled":true,"text":"მეგობარი ეკრანის გარეშე / ასამდე ენაზე ელაპარაკება / BUBABU.GE","placement":"big chunky soft-rounded Georgian Mkhedruli lowercase headline 'მეგობარი ეკრანის გარეშე' across the upper third in warm cream with a soft dark drop shadow; a smaller warm-cream Georgian line 'ასამდე ენაზე ელაპარაკება' just beneath; a tiny warm-cream pill 'BUBABU.GE' bottom-center-safe. No Mtavruli, no Cyrillic, no other text."},"advanced":{"negative_prompt":["cartoon","3d render","CGI","anime","Pixar","plastic skin","waxy skin","glowing goggles","open beak","realistic live owl","second plush","tablet screen visible","oversaturated HDR","face morphing","Mtavruli caps","Cyrillic","English title in image","character name text","price text","garbled letters","watermark","blurry"],"hdr_mode":true}}
```

### FALLBACK (clean-photo path - recommended; Mkhedruli baked text is risky on photos)
Same SPEC with `"text_rendering":{"enabled":false,"text":"","placement":""}` → render the clean photoreal child+plush+tablet poster → assemble the two Georgian lines + BUBABU.GE pill in CapCut/AE.

## EDITOR-OVERLAY ASSEMBLY (fallback)
1. **L0** the clean photoreal render.
2. **L1** headline `მეგობარი ეკრანის გარეშე` - chunky rounded Mkhedruli, warm-cream + soft dark shadow, upper third, ≥220px.
3. **L2** sub `ასამდე ენაზე ელაპარაკება` - warm-cream, ~90px, below.
4. **L3** `BUBABU.GE` warm-cream pill + deep-magenta UPPERCASE Latin, bottom-center.
5. Per-glyph Mkhedruli check: მ-ე-გ-ო-ბ-ა-რ-ი / ე-კ-რ-ა-ნ-ი-ს / გ-ა-რ-ე-შ-ე / ა-ს-ა-მ-დ-ე / ე-ნ-ა-ზ-ე / ე-ლ-ა-პ-ა-რ-ა-კ-ე-ბ-ა.

## TYPOGRAPHY HIERARCHY
| Layer | Text | Treatment | Color | Function |
|---|---|---|---|---|
| Headline | `მეგობარი ეკრანის გარეშე` | chunky rounded + warm-cream FILL + drop shadow | warm cream | the paradox hook |
| Sub | `ასამდე ენაზე ელაპარაკება` | rounded medium | warm cream/amber | concrete benefit |
| Brand | `BUBABU.GE` | warm-cream pill | magenta `#FF1F8F` | the one Latin element |

## SELF-CHECK SCORECARD
| # | Check | Verdict |
|---|---|---|
| 1 | 0.3-sec readable | ✅ "kid chose the owl over the screen" reads instantly |
| 2 | Mid-action | ✅ the reach toward the plush + tablet face-down - moment before the bond |
| 3 | Curiosity gap | ✅ photo shows kid+plush+dead tablet, headline says "a friend with no screen" |
| 4 | Contrast vs FB blue UI | ✅ warm butter-cream/amber, zero blue/navy dominant |
| 5 | One focal ≤3 elements | ✅ child face = focal; plush + face-down tablet secondary |
| 6 | Face emotion named | ✅ child delight (lit eyes) |
| 7 | Mobile text ≥220px | ✅ chunky rounded + drop shadow upper third |
| 8 | Safe zone | ✅ headline upper third, brand above caption rail |
| 9 | Style match | ✅ photoreal Portra matches the hyperreal video |
| 10 | No banned | ✅ no Mtavruli/Cyrillic, no English title, no name-text, no price, no glow on plush, tablet screen hidden |
| **FILL** | ≥1 FILL-bucket | ✅ warm-cream FILL + amber inner-lift |
| **EPIC** | anchor | ✅ PARADOX (friend without a screen) + benefit subline |
**Score: 10/10 → ship (after KA headline confirm + Archil sign-off).**

## A/B/C/D VARIANTS
- **B - HUG CLOSE:** the child hugging the plush, full delight, tablet face-down behind. Switch if A CTR < FB 1.5% / 48h.
- **C - SPLIT (screen vs friend):** left the cold blue tablet-glow on a bored face, right the same child warm and bright with the plush, headline across the seam.
- **D - PLUSH HERO:** the real Bubabu plush in warm hero focus, the child's reaching hand + the dead tablet soft behind. Pull if A+B+C flat.
- Trigger: A 48h → <1.5% CTR switch B → C → D.

## PLATFORM CROPS + CHANNEL
| Platform | Crop |
|---|---|
| TikTok / IG Reels / YT Shorts | 9:16 |
| IG feed | 1:1 |
| FB feed | 4:5 |
**Channel restriction:** Bubabu official + Axiom Smart + Bubabu Smart Gifts only. Not user personal channels without Axiom sign-off.

## Calibration
- L1 FORMAT - VERIFIED (9 sections, photoreal baked SPEC, self-check, A-D, crops).
- L2 SPEC-CONFORMANCE - VERIFIED (photoreal, child face shown, tablet screen hidden, no price/name, Mkhedruli-only, override declared).
- L3 GENERATOR-CONVERGENCE - PENDING NB2 render (Mkhedruli on photoreal often mis-renders → expect fallback overlay; child must match child_ref.png).
- L4 VIEWER-TEST - PENDING + Archil sign-off (brand break).
- **Pending user:** confirm KA headline native form before lock. RU cover = `cover_ru.md` on request (Slavic cast + RU/EN headline).
