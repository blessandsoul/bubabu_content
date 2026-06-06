# COVER — Bubabu Brain Remedy · Car Building Set (15 days)
## BUBABU CANDY-POP BAKED-TEXT TREATMENT (Bubabu cover override)

> Per Bubabu SKILL COVER OVERRIDE: kids-commercial Pixar candy-pop, PRIMARY = baked text, FALLBACK = editor-overlay after 3 Mkhedruli retries. EPIC HEADLINE + FILL TREATMENT + SELF-CHECK strict.
> Series formula — `[toy] 15 დღე` + series-locked second-person subtitle `რა ხდება შენი ბავშვის ტვინში?`. Mkhedruli lowercase, no Mtavruli, no Cyrillic, no character name, no typography tokens in image body. **Bubabu FRONTAL + round + no-tail** (render-drift fix).

<!-- engine-override: PROMPT_ENGINE_DETAIL_FLOOR reason: Bubabu Pixar-lock — Kelvin/lens/SSS dropped as photoreal/CSAM triggers; bright Pixar via style_anchor. -->

---

## DESIGN CONCEPT
Bright glossy Pixar candy-pop poster. Bubabu hero center-frame, **FRONTAL facing forward** (round ball, no tail), curious-wonder face, beak closed, holding ONE bright building brick up by his goggles; the half-built race car bright in front; a faint gold wonder-brain bubble pops above his shoulder. Racing energy, clean and punchy — "a toy is building something in his head" in 0.3s. **NOT soft, NOT atmospheric** — bright, glossy, saturated.

**Palette (60-20-10):** 60% warm butter-cream `#FFFAEB→#FFF6CC` · 20% coral→magenta focal on the headline · 10% racing-red `#E23B2E` + cobalt `#2B5BD7` accent (car energy). Zero blue/navy dominant; pops on FB.

## CENTRAL HEADLINE (baked, Mkhedruli lowercase)
- **Main:** `მანქანა 15 დღე` — *"Car, 15 days"* — NUMBER anchor 15. Two-word + number, chunky rounded. **KA proposed — user confirm** (alt: `კონსტრუქტორი 15 დღე`).
- **Subheadline (SERIES-LOCKED):** `რა ხდება შენი ბავშვის ტვინში?` — *"what happens in YOUR child's brain?"* — second-person, identical every episode. **KA user-verify.**
- No burst/ribbon. Tiny `BUBABU.GE` (UPPERCASE Latin, butter-cream pill + magenta) bottom-safe — the ONE Latin element. NO price, NO `ბუბაბუ` name-text.

**EPIC anchor:** NUMBER (15) + concrete nouns (`მანქანა` car / `ტვინი` brain) + curiosity question.

## TYPOGRAPHY STACK (≥1 FILL-bucket)
- **TY-FILL = GRADIENT FILL** — coral→magenta inside the headline letters (FILL bucket, required).
- TY-A chunky rounded weight · TY-B soft drop shadow. Sub = solid deep cyan `#5BC0DE`.
- Render visual-language (NOT px): *"big chunky soft-rounded Georgian headline with a coral-to-magenta gradient inside the letters and a soft drop shadow; smaller rounded deep-cyan question line beneath."*

---

## IMAGE PROMPT — PHOTOGRAPH LAYER (NB2 image SPEC, baked text)
**Refs:** `agents/bubabu/1.jpeg` + `2.jpeg` (NEVER `3.jpeg`) + `sku_ref.jpg` (Car Building Set — reference-only). Bubabu beak black closed, goggles matte fabric never glow, FRONTAL round no-tail, glow only on brain prop.

