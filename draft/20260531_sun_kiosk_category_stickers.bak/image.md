# image.md — Kiosk Category Stickers · DIE-CUT NB2 JSON SPECs

<!-- engine-override: PROMPT_ENGINE_DETAIL_FLOOR reason: Bubabu Pixar-lock drops photoreal fields (Kelvin/lens/aperture/lut/SSS/hdr/contrast/roughness/reflections); camera.model=Pixar virtual + style_anchor carry render intent. Die-cut format: text_rendering.enabled=true (text-bearing label, cover-style carve-out) + sticker_format/consistency_lock extension fields. -->

**Concept:** each category = a **die-cut vinyl sticker** — soft cloud-like organic shape (different per category on purpose) + thick glossy WHITE die-cut border + soft drop shadow, on a pure WHITE background. Unified by the white border + candy-pop palette + Bubabu owl + BUBABU.GE banner — NOT by an identical frame.
**Generator:** Nano Banana 2 — paste one JSON SPEC, one render. No reference image needed.
**Pre-save gates:** Pixar-lock (no photoreal fields, camera.model="Pixar virtual", style_anchor every SPEC) · text order Georgian headline → benefit → English · BUBABU.GE caps · zero Cyrillic · negative bans rectangle/straight-frame/photoreal.
**Text fallback:** if Georgian mis-renders 3×, set text_rendering.enabled:false, render icon+border only, overlay text in an editor.

---

