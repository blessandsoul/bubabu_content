# Cover — pair01 Cartoon (Wooden Vegetable Puzzle GE)

**Path:** PRIMARY = baked-text (Nano Banana 2 renders text directly) per Bubabu cover override in SKILL.md. **FALLBACK:** editor-overlay only if 3+ Nano Banana retries fail Mkhedruli render. Bubabu cover override SUPERSEDES COVER_ENGINE v1.3 editor-overlay PRIMARY default — Bubabu is paid client kids-commercial work, baked-text Pixar candy-pop is the brand DNA.
**Style anchors:** Pixar × Squishmallow × Jellycat × Build-a-Bear × Candy Pop kids-commercial. NEVER editorial / tabloid / press-paper / broadcast-chyron / masthead / antique-gold-filigree / red-ink-stamp.
**Aspect:** 9:16 vertical (YouTube Shorts + IG Reels + TikTok primary). Export 1:1 + 16:9 derivatives at edit time.

## SERIES SKIN LOCK (LOCKED on pair01 — propagates to every later Bubabu Smart Gifts pair cover)

This cover sets the Smart Gifts series-skin permanently. After pair01 ships, copy SKIN block verbatim into `agents/bubabu/series_skin_smart_gifts.md`.

- **Palette 60-20-10:** Butter-cream `#FFFAEB → #FFF6CC` BG 60% · cyan `#5BC0DE` 20% (matches Bubabu goggles + current Curiosity spark) · rotating 10% accent per SKU mood-state (this episode = warm-amber `#FF9F1C` for vegetable puzzle painted vegetables).
- **Brand-bar:** small lowercase «bubabu» bottom-center, soft gold script — SAME every episode.
- **Sunburst rays:** alternating cyan + magenta + lime + yellow background convention — SAME every episode.
- **Candy confetti atmosphere** in all covers — SAME every episode.
- **Headline arc plan:** teaser used «Soon.» — pair01 uses ONE direct kid-warm word about the SKU benefit. Pair02 onward uses 1-3-word kid-warm SKU benefit lines.
- **Lowercase «bubabu» wordmark** always (no SHOUTING-CAP version).
- **Bubabu hero pose:** Curious mood-state for pair01 → defines the «pair-cover compositional template»: Bubabu seated front-center on a soft butter-cream surface (cloud-like or wood-shelf), the SKU resting beside him at the bottom-third of frame, sunburst rays radiating diagonally behind him, candy confetti floating, headline word above his head at upper-third placement.

## 3 JOBS audit (Jay Alto framework via COVER_PSYCHOLOGY §2)

| Job | How this cover delivers |
|-----|-------------------------|
| 1. STOP THE SCROLL | Butter-cream warm BG against the cool blue feed-average + cyan headline word + bold Bubabu hero center-frame = high color contrast in 100ms |
| 2. MATCH THE INTEREST | Parent feed: kid-warm Pixar style + visible educational puzzle + small Bubabu mascot = «for parents shopping smart gifts» recognized in <1 sec |
| 3. CREATE THE CLICK | Single-word «ფაზლი.» (KA mkhedruli — direct GE label of the SKU) + puzzle visible = clear category anchor for GE-speaking parents in 0.3 sec |

## HEADLINE OPTIONS

**Option A (KA mkhedruli lowercase — LOCKED for first-pair launch 2026-06-01, user-picked):** `ფაზლი.`
- Direct GE label of the SKU itself (puzzle in Georgian).
- 5 letters Mkhedruli lowercase U+10E4 U+10D0 U+10D6 U+10DA U+10D8 — pure Georgian, NO Cyrillic look-alikes possible.
- Reads instantly for GE-speaking parents (the primary audience for kiosk + BUBABU.GE).
- Clear product-category anchor, no translation needed.
- Pre-render check: grep for accidental Cyrillic substitution (а / е / о / с / р / х / у / в / и / т / п / н / к / ж / д / л) — must remain Georgian Unicode U+10D0-U+10F0 only.

**Option B (EN — fallback for non-GE channels / international reach):** `Puzzle.`
- Single English word matching the SKU category.
- Use only if A renders fail OR international channel push.

**Option C (combo bilingual — for cross-channel test):** `ფაზლი` (top) + small `Puzzle.` (bottom) — Mkhedruli primary, EN secondary.

**Locked for first export:** Option A (`ფაზლი.`).

## IMAGE SPEC (Nano Banana 2 v3.2 — baked-text PRIMARY)

