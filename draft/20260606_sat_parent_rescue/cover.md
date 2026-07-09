<!-- engine-override: PROMPT_ENGINE_DETAIL_FLOOR + BUBABU_PIXAR_LOCK reason: user requested HYPERREAL 8K 2026-06-06 (hyperreal render + replace Pixar). Photoreal cover, brand-lock exception. Pixar candy-pop cover in git history. -->

# COVER (HYPERREAL 8K) - Bubabu «Parent Rescue»

> ⚠️ BRAND-STYLE BREAK - photoreal replaces the Bubabu candy-pop cover per user choice. **Needs Archil sign-off before publish.**
> Quality bar = user's Sony A1 / 85mm enhancer (Kodak Portra skin science, creamy bokeh, real pores, 8K). Mkhedruli lowercase only · no Cyrillic · no character name as text · no price.

---

## DESIGN CONCEPT
A warm photoreal domestic poster on the emotional TURN. The mother's relieved, amazed face (fully shown - adult, the money shot, Sony A1 85mm f/1.4, real pores, catchlight) fills the upper-left; the real Bubabu plush sits in warm focus lower-right where one child (from behind / over-the-shoulder) reaches toward it. Late-afternoon window light, dust motes, creamy bokeh. In 0.3s it reads: *"the moment a tired parent's room finally calms."* Mid-action - her relief is landing, not resolved.

**Palette (warm domestic, FB-blue-UI safe):** muted butter-cream + oatmeal + warm amber daylight, mustard cardigan accent, a single cyan note from the plush goggles. Warm earthy, zero blue/navy dominant.

## CENTRAL HEADLINE (baked, Mkhedruli lowercase - KA PROPOSED, user confirms native form before lock)
- **Main:** `როცა სახლი მშვიდდება` - *"when the house finally calms"* - chunky rounded, warm cream with a soft dark drop shadow for legibility on the photo.
- **Sub:** `ბავშვები თვალს ვერ აშორებენ` - *"the children can't look away"* - smaller, warm cream/amber.
- **Brand:** tiny `BUBABU.GE` (UPPERCASE Latin, warm-cream pill + deep-magenta text), bottom-center-safe.
- **NO price, NO character name `ბუბაბუ` as text.**

**EPIC anchor:** PARADOX / curiosity-gap (chaos → calm) + concrete benefit subline.

## TYPOGRAPHY STACK (≥1 FILL-bucket mandatory)
- **TY-FILL = WARM-CREAM SOLID + soft amber inner-glow** inside the headline letters (the FILL-bucket treatment; on a photoreal warm photo a gradient reads muddy, so a clean warm-cream fill with a subtle amber lift is the legible FILL choice).
- **TY-A = CHUNKY ROUNDED WEIGHT.**
- **TY-B = SOFT DARK DROP SHADOW** for lift off the warm photo.
- Visual-language for the render: *"big chunky soft-rounded warm-cream Georgian headline with a soft dark drop shadow; a smaller warm-cream line beneath; a tiny warm-cream pill wordmark bottom-center."*

---

## IMAGE PROMPT - PHOTOGRAPH LAYER (NB2 v3.2 image SPEC, PRIMARY = baked text)

**Refs uploaded:** `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg` (NEVER `3.jpeg`) + the Scene 4 mother-reference plate. No SKU (Bubabu is the product).
**LAW:** mother face shown (adult, filter-safe); child from behind only (face hidden); Bubabu photoreal plush, beak closed, matte goggles (no glow).

