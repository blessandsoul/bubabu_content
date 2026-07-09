# image.md - Kiosk Category Stickers · DIE-CUT NB2 JSON SPECs

<!-- engine-override: PROMPT_ENGINE_DETAIL_FLOOR reason: Bubabu Pixar-lock drops photoreal fields (Kelvin/lens/aperture/lut/SSS/hdr/contrast/roughness/reflections); camera.model=Pixar virtual + style_anchor carry render intent. Die-cut format: text_rendering.enabled=true (text-bearing label, cover-style carve-out) + sticker_format/consistency_lock extension fields. -->

**Concept:** each category = a **die-cut vinyl sticker** - soft cloud-like organic shape (different per category on purpose) + thick glossy WHITE die-cut border + soft drop shadow, on a pure WHITE background. Unified by the white border + candy-pop palette + Bubabu owl + BUBABU.GE banner - NOT by an identical frame.
**Generator:** Nano Banana 2 - paste one JSON SPEC. **Every sticker render MUST upload `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg` (Bubabu plush refs, MANDATORY) per kiosk unification 2026-05-31** - text-only DNA produces drift between 8 separate renders. Refs lock Bubabu visual identity across all 8 stickers.
**Pre-save gates:** Pixar-lock (no photoreal fields, camera.model="Pixar virtual", style_anchor every SPEC) · text order Georgian headline → benefit → English · BUBABU.GE caps · zero Cyrillic · negative bans rectangle/straight-frame/photoreal.
**Text fallback:** if Georgian mis-renders 3×, set text_rendering.enabled:false, render icon+border only, overlay text in an editor.

---

