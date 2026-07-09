# Bubabu - Box Label Strip (AI Companion)

**Asset:** printed sticker for toy box. Final size **25 × 2.5 cm = 10:1 strip**.
**Headline added by USER in editor (NOT baked):** `ბუბაბუ — კომპანიონი ხელოვნური ინტელექტით`
**Style:** candy-pop, matches the colorful 30% poster - butter-cream BG, multicolor sunburst rays, candy confetti, Bubabu hero.
**Refs to upload to Nano Banana 2:** `1.jpeg` + `2.jpeg` (normal cyan-eye plush). NEVER `3.jpeg` heart-eyes.

## Layout - TOP-CONCENTRATED (user crops the bottom off)
All meaningful content packed into the **TOP band**. Bottom ~40% is plain butter-cream = disposable crop margin.
- **Top-left:** Bubabu plush mascot, wings raised in cheerful celebration, sized to the top band.
- **Top, behind mascot:** multicolor sunburst rays fanning rightward; candy confetti + curly streamers along the **TOP edge only**.
- **Top-right:** CLEAN low-clutter butter-cream zone reserved for the user's Georgian headline.
- **Bottom ~40%:** plain empty butter-cream, NO elements, NO confetti - pure croppable margin.
- Text zone stays empty: `text_rendering.enabled = false`, negative bans all letters.

## NANO BANANA 2 - IMAGE SPEC

```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "user_intent": "Ultra-wide horizontal product-box LABEL STRIP (target print 25x2.5cm, 10:1). ALL content concentrated in the TOP band of the frame — the bottom ~40% is plain empty butter-cream that will be cropped off. Bubabu plush owl mascot anchored at TOP-LEFT with wings raised in celebration, a multicolor candy-pop sunburst fanning rightward behind it, confetti and curly streamers along the TOP edge only; the top-right is a clean uncluttered butter-cream area left intentionally empty for a headline to be added later in the editor. The lower portion of the frame is pure flat butter-cream with no elements. PURE Pixar 3D candy-pop kids-commercial look. NO baked text.",
  "meta": {
    "aspect_ratio": "21:9",
    "quality": "3d_render_octane",
    "seed": 5290011,
    "guidance_scale": 8.0
  },
  "sequence_logic": {
    "shot_type": "establishing_shot",
    "color_grading": {
      "palette_driver": "Candy-Pop kids-commercial: butter-cream cream base with cyan #5BC0DE, magenta #FF1F8F, lime #84CC16, yellow #FFEB3B, coral #FF6B6B, orange #FF9F1C accents",
      "lut_simulation": "High-saturation glossy print, clean bright",
      "contrast": "high_key"
    },
    "temporal_effects": "freeze_frame"
  },
  "subjects": [
    {
      "id": "Bubabu_mascot",
      "character_dna": {
        "bone_structure": "delicate",
        "persistent_features": [
          "round fluffy plush owl mascot, snowball ball-shaped body",
          "cyan-turquoise circular eye-goggle markings with cream-beige inner ring and yellow upper eyelid arcs",
          "small black closed triangle beak, caramel-brown stubby side wings, caramel-brown feet with three orange toes"
        ],
        "heritage": "Bubabu plush mascot, match uploaded 1.jpeg + 2.jpeg EXACTLY 1:1"
      },
      "spatial_layout": {
        "coordinates": { "x": -0.72, "y": 0.62, "z_index": 2 },
        "visual_weight": 0.55
      },
      "appearance": {
        "age": "plush toy",
        "expression": "bright cheerful welcome, eyes wide, both wings raised up in joyful celebration",
        "clothing": []
      },
      "interaction": {
        "target_id": "",
        "action": "positioned in the TOP-LEFT of the frame, wings raised in celebration, body angled slightly toward the open top-right banner zone as if presenting it",
        "emotional_state": "joyful, warm, welcoming"
      }
    }
  ],
  "scene": {
    "location": "ultra-wide horizontal box-label strip on a seamless studio candy-pop backdrop, all elements concentrated in the top band",
    "mise_en_scene": {
      "narrative_clutter": [
        "multicolor sunburst rays (cyan, magenta, lime, yellow, coral, orange) fanning out from behind the mascot toward the top-right",
        "scattered rounded candy confetti dots in the brand palette, top region only",
        "curly paper streamers ribboning along the TOP edge only",
        "a few small rounded five-point stars near the top",
        "soft floating bokeh sparkles, low density, upper area",
        "clean empty butter-cream banner field in the top-right reserved for headline",
        "lower 40 percent of the frame: flat plain butter-cream, no elements, disposable crop margin"
      ],
      "world_state": "new"
    },
    "lighting_advanced": {
      "color_temperature": 5500,
      "type": "cinematic",
      "volumetric_fog": 0.0
    }
  },
  "technical": {
    "camera": {
      "model": "ARRI Alexa Mini",
      "lens": "24mm_wide",
      "aperture": "f/8.0"
    },
    "material_science": {
      "roughness_global": 0.55,
      "subsurface_scattering": true,
      "reflections": "diffuse"
    }
  },
  "text_rendering": {
    "enabled": false,
    "text": "",
    "placement": ""
  },
  "advanced": {
    "negative_prompt": [
      "no text", "no letters", "no words", "no numbers", "no typography", "no captions", "no logo text", "no Cyrillic script",
      "no glow on body", "no goggle illumination", "no LED eyes", "no brown body (only wings and feet caramel)", "no open beak", "no heart-shaped eyes", "no second owl", "no realistic photographic owl",
      "no scary or dark mood", "no halo or aura", "no paper grain or gritty texture",
      "no deformed plush", "no warped face", "no watermark or signature", "blurry", "low-res"
    ],
    "hdr_mode": true
  }
}
```

## PRINT NOTE (read before generating)
- NB2 native widest = **21:9** (2.33:1). True **10:1** is not a native ratio.
- **Recommended:** generate at 21:9 → in editor **crop the BOTTOM off** down to the 2.5cm band. All content (mascot + rays + empty headline field) sits in the TOP band; the lower 40% is plain cream → crop it away cleanly. Mascot is sized to the top band, survives the crop.
- Alt: generate 21:9, then **outpaint width** left/right if you need more empty banner before placing text.
- Print: add **3 mm bleed** all sides, export **CMYK** (the cyan/magenta will shift slightly vs RGB - fine for this palette).
- Headline goes in the right cream zone, mkhedruli lowercase, your own typesetting.

## SELF-CHECK
- [x] Refs `1.jpeg`+`2.jpeg` instructed (no `3.jpeg`), no appearance re-dump in prose body
- [x] `text_rendering.enabled=false` + negatives ban all letters → clean zone for user text
- [x] Cyan goggles = printed fabric, beak closed, white body / caramel wings-feet (negatives enforce)
- [x] Candy-pop palette + sunburst + confetti = matches the 30% poster
- [x] No Cyrillic / no Russian in file · headline is Georgian mkhedruli
- [x] NB2 v3.2 image SPEC, strict-floor fields populated (seed, ≥3 persistent_features, ≥5 narrative_clutter, Kelvin, camera, ≥15 negatives)
- [ ] **L4 viewer/print test pending** - render + crop to 10:1 + eyeball before sticking on box
