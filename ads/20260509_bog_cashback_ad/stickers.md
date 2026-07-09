# Stickers - Chroma-Key Overlay Assets

**Purpose:** ALL Georgian text + branded badges generated as separate AI assets on **chroma-key BLUE `#0000FF` background** (NOT green). Designer cuts the blue in CapCut/After Effects and composites stickers over the main Bubabu video.

⚠️ **WHY BLUE, NOT GREEN - Chroma Key Color Safety rule (`feedback_chroma_key_color_safety.md`):**
Bubabu Candy Pop sticker palette contains **lime `#84CC16`** + **yellow `#FFEB3B`** + **cyan `#5BC0DE`**. All three share the GREEN channel. On a `#00B140` green chroma key, the de-spill step strips the green channel from EVERYTHING in frame - yellow becomes orange, lime becomes brown, cyan becomes blue. User incident 2026-05-06: shipped on green chroma → "сейчас я срезал зеленый и желтый стал оранжевым". Fix: BLUE chroma `#0000FF` strips blue channel - kills only blues/purples in palette, but Bubabu sticker palette has zero pure blues, so warm + green-family colors survive intact.

**Why this approach (chroma-key isolation in general):**
- Mkhedruli text rendering on AI = 60-90% failure rate when mixed with full scene
- Isolating each sticker on chroma blue = generator focuses ONLY on text + shape, success rate jumps to 70-85%
- Each sticker can be regenerated independently if it fails - no need to redo the whole video
- Designer has full timing/position control in editor

**6 stickers needed:**
1. **30% mega-sticker** (magenta circle stamp, "30%" + "ქეშბექი")
2. **9-10 მაისს date pill** (lime-yellow gradient)
3. **Price reveal** (360 → 252 ₾ with strikethrough)
4. **CTA URL pill** (bubabu.ge → lime-orange gradient)
5. **Plush wordmark** (Mkhedruli "ბუბაბუ" fleece-fabric)
6. **SOLO tag** (small white pill with bank ref - single word "SOLO" Latin only, no Mastercard suffix)

---

## STICKER 1 - 30% MEGA-STICKER

### IMAGE PROMPT

```
Single isolated 3D sticker badge on PURE CHROMA KEY BLUE BACKGROUND #0000FF — flat solid pure blue fills entire frame except the sticker itself. NO other elements. NO scene. NO Bubabu.

CENTER: chunky 3D rounded circle stamp/badge, hot magenta #FF1F8F fill, thick lime-green #84CC16 border ring (8 pixels). Slight 8-degree counterclockwise tilt. Soft drop shadow underneath. 3D bevel on the surface giving slight curvature.

ON THE STICKER (text baked in, large readable, pure clean): "30%" in chunky white sans-serif weight 900, with subtle 3D bevel and soft inner shadow. Below "30%" in smaller white Mkhedruli Georgian Bold: "ქეშბექი" (Georgian for "cashback" — established loanword).

The sticker should look like a printed-and-pinned 3D badge floating on green void.

STYLE: Pixar 3D maximalist sticker × kids commercial badge × playful candy aesthetic. Octane render.

NEGATIVE: any background other than solid chroma blue, any scene elements, any other text, Bubabu, owl, plush, any objects, dark mood, photorealistic drift, anime, 2D flat, cel-shaded outline, watermark, multiple stickers, blurry text, mtavruli capital Georgian, Cyrillic, Latin "cashback" / "back" / "behind", word "უკან" — ONLY Mkhedruli "ქეშბექი" allowed below the 30%.
```

**Aspect ratio:** 1:1 square (1080×1080)
**Generate:** 4 versions → pick cleanest "30%" + "ქეშბექი" rendering

### VIDEO PROMPT (animated pop-in)

