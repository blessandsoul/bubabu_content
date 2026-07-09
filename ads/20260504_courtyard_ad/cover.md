# Video Cover / Thumbnail - "ეზოს ბიჭები"

**Use:** YouTube thumbnail / Facebook video cover / Instagram Reels cover / TikTok cover frame
**Engine:** Bubabu COVER OVERRIDE per `feedback_bubabu_cover_override_baked_text.md` (NOT default COVER_ENGINE)
**Path:** PRIMARY baked-text (Nano Banana 2 / Imagen 3 / Midjourney v7 render directly into image). FALLBACK editor-overlay only after 3+ retries fail Mkhedruli.
**Master ratio:** 16:9 (1920×1080) → crops 1:1 / 9:16 / 4:5 / 851×315
**Style:** Pixar 3D × Squishmallow × Jellycat × Candy Pop kids-commercial brand polish - NOT editorial / tabloid / press chrome

---

## DESIGN CONCEPT

**Hook mechanic:** curiosity gap - viewer sees three Pixar 3D Georgian boys leaning in with WONDER faces + Bubabu plush owl in foreground center = "what just happened?" → click.

**Emotional read:** PURE AMAZEMENT (NOT shock, NOT fear) - Pixar wonder face. Plus Candy Pop joy.

**Style anchors:** Pixar Animation Studios × Coco family wonder × Squishmallow brand banner × Jellycat plush warmth × Build-a-Bear product photography. NEVER editorial / tabloid / broadcast-chyron.

---

## REFERENCES TO UPLOAD

- `1.jpeg` ⭐ standard cyan-eye plush state
- `2.jpeg` alt angle, standard state
- `character_bubabu.md` color lock (BLACK beak `#1A1A1A` / caramel-brown `#A47551` wings / white body / printed-fabric cyan eyes - NO LED glow)
- `main_boy_ref.png` (orange-stripe boy - Main Hero)
- `friend1_ref.png` (olive-hoodie glasses boy)
- `friend2_ref.png` (yellow-tee bracelet boy)

(Heart-state ref `3.jpeg` NOT used - cover = standard cyan eyes only.)

---

## FINAL RENDER LIST (exact text strings to bake into image)

| Position | Text | Notes |
|----------|------|-------|
| Top-center | `ბუბაბუ` | Plush-fabric Mkhedruli wordmark |
| Bottom third | `რა ელოდებოდათ ოთახში?` | Curiosity-gap headline - pure question, "what was waiting for them in the room?" |
| Top-right | `360 ₾` | Magenta circle price sticker |
| Bottom-center | `bubabu.ge` | Lime-orange gradient URL pill |

---

## LATIN WHITELIST (only these Latin strings allowed)

```
360 ₾
bubabu.ge
```

## MKHEDRULI WHITELIST (only these Mkhedruli strings allowed)

```
ბუბაბუ
რა ელოდებოდათ ოთახში?
```

## NEGATIVE TEXT (banned variants - must NOT appear in baked render)

```
mtavruli capital Georgian (ბუბაბუ in capitals = banned)
Cyrillic text of any kind
English transliteration of Mkhedruli ("bubabu" lowercase Latin in place of "ბუბაბუ" wordmark)
"BUBABU" all-caps Latin
character names "ბერნარდი" / "ნიკა" / quoted dialogue text
URL prefix "https://" or "www."
"360 GEL" / "360 lari" written-out Latin
typography spec leak: "Bold weight 900" / "Bricolage" / "26px" / "letter-spacing" / "Mkhedruli" / "Noto Sans"
character speech bubbles or comic dialogue
```

---

## IMAGE PROMPT (single compiled - text BAKED IN)

```
Pixar 3D animation kids-commercial video cover composition, wide 16:9 landscape 1920x1080. Hyper-saturated Candy Pop maximalist brand aesthetic. Style anchors: Pixar Animation Studios × Coco family wonder × Squishmallow brand × Jellycat plush warmth × Build-a-Bear product photography.

CENTER FOREGROUND: Bubabu plush owl (~25% of frame width — NOT giant, NOT realistic owl). Match attached `1.jpeg` + `2.jpeg` plush form EXACTLY 1:1. [pose: front-facing cute friendly stance, wings folded at sides, slight tilt] [expression: warm magnetic wonder, eye contact with viewer].

BEHIND BUBABU: three Pixar 3D Georgian boys arranged in shallow arc, leaning IN toward Bubabu with positive WONDER faces (delighted amazement, NOT fear, NOT shock):
— LEFT: olive-green-hoodie boy with thick-frame black glasses, thick wavy dark hair, strong dark eyebrows, jaw dropped open in awe
— CENTER (slightly higher): orange-stripe-tee boy with white tee + horizontal orange chest stripe, dark messy hair, small chin scar, eyes wide with delighted wonder, small smile starting to form
— RIGHT: tall yellow-tee boy with friendship bracelet on left wrist, dark side-swept hair, eyes huge with awe, mouth slightly open

All three boys' faces lit softly from butter-cream window light, NOT cyan-projected. Warm Pixar skin tones, no sci-fi cyan stripes on faces.

BACKGROUND: butter-cream radial gradient `#FFFAEB` to `#FFF6CC`. Soft hyper-saturated rainbow sunburst rays radiating gently from behind Bubabu in Candy Pop palette (lime `#84CC16`, sunny yellow `#FFEB3B`, hot orange `#FF9F1C`, candy coral `#FF6B6B`, hot magenta `#FF1F8F`, candy sky-blue `#5BC0DE`) — low-contrast so faces and Bubabu stay focal.