```json
{"schema_version":"PROMPT_ENGINE_v3.0","schema_kind":"image","meta":{"aspect_ratio":"9:16","quality":"ultra_photorealistic","seed":81950,"guidance_scale":6.2},"sequence_logic":{"shot_type":"portrait_poster","color_grading":{"palette_driver":"warm domestic naturalism, golden late-afternoon, muted butter-cream and amber, Kodak Portra skin science, creamy bokeh","lut_simulation":"Kodak Portra 400","contrast":"flat_log"},"temporal_effects":"freeze_frame"},"subjects":[{"id":"mom","character_dna":{"bone_structure":"high_cheekbones","persistent_features":["real Georgian adult mother, soft Caucasian Georgian features, warm brown eyes, olive-warm skin, warm natural face fully visible, real skin pores and fine peach-fuzz, catchlight in the eyes","dark-brown wavy hair in a loose low bun with loose strands, small stud earrings","mustard knit cardigan over a cream tee","natural soft skin with light smile-lines"],"heritage":"real Georgian adult mother, photoreal, face shown, olive-warm skin, matches Scene 4 reference plate / mom_ref.png"},"spatial_layout":{"coordinates":{"x":-0.25,"y":-0.2,"z_index":2},"visual_weight":0.55},"appearance":{"age":"adult mother","expression":"relief softening her face, a small amazed smile, eyes warm and a little glassy","clothing":[{"item":"mustard knit cardigan over a cream tee","fabric":"wool knit","weathering":"lived-in"}]},"interaction":{"target_id":"bubabu","action":"watching the plush with relief","emotional_state":"relieved, amazed"}},{"id":"bubabu","character_dna":{"bone_structure":"delicate","persistent_features":["real plush owl toy — photoreal short-pile fabric with visible fibers and seams","matte printed cyan-turquoise goggle fabric (NOT illuminated)","black felt triangular beak, closed","match uploaded 1.jpeg + 2.jpeg form and markings 1:1"],"heritage":"real Bubabu plush product, photoreal fabric, match 1.jpeg + 2.jpeg exactly"},"spatial_layout":{"coordinates":{"x":0.35,"y":0.3,"z_index":2},"visual_weight":0.45},"appearance":{"age":"n/a plush","expression":"sitting warm in focus on the rug, beak closed","clothing":[]},"interaction":{"target_id":"child","action":"sitting on the rug as the child reaches toward it","emotional_state":"n/a"}},{"id":"child","character_dna":{"bone_structure":"delicate","persistent_features":["Georgian school-age child about eleven seen FROM BEHIND only — back of head and shoulders","straight dark-brown tousled hair over the neck, olive-warm skin","striped long-sleeve top","small hand reaching"],"heritage":"real Georgian child, olive-warm skin, face NOT visible, shot from behind for child-safety"},"spatial_layout":{"coordinates":{"x":0.05,"y":0.45,"z_index":1},"visual_weight":0.25},"appearance":{"age":"about eleven (school-age)","expression":"reaching toward the plush from behind, eager posture (face not shown)","clothing":[{"item":"striped long-sleeve","fabric":"cotton","weathering":"worn"}]},"interaction":{"target_id":"bubabu","action":"reaching a small hand toward the plush","emotional_state":"drawn in"}}],"scene":{"location":"a warm real living room, late-afternoon window light, soft rug","mise_en_scene":{"narrative_clutter":["soft area rug","a low wooden shelf with books","a knitted throw blanket","a potted plant by the window","creamy bokeh highlights","dust motes in the window beam"],"world_state":"new"},"lighting_advanced":{"color_temperature":5200,"type":"cinematic","volumetric_fog":0.1}},"technical":{"camera":{"model":"Sony A1","lens":"Sony GM 85mm f/1.4","aperture":"f/1.8"},"material_science":{"roughness_global":0.55,"subsurface_scattering":true,"reflections":"ray_traced"}},"text_rendering":{"enabled":true,"text":"როცა სახლი მშვიდდება / ბავშვები თვალს ვერ აშორებენ / BUBABU.GE","placement":"big chunky soft-rounded Georgian Mkhedruli lowercase headline 'როცა სახლი მშვიდდება' across the upper third in warm cream with a soft dark drop shadow; a smaller warm-cream Georgian line 'ბავშვები თვალს ვერ აშორებენ' just beneath; a tiny warm-cream pill 'BUBABU.GE' bottom-center-safe. No Mtavruli, no Cyrillic, no other text."},"advanced":{"negative_prompt":["child face visible","front-facing child","sharp child facial features","cartoon","3d render","CGI","Pixar","anime","plastic skin","waxy skin","glowing goggles","open beak","realistic live owl","second plush","oversaturated HDR","face morphing","Mtavruli caps","Cyrillic","English title in image","character name text","price text","garbled letters","watermark","blurry"],"hdr_mode":true}}
```

