# COVER - Bubabu Brain Remedy · World Flags Puzzle (15 days)
## BUBABU CANDY-POP BAKED-TEXT TREATMENT (Bubabu cover override - NOT editorial tabloid)

> Per Bubabu SKILL **COVER OVERRIDE**: kids-commercial Pixar × Squishmallow × Candy Pop, PRIMARY = all text baked into the AI image, FALLBACK = editor-overlay after 3 Mkhedruli mis-render retries. Tabloid 7-layer stack (`bible/COVER_ENGINE.md` §3) does NOT apply. EPIC HEADLINE + FILL TREATMENT + SELF-CHECK still STRICT (`/bubabu` escalation).
> Format mirrors the Brain Remedy locked cover formula (ep1) - `[toy] 15 დღე` + `რა ხდება შენი ბავშვის ტვინში?` - series-consistent, only the toy swaps.
> Mkhedruli lowercase only · no Mtavruli · no Cyrillic · no character name as text · no typography px/font tokens in the image SPEC body (`feedback_no_typography_spec_in_image_prompts`).

<!-- engine-override: PROMPT_ENGINE_DETAIL_FLOOR reason: Bubabu Pixar-lock - Kelvin/lens/aperture/SSS dropped as photoreal + CSAM triggers per feedback_bubabu_pixar_render_lock_no_photoreal_spec_fields; Pixar intent via style_anchor + lighting_advanced.type string. -->

---

## DESIGN CONCEPT
Pixar feature-film candy-pop poster. Bubabu hero center-frame in **curious wonder** (Remedy face-map: curious wonder / quiet awe - the viewer wants to discover too), beak closed, leaning over the open puzzle with one piece held up to his goggles like a tiny window of light. A faint cute wonder-brain bubble glows soft above his shoulder - just enough to ask the question, never the finished puzzle (mid-action, never the result). Butter-cream sunburst behind, leaf-green and amber candy confetti (P2 sunlit-meadow tie-in). The whole frame says *"a toy is waking something up"* in 0.3s.