## 1 - Bubabu AI Friend (HERO)

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_01_bubabu_ai_friend",
  "user_intent": "Die-cut hero sticker — Bubabu plush owl as the icon, magenta accent, cloud-like shape with white die-cut border.",
  "meta": {
    "aspect_ratio": "3:2",
    "quality": "stylized_3d_render",
    "seed": 81001,
    "guidance_scale": 7.5
  },
  "sticker_format": {
    "type": "die-cut vinyl sticker",
    "shape": "soft cloud-like organic blob, unique to this category",
    "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette",
    "shadow": "soft drop shadow beneath like a real peel-and-stick sticker",
    "background": "pure solid white #FFFFFF"
  },
  "consistency_lock": {
    "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. BUBABU.GE always inside butter-cream rounded pill at bottom-center with deep magenta uppercase text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation, NO lowercase bubabu.ge). Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations. Bubabu master pose + DNA + Candy Pop 6-color rainbow arc behind — IDENTICAL visual across all 8 stickers (pose + appearance + rainbow position + colors LOCKED). BUBABU.GE butter-cream pill at bottom-center with magenta text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation)."
  },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": {
      "palette_driver": "candy-pop kids-commercial on pure white background, magenta #FF1F8F accent with cyan #5BC0DE echo, soft Pixar 3D"
    }
  },
  "subjects": [
    {
      "id": "bubabu_rainbow_arc",
      "character_dna": {
        "bone_structure": "candy_pop_6color_rainbow_arc_behind_bubabu",
        "persistent_features": [
          "small soft Candy Pop 6-color rainbow arc directly behind Bubabu's body",
          "scaled to approximately 120% of Bubabu's body radius (sized to Bubabu)",
          "color stripes in classic rainbow order: cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, orange #FF9F1C, coral #FF6B6B",
          "soft kid-pastel saturation, slightly tilted 5-10 degrees behind Bubabu's right shoulder",
          "matte flat shading — NO body-glow on Bubabu, NO rainbow shine spilling onto Bubabu's fur, NO halo effect"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — signature visual locked across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 1
        },
        "visual_weight": 0.36
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "bubabu",
        "action": "small Candy Pop rainbow arc rendered directly behind Bubabu's body, sized to him, signature brand visual",
        "emotional_state": "decorative_brand_signature"
      }
    },
    {
      "id": "bubabu_owl_hero",
      "character_dna": {
        "bone_structure": "plush round owl mascot (Bubabu — visual locked per kiosk unification)",
        "persistent_features": [
          "match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1",
          "round fluffy white plush owl mascot, ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring around each eye",
          "small triangular BLACK closed beak between the goggles (brand lock — STAYS CLOSED)",
          "caramel-brown stubby wings + caramel-brown feet with three orange toes each",
          "pure white ear tufts SAME white color as body fur",
          "soft light-grey outline so the white body reads on the white sticker background"
        ],
        "heritage": "Bubabu plush mascot, locked appearance + pose + rainbow per kiosk unification 2026-05-31 — IDENTICAL visual identity across all 8 stickers, only scale flexes (hero=big, badge=small)"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 2
        },
        "visual_weight": 0.9
      },
      "appearance": {
        "age": "plush toy",
        "expression": "serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed — IDENTICAL across all 8 stickers"
      },
      "interaction": {
        "target_id": "environment",
        "action": "the hero icon on the left of the die-cut sticker",
        "emotional_state": "warm and inviting (master expression locked across all 8 stickers)"
      }
    },
    {
      "id": "bubabu_ge_domain_pill",
      "character_dna": {
        "bone_structure": "butter_cream_rounded_pill_with_magenta_brand_text",
        "persistent_features": [
          "soft rounded pill capsule, butter-cream gradient #FFFAEB top fading to #FFF6CC bottom (matches Bubabu cover override + ad cover aesthetic)",
          "pill radius equals pill height divided by 2 (soft rounded ends, no harsh corners)",
          "BUBABU.GE uppercase text inside the pill, color = deep magenta #FF1F8F (brand primary, max contrast on butter-cream)",
          "flat matte shading — NO drop shadow, NO border outline, NO gradient on text",
          "centered horizontally, bottom-third of sticker frame — IDENTICAL position across all 8 stickers"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — domain pill IDENTICAL across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.5,
          "y": -0.4,
          "z_index": 4
        },
        "visual_weight": 0.25
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "environment",
        "action": "butter-cream rounded pill at bottom-center carrying BUBABU.GE in deep magenta uppercase text",
        "emotional_state": "brand_signature"
      }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": {
      "narrative_clutter": [
        "thick glossy white die-cut border around the whole shape",
        "soft drop shadow beneath the sticker",
        "soft Candy Pop 6-color rainbow arc directly behind Bubabu (signature brand visual, scaled to Bubabu, NO body-glow)",
        "butter-cream rounded pill at the bottom-center carrying BUBABU.GE in deep magenta uppercase text (unified across all 8 stickers per kiosk unification 2026-05-31)",
        "tiny soft cyan sparkle near the goggles",
        "soft cloud-like organic silhouette",
        "matte candy-pop finish"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "type": "Pixar stylized soft flat product light (NOT photoreal cinema)"
    }
  },
  "technical": {
    "camera": {
      "model": "Pixar virtual"
    }
  },
  "text_rendering": {
    "enabled": true,
    "text": "Georgian headline: ბუბაბუ AI მეგობარი | Georgian benefit: საუბრობს • სწავლობს • თამაშობს | English subtitle: Bubabu AI Friend | Bottom ribbon banner: BUBABU.GE",
    "placement": "Bubabu owl on the left; text stack on the right top-to-bottom — (1) Georgian headline in magenta, (2) Georgian benefit row with round dots, (3) small English subtitle; butter-cream rounded pill at the bottom-center with BUBABU.GE in deep magenta uppercase text (UNIFIED across all 8 stickers — no per-category ribbon)"
  },
  "advanced": {
    "negative_prompt": [
      "no rectangle frame",
      "no straight hard border",
      "no photoreal",
      "no live-action",
      "no DSLR",
      "no real-lens DOF",
      "no film grain",
      "no HDR cinema",
      "no ARRI",
      "no Sony",
      "no Sigma",
      "no Canon",
      "no realistic owl",
      "no glow or LED on goggles",
      "no heart-eyes owl",
      "no open beak",
      "no lowercase bubabu.ge",
      "no uppercase Georgian mtavruli",
      "no Cyrillic letters",
      "no gibberish text",
      "no watermark",
      "no busy texture",
      "no neon",
      "no dark moody mood"
    ]
  }
}
```

---

## 2 - Magnetic Toys

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_02_magnetic_toys",
  "user_intent": "Die-cut sticker for magnetic building toys — magnetic balls/blocks icon, cyan accent, cloud shape with white die-cut border.",
  "meta": {
    "aspect_ratio": "3:2",
    "quality": "stylized_3d_render",
    "seed": 81002,
    "guidance_scale": 7.5
  },
  "sticker_format": {
    "type": "die-cut vinyl sticker",
    "shape": "soft cloud-like organic blob, unique to this category",
    "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette",
    "shadow": "soft drop shadow beneath like a real peel-and-stick sticker",
    "background": "pure solid white #FFFFFF"
  },
  "consistency_lock": {
    "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. BUBABU.GE always inside butter-cream rounded pill at bottom-center with deep magenta uppercase text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation, NO lowercase bubabu.ge). Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations. Bubabu master pose + DNA + Candy Pop 6-color rainbow arc behind — IDENTICAL visual across all 8 stickers (pose + appearance + rainbow position + colors LOCKED). BUBABU.GE butter-cream pill at bottom-center with magenta text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation)."
  },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": {
      "palette_driver": "candy-pop kids-commercial on pure white background, bright cyan #5BC0DE accent, soft Pixar 3D"
    }
  },
  "subjects": [
    {
      "id": "magnetic_icon",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "three glossy-soft candy-pop magnetic balls and rounded building blocks",
          "blocks snapping together at a corner",
          "tiny soft sparkle at the join"
        ],
        "heritage": "generic candy-pop 3D toy icon"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 2
        },
        "visual_weight": 0.8
      },
      "appearance": {
        "age": "toy",
        "expression": "playful and constructive"
      },
      "interaction": {
        "target_id": "environment",
        "action": "magnetic balls and blocks clicking together as the left icon",
        "emotional_state": "playful"
      }
    },
    {
      "id": "bubabu_rainbow_arc",
      "character_dna": {
        "bone_structure": "candy_pop_6color_rainbow_arc_behind_bubabu",
        "persistent_features": [
          "small soft Candy Pop 6-color rainbow arc directly behind Bubabu's body",
          "scaled to approximately 120% of Bubabu's body radius (sized to Bubabu)",
          "color stripes in classic rainbow order: cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, orange #FF9F1C, coral #FF6B6B",
          "soft kid-pastel saturation, slightly tilted 5-10 degrees behind Bubabu's right shoulder",
          "matte flat shading — NO body-glow on Bubabu, NO rainbow shine spilling onto Bubabu's fur, NO halo effect"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — signature visual locked across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 2
        },
        "visual_weight": 0.048
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "bubabu",
        "action": "small Candy Pop rainbow arc rendered directly behind Bubabu's body, sized to him, signature brand visual",
        "emotional_state": "decorative_brand_signature"
      }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": {
        "bone_structure": "plush round owl mascot (Bubabu — visual locked per kiosk unification)",
        "persistent_features": [
          "match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1",
          "round fluffy white plush owl mascot, ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring around each eye",
          "small triangular BLACK closed beak between the goggles (brand lock — STAYS CLOSED)",
          "caramel-brown stubby wings + caramel-brown feet with three orange toes each",
          "pure white ear tufts SAME white color as body fur",
          "soft light-grey outline so the white body reads on the white sticker background"
        ],
        "heritage": "Bubabu plush mascot, locked appearance + pose + rainbow per kiosk unification 2026-05-31 — IDENTICAL visual identity across all 8 stickers, only scale flexes (hero=big, badge=small)"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 3
        },
        "visual_weight": 0.12
      },
      "appearance": {
        "age": "plush toy",
        "expression": "serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed — IDENTICAL across all 8 stickers"
      },
      "interaction": {
        "target_id": "environment",
        "action": "tiny Bubabu owl peeking from the bottom-right",
        "emotional_state": "warm and inviting (master expression locked across all 8 stickers)"
      }
    },
    {
      "id": "bubabu_ge_domain_pill",
      "character_dna": {
        "bone_structure": "butter_cream_rounded_pill_with_magenta_brand_text",
        "persistent_features": [
          "soft rounded pill capsule, butter-cream gradient #FFFAEB top fading to #FFF6CC bottom (matches Bubabu cover override + ad cover aesthetic)",
          "pill radius equals pill height divided by 2 (soft rounded ends, no harsh corners)",
          "BUBABU.GE uppercase text inside the pill, color = deep magenta #FF1F8F (brand primary, max contrast on butter-cream)",
          "flat matte shading — NO drop shadow, NO border outline, NO gradient on text",
          "centered horizontally, bottom-third of sticker frame — IDENTICAL position across all 8 stickers"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — domain pill IDENTICAL across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.5,
          "y": -0.4,
          "z_index": 4
        },
        "visual_weight": 0.25
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "environment",
        "action": "butter-cream rounded pill at bottom-center carrying BUBABU.GE in deep magenta uppercase text",
        "emotional_state": "brand_signature"
      }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": {
      "narrative_clutter": [
        "thick glossy white die-cut border around the whole shape",
        "soft drop shadow beneath the sticker",
        "soft Candy Pop 6-color rainbow arc directly behind Bubabu (signature brand visual, scaled to Bubabu, NO body-glow)",
        "butter-cream rounded pill at the bottom-center carrying BUBABU.GE in deep magenta uppercase text (unified across all 8 stickers per kiosk unification 2026-05-31)",
        "tiny soft sparkle accent",
        "soft cloud-like organic silhouette",
        "matte candy-pop finish"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "type": "Pixar stylized soft flat product light (NOT photoreal cinema)"
    }
  },
  "technical": {
    "camera": {
      "model": "Pixar virtual"
    }
  },
  "text_rendering": {
    "enabled": true,
    "text": "Georgian headline: მაგნიტური სათამაშოები | Georgian benefit: ააწყე • შექმენი • ისწავლე | English subtitle: Magnetic Toys | Bottom ribbon banner: BUBABU.GE",
    "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in cyan, (2) Georgian benefit row with round dots, (3) small English subtitle; butter-cream rounded pill at the bottom-center with BUBABU.GE in deep magenta uppercase text (UNIFIED across all 8 stickers — no per-category ribbon); tiny Bubabu owl bottom-right"
  },
  "advanced": {
    "negative_prompt": [
      "no rectangle frame",
      "no straight hard border",
      "no photoreal",
      "no live-action",
      "no DSLR",
      "no real-lens DOF",
      "no film grain",
      "no HDR cinema",
      "no ARRI",
      "no Sony",
      "no Sigma",
      "no Canon",
      "no realistic owl",
      "no glow on goggles",
      "no lowercase bubabu.ge",
      "no uppercase Georgian mtavruli",
      "no Cyrillic letters",
      "no gibberish text",
      "no watermark",
      "no busy texture",
      "no neon",
      "no dark moody mood",
      "no metal magnet hazard look"
    ]
  }
}
```

