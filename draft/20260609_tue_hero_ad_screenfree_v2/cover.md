<!-- engine-override: BUBABU_PIXAR_LOCK + PROMPT_ENGINE_DETAIL_FLOOR reason: AI HYPERREAL 8K cover matching the photoreal video (Sony A1 / Portra) per user 2026-06-09. Archil sign-off before publish. -->

# COVER - Bubabu «Screen-Free Friend v2» (HYPERREAL 8K · before/after split)

> Per `bible/COVER_ENGINE.md` v2.0 - ONE strong image + ONE thematic word. Editor-overlay default (`text_rendering.enabled:false`). Mid-action, 0.3-sec read. Georgian cast (matches video.md). Mkhedruli only, no Cyrillic, no character name as text, no price.

## IDEA (3 quick concepts - pick the most curious + scroll-stopping)
- the "wait, what?" = same kid, dead-on-the-screen vs alive-with-an-owl, in one frame.
- idea 1 - **before/after SPLIT**: left half cold-blue bored face on a tablet, right half the same child warm and laughing holding Bubabu, the word across the seam. ← **WINNER** (the contrast carries the hook with the word covered; it IS the proof).
- idea 2 - single warm shot: delighted child reaching for the real Bubabu while the tablet lies face-down (the winner's cover; strong but no contrast).
- idea 3 - Bubabu hero close, the child's reaching hand + a dead tablet soft behind (plush-first; weakest hook).

## THE WORD
`ეკრანის გარეშე` (without a screen) - the paradox that makes a parent stop: a *friend* with no screen. 2 words, Mkhedruli, not a character name.
source: the KA voiceover «ერთი, რომელსაც ეკრანი საერთოდ არ აქვს» (cue 2). **User confirms the native cover form before lock** (propose `ეკრანის გარეშე`).

## THE IMAGE (NB2 image SPEC - paste into Nano Banana 2, attach child_ref.png + 1.jpeg + 2.jpeg)
```json
{"schema_version":"PROMPT_ENGINE_v3.0","schema_kind":"image","scene_id":"screenfree_v2_cover","user_intent":"Before/after split poster: LEFT half the same Georgian child about nine slumped and glazed in cold-blue tablet light; RIGHT half the same child warm, laughing, holding the real Bubabu plush in golden light. Clean, no baked text (word added in editor across the seam).","meta":{"aspect_ratio":"9:16","quality":"ultra_photorealistic","seed":81250,"guidance_scale":6.2},"sequence_logic":{"shot_type":"portrait_poster","color_grading":{"palette_driver":"split grade — left cold blue screen-spill and grey, right warm golden butter-cream and amber, Kodak Portra skin science, a clean vertical seam down the middle","lut_simulation":"Kodak Portra 400","contrast":"flat_log"},"temporal_effects":"freeze_frame"},"subjects":[{"id":"child","character_dna":{"bone_structure":"delicate","persistent_features":["real Georgian child about nine years old, warm brown eyes, dark-brown straight hair, olive-warm skin, real pores","catchlight in the eyes, individual hair strands","match child_ref.png face exactly"],"heritage":"real Georgian child, photoreal, face shown, from child_ref.png"},"spatial_layout":{"coordinates":{"x":0.0,"y":-0.05,"z_index":2},"visual_weight":0.6},"appearance":{"age":"child about nine","expression":"LEFT half bored and glazed in cold-blue light; RIGHT half genuine laugh, eyes alive and bright in warm gold","clothing":[{"item":"grey hooded long-sleeve","fabric":"cotton fleece","weathering":"worn"}]},"interaction":{"target_id":"bubabu","action":"left side hunched to a screen, right side holding and laughing with the plush","emotional_state":"split — dull vs delighted"}},{"id":"bubabu","character_dna":{"bone_structure":"delicate","persistent_features":["real plush owl toy, photoreal short-pile fabric with visible fibers and seams","matte printed cyan-turquoise goggle fabric, NOT illuminated","black felt triangular beak, closed; match 1.jpeg + 2.jpeg 1:1"],"heritage":"real Bubabu plush product, match 1.jpeg + 2.jpeg exactly"},"spatial_layout":{"coordinates":{"x":0.35,"y":0.15,"z_index":2},"visual_weight":0.4},"appearance":{"age":"n/a plush","expression":"held warm in the child's hands on the right half, beak closed, sharp focus","clothing":[]},"interaction":{"target_id":"child","action":"cradled by the laughing child on the warm right half","emotional_state":"n/a"}}],"scene":{"location":"a warm real living room, split into a cold-blue left and a golden-warm right","mise_en_scene":{"narrative_clutter":["soft area rug","a low wooden shelf with books","a knitted throw blanket","a potted plant by the window","creamy bokeh highlights on the right","cold grey shadow on the left"],"world_state":"new"},"lighting_advanced":{"color_temperature":5000,"type":"cinematic","volumetric_fog":0.1}},"technical":{"camera":{"model":"Sony A1","lens":"Sony GM 85mm f/1.4","aperture":"f/1.8"},"material_science":{"roughness_global":0.58,"subsurface_scattering":true,"reflections":"ray_traced"}},"text_rendering":{"enabled":false,"text":"","placement":""},"advanced":{"negative_prompt":["cartoon","3d render","CGI","anime","Pixar","plastic skin","waxy skin","glowing goggles","open beak","realistic live owl","second plush","afro","curly hair","two different children","oversaturated HDR","face morphing","Mtavruli caps","Cyrillic","English title in image","character name text","price text","garbled letters","watermark","blurry"],"hdr_mode":true}}
```
Identity lock: child = `child_ref.png` (Georgian, ~9, dark straight hair, same face both halves) · Bubabu = `1.jpeg`+`2.jpeg` 1:1, beak closed, matte goggles no glow.

## WORD TREATMENT (editor overlay)
Font: **Noto Sans Georgian** (LOCKED) · big chunky weight · across the vertical seam, upper-middle · ONE fill = **warm-cream → pale-gold GRADIENT fill** inside the letters + a soft dark drop shadow for lift off the split photo · `ეკრანის გარეშე` stacked or one line.
Brand stamp: small `BUBABU.GE` (UPPERCASE Latin, warm-cream pill + deep-magenta text), bottom-center-safe - the one Latin element. No price.

## CHECK (all ✅)
- [x] 1-3 words (`ეკრანის გარეშე` = 2), not a sentence?
- [x] thematic + from source (the screen-free paradox, cue 2)? - user confirms native form.
- [x] image carries the hook with the word covered? (the split = dull vs alive = the proof)
- [x] font = Noto Sans Georgian + ONE fill treatment (warm-cream gradient + drop shadow)?
- [x] Mkhedruli not Mtavruli?
- [x] not a character name?
- [x] small domain stamp present (`BUBABU.GE`, the one Latin element)?
- [x] composition differs from the winner's cover (split vs single warm shot)?
- [x] no price, no Cyrillic, no English title baked, no glow on plush, beak closed?
