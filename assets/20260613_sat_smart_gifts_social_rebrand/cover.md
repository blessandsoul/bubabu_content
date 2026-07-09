# Bubabu - Smart Gifts Social-Page Rebrand · COVER / BANNER

**This file = the main rebrand asset.** It turns the page header into a **smart-gifts** look: Bubabu (hero owl + mascot) presenting a small cluster of **elegant wrapped gift boxes** - the visual code for "smart gifts", per the locked pivot rule "mascot physically in-frame with the assortment". No specific SKUs shown (avoids flagged-product + third-party-owl conflation). Wordmark + tagline + `BUBABU.GE` are **editor PNG overlays** (render clean, composite text in CapCut/Photoshop - see `name.md` lockup).

- **Facebook cover** → §1 (851×315)
- **YouTube banner** → §2 (2560×1440)
- **Instagram + TikTok** → no cover/banner exists on these. Profile = `avatar.md` + bio only. Nothing to render here.

## REFERENCES TO UPLOAD (both SPECs)
- `1.jpeg` ⭐ standard cyan-goggle plush state · `2.jpeg` alt angle · (NOT `3.jpeg` heart-eyes)
- Reference photo = source of truth; match exactly.

---

## §1 · FACEBOOK COVER

**Target:** 851×315 px (render 2× = 1702×630). Wide ~21:9 hero band.
**Safe zones:** bottom-left 170×170 = avatar overlay (keep clean) · bottom 100 px = mobile UI band (keep wordmark/domain above it) · center 60% = primary readable area.

### IMAGE SPEC (paste into Nano Banana 2 + upload refs)
```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "user_intent": "Facebook cover banner — Bubabu owl as the gift-shop mascot presenting elegant wrapped gifts; warm, premium-but-playful 'smart gifts' hero. Clean zones reserved for editor wordmark + avatar overlay.",
  "meta": { "aspect_ratio": "21:9", "quality": "3d_render_octane", "guidance_scale": 7.5 },
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
      "spatial_layout": { "coordinates": { "x": 0.5, "y": 0.5, "z_index": 2 }, "visual_weight": 0.55 },
      "appearance": {
        "age": "ageless plush mascot",
        "expression": "warm welcoming pride, gentle eye contact, soft bouncy energy, beak closed"
      },
      "interaction": { "target_id": "wrapped_gifts", "action": "STANDING in FULL BODY — entire owl visible head-to-feet with comfortable margin above the head and below the feet, NOT cropped; owl height ~75% of the banner, standing beside a small cluster of wrapped gifts and presenting one small ribboned gift toward the viewer", "emotional_state": "warm, generous, inviting" }
    }
  ],
  "scene": {
    "location": "soft Pixar gift-nook, FULL-BODY WIDE framing — Bubabu shown head-to-feet (NOT cropped) standing on a warm cream studio floor/ledge with a curated cluster of wrapped gifts beside him; left third kept as clean butter-cream gradient for avatar safety; soft sunburst behind",
    "style_anchor": "Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and material textures, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.",
    "mise_en_scene": {
      "narrative_clutter": [
        "3-4 elegant wrapped gift boxes with ribbons + bows in Candy Pop colors, clustered around Bubabu (generic gifts, NO branded products, NO labels)",
        "one soft gift bag with tissue paper peeking out",
        "a soft cream display ledge suggesting a curated gift assortment",
        "soft low-contrast rainbow sunburst rays behind Bubabu",
        "scattered 3D candy confetti — stars, dots, ribbons (NO hearts) — drifting in the upper third",
        "clean empty butter-cream zone in the LEFT THIRD + bottom-left for avatar overlay safety",
        "clean calm band across TOP-CENTER + BOTTOM-CENTER reserved for editor wordmark + domain (no objects there)"
      ],
      "world_state": "new"
    },
    "lighting_advanced": { "type": "Pixar stylized bright warm studio-polish light — soft key front-left, gentle fill, soft rim glow", "volumetric_fog": 0 }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": false, "text": "", "placement": "" },
  "advanced": {
    "negative_prompt": [
      "no photoreal","no live-action","no DSLR/real-lens DOF","no film grain","no HDR cinema","no ARRI/Sony real-camera look","no realistic real owl/animal",
      "no second owl","no other owl toy near Bubabu","no eyewear-as-removable-object","beak open","caramel/brown beak","brown ears","brown body",
      "heart eyes","hearts in confetti","glowing/LED eyes",
      "cropped owl","owl head or feet cut off","extreme close-up","zoomed-in owl filling the frame","owl too large",
      "baked text/letters/wordmark in image","watermark","objects in bottom-left avatar zone","busy chaotic composition","multiple Bubabus",
      "Cyrillic text","mtavruli capital Georgian","religious symbols","branded product packaging or readable labels"
    ]
  }
}
```

### SAFE ZONE MAP + EDITOR OVERLAY
```
┌──────────────────────────────────────────────────┐
│        [overlay: ბუბაბუ · SMART GIFTS]           │  ← top-center clean band
│                                                  │
│  [empty       🦉 full-body BUBABU (head→feet)   │
│   butter      standing, wrapped gifts beside    │
│   cream]      him on a cream ledge               │
│                                                  │
│            [overlay: AI Toys · ... · BUBABU.GE]  │  ← above bottom 100px
│─◯ avatar ────────────────────────────────────────┘
   170×170
```
**Editor overlay (PNG, real fonts - see `name.md`):** top-center `ბუბაბუ` (cyan plush, Noto Sans Georgian Bold) + `SMART GIFTS` (yellow/cream sans) · bottom-center `AI Toys · Educational Gifts · Smart Surprises` + `BUBABU.GE` (uppercase). Keep all text above the bottom 100px mobile band and out of the bottom-left avatar zone.