## 1 — Bubabu AI Friend (HERO)

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_01_bubabu_ai_friend",
  "user_intent": "Die-cut hero sticker — Bubabu plush owl as the icon, magenta accent, cloud-like shape with white die-cut border.",
  "meta": { "aspect_ratio": "3:2", "quality": "stylized_3d_render", "seed": 81001, "guidance_scale": 7.5 },
  "sticker_format": { "type": "die-cut vinyl sticker", "shape": "soft cloud-like organic blob, unique to this category", "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette", "shadow": "soft drop shadow beneath like a real peel-and-stick sticker", "background": "pure solid white #FFFFFF" },
  "consistency_lock": { "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. Bottom ribbon banner ALWAYS reads BUBABU.GE in white capitals, never lowercase. Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations." },
  "sequence_logic": { "shot_type": "master_shot", "color_grading": { "palette_driver": "candy-pop kids-commercial on pure white background, magenta #FF1F8F accent with cyan #5BC0DE echo, soft Pixar 3D" } },
  "subjects": [
    {
      "id": "bubabu_owl_hero",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": ["round fluffy white plush owl mascot", "cyan-turquoise circular eye-goggle markings with cream inner rings", "small black closed triangle beak", "caramel-brown stubby wings", "soft light-grey outline so the white body reads on the white sticker"],
        "heritage": "Bubabu plush mascot, cyan goggles, black closed beak"
      },
      "spatial_layout": { "coordinates": { "x": 0.24, "y": 0.46, "z_index": 2 }, "visual_weight": 0.9 },
      "appearance": { "age": "plush toy", "expression": "warm friendly, eyes calm and open, beak closed" },
      "interaction": { "target_id": "environment", "action": "the hero icon on the left of the die-cut sticker", "emotional_state": "warm and inviting" }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": { "narrative_clutter": ["thick glossy white die-cut border around the whole shape", "soft drop shadow beneath the sticker", "magenta ribbon banner at the bottom carrying the wordmark", "tiny soft cyan sparkle near the goggles", "soft cloud-like organic silhouette", "matte candy-pop finish"], "world_state": "new" },
    "lighting_advanced": { "type": "Pixar stylized soft flat product light (NOT photoreal cinema)" }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": true, "text": "Georgian headline: ბუბაბუ AI მეგობარი | Georgian benefit: საუბრობს • სწავლობს • თამაშობს | English subtitle: Bubabu AI Friend | Bottom ribbon banner: BUBABU.GE", "placement": "Bubabu owl on the left; text stack on the right top-to-bottom — (1) Georgian headline in magenta, (2) Georgian benefit row with round dots, (3) small English subtitle; magenta ribbon banner across the bottom with BUBABU.GE in white capitals" },
  "advanced": { "negative_prompt": ["no rectangle frame", "no straight hard border", "no photoreal", "no live-action", "no DSLR", "no real-lens DOF", "no film grain", "no HDR cinema", "no ARRI", "no Sony", "no Sigma", "no Canon", "no realistic owl", "no glow or LED on goggles", "no heart-eyes owl", "no open beak", "no lowercase bubabu.ge", "no uppercase Georgian mtavruli", "no Cyrillic letters", "no gibberish text", "no watermark", "no busy texture", "no neon", "no dark moody mood"] }
}
```

---

## 2 — Magnetic Toys

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_02_magnetic_toys",
  "user_intent": "Die-cut sticker for magnetic building toys — magnetic balls/blocks icon, cyan accent, cloud shape with white die-cut border.",
  "meta": { "aspect_ratio": "3:2", "quality": "stylized_3d_render", "seed": 81002, "guidance_scale": 7.5 },
  "sticker_format": { "type": "die-cut vinyl sticker", "shape": "soft cloud-like organic blob, unique to this category", "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette", "shadow": "soft drop shadow beneath like a real peel-and-stick sticker", "background": "pure solid white #FFFFFF" },
  "consistency_lock": { "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. Bottom ribbon banner ALWAYS reads BUBABU.GE in white capitals, never lowercase. Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations." },
  "sequence_logic": { "shot_type": "master_shot", "color_grading": { "palette_driver": "candy-pop kids-commercial on pure white background, bright cyan #5BC0DE accent, soft Pixar 3D" } },
  "subjects": [
    {
      "id": "magnetic_icon",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["three glossy-soft candy-pop magnetic balls and rounded building blocks", "blocks snapping together at a corner", "tiny soft sparkle at the join"], "heritage": "generic candy-pop 3D toy icon" },
      "spatial_layout": { "coordinates": { "x": 0.24, "y": 0.46, "z_index": 2 }, "visual_weight": 0.8 },
      "appearance": { "age": "toy", "expression": "playful and constructive" },
      "interaction": { "target_id": "environment", "action": "magnetic balls and blocks clicking together as the left icon", "emotional_state": "playful" }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["round fluffy white plush owl", "cyan-turquoise circular goggle markings", "black closed triangle beak", "soft light-grey outline so it reads on white"], "heritage": "Bubabu plush mascot" },
      "spatial_layout": { "coordinates": { "x": 0.9, "y": 0.82, "z_index": 3 }, "visual_weight": 0.12 },
      "appearance": { "age": "plush toy", "expression": "calm friendly, beak closed" },
      "interaction": { "target_id": "environment", "action": "tiny Bubabu owl peeking from the bottom-right", "emotional_state": "friendly" }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": { "narrative_clutter": ["thick glossy white die-cut border around the whole shape", "soft drop shadow beneath the sticker", "cyan ribbon banner at the bottom carrying the wordmark", "tiny soft sparkle accent", "soft cloud-like organic silhouette", "matte candy-pop finish"], "world_state": "new" },
    "lighting_advanced": { "type": "Pixar stylized soft flat product light (NOT photoreal cinema)" }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": true, "text": "Georgian headline: მაგნიტური სათამაშოები | Georgian benefit: ააწყე • შექმენი • ისწავლე | English subtitle: Magnetic Toys | Bottom ribbon banner: BUBABU.GE", "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in cyan, (2) Georgian benefit row with round dots, (3) small English subtitle; cyan ribbon banner across the bottom with BUBABU.GE in white capitals; tiny Bubabu owl bottom-right" },
  "advanced": { "negative_prompt": ["no rectangle frame", "no straight hard border", "no photoreal", "no live-action", "no DSLR", "no real-lens DOF", "no film grain", "no HDR cinema", "no ARRI", "no Sony", "no Sigma", "no Canon", "no realistic owl", "no glow on goggles", "no lowercase bubabu.ge", "no uppercase Georgian mtavruli", "no Cyrillic letters", "no gibberish text", "no watermark", "no busy texture", "no neon", "no dark moody mood", "no metal magnet hazard look"] }
}
```

---