---

## 3 - Smart Learning Gifts

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_03_smart_learning_gifts",
  "user_intent": "Die-cut sticker for learning gifts — glowing bulb + open book icon, lime accent, cloud shape with white die-cut border.",
  "meta": {
    "aspect_ratio": "3:2",
    "quality": "stylized_3d_render",
    "seed": 81003,
    "guidance_scale": 7.5
  },
  "sticker_format": {
    "type": "die-cut vinyl sticker",
    "shape": "soft cloud-like organic blob, unique to this category",
    "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette",
    "shadow": "soft drop shadow beneath like a real peel-and-stick sticker",
    "background": "pure solid white #FFFFFF"
  },
  "consistency_lock": {
    "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. BUBABU.GE always inside butter-cream rounded pill at bottom-center with deep magenta uppercase text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation, NO lowercase bubabu.ge). Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations. Bubabu master pose + DNA + Candy Pop 6-color rainbow arc behind — IDENTICAL visual across all 8 stickers (pose + appearance + rainbow position + colors LOCKED). BUBABU.GE butter-cream pill at bottom-center with magenta text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation)."
  },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": {
      "palette_driver": "candy-pop kids-commercial on pure white background, bright lime #84CC16 accent, soft Pixar 3D"
    }
  },
  "subjects": [
    {
      "id": "learning_icon",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "friendly soft 3D glowing light bulb",
          "small open book beneath the bulb",
          "tiny warm idea-sparkle"
        ],
        "heritage": "generic candy-pop 3D learning icon"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 2
        },
        "visual_weight": 0.8
      },
      "appearance": {
        "age": "icon",
        "expression": "bright and optimistic"
      },
      "interaction": {
        "target_id": "environment",
        "action": "bulb glowing above an open book as the left icon",
        "emotional_state": "curious"
      }
    },
    {
      "id": "bubabu_rainbow_arc",
      "character_dna": {
        "bone_structure": "candy_pop_6color_rainbow_arc_behind_bubabu",
        "persistent_features": [
          "small soft Candy Pop 6-color rainbow arc directly behind Bubabu's body",
          "scaled to approximately 120% of Bubabu's body radius (sized to Bubabu)",
          "color stripes in classic rainbow order: cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, orange #FF9F1C, coral #FF6B6B",
          "soft kid-pastel saturation, slightly tilted 5-10 degrees behind Bubabu's right shoulder",
          "matte flat shading — NO body-glow on Bubabu, NO rainbow shine spilling onto Bubabu's fur, NO halo effect"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — signature visual locked across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 2
        },
        "visual_weight": 0.048
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "bubabu",
        "action": "small Candy Pop rainbow arc rendered directly behind Bubabu's body, sized to him, signature brand visual",
        "emotional_state": "decorative_brand_signature"
      }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": {
        "bone_structure": "plush round owl mascot (Bubabu — visual locked per kiosk unification)",
        "persistent_features": [
          "match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1",
          "round fluffy white plush owl mascot, ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring around each eye",
          "small triangular BLACK closed beak between the goggles (brand lock — STAYS CLOSED)",
          "caramel-brown stubby wings + caramel-brown feet with three orange toes each",
          "pure white ear tufts SAME white color as body fur",
          "soft light-grey outline so the white body reads on the white sticker background"
        ],
        "heritage": "Bubabu plush mascot, locked appearance + pose + rainbow per kiosk unification 2026-05-31 — IDENTICAL visual identity across all 8 stickers, only scale flexes (hero=big, badge=small)"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 3
        },
        "visual_weight": 0.12
      },
      "appearance": {
        "age": "plush toy",
        "expression": "serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed — IDENTICAL across all 8 stickers"
      },
      "interaction": {
        "target_id": "environment",
        "action": "tiny Bubabu owl peeking from the bottom-right",
        "emotional_state": "warm and inviting (master expression locked across all 8 stickers)"
      }
    },
    {
      "id": "bubabu_ge_domain_pill",
      "character_dna": {
        "bone_structure": "butter_cream_rounded_pill_with_magenta_brand_text",
        "persistent_features": [
          "soft rounded pill capsule, butter-cream gradient #FFFAEB top fading to #FFF6CC bottom (matches Bubabu cover override + ad cover aesthetic)",
          "pill radius equals pill height divided by 2 (soft rounded ends, no harsh corners)",
          "BUBABU.GE uppercase text inside the pill, color = deep magenta #FF1F8F (brand primary, max contrast on butter-cream)",
          "flat matte shading — NO drop shadow, NO border outline, NO gradient on text",
          "centered horizontally, bottom-third of sticker frame — IDENTICAL position across all 8 stickers"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — domain pill IDENTICAL across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.5,
          "y": -0.4,
          "z_index": 4
        },
        "visual_weight": 0.25
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "environment",
        "action": "butter-cream rounded pill at bottom-center carrying BUBABU.GE in deep magenta uppercase text",
        "emotional_state": "brand_signature"
      }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": {
      "narrative_clutter": [
        "thick glossy white die-cut border around the whole shape",
        "soft drop shadow beneath the sticker",
        "soft Candy Pop 6-color rainbow arc directly behind Bubabu (signature brand visual, scaled to Bubabu, NO body-glow)",
        "butter-cream rounded pill at the bottom-center carrying BUBABU.GE in deep magenta uppercase text (unified across all 8 stickers per kiosk unification 2026-05-31)",
        "tiny soft idea-sparkle accent",
        "soft cloud-like organic silhouette",
        "matte candy-pop finish"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "type": "Pixar stylized soft flat product light (NOT photoreal cinema)"
    }
  },
  "technical": {
    "camera": {
      "model": "Pixar virtual"
    }
  },
  "text_rendering": {
    "enabled": true,
    "text": "Georgian headline: სასწავლო საჩუქრები | Georgian benefit: ისწავლე თამაშით | English subtitle: Smart Learning Gifts | Bottom ribbon banner: BUBABU.GE",
    "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in lime, (2) Georgian benefit line, (3) small English subtitle; butter-cream rounded pill at the bottom-center with BUBABU.GE in deep magenta uppercase text (UNIFIED across all 8 stickers — no per-category ribbon); tiny Bubabu owl bottom-right"
  },
  "advanced": {
    "negative_prompt": [
      "no rectangle frame",
      "no straight hard border",
      "no photoreal",
      "no live-action",
      "no DSLR",
      "no real-lens DOF",
      "no film grain",
      "no HDR cinema",
      "no ARRI",
      "no Sony",
      "no Sigma",
      "no Canon",
      "no realistic owl",
      "no glow on goggles",
      "no lowercase bubabu.ge",
      "no uppercase Georgian mtavruli",
      "no Cyrillic letters",
      "no gibberish text",
      "no watermark",
      "no busy texture",
      "no neon",
      "no dark moody mood"
    ]
  }
}
```

---

## 4 - STEM & Robotics

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_04_stem_robotics",
  "user_intent": "Die-cut sticker for STEM and robotics — friendly robot head + gear icon, deep teal-cyan accent, cloud shape with white die-cut border.",
  "meta": {
    "aspect_ratio": "3:2",
    "quality": "stylized_3d_render",
    "seed": 81004,
    "guidance_scale": 7.5
  },
  "sticker_format": {
    "type": "die-cut vinyl sticker",
    "shape": "soft cloud-like organic blob, unique to this category",
    "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette",
    "shadow": "soft drop shadow beneath like a real peel-and-stick sticker",
    "background": "pure solid white #FFFFFF"
  },
  "consistency_lock": {
    "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. BUBABU.GE always inside butter-cream rounded pill at bottom-center with deep magenta uppercase text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation, NO lowercase bubabu.ge). Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations. Bubabu master pose + DNA + Candy Pop 6-color rainbow arc behind — IDENTICAL visual across all 8 stickers (pose + appearance + rainbow position + colors LOCKED). BUBABU.GE butter-cream pill at bottom-center with magenta text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation)."
  },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": {
      "palette_driver": "candy-pop kids-commercial on pure white background, deep teal-cyan #2BA3C7 accent (reads tech), soft Pixar 3D"
    }
  },
  "subjects": [
    {
      "id": "robot_icon",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "adorable rounded soft 3D friendly robot head with big friendly eyes",
          "small soft gear beside it",
          "rounded antenna with a soft dot"
        ],
        "heritage": "generic candy-pop 3D friendly-robot icon"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 2
        },
        "visual_weight": 0.8
      },
      "appearance": {
        "age": "icon",
        "expression": "friendly and curious"
      },
      "interaction": {
        "target_id": "environment",
        "action": "cute robot head with a soft gear as the left icon",
        "emotional_state": "friendly"
      }
    },
    {
      "id": "bubabu_rainbow_arc",
      "character_dna": {
        "bone_structure": "candy_pop_6color_rainbow_arc_behind_bubabu",
        "persistent_features": [
          "small soft Candy Pop 6-color rainbow arc directly behind Bubabu's body",
          "scaled to approximately 120% of Bubabu's body radius (sized to Bubabu)",
          "color stripes in classic rainbow order: cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, orange #FF9F1C, coral #FF6B6B",
          "soft kid-pastel saturation, slightly tilted 5-10 degrees behind Bubabu's right shoulder",
          "matte flat shading — NO body-glow on Bubabu, NO rainbow shine spilling onto Bubabu's fur, NO halo effect"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — signature visual locked across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 2
        },
        "visual_weight": 0.048
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "bubabu",
        "action": "small Candy Pop rainbow arc rendered directly behind Bubabu's body, sized to him, signature brand visual",
        "emotional_state": "decorative_brand_signature"
      }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": {
        "bone_structure": "plush round owl mascot (Bubabu — visual locked per kiosk unification)",
        "persistent_features": [
          "match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1",
          "round fluffy white plush owl mascot, ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring around each eye",
          "small triangular BLACK closed beak between the goggles (brand lock — STAYS CLOSED)",
          "caramel-brown stubby wings + caramel-brown feet with three orange toes each",
          "pure white ear tufts SAME white color as body fur",
          "soft light-grey outline so the white body reads on the white sticker background"
        ],
        "heritage": "Bubabu plush mascot, locked appearance + pose + rainbow per kiosk unification 2026-05-31 — IDENTICAL visual identity across all 8 stickers, only scale flexes (hero=big, badge=small)"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 3
        },
        "visual_weight": 0.12
      },
      "appearance": {
        "age": "plush toy",
        "expression": "serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed — IDENTICAL across all 8 stickers"
      },
      "interaction": {
        "target_id": "environment",
        "action": "tiny Bubabu owl peeking from the bottom-right",
        "emotional_state": "warm and inviting (master expression locked across all 8 stickers)"
      }
    },
    {
      "id": "bubabu_ge_domain_pill",
      "character_dna": {
        "bone_structure": "butter_cream_rounded_pill_with_magenta_brand_text",
        "persistent_features": [
          "soft rounded pill capsule, butter-cream gradient #FFFAEB top fading to #FFF6CC bottom (matches Bubabu cover override + ad cover aesthetic)",
          "pill radius equals pill height divided by 2 (soft rounded ends, no harsh corners)",
          "BUBABU.GE uppercase text inside the pill, color = deep magenta #FF1F8F (brand primary, max contrast on butter-cream)",
          "flat matte shading — NO drop shadow, NO border outline, NO gradient on text",
          "centered horizontally, bottom-third of sticker frame — IDENTICAL position across all 8 stickers"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — domain pill IDENTICAL across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.5,
          "y": -0.4,
          "z_index": 4
        },
        "visual_weight": 0.25
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "environment",
        "action": "butter-cream rounded pill at bottom-center carrying BUBABU.GE in deep magenta uppercase text",
        "emotional_state": "brand_signature"
      }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": {
      "narrative_clutter": [
        "thick glossy white die-cut border around the whole shape",
        "soft drop shadow beneath the sticker",
        "soft Candy Pop 6-color rainbow arc directly behind Bubabu (signature brand visual, scaled to Bubabu, NO body-glow)",
        "butter-cream rounded pill at the bottom-center carrying BUBABU.GE in deep magenta uppercase text (unified across all 8 stickers per kiosk unification 2026-05-31)",
        "tiny soft gear-spark accent",
        "soft cloud-like organic silhouette",
        "matte candy-pop finish"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "type": "Pixar stylized soft flat product light (NOT photoreal cinema)"
    }
  },
  "technical": {
    "camera": {
      "model": "Pixar virtual"
    }
  },
  "text_rendering": {
    "enabled": true,
    "text": "Headline (Latin + Georgian): STEM & რობოტიკა | Georgian benefit: ტექნოლოგია • ლოგიკა • აღმოჩენა | English subtitle: STEM & Robotics | Bottom ribbon banner: BUBABU.GE",
    "placement": "icon on the left; text stack on the right top-to-bottom — (1) headline with STEM in clean Latin and რობოტიკა in Georgian, deep teal-cyan, (2) Georgian benefit row with round dots, (3) small English subtitle; deep teal-butter-cream rounded pill at the bottom-center with BUBABU.GE in deep magenta uppercase text (UNIFIED across all 8 stickers — no per-category ribbon); tiny Bubabu owl bottom-right"
  },
  "advanced": {
    "negative_prompt": [
      "no rectangle frame",
      "no straight hard border",
      "no photoreal",
      "no live-action",
      "no DSLR",
      "no real-lens DOF",
      "no film grain",
      "no HDR cinema",
      "no ARRI",
      "no Sony",
      "no Sigma",
      "no Canon",
      "no realistic owl",
      "no cold industrial robot",
      "no glow on goggles",
      "no lowercase bubabu.ge",
      "no uppercase Georgian mtavruli",
      "no Cyrillic letters",
      "no gibberish text",
      "no watermark",
      "no neon",
      "no dark moody mood"
    ]
  }
}
```