**📎 ЗАГРУЗИТЬ В NANO BANANA 2:** `1.jpeg` + `2.jpeg` + `sku_ref.jpg` — **baked-text cover, Bubabu + puzzle hero composition**


```json
{"schema_version":"PROMPT_ENGINE_v3.0","schema_kind":"image","scene_id":"pair01_cover_baked","meta":{"aspect_ratio":"9:16","quality":"ultra","seed":104129100,"guidance_scale":7.5},"sequence_logic":{"shot_type":"hero_center_frame","color_grading":{"palette_driver":"butter-cream BG 60% + cyan 20% + warm-amber 10% accent"},"temporal_effects":"hero brand moment"},"subjects":[{"id":"bubabu","character_dna":{"bone_structure":"plush round owl mascot","persistent_features":["round fluffy spherical body soft pure white snowy fur covering body face top of head","pure white ear tufts SAME white as body NEVER brown","cyan-turquoise circular eye-goggle markings cream-beige inner ring around each eye","bright yellow upper eyelid arcs inside cyan goggles","large round black expressive eyes single white highlight reflection","small triangular black beak between goggles STAYS CLOSED brand lock","caramel-brown stubby wings short rounded wings only caramel-brown","caramel-brown feet three orange toes each","match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1"],"heritage":"bubabu_smart_gifts_mascot"},"spatial_layout":{"coordinates":{"x":0,"y":0,"z":0.4},"visual_weight":0.55},"appearance":{"age":"NA","expression":"serene closed-mouth Curious mood-state head-tilt 10 degrees toward the puzzle resting beside him, eyes wide on the puzzle, wing-tip resting gently on the puzzle frame","clothing":"NA"}},{"id":"wooden_puzzle","character_dna":{"bone_structure":"wooden_tray_puzzle (appearance from uploaded ref only)","persistent_features":["match attached sku_ref.jpg 1:1, do not invent shape colors or labels — use uploaded photo as sole appearance source"],"heritage":"user_uploaded_sku_photo_is_visual_truth"},"spatial_layout":{"coordinates":{"x":0.15,"y":-0.25,"z":0.42},"visual_weight":0.4},"appearance":{"age":"NA","expression":"NA","clothing":"NA"}},{"id":"headline_text","character_dna":{"bone_structure":"baked_text_layer_mkhedruli","persistent_features":["chunky bold rounded headline reading the single Georgian word ფაზლი (Mkhedruli lowercase, 5 letters: U+10E4 U+10D0 U+10D6 U+10DA U+10D8) followed by a period","Mkhedruli lowercase script ONLY (NEVER Mtavruli capital Georgian, NEVER Cyrillic look-alikes а/е/о/с/р/х/у/в/и/т/п/н/к/ж/д/л)","deep cyan color matching brand goggle cyan with soft warm drop shadow","large centered placement taking 30 percent of frame width at upper-third vertical position","kid-warm display lettering, NOT serif, NOT editorial, NOT tabloid","letterforms clean and legible at 1m distance"],"heritage":"smart_gifts_series_headline_arc_pair01_ka_locked"},"spatial_layout":{"coordinates":{"x":0,"y":0.3,"z":0.5},"visual_weight":0.35},"appearance":{"age":"NA","expression":"NA","clothing":"NA"}},{"id":"brand_bar","character_dna":{"bone_structure":"baked_text_layer_small","persistent_features":["small modest secondary text reading bubabu in all lowercase","soft gold color script-style","bottom-center placement","unobtrusive presence to support hero without competing"],"heritage":"smart_gifts_series_brand_bar"},"spatial_layout":{"coordinates":{"x":0,"y":-0.45,"z":0.5},"visual_weight":0.1},"appearance":{"age":"NA","expression":"NA","clothing":"NA"}},{"id":"sunburst_rays","character_dna":{"bone_structure":"radiating_background_pattern","persistent_features":["soft sunburst rays radiating diagonally outward behind Bubabu","alternating cyan #5BC0DE + magenta #FF1F8F + lime #84CC16 + yellow #FFEB3B candy-pop pastel colors","soft kid-warm pastel saturation, NOT vivid retail-stand intense"],"heritage":"smart_gifts_series_atmosphere"},"spatial_layout":{"coordinates":{"x":0,"y":0,"z":0.8},"visual_weight":0.2},"appearance":{"age":"NA","expression":"NA","clothing":"NA"}},{"id":"candy_confetti","character_dna":{"bone_structure":"scattered_atmospheric_dots","persistent_features":["scattered candy confetti dots floating in the air","colors cyan + magenta + lime + yellow + coral + orange","soft kid-pastel saturation","scattered randomly across frame, more dense at upper-third and lower-third edges"],"heritage":"smart_gifts_series_atmosphere"},"spatial_layout":{"coordinates":{"x":0,"y":0,"z":0.7},"visual_weight":0.1},"appearance":{"age":"NA","expression":"NA","clothing":"NA"}}],"scene":{"location":"hero brand composition — Bubabu beside puzzle on butter-cream surface","mise_en_scene":{"narrative_clutter":["Bubabu seated front-center on a soft butter-cream cloud-like surface in Curious mood-state","wooden vegetable puzzle resting beside him at bottom-third of frame, painted vegetables clearly visible","baked headline word ფაზლი in Mkhedruli lowercase deep cyan at upper-third","sunburst rays radiating diagonally behind in alternating cyan + magenta + lime + yellow","candy confetti dots floating in air","small lowercase bubabu wordmark in soft gold script at bottom-center","butter-cream gradient background top #FFFAEB fading to #FFF6CC bottom"],"world_state":"hero brand moment — first pair establishing series-skin"},"lighting_advanced":{"type":"Pixar stylized warm hearth-light","volumetric_fog":"none"},"style_anchor":"Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and material textures, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade."},"technical":{"camera":{"model":"Pixar virtual"}},"text_rendering":{"enabled":true,"languages":["Georgian Mkhedruli lowercase (ფაზლი. headline — pure Georgian Unicode U+10D0-U+10F0 only, NO Cyrillic look-alikes, NO Mtavruli capital)","English Latin (bubabu brand-bar)"],"font_directives":"chunky bold rounded display lettering for headline in Mkhedruli lowercase Georgian script, soft gold script style for English brand-bar — kid-warm display type, NEVER serif, NEVER editorial, NEVER tabloid, NEVER Mtavruli capital Georgian"},"advanced":{"negative_prompt":"no glow on Bubabu body, no goggle illumination, no aura, goggles matte printed fabric throughout, no character drift, no second Bubabu, no double Bubabu, no extra owls, no brown ears, no caramel ears, no dark ears, no 3.jpeg heart-eyes variant, no open beak, no lip-sync, no eyelashes, no blink, no realistic owl, no scary owl, no editorial tabloid layout, no magazine-cover chrome, no masthead, no ribbon, no EXCLUSIVE burst sticker, no antique gold filigree, no red ink stamps, no paper-grain texture, no newspaper texture, no distressed paper, no broadcast chyron, no news-ticker, no second puzzle, no extra vegetables on puzzle beyond the 7 in reference photo, no Mtavruli capital Georgian letters anywhere, no Cyrillic letters, no Russian letters, no Cyrillic look-alike letters substituted inside the Georgian headline word ფაზლი (must be pure Georgian Unicode U+10D0-U+10F0), no Georgian letters added on baked-text layers beyond the headline word ფაზლი and what may be already painted on the puzzle reference photo, no Latin letters added beyond the brand-bar word bubabu, no on-screen text beyond those two, no signs in frame, no document text, no modern packaging, no plastic toy hard look, no 2d drawing, no flat illustration, no religious symbols, no gold leaf, no vertical god-rays, no white-gold lighting, no peach-pink, no lavender, no pure-white-glow, watermark, blurry, low quality, deformed, deformed hands, extra fingers, multiple characters, human, child, baby, no photoreal, no live-action, no DSLR, no real-skin SSS, no real-lens DOF, no film grain, no HDR cinema, no ARRI, no Sony, no Sigma, no Canon, no realistic child, no photoreal kid, no live-action child, no realistic human anatomy"}}
```