## 3 — Smart Learning Gifts

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_03_smart_learning_gifts",
  "user_intent": "Die-cut sticker for learning gifts — glowing bulb + open book icon, lime accent, cloud shape with white die-cut border.",
  "meta": { "aspect_ratio": "3:2", "quality": "stylized_3d_render", "seed": 81003, "guidance_scale": 7.5 },
  "sticker_format": { "type": "die-cut vinyl sticker", "shape": "soft cloud-like organic blob, unique to this category", "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette", "shadow": "soft drop shadow beneath like a real peel-and-stick sticker", "background": "pure solid white #FFFFFF" },
  "consistency_lock": { "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. Bottom ribbon banner ALWAYS reads BUBABU.GE in white capitals, never lowercase. Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations." },
  "sequence_logic": { "shot_type": "master_shot", "color_grading": { "palette_driver": "candy-pop kids-commercial on pure white background, bright lime #84CC16 accent, soft Pixar 3D" } },
  "subjects": [
    {
      "id": "learning_icon",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["friendly soft 3D glowing light bulb", "small open book beneath the bulb", "tiny warm idea-sparkle"], "heritage": "generic candy-pop 3D learning icon" },
      "spatial_layout": { "coordinates": { "x": 0.24, "y": 0.46, "z_index": 2 }, "visual_weight": 0.8 },
      "appearance": { "age": "icon", "expression": "bright and optimistic" },
      "interaction": { "target_id": "environment", "action": "bulb glowing above an open book as the left icon", "emotional_state": "curious" }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["round fluffy white plush owl", "cyan-turquoise circular goggle markings", "black closed triangle beak", "soft light-grey outline so it reads on white"], "heritage": "Bubabu plush mascot" },
      "spatial_layout": { "coordinates": { "x": 0.9, "y": 0.82, "z_index": 3 }, "visual_weight": 0.12 },
      "appearance": { "age": "plush toy", "expression": "calm friendly, beak closed" },
      "interaction": { "target_id": "environment", "action": "tiny Bubabu owl peeking from the bottom-right", "emotional_state": "friendly" }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": { "narrative_clutter": ["thick glossy white die-cut border around the whole shape", "soft drop shadow beneath the sticker", "lime ribbon banner at the bottom carrying the wordmark", "tiny soft idea-sparkle accent", "soft cloud-like organic silhouette", "matte candy-pop finish"], "world_state": "new" },
    "lighting_advanced": { "type": "Pixar stylized soft flat product light (NOT photoreal cinema)" }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": true, "text": "Georgian headline: სასწავლო საჩუქრები | Georgian benefit: ისწავლე თამაშით | English subtitle: Smart Learning Gifts | Bottom ribbon banner: BUBABU.GE", "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in lime, (2) Georgian benefit line, (3) small English subtitle; lime ribbon banner across the bottom with BUBABU.GE in white capitals; tiny Bubabu owl bottom-right" },
  "advanced": { "negative_prompt": ["no rectangle frame", "no straight hard border", "no photoreal", "no live-action", "no DSLR", "no real-lens DOF", "no film grain", "no HDR cinema", "no ARRI", "no Sony", "no Sigma", "no Canon", "no realistic owl", "no glow on goggles", "no lowercase bubabu.ge", "no uppercase Georgian mtavruli", "no Cyrillic letters", "no gibberish text", "no watermark", "no busy texture", "no neon", "no dark moody mood"] }
}
```

---

## 4 — STEM & Robotics

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_04_stem_robotics",
  "user_intent": "Die-cut sticker for STEM and robotics — friendly robot head + gear icon, deep teal-cyan accent, cloud shape with white die-cut border.",
  "meta": { "aspect_ratio": "3:2", "quality": "stylized_3d_render", "seed": 81004, "guidance_scale": 7.5 },
  "sticker_format": { "type": "die-cut vinyl sticker", "shape": "soft cloud-like organic blob, unique to this category", "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette", "shadow": "soft drop shadow beneath like a real peel-and-stick sticker", "background": "pure solid white #FFFFFF" },
  "consistency_lock": { "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. Bottom ribbon banner ALWAYS reads BUBABU.GE in white capitals, never lowercase. Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations." },
  "sequence_logic": { "shot_type": "master_shot", "color_grading": { "palette_driver": "candy-pop kids-commercial on pure white background, deep teal-cyan #2BA3C7 accent (reads tech), soft Pixar 3D" } },
  "subjects": [
    {
      "id": "robot_icon",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["adorable rounded soft 3D friendly robot head with big friendly eyes", "small soft gear beside it", "rounded antenna with a soft dot"], "heritage": "generic candy-pop 3D friendly-robot icon" },
      "spatial_layout": { "coordinates": { "x": 0.24, "y": 0.46, "z_index": 2 }, "visual_weight": 0.8 },
      "appearance": { "age": "icon", "expression": "friendly and curious" },
      "interaction": { "target_id": "environment", "action": "cute robot head with a soft gear as the left icon", "emotional_state": "friendly" }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["round fluffy white plush owl", "cyan-turquoise circular goggle markings", "black closed triangle beak", "soft light-grey outline so it reads on white"], "heritage": "Bubabu plush mascot" },
      "spatial_layout": { "coordinates": { "x": 0.9, "y": 0.82, "z_index": 3 }, "visual_weight": 0.12 },
      "appearance": { "age": "plush toy", "expression": "calm friendly, beak closed" },
      "interaction": { "target_id": "environment", "action": "tiny Bubabu owl peeking from the bottom-right", "emotional_state": "friendly" }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": { "narrative_clutter": ["thick glossy white die-cut border around the whole shape", "soft drop shadow beneath the sticker", "deep teal-cyan ribbon banner at the bottom carrying the wordmark", "tiny soft gear-spark accent", "soft cloud-like organic silhouette", "matte candy-pop finish"], "world_state": "new" },
    "lighting_advanced": { "type": "Pixar stylized soft flat product light (NOT photoreal cinema)" }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": true, "text": "Headline (Latin + Georgian): STEM & რობოტიკა | Georgian benefit: ტექნოლოგია • ლოგიკა • აღმოჩენა | English subtitle: STEM & Robotics | Bottom ribbon banner: BUBABU.GE", "placement": "icon on the left; text stack on the right top-to-bottom — (1) headline with STEM in clean Latin and რობოტიკა in Georgian, deep teal-cyan, (2) Georgian benefit row with round dots, (3) small English subtitle; deep teal-cyan ribbon banner across the bottom with BUBABU.GE in white capitals; tiny Bubabu owl bottom-right" },
  "advanced": { "negative_prompt": ["no rectangle frame", "no straight hard border", "no photoreal", "no live-action", "no DSLR", "no real-lens DOF", "no film grain", "no HDR cinema", "no ARRI", "no Sony", "no Sigma", "no Canon", "no realistic owl", "no cold industrial robot", "no glow on goggles", "no lowercase bubabu.ge", "no uppercase Georgian mtavruli", "no Cyrillic letters", "no gibberish text", "no watermark", "no neon", "no dark moody mood"] }
}
```