---

## 5 - Creative Gifts

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_05_creative_gifts",
  "user_intent": "Die-cut sticker for creative/art kits — paint brush + palette icon, orange accent, cloud shape with white die-cut border.",
  "meta": {
    "aspect_ratio": "3:2",
    "quality": "stylized_3d_render",
    "seed": 81005,
    "guidance_scale": 7.5
  },
  "sticker_format": {
    "type": "die-cut vinyl sticker",
    "shape": "soft cloud-like organic blob, unique to this category",
    "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette",
    "shadow": "soft drop shadow beneath like a real peel-and-stick sticker",
    "background": "pure solid white #FFFFFF"
  },
  "consistency_lock": {
    "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. BUBABU.GE always inside butter-cream rounded pill at bottom-center with deep magenta uppercase text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation, NO lowercase bubabu.ge). Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations. Bubabu master pose + DNA + Candy Pop 6-color rainbow arc behind — IDENTICAL visual across all 8 stickers (pose + appearance + rainbow position + colors LOCKED). BUBABU.GE butter-cream pill at bottom-center with magenta text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation)."
  },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": {
      "palette_driver": "candy-pop kids-commercial on pure white background, bright orange #FF9F1C accent, soft Pixar 3D"
    }
  },
  "subjects": [
    {
      "id": "creative_icon",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "chunky soft 3D paint brush",
          "rounded candy-pop color palette",
          "tiny burst of creative sparkle"
        ],
        "heritage": "generic candy-pop 3D creative-art icon"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 2
        },
        "visual_weight": 0.8
      },
      "appearance": {
        "age": "icon",
        "expression": "joyful and artistic"
      },
      "interaction": {
        "target_id": "environment",
        "action": "paint brush across a palette as the left icon",
        "emotional_state": "creative"
      }
    },
    {
      "id": "bubabu_rainbow_arc",
      "character_dna": {
        "bone_structure": "candy_pop_6color_rainbow_arc_behind_bubabu",
        "persistent_features": [
          "small soft Candy Pop 6-color rainbow arc directly behind Bubabu's body",
          "scaled to approximately 120% of Bubabu's body radius (sized to Bubabu)",
          "color stripes in classic rainbow order: cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, orange #FF9F1C, coral #FF6B6B",
          "soft kid-pastel saturation, slightly tilted 5-10 degrees behind Bubabu's right shoulder",
          "matte flat shading — NO body-glow on Bubabu, NO rainbow shine spilling onto Bubabu's fur, NO halo effect"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — signature visual locked across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 2
        },
        "visual_weight": 0.048
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "bubabu",
        "action": "small Candy Pop rainbow arc rendered directly behind Bubabu's body, sized to him, signature brand visual",
        "emotional_state": "decorative_brand_signature"
      }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": {
        "bone_structure": "plush round owl mascot (Bubabu — visual locked per kiosk unification)",
        "persistent_features": [
          "match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1",
          "round fluffy white plush owl mascot, ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring around each eye",
          "small triangular BLACK closed beak between the goggles (brand lock — STAYS CLOSED)",
          "caramel-brown stubby wings + caramel-brown feet with three orange toes each",
          "pure white ear tufts SAME white color as body fur",
          "soft light-grey outline so the white body reads on the white sticker background"
        ],
        "heritage": "Bubabu plush mascot, locked appearance + pose + rainbow per kiosk unification 2026-05-31 — IDENTICAL visual identity across all 8 stickers, only scale flexes (hero=big, badge=small)"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 3
        },
        "visual_weight": 0.12
      },
      "appearance": {
        "age": "plush toy",
        "expression": "serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed — IDENTICAL across all 8 stickers"
      },
      "interaction": {
        "target_id": "environment",
        "action": "tiny Bubabu owl peeking from the bottom-right",
        "emotional_state": "warm and inviting (master expression locked across all 8 stickers)"
      }
    },
    {
      "id": "bubabu_ge_domain_pill",
      "character_dna": {
        "bone_structure": "butter_cream_rounded_pill_with_magenta_brand_text",
        "persistent_features": [
          "soft rounded pill capsule, butter-cream gradient #FFFAEB top fading to #FFF6CC bottom (matches Bubabu cover override + ad cover aesthetic)",
          "pill radius equals pill height divided by 2 (soft rounded ends, no harsh corners)",
          "BUBABU.GE uppercase text inside the pill, color = deep magenta #FF1F8F (brand primary, max contrast on butter-cream)",
          "flat matte shading — NO drop shadow, NO border outline, NO gradient on text",
          "centered horizontally, bottom-third of sticker frame — IDENTICAL position across all 8 stickers"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — domain pill IDENTICAL across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.5,
          "y": -0.4,
          "z_index": 4
        },
        "visual_weight": 0.25
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "environment",
        "action": "butter-cream rounded pill at bottom-center carrying BUBABU.GE in deep magenta uppercase text",
        "emotional_state": "brand_signature"
      }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": {
      "narrative_clutter": [
        "thick glossy white die-cut border around the whole shape",
        "soft drop shadow beneath the sticker",
        "soft Candy Pop 6-color rainbow arc directly behind Bubabu (signature brand visual, scaled to Bubabu, NO body-glow)",
        "butter-cream rounded pill at the bottom-center carrying BUBABU.GE in deep magenta uppercase text (unified across all 8 stickers per kiosk unification 2026-05-31)",
        "tiny soft creative sparkle accent",
        "soft cloud-like organic silhouette",
        "matte candy-pop finish"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "type": "Pixar stylized soft flat product light (NOT photoreal cinema)"
    }
  },
  "technical": {
    "camera": {
      "model": "Pixar virtual"
    }
  },
  "text_rendering": {
    "enabled": true,
    "text": "Georgian headline: კრეატიული საჩუქრები | Georgian benefit: დახატე • შექმენი • გააფერადე | English subtitle: Creative Gifts | Bottom ribbon banner: BUBABU.GE",
    "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in orange, (2) Georgian benefit row with round dots, (3) small English subtitle; butter-cream rounded pill at the bottom-center with BUBABU.GE in deep magenta uppercase text (UNIFIED across all 8 stickers — no per-category ribbon); tiny Bubabu owl bottom-right"
  },
  "advanced": {
    "negative_prompt": [
      "no rectangle frame",
      "no straight hard border",
      "no photoreal",
      "no live-action",
      "no DSLR",
      "no real-lens DOF",
      "no film grain",
      "no HDR cinema",
      "no ARRI",
      "no Sony",
      "no Sigma",
      "no Canon",
      "no realistic owl",
      "no glow on goggles",
      "no lowercase bubabu.ge",
      "no uppercase Georgian mtavruli",
      "no Cyrillic letters",
      "no gibberish text",
      "no watermark",
      "no busy texture",
      "no neon",
      "no dark moody mood"
    ]
  }
}
```

---

## 6 - Fun Gifts

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_06_fun_gifts",
  "user_intent": "Die-cut sticker for fun/impulse items — wrapped gift + star + confetti icon, coral accent, cloud shape with white die-cut border.",
  "meta": {
    "aspect_ratio": "3:2",
    "quality": "stylized_3d_render",
    "seed": 81006,
    "guidance_scale": 7.5
  },
  "sticker_format": {
    "type": "die-cut vinyl sticker",
    "shape": "soft cloud-like organic blob, unique to this category",
    "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette",
    "shadow": "soft drop shadow beneath like a real peel-and-stick sticker",
    "background": "pure solid white #FFFFFF"
  },
  "consistency_lock": {
    "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. BUBABU.GE always inside butter-cream rounded pill at bottom-center with deep magenta uppercase text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation, NO lowercase bubabu.ge). Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations. Bubabu master pose + DNA + Candy Pop 6-color rainbow arc behind — IDENTICAL visual across all 8 stickers (pose + appearance + rainbow position + colors LOCKED). BUBABU.GE butter-cream pill at bottom-center with magenta text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation)."
  },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": {
      "palette_driver": "candy-pop kids-commercial on pure white background, bright coral #FF6B6B accent, soft Pixar 3D"
    }
  },
  "subjects": [
    {
      "id": "fun_icon",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "cheerful small soft 3D wrapped gift box with a bouncy bow",
          "a tiny star",
          "a couple of confetti dots"
        ],
        "heritage": "generic candy-pop 3D gift-box icon"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 2
        },
        "visual_weight": 0.8
      },
      "appearance": {
        "age": "icon",
        "expression": "cheerful and playful"
      },
      "interaction": {
        "target_id": "environment",
        "action": "small wrapped gift with a star as the left icon",
        "emotional_state": "joyful"
      }
    },
    {
      "id": "bubabu_rainbow_arc",
      "character_dna": {
        "bone_structure": "candy_pop_6color_rainbow_arc_behind_bubabu",
        "persistent_features": [
          "small soft Candy Pop 6-color rainbow arc directly behind Bubabu's body",
          "scaled to approximately 120% of Bubabu's body radius (sized to Bubabu)",
          "color stripes in classic rainbow order: cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, orange #FF9F1C, coral #FF6B6B",
          "soft kid-pastel saturation, slightly tilted 5-10 degrees behind Bubabu's right shoulder",
          "matte flat shading — NO body-glow on Bubabu, NO rainbow shine spilling onto Bubabu's fur, NO halo effect"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — signature visual locked across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 2
        },
        "visual_weight": 0.048
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "bubabu",
        "action": "small Candy Pop rainbow arc rendered directly behind Bubabu's body, sized to him, signature brand visual",
        "emotional_state": "decorative_brand_signature"
      }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": {
        "bone_structure": "plush round owl mascot (Bubabu — visual locked per kiosk unification)",
        "persistent_features": [
          "match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1",
          "round fluffy white plush owl mascot, ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring around each eye",
          "small triangular BLACK closed beak between the goggles (brand lock — STAYS CLOSED)",
          "caramel-brown stubby wings + caramel-brown feet with three orange toes each",
          "pure white ear tufts SAME white color as body fur",
          "soft light-grey outline so the white body reads on the white sticker background"
        ],
        "heritage": "Bubabu plush mascot, locked appearance + pose + rainbow per kiosk unification 2026-05-31 — IDENTICAL visual identity across all 8 stickers, only scale flexes (hero=big, badge=small)"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 3
        },
        "visual_weight": 0.12
      },
      "appearance": {
        "age": "plush toy",
        "expression": "serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed — IDENTICAL across all 8 stickers"
      },
      "interaction": {
        "target_id": "environment",
        "action": "tiny Bubabu owl peeking from the bottom-right",
        "emotional_state": "warm and inviting (master expression locked across all 8 stickers)"
      }
    },
    {
      "id": "bubabu_ge_domain_pill",
      "character_dna": {
        "bone_structure": "butter_cream_rounded_pill_with_magenta_brand_text",
        "persistent_features": [
          "soft rounded pill capsule, butter-cream gradient #FFFAEB top fading to #FFF6CC bottom (matches Bubabu cover override + ad cover aesthetic)",
          "pill radius equals pill height divided by 2 (soft rounded ends, no harsh corners)",
          "BUBABU.GE uppercase text inside the pill, color = deep magenta #FF1F8F (brand primary, max contrast on butter-cream)",
          "flat matte shading — NO drop shadow, NO border outline, NO gradient on text",
          "centered horizontally, bottom-third of sticker frame — IDENTICAL position across all 8 stickers"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — domain pill IDENTICAL across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.5,
          "y": -0.4,
          "z_index": 4
        },
        "visual_weight": 0.25
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "environment",
        "action": "butter-cream rounded pill at bottom-center carrying BUBABU.GE in deep magenta uppercase text",
        "emotional_state": "brand_signature"
      }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": {
      "narrative_clutter": [
        "thick glossy white die-cut border around the whole shape",
        "soft drop shadow beneath the sticker",
        "soft Candy Pop 6-color rainbow arc directly behind Bubabu (signature brand visual, scaled to Bubabu, NO body-glow)",
        "butter-cream rounded pill at the bottom-center carrying BUBABU.GE in deep magenta uppercase text (unified across all 8 stickers per kiosk unification 2026-05-31)",
        "tiny soft happy star accent",
        "soft cloud-like organic silhouette",
        "matte candy-pop finish"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "type": "Pixar stylized soft flat product light (NOT photoreal cinema)"
    }
  },
  "technical": {
    "camera": {
      "model": "Pixar virtual"
    }
  },
  "text_rendering": {
    "enabled": true,
    "text": "Georgian headline: სახალისო საჩუქრები | Georgian benefit: პატარა სიხარული | English subtitle: Fun Gifts | Bottom ribbon banner: BUBABU.GE",
    "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in coral, (2) Georgian benefit line, (3) small English subtitle; butter-cream rounded pill at the bottom-center with BUBABU.GE in deep magenta uppercase text (UNIFIED across all 8 stickers — no per-category ribbon); tiny Bubabu owl bottom-right"
  },
  "advanced": {
    "negative_prompt": [
      "no rectangle frame",
      "no straight hard border",
      "no photoreal",
      "no live-action",
      "no DSLR",
      "no real-lens DOF",
      "no film grain",
      "no HDR cinema",
      "no ARRI",
      "no Sony",
      "no Sigma",
      "no Canon",
      "no realistic owl",
      "no glow on goggles",
      "no lowercase bubabu.ge",
      "no uppercase Georgian mtavruli",
      "no Cyrillic letters",
      "no gibberish text",
      "no watermark",
      "no busy texture",
      "no neon",
      "no dark moody mood"
    ]
  }
}
```