```
Veo3 / Kling 2.0 img2vid — input attached 30% sticker image (chroma blue BG).

ACTION (3s):
- 0–0.3s: sticker invisible / off-screen
- 0.3–0.6s: sticker pops in with elastic BOUNCE — scales 0% → 110% → 100% with elastic ease, slight rotation overshoot
- 0.6–3s: idle wiggle — sticker rotates back-and-forth 2° every 1.5 seconds, very subtle

Background stays pure solid chroma blue #0000FF throughout — DO NOT change blue BG, DO NOT add elements. ONLY the sticker animates.

AUDIO: none (audio added in editor when sticker is composited).

CAMERA: LOCKED STATIC.
DURATION: 3s.

NEGATIVE: camera movement, background change from green, new elements appearing, sticker disappearing, color shifts on sticker, sticker leaving frame, multiple stickers, music, dialogue, scene changes.

DO NOT change anything except the sticker animation. Background MUST stay solid chroma blue.
```

---

## STICKER 2 - 9-10 მაისს DATE PILL

### IMAGE PROMPT

```
Single isolated 3D pill badge on PURE CHROMA KEY BLUE BACKGROUND #0000FF — flat solid pure blue fills entire frame except the pill itself. NO other elements.

CENTER: chunky rounded horizontal pill capsule. Gradient fill: lime green #84CC16 → sunny yellow #FFEB3B (left to right). Thick white outline 4 pixels. Soft drop shadow underneath. Slight 4-degree clockwise tilt.

ON THE PILL (text baked in, large readable): "9-10 მაისს" in chunky dark navy #2A6B8A Mkhedruli Bold weight 900. Numbers "9-10" in geometric sans, "მაისი" in Mkhedruli Bold. Equal vertical centering.

STYLE: Pixar 3D maximalist sticker × kids commercial badge. Octane render.

NEGATIVE: any background other than solid chroma blue, any scene elements, Bubabu, owl, any objects, ANY TEXT OTHER THAN "9-10 მაისს", Latin "May", "may", any other date format, mtavruli capital Georgian, Cyrillic, dark mood, photorealistic, anime, 2D flat, watermark, multiple pills, blurry text rendering.
```

**Aspect ratio:** 16:9 wide (or 1:1 if compositing flexible)
**Generate:** 4 versions → pick cleanest Mkhedruli "მაისი" rendering

### VIDEO PROMPT (animated)

```
Veo3 / Kling 2.0 img2vid — input attached date-pill image (chroma blue BG).

ACTION (3s):
- 0–0.4s: pill slides in from below frame (off-screen) into position with elastic ease
- 0.4–3s: idle gentle bob — pill bobs up-down 1cm every 1.5 seconds, very subtle

Background stays pure solid chroma blue #0000FF throughout. ONLY pill animates.

CAMERA: LOCKED STATIC.
DURATION: 3s.

NEGATIVE: camera movement, background change from green, new elements, pill disappearing, color shifts, pill leaving frame, multiple pills, ANY TEXT CHANGES, music, dialogue, scene changes.

DO NOT change anything except pill animation. Background solid chroma blue.
```

---

## STICKER 3 - PRICE REVEAL (360 → 252 ₾)

### IMAGE PROMPT

```
Single isolated price-stack composition on PURE CHROMA KEY BLUE BACKGROUND #0000FF — flat solid pure blue fills entire frame except the price elements. NO other graphics.

LEFT-CENTER: "360 ₾" in dark gray #555555 chunky sans-serif weight 700, with red diagonal STRIKETHROUGH line crossing through the number. Lari ₾ symbol smaller next to "360".

CENTER: a small magenta arrow "→" pointing right.

RIGHT-CENTER: "252 ₾" in chunky 3D magenta-coral #FF1F8F sans-serif weight 900 with white outline (4 pixels) and soft drop shadow. Lari ₾ symbol larger and matching color. Slight 3D bevel giving the number depth. Slightly larger than the "360 ₾" on left for visual hierarchy.

Composition: horizontal stack, all on pure chroma blue void.

STYLE: Pixar 3D price-reveal stack × kids commercial badge × candy aesthetic. Octane render. Clean clear typography.

NEGATIVE: any background other than solid chroma blue, any scene elements, Bubabu, owl, any objects, ANY TEXT OTHER THAN "360 ₾ → 252 ₾", different prices, additional currency, scene background, mtavruli capital Georgian, Cyrillic, blurry text, watermark, multiple price stacks.
```