---

## 5 — Creative Gifts

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_05_creative_gifts",
  "user_intent": "Die-cut sticker for creative/art kits — paint brush + palette icon, orange accent, cloud shape with white die-cut border.",
  "meta": { "aspect_ratio": "3:2", "quality": "stylized_3d_render", "seed": 81005, "guidance_scale": 7.5 },
  "sticker_format": { "type": "die-cut vinyl sticker", "shape": "soft cloud-like organic blob, unique to this category", "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette", "shadow": "soft drop shadow beneath like a real peel-and-stick sticker", "background": "pure solid white #FFFFFF" },
  "consistency_lock": { "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. Bottom ribbon banner ALWAYS reads BUBABU.GE in white capitals, never lowercase. Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations." },
  "sequence_logic": { "shot_type": "master_shot", "color_grading": { "palette_driver": "candy-pop kids-commercial on pure white background, bright orange #FF9F1C accent, soft Pixar 3D" } },
  "subjects": [
    {
      "id": "creative_icon",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["chunky soft 3D paint brush", "rounded candy-pop color palette", "tiny burst of creative sparkle"], "heritage": "generic candy-pop 3D creative-art icon" },
      "spatial_layout": { "coordinates": { "x": 0.24, "y": 0.46, "z_index": 2 }, "visual_weight": 0.8 },
      "appearance": { "age": "icon", "expression": "joyful and artistic" },
      "interaction": { "target_id": "environment", "action": "paint brush across a palette as the left icon", "emotional_state": "creative" }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["round fluffy white plush owl", "cyan-turquoise circular goggle markings", "black closed triangle beak", "soft light-grey outline so it reads on white"], "heritage": "Bubabu plush mascot" },
      "spatial_layout": { "coordinates": { "x": 0.9, "y": 0.82, "z_index": 3 }, "visual_weight": 0.12 },
      "appearance": { "age": "plush toy", "expression": "calm friendly, beak closed" },
      "interaction": { "target_id": "environment", "action": "tiny Bubabu owl peeking from the bottom-right", "emotional_state": "friendly" }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": { "narrative_clutter": ["thick glossy white die-cut border around the whole shape", "soft drop shadow beneath the sticker", "orange ribbon banner at the bottom carrying the wordmark", "tiny soft creative sparkle accent", "soft cloud-like organic silhouette", "matte candy-pop finish"], "world_state": "new" },
    "lighting_advanced": { "type": "Pixar stylized soft flat product light (NOT photoreal cinema)" }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": true, "text": "Georgian headline: კრეატიული საჩუქრები | Georgian benefit: დახატე • შექმენი • გააფერადე | English subtitle: Creative Gifts | Bottom ribbon banner: BUBABU.GE", "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in orange, (2) Georgian benefit row with round dots, (3) small English subtitle; orange ribbon banner across the bottom with BUBABU.GE in white capitals; tiny Bubabu owl bottom-right" },
  "advanced": { "negative_prompt": ["no rectangle frame", "no straight hard border", "no photoreal", "no live-action", "no DSLR", "no real-lens DOF", "no film grain", "no HDR cinema", "no ARRI", "no Sony", "no Sigma", "no Canon", "no realistic owl", "no glow on goggles", "no lowercase bubabu.ge", "no uppercase Georgian mtavruli", "no Cyrillic letters", "no gibberish text", "no watermark", "no busy texture", "no neon", "no dark moody mood"] }
}
```

---

## 6 — Fun Gifts

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_06_fun_gifts",
  "user_intent": "Die-cut sticker for fun/impulse items — wrapped gift + star + confetti icon, coral accent, cloud shape with white die-cut border.",
  "meta": { "aspect_ratio": "3:2", "quality": "stylized_3d_render", "seed": 81006, "guidance_scale": 7.5 },
  "sticker_format": { "type": "die-cut vinyl sticker", "shape": "soft cloud-like organic blob, unique to this category", "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette", "shadow": "soft drop shadow beneath like a real peel-and-stick sticker", "background": "pure solid white #FFFFFF" },
  "consistency_lock": { "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. Bottom ribbon banner ALWAYS reads BUBABU.GE in white capitals, never lowercase. Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations." },
  "sequence_logic": { "shot_type": "master_shot", "color_grading": { "palette_driver": "candy-pop kids-commercial on pure white background, bright coral #FF6B6B accent, soft Pixar 3D" } },
  "subjects": [
    {
      "id": "fun_icon",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["cheerful small soft 3D wrapped gift box with a bouncy bow", "a tiny star", "a couple of confetti dots"], "heritage": "generic candy-pop 3D gift-box icon" },
      "spatial_layout": { "coordinates": { "x": 0.24, "y": 0.46, "z_index": 2 }, "visual_weight": 0.8 },
      "appearance": { "age": "icon", "expression": "cheerful and playful" },
      "interaction": { "target_id": "environment", "action": "small wrapped gift with a star as the left icon", "emotional_state": "joyful" }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["round fluffy white plush owl", "cyan-turquoise circular goggle markings", "black closed triangle beak", "soft light-grey outline so it reads on white"], "heritage": "Bubabu plush mascot" },
      "spatial_layout": { "coordinates": { "x": 0.9, "y": 0.82, "z_index": 3 }, "visual_weight": 0.12 },
      "appearance": { "age": "plush toy", "expression": "calm friendly, beak closed" },
      "interaction": { "target_id": "environment", "action": "tiny Bubabu owl peeking from the bottom-right", "emotional_state": "friendly" }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": { "narrative_clutter": ["thick glossy white die-cut border around the whole shape", "soft drop shadow beneath the sticker", "coral ribbon banner at the bottom carrying the wordmark", "tiny soft happy star accent", "soft cloud-like organic silhouette", "matte candy-pop finish"], "world_state": "new" },
    "lighting_advanced": { "type": "Pixar stylized soft flat product light (NOT photoreal cinema)" }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": true, "text": "Georgian headline: სახალისო საჩუქრები | Georgian benefit: პატარა სიხარული | English subtitle: Fun Gifts | Bottom ribbon banner: BUBABU.GE", "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in coral, (2) Georgian benefit line, (3) small English subtitle; coral ribbon banner across the bottom with BUBABU.GE in white capitals; tiny Bubabu owl bottom-right" },
  "advanced": { "negative_prompt": ["no rectangle frame", "no straight hard border", "no photoreal", "no live-action", "no DSLR", "no real-lens DOF", "no film grain", "no HDR cinema", "no ARRI", "no Sony", "no Sigma", "no Canon", "no realistic owl", "no glow on goggles", "no lowercase bubabu.ge", "no uppercase Georgian mtavruli", "no Cyrillic letters", "no gibberish text", "no watermark", "no busy texture", "no neon", "no dark moody mood"] }
}
```

