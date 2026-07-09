# Bubabu - Smart Gifts Social-Page Rebrand · AVATAR (profile picture)

**Aspect:** 1:1 square · **Use:** ONE master for FB + Instagram + TikTok + YouTube profile icon
**Output:** 1080×1080 master → 320×320 → 96×96 thumbnail · **Critical:** FULL BODY (head-to-feet) visible, centered with margin all around, NOT cropped/zoomed, still legible at 96×96
**Generator:** Nano Banana 2 (paste the SPEC below) · **Generate 4 versions → pick warmest face + sharpest cyan goggles**

> The avatar = Bubabu in **FULL BODY** (whole owl head-to-feet), centered on a clean background - the round plush owl IS the brand mark. The "Smart Gifts" story lives on the **cover/banner** (`cover.md`) and in the **bio** (`bio.md`).

## REFERENCES TO UPLOAD
- `1.jpeg` ⭐ standard cyan-goggle plush state
- `2.jpeg` alt angle, standard state
- (NOT `3.jpeg` heart-eyes - avatar = standard goggles.)
Reference photo is the source of truth - match it exactly, do not invent or restyle.

## IMAGE SPEC (paste into Nano Banana 2 + upload `1.jpeg` & `2.jpeg`)
```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "user_intent": "Bubabu plush-owl brand profile icon — FULL-BODY owl (head-to-feet) centered with margin, for FB/IG/TikTok/YouTube avatar.",
  "meta": { "aspect_ratio": "1:1", "quality": "3d_render_octane", "guidance_scale": 7.5 },
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
      "interaction": { "target_id": "viewer", "action": "front-facing FULL BODY — entire owl head-to-feet visible with comfortable margin all around (NOT cropped, NOT zoomed), standing centered, slight friendly forward-tilt", "emotional_state": "warm, welcoming" }
    }
  ],
  "scene": {
    "location": "clean studio icon background — butter-cream radial gradient #FFFAEB → #FFF6CC, soft low-contrast Candy Pop sunburst rays behind the full-body owl",
    "style_anchor": "Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and material textures, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.",
    "mise_en_scene": {
      "narrative_clutter": [
        "soft low-contrast rainbow sunburst rays radiating from behind the head",
        "a few small 3D candy confetti dots drifting in the corners (NO hearts)",
        "gentle butter-cream vignette keeping the whole owl focal"
      ],
      "world_state": "new"
    },
    "lighting_advanced": { "type": "Pixar stylized bright warm studio-polish light — soft key front, gentle fill, soft rim glow on top of head", "volumetric_fog": 0 }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": false, "text": "", "placement": "" },
  "advanced": {
    "negative_prompt": [
      "no photoreal","no live-action","no DSLR / real-lens DOF","no film grain","no HDR cinema","no ARRI/Sony real-camera look","no realistic real owl/animal",
      "no eyewear-as-removable-object","no frames/lenses/strap","beak open","mouth appearing","caramel/brown beak","brown ears","brown body",
      "heart eyes","hearts in confetti","glowing/LED eyes","eye halo/godrays",
      "scary or dark mood","text in image","watermark","multiple Bubabus","deformed body","cropped owl","head or feet cut off","extreme close-up","zoomed-in owl too large filling the frame",
      "Cyrillic text","mtavruli capital Georgian","religious symbols"
    ]
  }
}
```

## SELF-CHECK
- [ ] FULL BODY head-to-feet visible · centered with margin · NOT cropped/zoomed · still recognizable at 96×96
- [ ] Cyan goggles intact (NOT removable glasses) · BLACK beak closed
- [ ] WHITE body/ears (caramel only on wings/feet)
- [ ] No baked text · no watermark
- [ ] Pixar-lock: `camera.model:"Pixar virtual"`, no lut/Kelvin/aperture/lens-mm/SSS/hdr_mode, `style_anchor` present
- [ ] No heart eyes, no hearts in confetti
- [ ] 1:1 square