UPPER FOREGROUND: scattered 3D candy confetti — small stars, dots, ribbons, sparkles in Candy Pop palette colors drifting upper third. NO hearts in confetti.

BAKED TEXT ELEMENTS (render directly into image at exact positions and styles below):

1. TOP-CENTER (~6% from top, ~18% width): plush-fabric Mkhedruli wordmark "ბუბაბუ" rendered as soft stuffed-plush fabric letters with fleece fiber surface texture (slightly fuzzy, NOT glossy NOT chrome NOT balloon), stitched seams in darker navy thread visible along letter edges, subtle fuzz halo, solid cyan turquoise color across all letters, soft drop shadow.

2. TOP-RIGHT CORNER (~5% from top, ~5% from right): hot magenta `#FF1F8F` 3D circle stamp/badge with thick lime-green `#84CC16` border ring, slight 8-degree counterclockwise tilt, soft drop shadow underneath. ON THE STICKER: chunky white sans-serif Latin "360 ₾" big bold with subtle 3D bevel.

3. BOTTOM THIRD (~70% from top, full width centered): chunky bold rounded headline text "რა ელოდებოდათ ოთახში?" in dark navy `#2A6B8A` Mkhedruli, with soft white glow halo for legibility on the butter-cream and confetti backdrop, single line preferred (two lines max), mobile-readable at thumbnail size. Question mark fully visible — it carries the curiosity hook.

4. VERY BOTTOM (~92% from top, leaving 8% mobile-UI safe zone clear, ~22% width centered): chunky rounded horizontal pill capsule with lime to sunny-yellow to hot-orange gradient fill, thick white outline, soft drop shadow. ON THE PILL: chunky white Latin "bubabu.ge" with white arrow "→" on right edge.

LIGHTING: bright 5500K commercial product light, soft drop shadows under Bubabu and boys. NO rim glow on Bubabu plush. Warm golden tone on boys' cheeks. Cyan stays inside Bubabu's printed eye area only — no cyan lighting projected onto faces or surfaces.

QUALITY TAIL: Octane render, subsurface scattering on plush fabric and on boys' skin, crisp readable text at every overlay element, mobile-thumbnail legibility at 320px wide, hyper-saturated Candy Pop maximalist polish. Clean composition, locked tight framing, no dutch angle, no tilted camera.

NEGATIVE: glasses on Bubabu, aviator goggles, eyewear on Bubabu, frames, lenses, strap, beak open, mouth appearing on Bubabu, second mouth, scared faces on kids, fear, horror, panic, traumatized look, dramatic dark mood, dramatic shadows, photorealistic real owl, Bubabu becoming giant, Bubabu transforming, Bubabu shape-shifting, Bubabu gaining real feathers/talons, anime, 2D flat, cel-shaded outline, glowing eyes, LED eyes, eye halo, eye godrays, eye rim light, spaceship aesthetic, sci-fi glow on plush, cyan rays projecting on kids' faces or bodies, neon stripes on cheeks, light beams across surfaces, heart eyes, heart-shape pulse, heart pattern in eyes, pink hearts anywhere, hearts in confetti, blinking eye, winking eye, eyelid sliding, mtavruli capital Georgian, Cyrillic text, English transliteration of Mkhedruli, "BUBABU" all-caps Latin, "360 GEL" written-out, "https://" URL prefix, "www." URL prefix, character names visible, character speech bubbles, comic dialogue, blurry text rendering, illegible Mkhedruli, typography spec text "weight 900" "26px" "Bricolage" "Mkhedruli", religious symbols, watermark, tilted camera, dutch angle, multiple Bubabus, deformed body, editorial paper grain texture, antique gold filigree, red ink stamp, "EXCLUSIVE" burst sticker chrome, tabloid magazine masthead 3D extruded gold, broadcast chyron lower-third.
```

**Aspect ratio:** 16:9 master (1920×1080)
**Generate:** 6-8 versions → pick clearest wonder-face expressions + cleanest Mkhedruli rendering across all baked elements

---

## SELF-CHECK (≥8/10 to ship)

- [ ] All 4 text elements rendered correctly and legible (per FINAL RENDER LIST)
- [ ] Mkhedruli wordmark "ბუბაბუ" + headline "სამმა ბიჭმა ტელეფონი ერთად დააგდო" both clean (no mtavruli drift, no Cyrillic, no Latin transliteration)
- [ ] Latin "360 ₾" + "bubabu.ge" clean (no extra characters, no smudge)
- [ ] No banned text variants present (per NEGATIVE TEXT block)
- [ ] No typography-spec vocabulary visible in baked text
- [ ] Bubabu plush form correct: BLACK beak `#1A1A1A`, caramel-brown wings, white body, printed cyan plush eyes (NO LED glow / NO halo / NO heart eyes)
- [ ] All 3 boys' WONDER faces (positive amazement, NOT fear / shock / panic)
- [ ] Boys' faces lit warm window light, NOT cyan-projected
- [ ] Candy Pop palette locked (butter-cream BG, cyan/magenta/lime/yellow accents - NO editorial desaturated 60-20-10)
- [ ] Bubabu hero ~25% of frame width, NOT giant realistic owl
- [ ] No editorial chrome (NO antique gold filigree / NO red ink stamp / NO `EXCLUSIVE` burst / NO Dinastia-style masthead / NO press-paper texture)
- [ ] No character names anywhere on cover
- [ ] Mobile readable at 320 px wide thumbnail
- [ ] References enumerated (`1.jpeg` + `2.jpeg` + boy refs uploaded with prompt)
- [ ] Channel restriction: Bubabu + Axiom Smart channels only