### FALLBACK (clean-photo path - recommended for photoreal, Mkhedruli baked text is risky on photos)
Same SPEC with `"text_rendering":{"enabled":false,"text":"","placement":""}` → render the clean photoreal mother+plush+child poster → assemble the two Georgian lines + BUBABU.GE pill in CapCut/AE.

## EDITOR-OVERLAY ASSEMBLY (fallback)
1. **L0** the clean photoreal render.
2. **L1** headline `როცა სახლი მშვიდდება` - chunky rounded Mkhedruli, warm-cream + soft dark shadow, upper third, ≥220px.
3. **L2** sub `ბავშვები თვალს ვერ აშორებენ` - warm-cream, ~90px, below.
4. **L3** `BUBABU.GE` warm-cream pill + deep-magenta UPPERCASE Latin, bottom-center.
5. Per-glyph Mkhedruli check: რ-ო-ც-ა / ს-ა-ხ-ლ-ი / მ-შ-ვ-ი-დ-დ-ე-ბ-ა / ბ-ა-ვ-შ-ვ-ე-ბ-ი / თ-ვ-ა-ლ-ს / ვ-ე-რ / ა-შ-ო-რ-ე-ბ-ე-ნ.

## TYPOGRAPHY HIERARCHY
| Layer | Text | Treatment | Color | Function |
|---|---|---|---|---|
| Headline | `როცა სახლი მშვიდდება` | chunky rounded + warm-cream FILL + drop shadow | warm cream | pain→relief promise |
| Sub | `ბავშვები თვალს ვერ აშორებენ` | rounded medium | warm cream/amber | concrete benefit |
| Brand | `BUBABU.GE` | warm-cream pill | magenta `#FF1F8F` | the one Latin element |

## SELF-CHECK SCORECARD
| # | Check | Verdict |
|---|---|---|
| 1 | 0.3-sec readable | ✅ "a tired parent's room calms" reads instantly |
| 2 | Mid-action | ✅ mother's relief landing + child reaching - moment before the calm settles |
| 3 | Curiosity gap | ✅ photo shows relief + plush, headline asks what calmed the house |
| 4 | Contrast vs FB blue UI | ✅ warm butter-cream/amber, zero blue/navy dominant |
| 5 | One focal ≤3 elements | ✅ mother face = focal; plush + child-from-behind secondary |
| 6 | Face emotion named | ✅ mother relief/quiet awe (adult, filter-safe) |
| 7 | Mobile text ≥220px | ✅ chunky rounded + drop shadow upper third |
| 8 | Safe zone | ✅ headline upper third, brand above caption rail |
| 9 | Style match | ✅ photoreal Portra matches the hyperreal video |
| 10 | No banned | ✅ no child face, no Mtavruli/Cyrillic, no English title, no name-text, no price, no glow on plush |
| **FILL** | ≥1 FILL-bucket | ✅ warm-cream FILL + amber inner-lift |
| **EPIC** | anchor | ✅ PARADOX (chaos→calm) + benefit subline |
**Score: 10/10 → ship (after KA headline confirm + Archil sign-off).**

## A/B/C/D VARIANTS
- **B - MOTHER 85mm CLOSE:** 70% crop on the mother's relieved face (Scene 4 frame), plush soft-focus beside. Switch if A CTR < FB 1.5% / 48h.
- **C - CHAOS→CALM SPLIT:** left the loud room (kids from behind romping), right the same room calm with the plush, headline across the seam.
- **D - PLUSH HERO:** the real plush in warm hero focus, child's reaching hand + mother blurred behind. Pull if A+B+C flat.
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
- L2 SPEC-CONFORMANCE - VERIFIED (photoreal, child from behind, mother face shown, no price/name, Mkhedruli-only, override declared).
- L3 GENERATOR-CONVERGENCE - PENDING NB2 render (Mkhedruli on photoreal often mis-renders → expect fallback overlay; mother must match Scene 4 plate).
- L4 VIEWER-TEST - PENDING + Archil sign-off (brand break).
- **Pending user:** confirm KA headline native form before lock.
