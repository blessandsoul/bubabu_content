# Bubabu - Wolt store images · 4 clean SPECs (NO logo, NO text)

**Generator:** Nano Banana 2 - paste each JSON SPEC + **upload `1.jpeg` & `2.jpeg`** (NEVER `3.jpeg` heart-eyes). Reference photo = source of truth, match exactly.
**All four:** Pixar 3D plush Bubabu · Candy Pop palette · butter-cream ground + soft sunburst + candy confetti (NO hearts) · BLACK closed beak · cyan goggles matte (never lit) · WHITE body (caramel only on wings/feet) · `text_rendering.enabled:false` (zero baked text, zero logo).
**Render & export:** slots 1-3 at 16:9 → export **2880×1620**; slot 4 at 1:1 → export **1024×1024**. Save JPEG or PNG. Generate 3-4 versions per slot, pick warmest face + sharpest cyan goggles.

---

## §1 · DISCOVERY / LIST IMAGE - 2880×1620 (16:9)

**Role:** the storefront card in the Wolt feed - the "tap into the store" shot. Bubabu hero front-and-center, inviting, brand-forward.
**Wolt safe-zone:** keep the **bottom-center band (~bottom 15%) calm and clean** - Wolt overlays the store name + rating chip there. No objects/owl-feet crossing into it.

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "wolt_discovery_list",
  "user_intent": "Wolt store discovery/list card — Bubabu plush-owl mascot front-and-center welcoming the shopper into a warm smart-gifts world; inviting 'tap me' storefront energy. Clean bottom band reserved for Wolt's store-name + rating overlay.",
  "meta": { "aspect_ratio": "16:9", "quality": "3d_render_octane", "guidance_scale": 7.5, "seed": 481620 },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": { "palette_driver": "Candy Pop kids-brand palette — Bubabu Cyan #5BC0DE goggles (sacred), butter-cream #FFFAEB ground, lime/sunny-yellow/orange/coral/magenta gift + sunburst accents" }
  },
  "subjects": [
    {
      "id": "Bubabu",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "round fluffy ball-shaped pure-WHITE plush owl — white fur on body, face AND top of head",
          "signature cyan-turquoise goggle eye-markings with cream inner ring + yellow eyelid arcs — SACRED, never remove/recolor",
          "small triangular BLACK closed beak + large round black eyes with single white highlight",
          "two tiny WHITE ear tufts; caramel-brown stubby wings + feet are the ONLY non-white parts"
        ],
        "heritage": "plush owl mascot — match uploaded 1.jpeg + 2.jpeg EXACTLY; reference photo is the source of truth"
      },
      "spatial_layout": { "coordinates": { "x": 0.5, "y": 0.42, "z_index": 2 }, "visual_weight": 0.6 },
      "appearance": {
        "age": "ageless plush mascot",
        "expression": "warm welcoming wonder, gentle eye contact with the viewer, soft bouncy waving-hello energy, beak closed"
      },
      "interaction": { "target_id": "wrapped_gifts", "action": "STANDING in FULL BODY — entire owl head-to-feet visible with comfortable margin above the head, NOT cropped; owl height ~62% of the frame, centered slightly high, presenting one small ribboned gift toward the viewer with a curated cluster of wrapped gifts beside him", "emotional_state": "warm, generous, inviting" }
    }
  ],
  "scene": {
    "location": "soft Pixar gift-nook, FULL-BODY framing — Bubabu shown head-to-feet (NOT cropped) standing on a warm cream studio ledge with a small curated cluster of wrapped gifts beside him; lower-center kept as a clean calm butter-cream band; soft sunburst behind",
    "style_anchor": "Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and material textures, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.",
    "mise_en_scene": {
      "narrative_clutter": [
        "3-4 elegant wrapped gift boxes with ribbons + bows in Candy Pop colors clustered around Bubabu (generic gifts, NO branded products, NO labels)",
        "one soft gift bag with tissue paper peeking out",
        "a soft cream display ledge suggesting a curated gift assortment",
        "soft low-contrast rainbow sunburst rays behind Bubabu",
        "scattered 3D candy confetti — stars, dots, ribbons (NO hearts) — drifting in the upper third",
        "clean calm butter-cream band across the BOTTOM-CENTER reserved for Wolt store-name + rating overlay (no objects there)"
      ],
      "world_state": "new"
    },
    "lighting_advanced": { "type": "Pixar stylized bright warm studio-polish light — soft key front-left, gentle fill, soft rim glow on top of head", "volumetric_fog": 0 }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": false, "text": "", "placement": "" },
  "advanced": {
    "negative_prompt": [
      "no photoreal","no live-action","no DSLR/real-lens DOF","no film grain","no HDR cinema","no ARRI/Sony real-camera look","no realistic real owl/animal",
      "no second owl","no other owl toy near Bubabu","beak open","caramel/brown beak","brown ears","brown body",
      "heart eyes","hearts in confetti","glowing/LED eyes","no halo/godrays",
      "cropped owl","owl head or feet cut off","objects crossing the bottom name band",
      "baked text/letters/wordmark/logos in image","watermark","multiple Bubabus",
      "Cyrillic text","mtavruli capital Georgian","branded product packaging or readable labels"
    ]
  }
}
```

---

## §2 · HEADER - 2880×1620 (16:9)

**Role:** the hero banner at the top of the Wolt store page. Wider establishing brand world; **most generous clean zones of the set.**
**Wolt safe-zone:** Wolt overlays the **store logo badge + store name + delivery info over the lower-left / lower band** - keep Bubabu in the **right third**, keep **left half + lower third airy and clean butter-cream** (no objects).

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "wolt_header_banner",
  "user_intent": "Wolt store-page header banner — Bubabu owl as gift-shop mascot in a wide smart-gifts nook, positioned to the right with airy clean butter-cream space on the left + lower band reserved for Wolt's logo badge, store name and delivery info overlay.",
  "meta": { "aspect_ratio": "16:9", "quality": "3d_render_octane", "guidance_scale": 7.5, "seed": 482880 },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": { "palette_driver": "Candy Pop kids-brand palette — Bubabu Cyan #5BC0DE goggles (sacred), butter-cream #FFFAEB ground, lime/sunny-yellow/orange/coral/magenta gift + sunburst accents" }
  },
  "subjects": [
    {
      "id": "Bubabu",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "round fluffy ball-shaped pure-WHITE plush owl — white fur on body, face AND top of head",
          "signature cyan-turquoise goggle eye-markings with cream inner ring + yellow eyelid arcs — SACRED, never remove/recolor",
          "small triangular BLACK closed beak + large round black eyes with single white highlight",
          "two tiny WHITE ear tufts; caramel-brown stubby wings + feet are the ONLY non-white parts"
        ],
        "heritage": "plush owl mascot — match uploaded 1.jpeg + 2.jpeg EXACTLY; reference photo is source of truth"
      },
      "spatial_layout": { "coordinates": { "x": 0.72, "y": 0.46, "z_index": 2 }, "visual_weight": 0.5 },
      "appearance": {
        "age": "ageless plush mascot",
        "expression": "warm welcoming pride, gentle eye contact, soft bouncy energy, beak closed"
      },
      "interaction": { "target_id": "wrapped_gifts", "action": "STANDING in FULL BODY — entire owl head-to-feet visible with comfortable margin, NOT cropped; owl height ~70% of the frame, placed in the RIGHT THIRD, standing among a few wrapped gifts and presenting one ribboned gift, leaving the left half open", "emotional_state": "warm, generous, inviting" }
    }
  ],
  "scene": {
    "location": "soft Pixar gift-nook spanning a wide 16:9 frame, FULL-BODY framing — Bubabu shown head-to-feet (NOT cropped) standing in the RIGHT THIRD with a few wrapped gifts beside him; the LEFT HALF and the LOWER THIRD held as clean open butter-cream gradient for Wolt's logo-badge + store-name + delivery-info overlay; soft sunburst behind the owl",
    "style_anchor": "Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and material textures, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.",
    "mise_en_scene": {
      "narrative_clutter": [
        "2-3 elegant wrapped gift boxes with ribbons + bows in Candy Pop colors clustered to the owl's side on the right (generic gifts, NO branded products, NO labels)",
        "a soft cream display ledge under the owl + gifts on the right",
        "soft low-contrast rainbow sunburst rays behind Bubabu on the right side",
        "a few small 3D candy confetti dots drifting in the upper-right (NO hearts)",
        "wide clean open butter-cream gradient filling the LEFT HALF for the Wolt logo + store-name overlay (no objects there)",
        "clean calm LOWER THIRD reserved for Wolt delivery-info overlay (no objects there)"
      ],
      "world_state": "new"
    },
    "lighting_advanced": { "type": "Pixar stylized bright warm studio-polish light — soft key front-right, gentle fill, soft rim glow", "volumetric_fog": 0 }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": false, "text": "", "placement": "" },
  "advanced": {
    "negative_prompt": [
      "no photoreal","no live-action","no DSLR/real-lens DOF","no film grain","no HDR cinema","no ARRI/Sony real-camera look","no realistic real owl/animal",
      "no second owl","no other owl toy near Bubabu","beak open","caramel/brown beak","brown ears","brown body",
      "heart eyes","hearts in confetti","glowing/LED eyes","no halo/godrays",
      "cropped owl","owl head or feet cut off","objects in the clean left half","objects in the lower band",
      "baked text/letters/wordmark/logos in image","watermark","multiple Bubabus","busy chaotic composition",
      "Cyrillic text","mtavruli capital Georgian","branded product packaging or readable labels"
    ]
  }
}
```