---

## A/B/C/D HEADLINE VARIANTS (test 4 versions if launching paid)

Same baked-text path, swap only the headline string in IMAGE PROMPT element 3:

| Variant | Headline (Mkhedruli) | Hook angle |
|---------|---------------------|-----------|
| **A** ⭐ | `რა ელოდებოდათ ოთახში?` | pure question / curiosity gap (recommended baseline - "what was waiting for them in the room?") |
| **B** | `ის პირველი ლაპარაკობს` | magic moment / product reveal |
| **C** | `ცოცხალი მეგობარი — ეკრანის გარეშე` | direct value (good for cold audience) |
| **D** | `სამი ბიჭი. სამი ტელეფონი. ერთი მეგობარი.` | three-beat rhythm / arithmetic mystery (3+3=1) |

When swapping headline, also update MKHEDRULI WHITELIST + NEGATIVE TEXT to match.

**Test plan:** start with A on FB/YT, B for IG Reels cover, C for paid ads, D for organic Reels.

---

## PLATFORM CROPS

| Platform | Ratio | Crop strategy |
|----------|-------|---------------|
| YouTube thumbnail | 16:9 | Master 1920×1080 - primary deliverable |
| Facebook video cover | 16:9 → 1280×720 | Same as YouTube |
| Instagram feed video | 1:1 → 1080×1080 | Crop center - keep Bubabu + center boy + headline, lose left/right edges |
| Instagram Reels cover | 9:16 → 1080×1920 | Vertical reframe - Bubabu top half, headline middle, kids' faces tighter behind Bubabu |
| TikTok cover | 9:16 → 1080×1920 | Same as Reels |
| FB / IG Story | 9:16 | Same as Reels |
| FB cover banner (page) | 851×315 → 16:5.7 | Use brand FB cover instead - see `agents/bubabu/content/20260504_social_brand_assets/facebook_cover.md` |

---

## FALLBACK - EDITOR-OVERLAY (only if 3+ retries fail Mkhedruli baked render)

If Nano Banana / Imagen / Midjourney consistently fail to render Mkhedruli wordmark "ბუბაბუ" or headline "სამმა ბიჭმა ტელეფონი ერთად დააგდო":

1. Generate clean photograph WITHOUT failing Mkhedruli element (mark empty zone in prompt)
2. Latin text + numerals + URL still bake in (modern generators handle Latin reliably)
3. Add failed Mkhedruli string as PNG overlay in CapCut / Photoshop using real **Noto Sans Georgian Bold** tinted to match the surrounding text element's color (cyan for wordmark, navy for headline)
4. Match position + size + drop shadow + outline per IMAGE PROMPT visual styling

This guarantees crisp Mkhedruli at the cost of an extra editor step. Use only when generator proves stubborn on specific Georgian strings - not as default path.

---

## CHANNEL RESTRICTION

Courtyard ad cover ships only on:
- Bubabu official Facebook / Instagram / TikTok / YouTube channels
- Axiom Smart official social channels
- Bubabu.ge website / product page
- Bank of Georgia co-promo with their approval

NEVER on user's personal channels (Andrew Altair / aiNOW personal / personal series accounts) without explicit Axiom Smart sign-off.