---

## 7 — Gift Sets

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_07_gift_sets",
  "user_intent": "Die-cut sticker for ready-made gift bundles — stacked wrapped gifts + bow icon, warm yellow accent, cloud shape with white die-cut border.",
  "meta": { "aspect_ratio": "3:2", "quality": "stylized_3d_render", "seed": 81007, "guidance_scale": 7.5 },
  "sticker_format": { "type": "die-cut vinyl sticker", "shape": "soft cloud-like organic blob, unique to this category", "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette", "shadow": "soft drop shadow beneath like a real peel-and-stick sticker", "background": "pure solid white #FFFFFF" },
  "consistency_lock": { "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. Bottom ribbon banner ALWAYS reads BUBABU.GE in white capitals, never lowercase. Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations." },
  "sequence_logic": { "shot_type": "master_shot", "color_grading": { "palette_driver": "candy-pop kids-commercial on pure white background, warm yellow #FFEB3B accent (headline in warm gold for readability), soft Pixar 3D" } },
  "subjects": [
    {
      "id": "giftset_icon",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["neat stack of two to three soft 3D wrapped gift boxes", "one elegant ribbon bow tying the stack", "warm yellow coral and cyan boxes"], "heritage": "generic candy-pop 3D gift-bundle icon" },
      "spatial_layout": { "coordinates": { "x": 0.24, "y": 0.46, "z_index": 2 }, "visual_weight": 0.8 },
      "appearance": { "age": "icon", "expression": "premium and warm" },
      "interaction": { "target_id": "environment", "action": "stacked wrapped gifts with a bow as the left icon", "emotional_state": "generous" }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["round fluffy white plush owl", "cyan-turquoise circular goggle markings", "black closed triangle beak", "soft light-grey outline so it reads on white"], "heritage": "Bubabu plush mascot" },
      "spatial_layout": { "coordinates": { "x": 0.9, "y": 0.82, "z_index": 3 }, "visual_weight": 0.12 },
      "appearance": { "age": "plush toy", "expression": "calm friendly, beak closed" },
      "interaction": { "target_id": "environment", "action": "tiny Bubabu owl peeking from the bottom-right", "emotional_state": "friendly" }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": { "narrative_clutter": ["thick glossy white die-cut border around the whole shape", "soft drop shadow beneath the sticker", "warm yellow ribbon banner at the bottom carrying the wordmark", "tiny soft ribbon-shine accent", "soft cloud-like organic silhouette", "matte candy-pop finish"], "world_state": "new" },
    "lighting_advanced": { "type": "Pixar stylized soft flat product light (NOT photoreal cinema)" }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": true, "text": "Georgian headline: საჩუქრის ნაკრებები | Georgian benefit: მზად არის საჩუქრად | English subtitle: Gift Sets | Bottom ribbon banner: BUBABU.GE", "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in warm gold with a soft darker outline for contrast, (2) Georgian benefit line, (3) small English subtitle; warm yellow ribbon banner across the bottom with BUBABU.GE in white capitals; tiny Bubabu owl bottom-right" },
  "advanced": { "negative_prompt": ["no rectangle frame", "no straight hard border", "no photoreal", "no live-action", "no DSLR", "no real-lens DOF", "no film grain", "no HDR cinema", "no ARRI", "no Sony", "no Sigma", "no Canon", "no realistic owl", "no glow on goggles", "no metallic gold", "no lowercase bubabu.ge", "no uppercase Georgian mtavruli", "no Cyrillic letters", "no gibberish text", "no watermark", "no neon", "no dark moody mood"] }
}
```

---

## 8 — Screen-Free Gifts

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_08_screen_free_gifts",
  "user_intent": "Die-cut brand-philosophy sticker — happy child face + heart + gentle screen-free badge, cyan + lime accent, cloud shape with white die-cut border.",
  "meta": { "aspect_ratio": "3:2", "quality": "stylized_3d_render", "seed": 81008, "guidance_scale": 7.5 },
  "sticker_format": { "type": "die-cut vinyl sticker", "shape": "soft cloud-like organic blob, unique to this category", "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette", "shadow": "soft drop shadow beneath like a real peel-and-stick sticker", "background": "pure solid white #FFFFFF" },
  "consistency_lock": { "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. Bottom ribbon banner ALWAYS reads BUBABU.GE in white capitals, never lowercase. Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations." },
  "sequence_logic": { "shot_type": "master_shot", "color_grading": { "palette_driver": "candy-pop kids-commercial on pure white background, cyan #5BC0DE and lime #84CC16 duo accent, soft Pixar 3D" } },
  "subjects": [
    {
      "id": "screenfree_icon",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["happy soft 3D Pixar-stylized child face with large stylized eyes, toy-like proportions", "small warm heart beside the face", "tiny gentle screen-free badge — a rounded device shape with a soft diagonal line, positive not alarming"], "heritage": "Pixar-stylized 3D child-face icon, NOT a realistic child" },
      "spatial_layout": { "coordinates": { "x": 0.24, "y": 0.46, "z_index": 2 }, "visual_weight": 0.8 },
      "appearance": { "age": "Pixar stylized child icon", "expression": "happy and reassured" },
      "interaction": { "target_id": "environment", "action": "smiling child face with a heart as the left icon", "emotional_state": "safe and warm" }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": { "bone_structure": "delicate", "persistent_features": ["round fluffy white plush owl", "cyan-turquoise circular goggle markings", "black closed triangle beak", "soft light-grey outline so it reads on white"], "heritage": "Bubabu plush mascot" },
      "spatial_layout": { "coordinates": { "x": 0.9, "y": 0.82, "z_index": 3 }, "visual_weight": 0.12 },
      "appearance": { "age": "plush toy", "expression": "calm friendly, beak closed" },
      "interaction": { "target_id": "environment", "action": "tiny Bubabu owl peeking from the bottom-right", "emotional_state": "friendly" }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": { "narrative_clutter": ["thick glossy white die-cut border around the whole shape", "soft drop shadow beneath the sticker", "cyan ribbon banner with a lime edge at the bottom carrying the wordmark", "tiny soft warm heart accent", "soft cloud-like organic silhouette", "matte candy-pop finish"], "world_state": "new" },
    "lighting_advanced": { "type": "Pixar stylized soft flat product light (NOT photoreal cinema)" }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": true, "text": "Georgian headline: ეკრანის გარეშე | Georgian benefit: უსაფრთხო თამაში და სწავლა | English subtitle: Screen-Free Gifts | Bottom ribbon banner: BUBABU.GE", "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in cyan, (2) Georgian benefit line, (3) small English subtitle; cyan-with-lime ribbon banner across the bottom with BUBABU.GE in white capitals; tiny Bubabu owl bottom-right" },
  "advanced": { "negative_prompt": ["no rectangle frame", "no straight hard border", "no photoreal", "no live-action", "no DSLR", "no real-lens DOF", "no film grain", "no HDR cinema", "no ARRI", "no Sony", "no Sigma", "no Canon", "no realistic owl", "no realistic child", "no photoreal kid", "no glow on goggles", "no lowercase bubabu.ge", "no uppercase Georgian mtavruli", "no Cyrillic letters", "no gibberish text", "no watermark", "no dark moody mood"] }
}
```

---

## Paste protocol
1. Copy one JSON block (full outer braces).
2. Paste into Nano Banana 2 → render (no reference image needed).
3. Cut along the white die-cut border (kiss-cut vinyl). Shelf placement + colors → `print_spec.md`.
4. Georgian text broken after 3 tries → set `text_rendering.enabled: false`, render icon + border only, overlay text in an editor.