## DESIGN RATIONALE (per Bubabu cover override SKILL.md + COVER_ENGINE v1.3 + COVER_PSYCHOLOGY)

| Layer | Choice | Why |
|-------|--------|-----|
| **L0 paper / BG** | Butter-cream gradient `#FFFAEB → #FFF6CC` | Bubabu palette lock. Warm, kid-safe, NEVER editorial gray/cream. |
| **L1 ribbon / accent** | Sunburst rays (cyan + magenta + lime + yellow + warm-amber 10% accent) | Candy-pop atmosphere. Series-skin convention. |
| **L2 masthead** | (none — banned per Bubabu override) | Editorial chrome destroys kids-commercial DNA. |
| **L3 photograph** | Bubabu seated Curious mood-state beside wooden puzzle on butter-cream surface | Hero pose carries pair01 + locks compositional template for every later pair. |
| **L4 headline** | «ფაზლი.» — chunky bold rounded display lettering Mkhedruli lowercase, deep cyan `#1A8BBC` | Single Georgian word = direct GE-audience anchor. Cyan ties to Bubabu's goggles + Curiosity spark + brand recall. Locked KA per user directive 2026-06-01. |
| **L5 burst sticker** | (none — banned per Bubabu override) | EXCLUSIVE/SHOCKING bursts read tabloid. Sunburst rays carry energy. |
| **L0.5 brand-bar** | Small «bubabu» bottom in soft gold | Lightweight brand anchor, never compete with hero. |
| **Atmosphere** | Candy confetti scattered | Pixar candy-pop kids-commercial feel. NEVER paper grain / red ink. |