**Aspect ratio:** 16:9 wide
**Generate:** 4 versions → pick cleanest number rendering + readable strikethrough

### VIDEO PROMPT (animated price reveal)

```
Veo3 / Kling 2.0 img2vid — input attached price-stack image (chroma blue BG).

ACTION (4s):
- 0–0.5s: only "360 ₾" visible (no strikethrough yet, no arrow, no 252)
- 0.5–1s: red strikethrough line draws from left-to-right across "360 ₾"
- 1–1.5s: arrow "→" appears with slight pop
- 1.5–2.2s: "252 ₾" pops in with elastic BOUNCE (0% → 110% → 100%), slight rotation overshoot
- 2.2–4s: "252 ₾" idle gentle pulse — scales 100% → 103% → 100% every 1.5 seconds

Background stays pure solid chroma blue #0000FF throughout.

CAMERA: LOCKED STATIC.
DURATION: 4s.

NEGATIVE: camera movement, background change from green, new elements, prices changing, "360" disappearing entirely, "252" disappearing, color shifts on numbers, scene background appearing, ANY TEXT CHANGES OTHER THAN ANIMATION ABOVE, music, dialogue.

DO NOT change anything except the animation sequence above. Background solid chroma blue.
```

---

## STICKER 4 - CTA URL PILL (bubabu.ge →)

### IMAGE PROMPT

```
Single isolated 3D pill button on PURE CHROMA KEY BLUE BACKGROUND #0000FF — flat solid pure blue fills entire frame except the pill itself.

CENTER: chunky rounded horizontal pill capsule, large size. Gradient fill: lime green #84CC16 → sunny yellow #FFEB3B → orange #FF6B35 (left to right). Thick white outline 5 pixels. Strong soft drop shadow underneath giving 3D depth.

ON THE PILL (text baked in): "bubabu.ge" in chunky white sans-serif weight 900 (Inter Black or geometric sans). Followed by a white arrow "→" symbol on the right edge of the pill. Slight 3D bevel on text.

The pill should look like a tap-ready commercial CTA button floating on green void.

STYLE: Pixar 3D commercial button × kids brand × candy aesthetic. Octane render.

NEGATIVE: any background other than solid chroma blue, any scene elements, Bubabu, owl, any objects, ANY TEXT OTHER THAN "bubabu.ge →", URL changes, "www." prefix, "https://", different domain, Mkhedruli text, Cyrillic, dark mood, photorealistic, anime, 2D flat, watermark, multiple pills, blurry text.
```

**Aspect ratio:** 16:9 wide
**Generate:** 4 versions → pick cleanest "bubabu.ge" + arrow rendering

### VIDEO PROMPT (animated)

```
Veo3 / Kling 2.0 img2vid — input attached CTA pill image (chroma blue BG).

ACTION (3s):
- 0–0.4s: pill slides in from bottom of frame (off-screen) into position with elastic ease
- 0.4–3s: idle BOUNCE — pill bobs up-down 2cm every 1.5 seconds. White arrow "→" pulses brighter every bounce (scales 100% → 115% → 100%).

Background stays pure solid chroma blue #0000FF throughout.

CAMERA: LOCKED STATIC.
DURATION: 3s.

NEGATIVE: camera movement, background change from green, new elements, URL changing, pill disappearing, color shifts, pill leaving frame, multiple pills, ANY TEXT CHANGES, music, dialogue.

DO NOT change anything except pill animation. Background solid chroma blue.
```

---

## STICKER 5 - PLUSH WORDMARK ბუბაბუ (Mkhedruli)

### IMAGE PROMPT