---

## §3 · PRODUCT PHOTO / MENU IMAGE - 2880×1620 (16:9)

**Role:** the Wolt menu-item photo - the **Bubabu plush toy itself** as a clean, appetizing-retail product hero. Product-forward, NOT lifestyle.
**Composition:** Bubabu centered on a clean butter-cream studio sweep, crisp product detail, at most ONE small gift box beside for scale; lots of clean breathing room.

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "wolt_product_menu_hero",
  "user_intent": "Wolt menu-item product photo — the Bubabu plush owl toy itself as a clean premium product hero on a butter-cream studio sweep; crisp, appetizing-retail clarity, product-forward, lots of breathing room.",
  "meta": { "aspect_ratio": "16:9", "quality": "3d_render_octane", "guidance_scale": 7.5, "seed": 483333 },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": { "palette_driver": "Candy Pop kids-brand palette — Bubabu Cyan #5BC0DE goggles (sacred), butter-cream #FFFAEB ground, soft lime/yellow/orange/coral/magenta accents" }
  },
  "subjects": [
    {
      "id": "Bubabu",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "round fluffy ball-shaped pure-WHITE plush owl — white fur on body, face AND top of head",
          "signature cyan-turquoise goggle eye-markings with cream inner ring + yellow eyelid arcs — SACRED, never remove/recolor",
          "small triangular BLACK closed beak + large round black eyes with single white highlight",
          "two tiny WHITE ear tufts; caramel-brown stubby wings + feet are the ONLY non-white parts"
        ],
        "heritage": "plush owl mascot — match uploaded 1.jpeg + 2.jpeg EXACTLY; reference photo is the source of truth"
      },
      "spatial_layout": { "coordinates": { "x": 0.5, "y": 0.5, "z_index": 2 }, "visual_weight": 0.72 },
      "appearance": {
        "age": "ageless plush mascot",
        "expression": "warm friendly idle wonder, gentle eye contact with viewer, soft calm pride, beak closed"
      },
      "interaction": { "target_id": "viewer", "action": "front-facing FULL BODY hero product pose — entire owl head-to-feet crisply visible with clean margin all around (NOT cropped, NOT extreme close-up), standing centered on a clean cream studio sweep, slight friendly forward-tilt, premium product presentation", "emotional_state": "calm, premium, inviting" }
    }
  ],
  "scene": {
    "location": "clean Pixar product-studio sweep — seamless butter-cream #FFFAEB → #FFF6CC gradient backdrop with a soft cream floor, Bubabu centered as the clean product hero with one small wrapped gift box beside him for scale; lots of clean breathing room, soft contact shadow under the owl",
    "style_anchor": "Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and material textures, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.",
    "mise_en_scene": {
      "narrative_clutter": [
        "one small elegant wrapped gift box with a ribbon beside the owl for scale (generic, NO branded product, NO label)",
        "soft cream studio floor with a gentle soft contact shadow under Bubabu",
        "very soft low-contrast sunburst glow behind the owl keeping him focal",
        "a few tiny 3D candy confetti dots in the far corners (NO hearts)",
        "wide clean empty butter-cream margin all around the product (no clutter)"
      ],
      "world_state": "new"
    },
    "lighting_advanced": { "type": "Pixar stylized bright warm studio-polish product light — soft key front, gentle fill, soft rim glow on top of head, clean catchlight", "volumetric_fog": 0 }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": false, "text": "", "placement": "" },
  "advanced": {
    "negative_prompt": [
      "no photoreal","no live-action","no DSLR/real-lens DOF","no film grain","no HDR cinema","no ARRI/Sony real-camera look","no realistic real owl/animal",
      "no second owl","no other owl toy near Bubabu","beak open","caramel/brown beak","brown ears","brown body",
      "heart eyes","hearts in confetti","glowing/LED eyes","no halo/godrays",
      "cropped owl","owl head or feet cut off","extreme close-up","busy cluttered background",
      "baked text/letters/wordmark/logos in image","watermark","multiple Bubabus",
      "Cyrillic text","mtavruli capital Georgian","branded product packaging or readable labels"
    ]
  }
}
```

---

## §4 · LOGO IMAGE - 1024×1024 (1:1)

**Role:** the Wolt store logo badge. Clean centered Bubabu mascot - **the round plush owl IS the brand mark, NO wordmark, NO text.** Must stay legible small (Wolt shows it as a small badge).
**Composition:** mirror the brand avatar - full body, centered with margin all around, NOT cropped/zoomed, recognizable at 96×96.

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "wolt_logo_badge",
  "user_intent": "Wolt store logo badge — Bubabu plush-owl mascot, FULL-BODY (head-to-feet) centered with margin on a clean butter-cream icon background; the owl IS the brand mark, no wordmark, recognizable at small badge size.",
  "meta": { "aspect_ratio": "1:1", "quality": "3d_render_octane", "guidance_scale": 7.5, "seed": 481024 },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": { "palette_driver": "Candy Pop kids-brand palette — Bubabu Cyan #5BC0DE goggles (sacred), butter-cream #FFFAEB ground, soft lime/yellow/orange/coral/magenta sunburst accents" }
  },
  "subjects": [
    {
      "id": "Bubabu",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "round fluffy ball-shaped pure-WHITE plush owl — white fur on body, face AND top of head",
          "signature cyan-turquoise circular goggle eye-markings (built-in aviator style) with cream inner ring + yellow eyelid arcs — SACRED brand mark, never remove/recolor",
          "small triangular BLACK beak (closed) + large round black eyes with single white highlight",
          "two tiny WHITE ear tufts; caramel-brown stubby wings + feet are the ONLY non-white parts"
        ],
        "heritage": "plush owl mascot — match uploaded 1.jpeg + 2.jpeg EXACTLY; reference photo is the source of truth"
      },
      "spatial_layout": { "coordinates": { "x": 0.5, "y": 0.5, "z_index": 1 }, "visual_weight": 0.7 },
      "appearance": {
        "age": "ageless plush mascot",
        "expression": "warm friendly idle wonder, gentle eye contact with viewer, soft bouncy waving-hello energy, beak closed"
      },
      "interaction": { "target_id": "viewer", "action": "front-facing FULL BODY — entire owl head-to-feet visible with comfortable margin all around (NOT cropped, NOT zoomed), standing centered, slight friendly forward-tilt, still recognizable at 96x96 badge size", "emotional_state": "warm, welcoming" }
    }
  ],
  "scene": {
    "location": "clean studio icon background — butter-cream radial gradient #FFFAEB → #FFF6CC, soft low-contrast Candy Pop sunburst rays behind the full-body owl",
    "style_anchor": "Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and material textures, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.",
    "mise_en_scene": {
      "narrative_clutter": [
        "soft low-contrast rainbow sunburst rays radiating from behind the head",
        "a few small 3D candy confetti dots drifting in the corners (NO hearts)",
        "gentle butter-cream vignette keeping the whole owl focal",
        "clean empty margin all around the owl so it reads as a centered badge",
        "no props, no gifts — the owl alone is the mark"
      ],
      "world_state": "new"
    },
    "lighting_advanced": { "type": "Pixar stylized bright warm studio-polish light — soft key front, gentle fill, soft rim glow on top of head", "volumetric_fog": 0 }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": false, "text": "", "placement": "" },
  "advanced": {
    "negative_prompt": [
      "no photoreal","no live-action","no DSLR/real-lens DOF","no film grain","no HDR cinema","no ARRI/Sony real-camera look","no realistic real owl/animal",
      "no second owl","no other owl toy","no eyewear-as-removable-object","beak open","caramel/brown beak","brown ears","brown body",
      "heart eyes","hearts in confetti","glowing/LED eyes","eye halo/godrays",
      "cropped owl","head or feet cut off","extreme close-up","zoomed-in owl filling the frame",
      "baked text/letters/wordmark/logos in image","watermark","multiple Bubabus",
      "Cyrillic text","mtavruli capital Georgian","religious symbols"
    ]
  }
}
```

---

## SELF-CHECK (all 4 SPECs)
- [ ] Owl FULL BODY head-to-feet, NOT cropped/zoomed · WHITE body+ears · cyan goggles intact · BLACK closed beak · caramel only wings/feet
- [ ] `text_rendering.enabled:false` - zero baked text, zero logo, zero wordmark in every SPEC
- [ ] Pixar-lock: `camera.model:"Pixar virtual"` only · no lut/Kelvin/aperture/lens-mm/SSS/hdr_mode · `style_anchor` present verbatim
- [ ] No second owl / other owl toy (third-party Musical-Owl conflation ban) · no labels/branded packaging
- [ ] No hearts (eyes or confetti) · no Cyrillic · no mtavruli
- [ ] Aspect: §1-§3 = 16:9 (→2880×1620) · §4 = 1:1 (→1024×1024)
- [ ] Wolt safe-zones: §1 clean bottom band · §2 clean left half + lower third · §4 legible at 96×96
- [ ] Upload `1.jpeg` + `2.jpeg` (NEVER `3.jpeg`) to every render