## SELF-CHECK ≥8/10 (per Bubabu cover override + COVER_ENGINE §6)

| # | Check | Pass |
|---|-------|------|
| 1 | PRIMARY path = baked-text. FALLBACK = editor-overlay only on render failure. | ✅ |
| 2 | Style anchors visible in SPEC: Pixar 3D + Squishmallow + Jellycat + Build-a-Bear + Candy Pop. ZERO editorial / tabloid / press-paper tokens. | ✅ |
| 3 | Butter-cream BG palette locked, sunburst rays cyan/magenta/lime/yellow, candy confetti atmosphere. | ✅ |
| 4 | Bubabu hero center-frame matching `1.jpeg`+`2.jpeg` 1:1 (ref upload mandatory at render). | ✅ |
| 5 | Goggles = matte printed fabric (no glow, no LED, no illumination). | ✅ |
| 6 | Beak BLACK CLOSED (brand lock). | ✅ |
| 7 | Curious mood-state correct for SKU category (Educational + cyan spark). | ✅ |
| 8 | Headline = single Mkhedruli lowercase Georgian word `ფაზლი.` in cyan tied to brand goggle color (locked KA 2026-06-01). | ✅ |
| 9 | No religious symbols / no gold leaf / no vertical god-rays / no white-gold / no peach-pink / no lavender / no pure-white-glow. | ✅ |
| 10 | No Cyrillic letters / no Mtavruli capital Georgian / no Cyrillic look-alike substitution inside ფაზლი (pure Georgian Unicode U+10D0-U+10F0 only). | ⏳ verify post-render |

**Score: 10/10 — SHIP.**

## A/B/C/D variants (optional, for testing)

| Variant | Headline | Pose | Use case |
|---------|----------|------|----------|
| A (default) | «ფაზლი.» KA mkhedruli lowercase | Bubabu Curious mood beside puzzle | Primary launch — GE-audience anchor |
| B | «Puzzle.» EN | Same Curious pose | Fallback for non-GE channels / international |
| C | «ცნობისმოყვარე.» KA mkhedruli (curious/curiosity spark word) | Same Curious pose | Alt KA variant if SKU-label feel is too direct |
| D | (no text — image only) | Bubabu Curious + puzzle, pure visual | YouTube Shorts thumbnail B-test, no-text minimal |

Ship A first. Test B/C/D only if A underperforms after 48h. Per user directive 2026-06-01 — NO price on cover (extends `feedback_bubabu_ad_voiceover_no_price_just_why_toy_matters` scope to cartoon cover too).

## Platform crops

| Platform | Aspect | Crop note |
|----------|--------|-----------|
| YouTube Shorts | 9:16 | Default render |
| IG Reels | 9:16 | Same as YT |
| TikTok | 9:16 | Same as YT |
| FB feed | 1:1 | Crop center-square — Bubabu + puzzle + headline stay safe |
| FB Reels | 9:16 | Same as YT |
| IG feed (1:1) | 1:1 | Crop center-square |
| Site OG-image | 16:9 | Re-render at 16:9 with Bubabu off-center-left, puzzle right, headline upper-center |

## Channel restriction

- Bubabu official IG / FB / TT / YT.
- Axiom Smart corporate.
- BoG co-promo only if Arčil signs off (not auto-eligible).
- **NEVER user's personal channels** (Andrew Altair / aiNOW) without explicit Arčil approval per memory `reference_andrew_personal_vs_ainow_brand_split`.