```
Single isolated plush-fabric wordmark on PURE CHROMA KEY BLUE BACKGROUND #0000FF — flat solid pure blue fills entire frame except the wordmark itself.

CENTER: custom Mkhedruli Georgian wordmark "ბუბაბუ" rendered as soft stuffed plush fabric letters. Spec:
— Chunky rounded display Mkhedruli (Georgian script — NOT Latin, NOT mtavruli)
— Fleece fiber surface texture (slightly fuzzy, soft, NOT glossy, NOT chrome, NOT balloon, NOT rubber)
— Stitched seams in darker navy #2A6B8A thread visible along the letter edges
— Subtle fuzz halo around each letter (matte fabric character)
— Solid cyan turquoise #5BC0DE color across all letters
— Soft drop shadow underneath wordmark

Optional small embroidered ✨ star accent on top-right corner of the last letter.

The wordmark should look like real plush stitched letters from Squishmallow / Build-a-Bear / Jellycat fabric — but rendered in Mkhedruli Georgian script.

STYLE: Photorealistic plush fabric × Squishmallow brand wordmark × Jellycat warmth × nursery felt-letter cushions, Mkhedruli typography. Octane render.

NEGATIVE: any background other than solid chroma blue, any scene elements, Bubabu owl plush, any objects, ANY TEXT OTHER THAN Mkhedruli "ბუბაბუ", Latin "Bubabu" wordmark, Latin "BUBABU", all-caps mtavruli, mtavruli capital Georgian, Cyrillic, English transliteration, balloon style, glossy chrome, marshmallow, eyes inside letters, goggles inside letters, photorealistic real fabric photography, anime, 2D flat, blurry text, illegible Mkhedruli, multiple wordmarks, watermark.
```

**Aspect ratio:** 16:9 wide
**Generate:** 5 versions → pick cleanest Mkhedruli "ბუბაბუ" rendering with visible plush texture
**Fallback if AI fails Mkhedruli 3+ times:** generate just the plush-fabric LETTERS without text content + render real "ბუბაბუ" overlay in Photoshop using Noto Sans Georgian Bold tinted cyan + add fabric texture in editor.

### VIDEO PROMPT (animated)

```
Veo3 / Kling 2.0 img2vid — input attached wordmark image (chroma blue BG).

ACTION (3s):
- 0–0.5s: wordmark fades in with slight bounce
- 0.5–3s: idle gentle FLOAT — wordmark bobs up-down 1cm every 2 seconds. Tiny ✨ star sparkle (if present) glows once per second with soft cyan flash.

Background stays pure solid chroma blue #0000FF throughout.

CAMERA: LOCKED STATIC.
DURATION: 3s.

NEGATIVE: camera movement, background change from green, new elements, wordmark disappearing, color shifts, wordmark leaving frame, multiple wordmarks, ANY TEXT CHANGES, music, dialogue, plush texture changing to chrome or balloon.

DO NOT change anything except wordmark animation. Background solid chroma blue. Plush fabric texture preserved.
```

---

## STICKER 6 - SOLO TAG (Bank of Georgia premium card line, Mastercard suffix dropped)

### IMAGE PROMPT

```
Single isolated small horizontal tag/pill on PURE CHROMA KEY BLUE BACKGROUND #0000FF — flat solid pure blue fills entire frame except the tag itself.

CENTER: small clean rounded horizontal tag/pill capsule. White fill with thin lime-green #84CC16 border (3 pixels). Subtle soft drop shadow.

ON THE TAG (text baked in, Latin only): single word "SOLO" in dark navy #2A6B8A — Latin sans-serif weight 900 (geometric like Inter Black). Optional subtle orange-red #FF6B35 highlight dot or underline accent to evoke BoG SOLO premium product line. One word centered on a single horizontal line with even kerning and clean tracking. Use ONLY this single Latin word "SOLO" — this is the short brand-mark of the eligible card line.

Modest size — secondary information element, not a hero badge.

STYLE: Pixar 3D clean info tag × kids commercial subtle badge × premium credit-card brand polish. Octane render.

NEGATIVE: any background other than solid chroma blue, any scene elements, Bubabu, owl, any objects, ANY TEXT OTHER THAN Latin "SOLO" single word, "MASTERCARD" word, "Mastercard" word, "Solomastercard" jammed wordmark, Mkhedruli text of any kind, "ბარათით" word, "Bank of Georgia" full name, "BoG" abbreviation, "World Elite" subtitle, Russian translation, mtavruli capital Georgian, Cyrillic, lowercase "solo", blurry text, watermark, multiple tags, oversized hero treatment, Mastercard logo circles graphic, card chip graphic.
```