---

## §2 · YOUTUBE BANNER (channel art)

**Target:** 2560×1440 px. **TV/desktop/mobile safe area = center 1546×423** - ALL critical art (owl + key gifts + wordmark + `BUBABU.GE`) must sit inside this center box; gifts/sunburst spread to the wide edges as decorative, croppable fill.

### IMAGE SPEC (paste into Nano Banana 2 + upload refs)
```json
{
  "schema_version": "PROMPT_ENGINE_v3.0",
  "schema_kind": "image",
  "user_intent": "YouTube channel banner — Bubabu owl as gift-shop mascot presenting wrapped gifts, key art centered inside the TV-safe area, decorative gifts/sunburst bleeding to the wide edges.",
  "meta": { "aspect_ratio": "16:9", "quality": "3d_render_octane", "guidance_scale": 7.5 },
  "sequence_logic": {
    "shot_type": "master_shot",
    "color_grading": { "palette_driver": "Candy Pop kids-brand palette — Bubabu Cyan #5BC0DE goggles (sacred), butter-cream #FFFAEB ground, lime/yellow/orange/coral/magenta gift + sunburst accents" }
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
      "spatial_layout": { "coordinates": { "x": 0.5, "y": 0.5, "z_index": 2 }, "visual_weight": 0.55 },
      "appearance": {
        "age": "ageless plush mascot",
        "expression": "warm welcoming pride, gentle eye contact, soft bouncy energy, beak closed"
      },
      "interaction": { "target_id": "wrapped_gifts", "action": "STANDING in FULL BODY — entire owl visible head-to-feet with comfortable margin above the head and below the feet, NOT cropped; owl height ~60% of the center safe area, centered, standing among wrapped gifts and presenting one ribboned gift toward the viewer", "emotional_state": "warm, generous, inviting" }
    }
  ],
  "scene": {
    "location": "soft Pixar gift-nook spanning a wide 16:9 frame, FULL-BODY framing — Bubabu shown head-to-feet (NOT cropped) standing centered inside the TV-safe box with key wrapped gifts beside him; more wrapped gifts + sunburst rays spread symmetrically to the left/right edges as croppable decoration",
    "style_anchor": "Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and material textures, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.",
    "mise_en_scene": {
      "narrative_clutter": [
        "a centered cluster of 3-4 elegant wrapped gift boxes with ribbons + bows in Candy Pop colors around Bubabu (generic, NO branded products, NO labels)",
        "more wrapped gifts repeating toward the left + right wide edges as symmetric croppable fill",
        "soft cream display ledge suggesting a curated gift assortment",
        "soft low-contrast rainbow sunburst rays radiating from center",
        "scattered 3D candy confetti — stars, dots, ribbons (NO hearts)",
        "calm clean center band reserved for the editor wordmark + domain (no objects overlapping it)"
      ],
      "world_state": "new"
    },
    "lighting_advanced": { "type": "Pixar stylized bright warm studio-polish light — soft key, gentle fill, soft rim glow", "volumetric_fog": 0 }
  },
  "technical": { "camera": { "model": "Pixar virtual" } },
  "text_rendering": { "enabled": false, "text": "", "placement": "" },
  "advanced": {
    "negative_prompt": [
      "no photoreal","no live-action","no DSLR/real-lens DOF","no film grain","no HDR cinema","no ARRI/Sony real-camera look","no realistic real owl/animal",
      "no second owl","no other owl toy near Bubabu","no eyewear-as-removable-object","beak open","caramel/brown beak","brown ears","brown body",
      "heart eyes","hearts in confetti","glowing/LED eyes",
      "cropped owl","owl head or feet cut off","extreme close-up","zoomed-in owl filling the frame","owl too large",
      "baked text/letters/wordmark in image","watermark","critical art outside center safe area","multiple Bubabus","busy chaotic composition",
      "Cyrillic text","mtavruli capital Georgian","religious symbols","branded product packaging or readable labels"
    ]
  }
}
```

**Editor overlay (PNG):** inside the center 1546×423 safe box - `ბუბაბუ` (cyan plush) + `SMART GIFTS` + `BUBABU.GE` (uppercase). Per `name.md` lockup.

---

## SELF-CHECK (both SPECs)
- [ ] **Owl FULL BODY - head-to-feet visible, STANDING, NOT cropped, NOT zoomed** (FB ~75% / YT ~60% of frame height, margin above head + below feet)
- [ ] Bubabu identity: WHITE body/ears, cyan goggles, BLACK closed beak, caramel only wings/feet
- [ ] Gift motif present (generic wrapped gifts) - reads as "smart gifts", NO specific/branded SKUs, NO labels
- [ ] **No second owl / other owl toy** (third-party Musical Owl conflation ban)
- [ ] Pixar-lock: `camera.model:"Pixar virtual"`, no lut/Kelvin/aperture/lens-mm/SSS/hdr_mode, `style_anchor` present
- [ ] `text_rendering.enabled:false` - wordmark/domain are editor overlays only
- [ ] FB: bottom-left 170×170 clean for avatar · text above bottom 100px mobile band
- [ ] YT: all critical art + wordmark + `BUBABU.GE` inside center 1546×423 safe area
- [ ] `BUBABU.GE` uppercase in overlay · Mkhedruli only · no Cyrillic/mtavruli
- [ ] No hearts (eyes or confetti) · no banned dilution wording in any overlay