```json
{"schema_version":"PROMPT_ENGINE_v3.0","schema_kind":"image","user_intent":"Bright candy-pop Pixar poster: Bubabu frontal holding a building brick up, the half-built race car in front, a gold wonder-brain above, baked Georgian headline.","meta":{"aspect_ratio":"9:16","quality":"3d_render_octane","seed":60600,"guidance_scale":8},"sequence_logic":{"shot_type":"master_shot","color_grading":{"palette_driver":"bright glossy butter-cream Candy-Pop poster, coral and magenta focal, racing-red and cobalt accent, vivid saturated kid-toy","lut_simulation":"none — Pixar stylized","contrast":"high_key"},"temporal_effects":"freeze_frame"},"subjects":[{"id":"bubabu","character_dna":{"bone_structure":"delicate","persistent_features":["match attached 1.jpeg + 2.jpeg EXACTLY 1:1 — do NOT describe or invent Bubabu's appearance, the uploaded photos are the sole source"],"heritage":"match uploaded 1.jpeg + 2.jpeg EXACTLY 1:1"},"spatial_layout":{"coordinates":{"x":0.5,"y":0.5,"z_index":2},"visual_weight":0.85},"appearance":{"age":"timeless plush mascot","expression":"curious wonder, soft closed-beak smile, FRONTAL facing forward, perfectly round ball, no tail","clothing":[]},"interaction":{"target_id":"car","action":"sitting upright FRONTAL facing forward, holding one bright building brick up near his goggles","emotional_state":"curious wonder"}},{"id":"car","character_dna":{"bone_structure":"delicate","persistent_features":["match attached sku_ref.jpg 1:1, do not invent shape colors or design — use uploaded photo as sole appearance source"],"heritage":"Car Building Set, uploaded sku_ref.jpg"},"spatial_layout":{"coordinates":{"x":0.38,"y":0.66,"z_index":1},"visual_weight":0.5},"appearance":{"age":"the gift","expression":"the half-built brick race car bright in front of Bubabu","clothing":[]},"interaction":{"target_id":"bubabu","action":"the half-built race car and a few bright bricks in front of Bubabu","emotional_state":"inviting"}},{"id":"brain","character_dna":{"bone_structure":"delicate","persistent_features":["soft rounded Pixar wonder-brain prop, coral-pink plush-soft folds, toy-like NOT anatomical","inside a translucent bubble of light","a gold region glowing bright"],"heritage":"stylized Pixar wonder-brain prop, non-clinical"},"spatial_layout":{"coordinates":{"x":0.74,"y":0.3,"z_index":3},"visual_weight":0.3},"appearance":{"age":"bright","expression":"a small bright gold glow","clothing":[]},"interaction":{"target_id":"bubabu","action":"a faint gold wonder-brain bubble popping above Bubabu's shoulder","emotional_state":"the question"}}],"scene":{"location":"a bright candy-pop studio poster background, glossy butter-cream burst, no real room","mise_en_scene":{"narrative_clutter":["a glossy butter-cream radial burst","bright candy confetti in coral, racing-red and cobalt","a few bright building bricks near the car","tiny sparkle pops","a clean bright halo behind Bubabu"],"world_state":"new"},"lighting_advanced":{"type":"bright clean Pixar candy-pop studio light, the subject pops glossy, NOT soft NOT hazy","volumetric_fog":0.0}},"style_anchor":"Pixar 3D cartoon render, bright and glossy, vivid saturated Candy-Pop colors, ultra cute, ultra sharp high clarity, clean bright lighting that makes the subject POP. NOT soft, NOT muted, NOT washed out, NOT hazy, NOT atmospheric, NOT photoreal, NOT live-action.","technical":{"camera":{"model":"Pixar virtual"},"material_science":{"roughness_global":0.4,"reflections":"glossy"}},"text_rendering":{"enabled":true,"text":"მანქანა 15 დღე","placement":"big chunky soft-rounded Georgian Mkhedruli lowercase headline across the upper-center third, coral-to-magenta gradient inside the letters with a soft drop shadow; smaller rounded deep-cyan Georgian question line 'რა ხდება შენი ბავშვის ტვინში?' beneath it; tiny butter-cream pill 'BUBABU.GE' bottom-center-safe. No Mtavruli, no Cyrillic, no other text."},"advanced":{"negative_prompt":["no glow on Bubabu body","no glow on goggles","no open beak","no 3.jpeg variant","no second Bubabu","no scary owl","no tail","no tail feathers","no bird tail","perfectly round ball body","no stretching","no clinical brain","no second car","no screen, no phone","no soft haze","no dust-motes","no atmospheric blur","no photoreal","no live-action","no Mtavruli caps","no Cyrillic","no English title in image","no character name text","no price text","no garbled letters","watermark","blurry"],"hdr_mode":false}}
```