**Aspect ratio:** 16:9 wide (small element)
**Generate:** 4 versions → pick cleanest Latin "SOLO" rendering with proper kerning (single word only - NO "MASTERCARD" suffix leak)

### VIDEO PROMPT (animated)

```
Veo3 / Kling 2.0 img2vid — input attached tag image (chroma blue BG).

ACTION (3s):
- 0–0.3s: tag slides in from left with smooth ease
- 0.3–3s: stays static with very subtle 1cm bob every 2 seconds

Background stays pure solid chroma blue #0000FF throughout.

CAMERA: LOCKED STATIC.
DURATION: 3s.

NEGATIVE: camera movement, background change from green, new elements, tag disappearing, color shifts, tag leaving frame, multiple tags, ANY TEXT CHANGES, music, dialogue.

DO NOT change anything except tag animation. Background solid chroma blue.
```

---

## CHROMA KEY COMPOSITING NOTES (for designer)

### Cutting in CapCut / After Effects
- Use **Color Key effect** with target color **`#0000FF` BLUE** (NOT green - Bubabu sticker palette contains green-channel colors that would degrade on green key)
- Spill suppression: 5-10% **yellow** complementary to remove blue halo (NOT magenta)
- Edge feathering: 1-2 pixels for soft anti-aliased edges
- If blue still visible at edges, use **Despill HSL plugin** in After Effects targeting blue
- ⚠️ **De-spill warning:** keying the blue channel will mildly affect cyan/blue/purple colors in the sticker. Bubabu sticker palette has zero pure blues, so this is safe. NEVER reintroduce a green chroma key just because mascot agent uses one - that's a different content with different palette constraints.

### Layering order (top to bottom in timeline)
1. Sticker 5 - Plush wordmark "ბუბაბუ" (top of frame)
2. Sticker 1 - 30% mega-sticker (top-right corner)
3. Sticker 2 - 9-10 მაისს date pill (below 30%)
4. Sticker 3 - Price reveal (middle-right or center)
5. Sticker 4 - CTA URL pill (bottom)
6. Sticker 6 - SOLO tag (bottom-left corner, smallest, single Latin word)
7. Background: Cut A/B/C clean Bubabu video

### Timing on master 6s cut
- 0:00 - Bubabu video starts
- 0:30s - Sticker 5 wordmark fades in (top)
- 0:50s - Sticker 1 (30%) elastic pop
- 1:50s - Sticker 2 (9-10 მაისს) slides in below
- 4:00s - Sticker 4 (CTA pill) slides up from bottom
- 4:00s - Sticker 6 (BoG tag) slides in (bottom-left)
- 5:50s - All hold for final beat

### Timing on master 15s cut
- Add Sticker 3 (price reveal) at 5:00 - full bounce animation
- Other stickers stay layered through full 15s
- Wordmark and CTA pill have continuous gentle animation

---

## SELF-CHECK before generating each sticker

- [ ] Background = solid chroma blue `#0000FF` ONLY, no scenes
- [ ] Sticker palette contains lime/yellow/cyan (which is WHY we use blue not green) - NEGATIVE prompts ban blue-tint on subject edges
- [ ] Only ONE sticker element per frame
- [ ] No Bubabu, no owl, no characters in sticker frame
- [ ] Mkhedruli text in mkhedruli only (NO mtavruli)
- [ ] No Cyrillic
- [ ] Latin only where appropriate (URL, "30%", "₾")
- [ ] Negative prompt explicitly bans every wrong text variant
- [ ] Generate 4-5 versions, pick cleanest text rendering

---

## FALLBACK if AI fails Mkhedruli rendering 3+ times in a row

1. Generate sticker WITHOUT text (just shape + chroma blue)
2. Add text manually in After Effects / Photoshop using real **Noto Sans Georgian Bold** font
3. Match colors and styling per spec above

This guarantees crisp Mkhedruli at the cost of an extra editor step. Ship route if AI proves stubborn.
