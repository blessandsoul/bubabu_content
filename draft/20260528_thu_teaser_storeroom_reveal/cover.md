# Cover - Storeroom Reveal Teaser

**Path:** PRIMARY = baked-text (Nano Banana 2 renders text directly) per Bubabu cover override.
**FALLBACK:** editor-overlay (only if 3+ Nano Banana retries fail Mkhedruli render).
**Style anchors:** Pixar × Squishmallow × Jellycat × Build-a-Bear × Candy Pop kids-commercial. NEVER editorial / tabloid / press-paper / broadcast-chyron.
**Aspect:** 9:16 vertical (YouTube Shorts + IG Reels + TikTok primary). Also export 1:1 + 16:9 derivatives at edit time.

## HEADLINE OPTIONS

**Option A (EN - recommended for teaser universal-reach):** `Soon.`
- Single word, large, central.
- Echoes the voiceover punchline «Soon... very soon... one child will wake up...»
- Works on every platform without translation.

**Option B (KA mkhedruli lowercase - for GE-channel cuts):** `მალე.`
- User produces this verbatim (per memory rule `feedback_bubabu_no_ai_ka_verse_or_prose` - I write EN draft only).
- User pre-render check: grep for accidental Cyrillic look-alikes (а / е / о / с / р / х / у / в / и / т / п / н / к / ж / д / л - must be Georgian Unicode U+10D0-U+10F0 only).

**Option C (combo - for IG carousel cover variant):** `Soon` (top) + small `მალე.` (bottom) - bilingual stack.

**Locked for first export:** Option A.

## IMAGE PROMPT (Nano Banana 2 - baked-text PRIMARY)

```
A single Bubabu plush owl mascot character — match uploaded 1.jpeg + 2.jpeg plush form EXACTLY 1:1 — round fluffy spherical body soft pure white snowy fur covering entire body face and top of head, two tiny pointed pure white ear tufts matching body fur exactly never brown never caramel, signature cyan-turquoise circular eye-goggle markings on face like aviator pilot goggles with cream-beige inner ring around each eye, bright yellow upper eyelid arcs inside the cyan goggle rings, large round black expressive eyes with single white highlight reflection, small triangular black beak between the goggles STAYS CLOSED, two small caramel-brown stubby wings sticking out from sides wings ONLY caramel-brown, two small caramel-brown feet at bottom with three orange toes feet ONLY caramel-brown, soft cute kawaii expression gentle calm wise look. Bubabu seated center-frame in COZY POSE on a low woven-twig pedestal beside an ancient hand-carved wooden chest, chest lid open about 45 degrees, soft warm gold light pouring up from the chest washing the lower half of Bubabu's body in gentle gold. Bubabu's wing-tip resting gently on the chest's lid edge. Background: butter-cream warm gradient sunrise BG color #FFFAEB at top fading to #FFF6CC at bottom, soft sunburst rays radiating diagonally outward behind Bubabu in alternating cyan #5BC0DE and magenta #FF1F8F and lime #84CC16 and yellow #FFEB3B candy-pop pastel colors, scattered candy confetti dots floating in the air in cyan and magenta and lime and yellow and coral and orange. Above Bubabu's head: massive chunky bold rounded headline text reading the single word "Soon." in deep cyan color #1A8BBC with soft warm drop shadow, large centered placement taking up about 30 percent of frame width at the upper-third vertical position. Below Bubabu near the bottom edge of frame: small clean modest secondary text reading "bubabu" in soft gold script. Camera: centered straight-on eye-level, slight low-angle suggesting hero pose. Pure Pixar 3D feature-film render quality Bao La Luna Up Coco aesthetic, smooth subsurface, soft volumetric lighting, stylized Pixar geometry, ultra-detailed plush fur shader on Bubabu, warm woodgrain shader on the chest, kids-commercial Squishmallow Jellycat Build-a-Bear candy-pop kawaii proportions. Vertical 9:16 aspect ratio.
```

**Negative:**

```
no glow on body, no glow on goggles, no goggle illumination, no chest light coming from Bubabu's body, no aura around character, no halo, no body radiance, no light wrapping torso, no rim-light on plush body, goggles remain matte printed fabric throughout, no character drift, no second Bubabu, no double Bubabu, no extra owls, brown ears, caramel ears, dark ears, brown body, caramel body, no 3.jpeg heart-eyes variant, open beak, mouth, lip-sync, eyelashes, blink, realistic owl, real bird anatomy, scary owl, dark menacing, sharp talons, large wings, editorial tabloid layout, magazine-cover chrome, masthead, ribbon, EXCLUSIVE burst sticker, antique gold filigree, red ink stamps, paper-grain texture, newspaper texture, distressed paper, broadcast chyron, news-ticker, watermark, blurry, low quality, deformed, deformed hands, extra fingers, multiple characters, human, child, baby, religious symbols, gold leaf, vertical god-rays, white-gold lighting, peach-pink, lavender, pure-white-glow, Cyrillic letters, Russian letters, Georgian Mtavruli capital letters (mkhedruli lowercase OK), Latin letters other than the headline word "Soon" and the brand word "bubabu", on-screen text beyond those two, signs in frame, document text, modern packaging, plastic toy hard look, 2d drawing, flat illustration
```

