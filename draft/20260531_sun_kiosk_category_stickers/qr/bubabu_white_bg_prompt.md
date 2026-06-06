# Bubabu on pure white BG — Nano Banana 2 prompt

**Purpose:** isolate Bubabu plush from 1.jpeg + 2.jpeg refs onto pure white background. Use as cleaner center logo for QR (or any sticker where you need Bubabu cutout-style on white).

**Upload to NB2:** `C:\Users\User\Desktop\BUBABU\1.jpeg` + `C:\Users\User\Desktop\BUBABU\2.jpeg` (mandatory plush refs).

**Aspect:** 1:1 square (best for QR center, easy to crop later).

**📎 ЗАГРУЗИТЬ В NANO BANANA 2:** `1.jpeg` + `2.jpeg` (mandatory)

## SPEC

```json
{"schema_version":"PROMPT_ENGINE_v3.0","schema_kind":"image","scene_id":"bubabu_white_bg_isolated","meta":{"aspect_ratio":"1:1","quality":"ultra","seed":105050001,"guidance_scale":8.0},"sequence_logic":{"shot_type":"product_cutout_isolated","color_grading":{"palette_driver":"Bubabu plush colors on pure white background, no environment, no atmosphere"}},"subjects":[{"id":"bubabu","character_dna":{"bone_structure":"plush round owl mascot (Bubabu — appearance from uploaded refs only)","persistent_features":["match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1","round fluffy white plush owl mascot, ball-shaped body","cyan-turquoise circular eye-goggle markings with cream-beige inner ring","small triangular BLACK closed beak (brand lock — STAYS CLOSED)","caramel-brown stubby wings + caramel-brown feet with three orange toes","pure white ear tufts SAME white color as body fur","Bubabu rendered IDENTICAL to the uploaded reference photos"],"heritage":"Bubabu plush mascot, isolated cutout for QR center / sticker logo"},"spatial_layout":{"coordinates":{"x":0,"y":0,"z":0.5},"visual_weight":0.85},"appearance":{"age":"plush toy","expression":"serene closed-mouth, calm warm friendly, head facing forward, eyes soft warm centered, beak closed"}}],"scene":{"location":"pure solid white background #FFFFFF — NO environment, NO atmosphere, NO floor, NO shadow ground, NO sky, NO context. Bubabu isolated like a product cutout on a clean white catalog page","style_anchor":"Pure Pixar feature-film 3D render — Bao / La Luna / Up / Monsters Inc / Inside Out aesthetic. Stylized geometry, toy-like proportions, NOT photoreal, NOT live-action, NOT cinematic film. Clean product cutout style on white.","mise_en_scene":{"narrative_clutter":["Bubabu centered in frame","pure solid white background #FFFFFF filling the entire canvas around Bubabu","NO drop shadow beneath Bubabu","NO atmospheric haze","NO gradient","NO vignette","NO other objects","NO text","NO sparkles","NO confetti","NO rainbow"],"world_state":"isolated_product_cutout"},"lighting_advanced":{"type":"Pixar stylized soft flat product light (NOT photoreal cinema) — even diffuse light from front, no harsh shadows, no rim lighting, no atmospheric volumetrics"}},"technical":{"camera":{"model":"Pixar virtual"}},"text_rendering":{"enabled":false},"advanced":{"negative_prompt":"no background other than pure white #FFFFFF, no environment, no atmosphere, no sky, no clouds, no floor, no ground surface, no drop shadow on ground, no scene context, no other objects, no other characters, no text, no signs, no Latin letters, no Cyrillic, no Mtavruli capital Georgian, no logo, no watermark, no sparkles, no confetti, no rainbow, no aura, no halo, no glow on Bubabu body, no goggle illumination, no goggles glowing, goggles matte printed fabric throughout, no character drift, no second Bubabu, no double Bubabu, no extra owls, no brown ears, no caramel ears, no 3.jpeg heart-eyes variant, no open beak, no lip-sync, no eyelashes, no blink, no realistic owl, no scary owl, no plastic toy hard look, no 2d drawing, no flat illustration, no religious symbols, no gold leaf, no peach-pink, no lavender, no pure-white-glow on body, no second human, no child, no parent, watermark, blurry, low quality, deformed, deformed hands, extra fingers, no photoreal, no live-action, no DSLR, no real-skin SSS, no real-lens DOF, no film grain, no HDR cinema, no ARRI, no Sony, no Sigma, no Canon, no realistic anatomy, no gradient background, no vignette, no atmospheric haze, no fog"}}
```

## Pre-render checks

- [ ] Both `1.jpeg` + `2.jpeg` uploaded to Nano Banana 2 (mandatory — generator uses them as appearance source).
- [ ] Aspect 1:1 square.
- [ ] After render: pure white background, NO shadow, NO atmosphere, Bubabu visible from his classic 3/4 angle, beak closed, goggles matte cyan.

## If first render adds shadow / atmosphere drift

Re-prompt explicitly: «pure solid white background only, NO drop shadow, NO atmospheric haze, like a product cutout on a clean white catalog page».

If 3+ retries fail → manual background removal in editor (Photoshop / GIMP / online remove.bg).

## Post-render usage

1. Save NB2 output as `bubabu_white.png` (or `bubabu_white.jpg`).
2. Place in: `C:\Users\User\Desktop\BUBABU\bubabu_white.png` (alongside 1/2/3.jpeg refs).
3. Update QR script to use `bubabu_white.png` instead of `1.jpeg`:
   - Change `BUBABU_REF` constant at top of `scripts/bubabu_qr_maximal.py` from `1.jpeg` to `bubabu_white.png`.
4. Re-run script → QR center will use the cleaner cutout.

## Calibration

L1 FORMAT — SPEC ready to paste. L2 SPEC — Pixar lock + no-appearance-dump (refs attached) + isolated cutout vocabulary. L3 — PENDING NB2 render (will it actually produce clean white-only BG?). L4 — viewer test = does cleaner cutout improve QR center visual?