**Palette (60-20-10, FB-blue-UI contrast):** 60% warm butter-cream `#FFFAEB→#FFF6CC` · 20% coral→magenta focal (`#FF6B6B`/`#FF1F8F`) on the headline + confetti · 10% leaf-green `#84CC16` + amber + cyan `#5BC0DE` Bubabu-goggle accent. Warm-saturated, zero blue/navy dominant (pops against Facebook's blue chrome; green is FB-safe per COVER_PSYCHOLOGY).

## CENTRAL HEADLINE (baked, Mkhedruli lowercase)
- **Main headline:** `ფაზლი 15 დღე` - *"Puzzle, 15 days"* - **NUMBER anchor = 15** (EPIC mandate satisfied). Two-word + number, chunky rounded.
- **Subheadline (curiosity gap, SERIES-LOCKED 2026-06-05):** `რა ხდება შენი ბავშვის ტვინში?` - *"what happens in YOUR child's brain?"* - **second-person upgrade** (replaces third-person "a child's"): targets the watching parent + fires the "your child" > "children" share-trigger (channel data), while staying semantically correct (the brain is the child's, not the parent's - so NOT remedy's literal "your body"). The image shows WHAT (toy + glowing wonder-brain), the title asks WHAT-INSIDE. Complement, not duplicate. **KA PROPOSED - user confirms native form before it locks across all 15 covers.**
- **No burst sticker / no ribbon** (kids-commercial override - keeps it clean, not tabloid). Optional tiny brand wordmark `BUBABU.GE` (UPPERCASE Latin, butter-cream pill + deep-magenta text) bottom-safe, the ONE Latin element.
- **NO price, NO character name `ბუბაბუ` as text.**

**EPIC anchor declared:** NUMBER (`15`) + concrete noun pair (`ფაზლი` puzzle / `ტვინი` brain) + curiosity question. Zero banned slop intensifiers.

## TYPOGRAPHY STACK (codes - editor/baked, ≥1 FILL-bucket mandatory)
- **TY-FILL = GRADIENT FILL** - coral→magenta vertical gradient *inside* the headline letters (the FILL-bucket treatment, STRICT-required). Candy, warm, FB-contrast.
- **TY-A = CHUNKY ROUNDED WEIGHT** - fat soft-rounded sans, kid-friendly (cosmetic).
- **TY-B = SOFT DROP SHADOW** - gentle butter-cream-dark shadow for lift off the sunburst (cosmetic).
- Subheadline = solid deep cyan `#5BC0DE`, smaller, rounded, bottom-center-upper.
- Visual-language for the render (NOT px/font): *"big chunky soft-rounded Georgian headline with a warm coral-to-magenta gradient inside the letters and a soft drop shadow; smaller rounded deep-cyan question line beneath."*

---

## IMAGE PROMPT - PHOTOGRAPH LAYER (NB2 v3.2 image SPEC, PRIMARY = baked text)

**Refs uploaded:** `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg` (Bubabu form, NEVER `3.jpeg`) + `sku_ref.jpg` (Wooden World Flags Puzzle - reference-only, appearance never described).
**HEAD/BODY LAW:** Bubabu beak BLACK CLOSED, cyan goggles = matte printed fabric NEVER glow, white body / caramel wings+feet only, no squash. Glow lives ONLY on the wonder-brain prop.

```json
{"schema_version":"PROMPT_ENGINE_v3.0","schema_kind":"image","user_intent":"Candy-pop Pixar poster: Bubabu in curious wonder over a world-flags puzzle, a faint wonder-brain glowing above, baked Georgian headline.","meta":{"aspect_ratio":"9:16","quality":"3d_render_octane","seed":60400,"guidance_scale":8},"sequence_logic":{"shot_type":"master_shot","color_grading":{"palette_driver":"warm butter-cream Candy Pop poster palette, coral and magenta focal, leaf-green and amber confetti, cyan Bubabu-goggle accent, vivid saturated kid-toy","lut_simulation":"none — Pixar stylized non-photometric grade","contrast":"high_key"},"temporal_effects":"freeze_frame"},"subjects":[{"id":"bubabu","character_dna":{"bone_structure":"delicate","persistent_features":["match attached 1.jpeg + 2.jpeg EXACTLY 1:1 — do NOT describe or invent Bubabu's appearance, the uploaded photos are the sole source"],"heritage":"match uploaded 1.jpeg + 2.jpeg EXACTLY 1:1"},"spatial_layout":{"coordinates":{"x":0.5,"y":0.52,"z_index":2},"visual_weight":0.85},"appearance":{"age":"timeless plush mascot","expression":"curious wonder, quiet awe, soft closed-beak smile, eyes bright on the piece","clothing":[]},"interaction":{"target_id":"puzzle","action":"leaning over the open puzzle, holding one puzzle piece up near his goggles like a small window of light","emotional_state":"curious wonder"}},{"id":"puzzle","character_dna":{"bone_structure":"delicate","persistent_features":["match attached sku_ref.jpg 1:1, do not invent shape colors or labels — use uploaded photo as sole appearance source"],"heritage":"Wooden World Flags Puzzle, uploaded sku_ref.jpg"},"spatial_layout":{"coordinates":{"x":0.38,"y":0.66,"z_index":1},"visual_weight":0.5},"appearance":{"age":"the gift","expression":"open puzzle board, one piece lifted in Bubabu's wing","clothing":[]},"interaction":{"target_id":"bubabu","action":"open puzzle in front of Bubabu, one piece held up in his wing","emotional_state":"inviting"}},{"id":"wonder_brain","character_dna":{"bone_structure":"delicate","persistent_features":["soft rounded Pixar wonder-brain prop, coral-pink plush-soft folds, toy-like NOT anatomical","floating inside a translucent soap-bubble of warm light","tiny constellation sparkles, soft cyan and coral regions glowing"],"heritage":"stylized Pixar wonder-brain prop, non-clinical, non-anatomical"},"spatial_layout":{"coordinates":{"x":0.74,"y":0.32,"z_index":3},"visual_weight":0.3},"appearance":{"age":"waking","expression":"a small cute glow, soft cyan and coral regions warming","clothing":[]},"interaction":{"target_id":"bubabu","action":"a faint cute wonder-brain bubble glowing softly above Bubabu's shoulder","emotional_state":"the question"}}],"scene":{"location":"a bright candy-pop studio poster background, warm butter-cream sunburst, no real room","mise_en_scene":{"narrative_clutter":["warm butter-cream radial sunburst","soft candy confetti in coral, leaf-green and amber","a few loose bright puzzle pieces near the board","tiny drifting sparkle motes","a soft halo of warm light behind Bubabu"],"world_state":"new"},"lighting_advanced":{"type":"Pixar stylized bright clear candy-pop studio light, warm key + soft fill + gentle rim, NOT photoreal","volumetric_fog":0.05}},"style_anchor":"Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation, high-frequency plush fur detail on Bubabu, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.","technical":{"camera":{"model":"Pixar virtual"},"material_science":{"roughness_global":0.45,"reflections":"diffuse"}},"text_rendering":{"enabled":true,"text":"ფაზლი 15 დღე","placement":"big chunky soft-rounded Georgian Mkhedruli lowercase headline across the upper-center third, warm coral-to-magenta gradient inside the letters with a soft drop shadow; smaller rounded deep-cyan Georgian question line 'რა ხდება შენი ბავშვის ტვინში?' beneath it; tiny butter-cream pill 'BUBABU.GE' bottom-center-safe. No Mtavruli, no Cyrillic, no other text."},"advanced":{"negative_prompt":["no glow on Bubabu body","no glow on goggles","no goggle illumination","no LED eyes","no open beak","no 3.jpeg heart-eyes variant","no second Bubabu","no scary owl","no realistic owl","no brown ears","no caramel body","no clinical brain","no anatomical brain","no medical imagery","no second puzzle","no duplicate puzzle","no photoreal","no live-action","no DSLR","no real-skin SSS","no film grain","no HDR cinema","no ARRI","no Sony","no Mtavruli caps","no Cyrillic","no English title in image","no character name text","no price text","no garbled letters","watermark","blurry","low quality"],"hdr_mode":false}}
```

### FALLBACK (clean-photograph path - only if Mkhedruli mis-renders 3×)
Same SPEC with `"text_rendering":{"enabled":false,"text":"","placement":""}` → render clean Bubabu+puzzle+wonder-brain poster → assemble the two Georgian lines + BUBABU.GE pill in CapCut/AE (see assembly).

## EDITOR-OVERLAY ASSEMBLY (fallback path)
1. **L0** butter-cream sunburst BG (or use the clean render).
2. **L1** headline `ფაზლი 15 დღე` - chunky rounded Mkhedruli, **coral→magenta GRADIENT FILL**, soft drop shadow, upper-center, ≥220px.
3. **L2** sub `რა ხდება შენი ბავშვის ტვინში?` - deep cyan rounded, ~90px, just below headline.
4. **L3** `BUBABU.GE` butter-cream pill + deep-magenta UPPERCASE Latin, bottom-center, above the TikTok caption rail.
5. Per-glyph Mkhedruli render check: ფ-ა-ზ-ლ-ი / 1-5 / დ-ღ-ე / რ-ა / ხ-დ-ე-ბ-ა / ბ-ა-ვ-შ-ვ-ი-ს / ტ-ვ-ი-ნ-შ-ი.

## TYPOGRAPHY HIERARCHY
| Layer | Text | Treatment | Color | Function |
|---|---|---|---|---|
| Headline | `ფაზლი 15 დღე` | chunky rounded + GRADIENT FILL + soft shadow | coral→magenta | promise + number hook |
| Sub | `რა ხდება შენი ბავშვის ტვინში?` | rounded medium | deep cyan `#5BC0DE` | curiosity question |
| Brand | `BUBABU.GE` | butter-cream pill | magenta `#FF1F8F` | the one Latin element |

## SELF-CHECK SCORECARD (COVER_ENGINE §6 + COVER_PSYCHOLOGY $8)
| # | Check | Verdict |
|---|---|---|
| 1 | 0.3-sec readable | ✅ "a toy is waking a child's brain" reads instantly |
| 2 | Mid-action | ✅ Bubabu curious over the puzzle + faint brain glow - the moment of mid-discovery, never the finished board |
| 3 | Curiosity gap | ✅ image shows toy+glow, title asks "what happens in the brain?" - complement not duplicate |
| 4 | Color contrast vs FB blue UI | ✅ warm butter-cream + coral→magenta headline + green-amber confetti, zero blue/navy dominant |
| 5 | One focal ≤3 elements | ✅ Bubabu face = focal; puzzle + brain-glow secondary (Z-pattern) |
| 6 | Face emotion named | ✅ curious wonder / quiet awe (Remedy map, anticipation/interest - Plutchik) |
| 7 | Mobile text ≥220px outlined | ✅ chunky rounded + gradient fill + drop shadow, upper-center |
| 8 | Safe zone | ✅ headline upper-center, brand above caption rail, nothing in last 200px |
| 9 | Style match | ✅ Pixar candy-pop matches the video render exactly |
| 10 | No banned | ✅ no Mtavruli, no Cyrillic, no English title-in-image, no `ბუბაბუ` name-text, no price, no plastic/ringlight, no glow on Bubabu |
| **FILL** | ≥1 FILL-bucket treatment | ✅ GRADIENT FILL (coral→magenta inside letters) |
| **EPIC** | number/entity/paradox anchor | ✅ NUMBER `15` + concrete nouns + curiosity question |
**Score: 10/10 → ship.**

## A/B/C/D VARIANTS
- **B - HANDS-FIRST:** close on the boy's small hands fitting one piece into the board, Bubabu soft-focus behind, same headline. Switch if A's mascot-poster CTR < FB 1.5% after 48h.
- **C - SPLIT BRAIN:** left half a dim sleepy wonder-brain, right half the same brain bright and glowing, the puzzle between, headline across. Gravitas / clearer before-after. Try if curiosity-gap underperforms.
- **D - BUBABU CLOSE-UP:** 70% face crop of Bubabu in pure wonder, one puzzle piece reflected in the goggle-fabric (no glow), tiny brain bubble corner. Pull only if A+B+C flat - strongest emotional-face option.
- Trigger: run A 48h → FB CTR <1.5% switch B → still flat try C → D experimental.

## PLATFORM CROPS + CHANNEL
| Platform | Crop | Note |
|---|---|---|
| TikTok | 9:16 | headline upper-third, clear of right action rail + bottom caption |
| IG Reels/feed | 9:16 / 1:1 | 1:1 centers Bubabu + headline |
| FB feed | 4:5 | warm palette pops on blue UI |
| YT Shorts | 9:16 | same master |

**Channel restriction:** Bubabu official + Axiom Smart + Bubabu Smart Gifts channels only. Not user personal channels without Axiom sign-off.