### FALLBACK (clean-photograph path — Mkhedruli mis-render 3×)
Same SPEC with `"text_rendering":{"enabled":false,"text":"","placement":""}` → clean Bubabu+car+brain poster → assemble the two Georgian lines + BUBABU.GE pill in editor.

## EDITOR-OVERLAY ASSEMBLY
1. **L0** glossy butter-cream burst BG (or the clean render).
2. **L1** headline `მანქანა 15 დღე` — chunky rounded Mkhedruli, coral→magenta GRADIENT FILL, soft shadow, upper-center, ≥220px.
3. **L2** sub `რა ხდება შენი ბავშვის ტვინში?` — deep cyan rounded, ~90px.
4. **L3** `BUBABU.GE` butter-cream pill + magenta UPPERCASE, bottom-center.
5. Per-glyph check: მ-ა-ნ-ქ-ა-ნ-ა / 1-5 / დ-ღ-ე / რ-ა / ხ-დ-ე-ბ-ა / შ-ე-ნ-ი / ბ-ა-ვ-შ-ვ-ი-ს / ტ-ვ-ი-ნ-შ-ი.

## TYPOGRAPHY HIERARCHY
| Layer | Text | Treatment | Color | Function |
|---|---|---|---|---|
| Headline | `მანქანა 15 დღე` | chunky rounded + GRADIENT FILL + shadow | coral→magenta | promise + number |
| Sub | `რა ხდება შენი ბავშვის ტვინში?` | rounded medium | deep cyan | curiosity (series-locked) |
| Brand | `BUBABU.GE` | butter-cream pill | magenta | the one Latin element |

## SELF-CHECK SCORECARD
| # | Check | Verdict |
|---|---|---|
| 1 | 0.3-sec readable | ✅ "a toy is building his brain" instant |
| 2 | Mid-action | ✅ Bubabu holds a brick + half-car + gold glow, mid-build never finished |
| 3 | Curiosity gap | ✅ image shows toy+glow, title asks what's inside |
| 4 | Color contrast vs FB | ✅ butter-cream + coral→magenta + racing-red/cobalt, zero blue dominant |
| 5 | One focal ≤3 | ✅ Bubabu face focal; car + brain secondary |
| 6 | Face emotion named | ✅ curious wonder |
| 7 | Mobile text ≥220px | ✅ chunky + gradient + shadow |
| 8 | Safe zone | ✅ headline upper-center, brand above caption rail |
| 9 | Style match | ✅ bright glossy Pixar matches the video |
| 10 | No banned | ✅ no Mtavruli/Cyrillic/English-title/name-text/price; Bubabu frontal no-tail |
| FILL | ≥1 FILL treatment | ✅ GRADIENT FILL |
| EPIC | anchor | ✅ NUMBER 15 + nouns + question |
**Score 10/10 → ship.**

## A/B/C/D VARIANTS
- **B — HANDS-FIRST:** close on the boy's hands clicking two bricks, the half-car beside, same headline. Switch if A CTR < FB 1.5% / 48h.
- **C — ROLLING CAR:** the finished race car mid-roll across the floor, the boy proud behind, gold brain above. Strong payoff option.
- **D — SPLIT BRAIN:** dim grey brain vs bright gold brain, the car between. Before-after gravitas.
- Trigger: A 48h → <1.5% switch B → flat try C → D experimental.

## PLATFORM CROPS + CHANNEL
| Platform | Crop | Note |
|---|---|---|
| TikTok | 9:16 | headline upper-third clear of rails |
| IG | 9:16 / 1:1 | 1:1 centers Bubabu |
| FB | 4:5 | warm palette pops on blue UI |
| YT Shorts | 9:16 | same master |

**Channel:** Bubabu official + Axiom Smart + Bubabu Smart Gifts only.