## DESIGN RATIONALE (per `bible/COVER_ENGINE.md` + Bubabu cover override SKILL.md)

| Layer | Choice | Why |
|-------|--------|-----|
| **L0 paper / BG** | Butter-cream gradient `#FFFAEB → #FFF6CC` | Bubabu palette lock. Warm, kid-safe, NEVER editorial gray/cream. |
| **L1 ribbon / accent** | Sunburst rays (cyan + magenta + lime + yellow) | Candy-pop atmosphere. Replaces editorial ribbon convention. |
| **L2 masthead** | (none - banned per Bubabu override) | Editorial chrome destroys kids-commercial DNA. |
| **L3 photograph** | Bubabu seated cozy beside open chest, gold spill | Hero pose carries the teaser story in single frame. |
| **L4 headline** | «Soon.» - chunky bold rounded, deep cyan `#1A8BBC` | Single word, scannable in 0.3 sec. Cyan ties to Bubabu's goggles (brand recall). |
| **L5 burst sticker** | (none - banned per Bubabu override) | EXCLUSIVE/SHOCKING bursts read tabloid. Sunburst rays carry energy. |
| **L0.5 brand-bar** | Small «bubabu» bottom in soft gold | Lightweight brand anchor, never compete with hero. |
| **Atmosphere** | Candy confetti scattered | Pixar candy-pop kids-commercial feel. NEVER paper grain / red ink. |

## SERIES SKIN LOCK (this cover = EP01 of Smart Gifts series - propagates to all later pair covers)

When the first paired SKU cartoon+ad ships, **lock these as series-skin** in `agents/bubabu/series_skin_smart_gifts.md`:

- **Palette 60-20-10:** Butter-cream 60% + cyan 20% + (magenta/lime/yellow/coral/orange) 20% rotating per SKU mood-state.
- **Brand-bar:** small «bubabu» bottom soft gold (same every ep).
- **Sunburst rays:** cyan + magenta + lime + yellow background convention.
- **Candy confetti atmosphere** in all covers.
- **Headline arc plan:** teaser = «Soon.» → first pair = the SKU's hero benefit in 1-3 words → ongoing pairs = SKU-specific short hooks.
- **Lowercase «bubabu» wordmark** always (no SHOUTING-CAP version).

## SELF-CHECK ≥8/10 (per Bubabu cover override + `bible/COVER_ENGINE.md` §SC)

- [x] PRIMARY path = baked-text. FALLBACK = editor-overlay only on render failure.
- [x] Style anchors visible in prompt: Pixar 3D + Squishmallow + Jellycat + Build-a-Bear + Candy Pop. ZERO editorial / tabloid / press-paper tokens.
- [x] Butter-cream BG palette locked, sunburst rays in cyan/magenta/lime/yellow, candy confetti atmosphere.
- [x] Bubabu hero center-frame matching `1.jpeg`+`2.jpeg` 1:1 (ref upload mandatory at render).
- [x] Goggles = matte printed fabric (no glow, no LED, no illumination).
- [x] Beak BLACK CLOSED (brand lock).
- [x] No typography vocabulary in image prompt body (no `weight 900` / `26px` / font-name / `letter-spacing` / Mkhedruli script-name as instruction - only visual description «chunky bold rounded»).
- [x] Headline = single word in cyan tied to brand goggle color.
- [x] No religious symbols / no gold leaf / no vertical god-rays / no white-gold / no peach-pink / no lavender / no pure-white-glow (Bubabu cartoon canon v3 anti-heaven-iconography).
- [x] No Cyrillic letters / no Mtavruli capital Georgian.
- [x] Channel restriction documented: Bubabu official + Axiom Smart only. No personal channels without sign-off.

## A/B/C/D variants (optional, for testing)

| Variant | Headline | Pose | Use case |
|---------|----------|------|----------|
| A (default) | «Soon.» EN | Cozy seated by chest | Universal channels |
| B | «მალე.» KA mkhedruli lowercase (user writes) | Same cozy | GE-channel cuts |
| C | «Coming.» EN | Curious head-tilt toward open chest | Test variant - slightly more action |
| D | (no text - image only) | Excited at branch edge with paper-glider | YouTube Shorts thumbnail B-test |

Ship A first. Test B/C/D only if A underperforms after 48h.

## Platform crops

| Platform | Aspect | Crop note |
|----------|--------|-----------|
| YouTube Shorts | 9:16 | Default render |
| IG Reels | 9:16 | Same as YT |
| TikTok | 9:16 | Same as YT |
| FB feed | 1:1 | Crop center-square - Bubabu + chest + headline stay safe |
| FB Reels | 9:16 | Same as YT |
| IG feed (1:1) | 1:1 | Crop center-square |
| Site OG-image | 16:9 | Re-render at 16:9 with Bubabu off-center-right, headline left |

## Channel restriction

- Bubabu official IG / FB / TT / YT.
- Axiom Smart corporate.
- BoG co-promo only if Archil signs off (not auto-eligible).
- **NEVER user's personal channels** (Andrew Altair / aiNOW) without explicit Archil approval.