---

## 7 - Gift Sets

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_07_gift_sets",
  "user_intent": "Die-cut sticker for ready-made gift bundles — stacked wrapped gifts + bow icon, warm yellow accent, cloud shape with white die-cut border.",
  "meta": {
    "aspect_ratio": "3:2",
    "quality": "stylized_3d_render",
    "seed": 81007,
    "guidance_scale": 7.5
  },
  "sticker_format": {
    "type": "die-cut vinyl sticker",
    "shape": "soft cloud-like organic blob, unique to this category",
    "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette",
    "shadow": "soft drop shadow beneath like a real peel-and-stick sticker",
    "background": "pure solid white #FFFFFF"
  },
  "consistency_lock": {
    "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. BUBABU.GE always inside butter-cream rounded pill at bottom-center with deep magenta uppercase text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation, NO lowercase bubabu.ge). Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations. Bubabu master pose + DNA + Candy Pop 6-color rainbow arc behind — IDENTICAL visual across all 8 stickers (pose + appearance + rainbow position + colors LOCKED). BUBABU.GE butter-cream pill at bottom-center with magenta text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation)."
  },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": {
      "palette_driver": "candy-pop kids-commercial on pure white background, warm yellow #FFEB3B accent (headline in warm gold for readability), soft Pixar 3D"
    }
  },
  "subjects": [
    {
      "id": "giftset_icon",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "neat stack of two to three soft 3D wrapped gift boxes",
          "one elegant ribbon bow tying the stack",
          "warm yellow coral and cyan boxes"
        ],
        "heritage": "generic candy-pop 3D gift-bundle icon"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 2
        },
        "visual_weight": 0.8
      },
      "appearance": {
        "age": "icon",
        "expression": "premium and warm"
      },
      "interaction": {
        "target_id": "environment",
        "action": "stacked wrapped gifts with a bow as the left icon",
        "emotional_state": "generous"
      }
    },
    {
      "id": "bubabu_rainbow_arc",
      "character_dna": {
        "bone_structure": "candy_pop_6color_rainbow_arc_behind_bubabu",
        "persistent_features": [
          "small soft Candy Pop 6-color rainbow arc directly behind Bubabu's body",
          "scaled to approximately 120% of Bubabu's body radius (sized to Bubabu)",
          "color stripes in classic rainbow order: cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, orange #FF9F1C, coral #FF6B6B",
          "soft kid-pastel saturation, slightly tilted 5-10 degrees behind Bubabu's right shoulder",
          "matte flat shading — NO body-glow on Bubabu, NO rainbow shine spilling onto Bubabu's fur, NO halo effect"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — signature visual locked across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 2
        },
        "visual_weight": 0.048
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "bubabu",
        "action": "small Candy Pop rainbow arc rendered directly behind Bubabu's body, sized to him, signature brand visual",
        "emotional_state": "decorative_brand_signature"
      }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": {
        "bone_structure": "plush round owl mascot (Bubabu — visual locked per kiosk unification)",
        "persistent_features": [
          "match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1",
          "round fluffy white plush owl mascot, ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring around each eye",
          "small triangular BLACK closed beak between the goggles (brand lock — STAYS CLOSED)",
          "caramel-brown stubby wings + caramel-brown feet with three orange toes each",
          "pure white ear tufts SAME white color as body fur",
          "soft light-grey outline so the white body reads on the white sticker background"
        ],
        "heritage": "Bubabu plush mascot, locked appearance + pose + rainbow per kiosk unification 2026-05-31 — IDENTICAL visual identity across all 8 stickers, only scale flexes (hero=big, badge=small)"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 3
        },
        "visual_weight": 0.12
      },
      "appearance": {
        "age": "plush toy",
        "expression": "serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed — IDENTICAL across all 8 stickers"
      },
      "interaction": {
        "target_id": "environment",
        "action": "tiny Bubabu owl peeking from the bottom-right",
        "emotional_state": "warm and inviting (master expression locked across all 8 stickers)"
      }
    },
    {
      "id": "bubabu_ge_domain_pill",
      "character_dna": {
        "bone_structure": "butter_cream_rounded_pill_with_magenta_brand_text",
        "persistent_features": [
          "soft rounded pill capsule, butter-cream gradient #FFFAEB top fading to #FFF6CC bottom (matches Bubabu cover override + ad cover aesthetic)",
          "pill radius equals pill height divided by 2 (soft rounded ends, no harsh corners)",
          "BUBABU.GE uppercase text inside the pill, color = deep magenta #FF1F8F (brand primary, max contrast on butter-cream)",
          "flat matte shading — NO drop shadow, NO border outline, NO gradient on text",
          "centered horizontally, bottom-third of sticker frame — IDENTICAL position across all 8 stickers"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — domain pill IDENTICAL across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.5,
          "y": -0.4,
          "z_index": 4
        },
        "visual_weight": 0.25
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "environment",
        "action": "butter-cream rounded pill at bottom-center carrying BUBABU.GE in deep magenta uppercase text",
        "emotional_state": "brand_signature"
      }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": {
      "narrative_clutter": [
        "thick glossy white die-cut border around the whole shape",
        "soft drop shadow beneath the sticker",
        "soft Candy Pop 6-color rainbow arc directly behind Bubabu (signature brand visual, scaled to Bubabu, NO body-glow)",
        "butter-cream rounded pill at the bottom-center carrying BUBABU.GE in deep magenta uppercase text (unified across all 8 stickers per kiosk unification 2026-05-31)",
        "tiny soft ribbon-shine accent",
        "soft cloud-like organic silhouette",
        "matte candy-pop finish"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "type": "Pixar stylized soft flat product light (NOT photoreal cinema)"
    }
  },
  "technical": {
    "camera": {
      "model": "Pixar virtual"
    }
  },
  "text_rendering": {
    "enabled": true,
    "text": "Georgian headline: საჩუქრის ნაკრებები | Georgian benefit: მზად არის საჩუქრად | English subtitle: Gift Sets | Bottom ribbon banner: BUBABU.GE",
    "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in warm gold with a soft darker outline for contrast, (2) Georgian benefit line, (3) small English subtitle; butter-cream rounded pill at the bottom-center with BUBABU.GE in deep magenta uppercase text (UNIFIED across all 8 stickers — no per-category ribbon); tiny Bubabu owl bottom-right"
  },
  "advanced": {
    "negative_prompt": [
      "no rectangle frame",
      "no straight hard border",
      "no photoreal",
      "no live-action",
      "no DSLR",
      "no real-lens DOF",
      "no film grain",
      "no HDR cinema",
      "no ARRI",
      "no Sony",
      "no Sigma",
      "no Canon",
      "no realistic owl",
      "no glow on goggles",
      "no metallic gold",
      "no lowercase bubabu.ge",
      "no uppercase Georgian mtavruli",
      "no Cyrillic letters",
      "no gibberish text",
      "no watermark",
      "no neon",
      "no dark moody mood"
    ]
  }
}
```

---

## 8 - Screen-Free Gifts

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "scene_id": "sticker_08_screen_free_gifts",
  "user_intent": "Die-cut brand-philosophy sticker — happy child face + heart + gentle screen-free badge, cyan + lime accent, cloud shape with white die-cut border.",
  "meta": {
    "aspect_ratio": "3:2",
    "quality": "stylized_3d_render",
    "seed": 81008,
    "guidance_scale": 7.5
  },
  "sticker_format": {
    "type": "die-cut vinyl sticker",
    "shape": "soft cloud-like organic blob, unique to this category",
    "outline": "thick even glossy WHITE die-cut border hugging the whole silhouette",
    "shadow": "soft drop shadow beneath like a real peel-and-stick sticker",
    "background": "pure solid white #FFFFFF"
  },
  "consistency_lock": {
    "do_not_vary": "White die-cut border ALWAYS thick and present. Background ALWAYS pure white #FFFFFF. Accent (banner + headline) ALWAYS exactly this spec hex. BUBABU.GE always inside butter-cream rounded pill at bottom-center with deep magenta uppercase text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation, NO lowercase bubabu.ge). Text order ALWAYS Georgian headline top, then Georgian benefit, then small English subtitle. The white owl carries a soft grey outline so it reads on white. NO rectangle, NO straight hard frame, NO extra decorations. Bubabu master pose + DNA + Candy Pop 6-color rainbow arc behind — IDENTICAL visual across all 8 stickers (pose + appearance + rainbow position + colors LOCKED). BUBABU.GE butter-cream pill at bottom-center with magenta text — IDENTICAL across all 8 stickers (NO per-category ribbon color variation)."
  },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": {
      "palette_driver": "candy-pop kids-commercial on pure white background, cyan #5BC0DE and lime #84CC16 duo accent, soft Pixar 3D"
    }
  },
  "subjects": [
    {
      "id": "screenfree_icon",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "happy soft 3D Pixar-stylized child face with large stylized eyes, toy-like proportions",
          "small warm heart beside the face",
          "tiny gentle screen-free badge — a rounded device shape with a soft diagonal line, positive not alarming"
        ],
        "heritage": "Pixar-stylized 3D child-face icon, NOT a realistic child"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.24,
          "y": 0.46,
          "z_index": 2
        },
        "visual_weight": 0.8
      },
      "appearance": {
        "age": "Pixar stylized child icon",
        "expression": "happy and reassured"
      },
      "interaction": {
        "target_id": "environment",
        "action": "smiling child face with a heart as the left icon",
        "emotional_state": "safe and warm"
      }
    },
    {
      "id": "bubabu_rainbow_arc",
      "character_dna": {
        "bone_structure": "candy_pop_6color_rainbow_arc_behind_bubabu",
        "persistent_features": [
          "small soft Candy Pop 6-color rainbow arc directly behind Bubabu's body",
          "scaled to approximately 120% of Bubabu's body radius (sized to Bubabu)",
          "color stripes in classic rainbow order: cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, orange #FF9F1C, coral #FF6B6B",
          "soft kid-pastel saturation, slightly tilted 5-10 degrees behind Bubabu's right shoulder",
          "matte flat shading — NO body-glow on Bubabu, NO rainbow shine spilling onto Bubabu's fur, NO halo effect"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — signature visual locked across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 2
        },
        "visual_weight": 0.048
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "bubabu",
        "action": "small Candy Pop rainbow arc rendered directly behind Bubabu's body, sized to him, signature brand visual",
        "emotional_state": "decorative_brand_signature"
      }
    },
    {
      "id": "bubabu_owl_badge",
      "character_dna": {
        "bone_structure": "plush round owl mascot (Bubabu — visual locked per kiosk unification)",
        "persistent_features": [
          "match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1",
          "round fluffy white plush owl mascot, ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring around each eye",
          "small triangular BLACK closed beak between the goggles (brand lock — STAYS CLOSED)",
          "caramel-brown stubby wings + caramel-brown feet with three orange toes each",
          "pure white ear tufts SAME white color as body fur",
          "soft light-grey outline so the white body reads on the white sticker background"
        ],
        "heritage": "Bubabu plush mascot, locked appearance + pose + rainbow per kiosk unification 2026-05-31 — IDENTICAL visual identity across all 8 stickers, only scale flexes (hero=big, badge=small)"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.9,
          "y": 0.82,
          "z_index": 3
        },
        "visual_weight": 0.12
      },
      "appearance": {
        "age": "plush toy",
        "expression": "serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed — IDENTICAL across all 8 stickers"
      },
      "interaction": {
        "target_id": "environment",
        "action": "tiny Bubabu owl peeking from the bottom-right",
        "emotional_state": "warm and inviting (master expression locked across all 8 stickers)"
      }
    },
    {
      "id": "bubabu_ge_domain_pill",
      "character_dna": {
        "bone_structure": "butter_cream_rounded_pill_with_magenta_brand_text",
        "persistent_features": [
          "soft rounded pill capsule, butter-cream gradient #FFFAEB top fading to #FFF6CC bottom (matches Bubabu cover override + ad cover aesthetic)",
          "pill radius equals pill height divided by 2 (soft rounded ends, no harsh corners)",
          "BUBABU.GE uppercase text inside the pill, color = deep magenta #FF1F8F (brand primary, max contrast on butter-cream)",
          "flat matte shading — NO drop shadow, NO border outline, NO gradient on text",
          "centered horizontally, bottom-third of sticker frame — IDENTICAL position across all 8 stickers"
        ],
        "heritage": "Bubabu kiosk unification 2026-05-31 — domain pill IDENTICAL across all 8 stickers"
      },
      "spatial_layout": {
        "coordinates": {
          "x": 0.5,
          "y": -0.4,
          "z_index": 4
        },
        "visual_weight": 0.25
      },
      "appearance": {
        "age": "graphic",
        "expression": "NA"
      },
      "interaction": {
        "target_id": "environment",
        "action": "butter-cream rounded pill at bottom-center carrying BUBABU.GE in deep magenta uppercase text",
        "emotional_state": "brand_signature"
      }
    }
  ],
  "scene": {
    "location": "a die-cut vinyl sticker, cloud-like organic shape, on a pure white background",
    "style_anchor": "Pure Pixar feature-film 3D render — Bao / La Luna / Up / Inside Out aesthetic. Stylized toy-like proportions, NOT photoreal, NOT live-action. Die-cut sticker look with thick white border.",
    "mise_en_scene": {
      "narrative_clutter": [
        "thick glossy white die-cut border around the whole shape",
        "soft drop shadow beneath the sticker",
        "soft Candy Pop 6-color rainbow arc directly behind Bubabu (signature brand visual, scaled to Bubabu, NO body-glow)",
        "butter-cream rounded pill at the bottom-center carrying BUBABU.GE in deep magenta uppercase text (unified across all 8 stickers per kiosk unification 2026-05-31)",
        "tiny soft warm heart accent",
        "soft cloud-like organic silhouette",
        "matte candy-pop finish"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "type": "Pixar stylized soft flat product light (NOT photoreal cinema)"
    }
  },
  "technical": {
    "camera": {
      "model": "Pixar virtual"
    }
  },
  "text_rendering": {
    "enabled": true,
    "text": "Georgian headline: ეკრანის გარეშე | Georgian benefit: უსაფრთხო თამაში და სწავლა | English subtitle: Screen-Free Gifts | Bottom ribbon banner: BUBABU.GE",
    "placement": "icon on the left; text stack on the right top-to-bottom — (1) Georgian headline in cyan, (2) Georgian benefit line, (3) small English subtitle; cyan-with-butter-cream rounded pill at the bottom-center with BUBABU.GE in deep magenta uppercase text (UNIFIED across all 8 stickers — no per-category ribbon); tiny Bubabu owl bottom-right"
  },
  "advanced": {
    "negative_prompt": [
      "no rectangle frame",
      "no straight hard border",
      "no photoreal",
      "no live-action",
      "no DSLR",
      "no real-lens DOF",
      "no film grain",
      "no HDR cinema",
      "no ARRI",
      "no Sony",
      "no Sigma",
      "no Canon",
      "no realistic owl",
      "no realistic child",
      "no photoreal kid",
      "no glow on goggles",
      "no lowercase bubabu.ge",
      "no uppercase Georgian mtavruli",
      "no Cyrillic letters",
      "no gibberish text",
      "no watermark",
      "no dark moody mood"
    ]
  }
}
```

---

## Paste protocol
1. Copy one JSON block (full outer braces).
2. **Upload `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg` to Nano Banana 2** (Bubabu refs MANDATORY per unification rule), then paste the JSON block → render.
3. Cut along the white die-cut border (kiss-cut vinyl). Shelf placement + colors → `print_spec.md`.
4. Georgian text broken after 3 tries → set `text_rendering.enabled: false`, render icon + border only, overlay text in an editor.
