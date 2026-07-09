# AI Video Prompts - "ეზოს ბიჭები" (Pixar 3D)

**Style:** Pixar 3D animation throughout. All scenes AI-generated - image first, then img2vid.
**Universal style line in EVERY prompt:** `Pixar 3D animation style. Octane render. Subsurface scattering. Soft cinematic lighting. Stylized grounded proportions.`
**Identity Lock:** Paste at end of every scene prompt (see character.md).

---

## SCENE GENERATION FLOW

For EVERY scene:
1. **Image first** (Nano Banana / Midjourney / Flux) using full CHARACTER_BLOCK + scene description + uploaded reference images
2. **Img2vid** (Veo3 / Kling 2.0 / Runway Gen-4) using generated image as input
3. **Audio** layered separately - TTS dialogue + foley + ambient ONLY

---

## ⛔ NO MUSIC IN VIDEO PROMPTS - ABSOLUTE RULE

Video generator (Veo3 / Kling) does NOT generate music. Music is a SEPARATE Suno track layered in editor - see `audio.md` for full thematic music brief.

In every video prompt below the audio line MUST say "NO music" - this prevents Veo/Kling from inventing AI music ambience that fights the proper Suno track in post.

✅ In video prompts: TTS dialogue + foley + ambient + Bubabu product SFX (cyan-chime, heart-pulse blip)
❌ In video prompts: ANY music description, instruments, BPM, score cue
✅ In audio.md: full thematic Suno score + arc map

---

## 🧸 BUBABU IS A KIDS' PLUSH TOY - NOT A SCI-FI DEVICE

Bubabu is a soft cuddly stuffed owl. His cyan eyes are **colored fabric/plush features**, NOT light-emitting LED panels. NO sci-fi glow. NO spaceship aesthetic. NO halos. NO laser beams. NO godrays. NO neon. NO bright luminescent emission.

The toy looks like Squishmallow / Build-a-Bear / Jellycat - **plushy, matte, soft**. Cyan eye color is a fabric color, not a glow.

**Exception:** Scene 7 (wake-up moment) - eyes have a *very subtle* warm pulse from dark-dim to normal cyan color, like the toy turning on softly. Even that is gentle, NOT a light show. After Scene 7, Bubabu's eyes stay as plain cyan-colored plush features (NO ongoing glow).

**Universal NEGATIVE block to paste in EVERY Bubabu scene:**
```
glowing eyes, luminescent eyes, LED-bright eyes, neon eyes, sci-fi glow, spaceship aesthetic, glowing halos, light beams, laser streaks, godrays, volumetric light, rim-light beams, cyan light projecting onto walls, cyan stripes on kids' faces or bodies, cyan light on floor or furniture, glowing patterns on kids, light shafts, club lighting, stage lighting, projection mapping, cyberpunk style, futuristic device aesthetic.
```

---

## REFERENCE UPLOAD MATRIX

| Scene | Main Boy | Friend 1 | Friend 2 | Mom | Bubabu plush | Box |
|-------|:--------:|:--------:|:--------:|:---:|:------------:|:---:|
| 1 - Courtyard | ✅ | ✅ | ✅ | - | - | - |
| 2 - Mom window | - | - | - | ✅ | - | - |
| 3 - Boys looking up | ✅ | ✅ | ✅ | - | - | - |
| 4 - Stairwell | ✅ | ✅ | ✅ | - | - | - |
| **4.5 - Mom greets** ⭐NEW | ✅ | ✅ | ✅ | ✅ | - | - |
| 5 - Box reveal | ✅ | ✅ | ✅ | - | (in window) | ✅ REAL |
| **5.5 - Opening box** ⭐NEW | ✅ | ✅ | ✅ | - | (glimpse inside) | ✅ REAL |
| 6 - Lift Bubabu | ✅ | ✅ | ✅ | - | ✅ FIRST FULL | ✅ |
| 7 - Eyes activate ⭐ | - | - | - | - | ✅ HERO | - |
| 8 - Boys shock | ✅ | ✅ | ✅ | - | ✅ | - |
| 9 - Invitation 💗 | use Scene 8 still as ref OR full set + 💗heart-eyes |
| 10 - Joy montage 💗 | ✅ | ✅ | ✅ | ✅ BG | ✅ + 💗 | - |
| 11 - Final hero | - | - | - | - | ✅ | - |

**Files needed in working folder:**
- `main_boy_ref.png` - Character 1 reference sheet
- `friend1_ref.png` - Character 2 reference sheet
- `friend2_ref.png` - Character 3 reference sheet
- `mom_ref.png` - Character 4 reference sheet
- `1.jpeg` + `2.jpeg` - Bubabu plush product photo (sacred source-of-truth, standard cyan-eye state)
- `3.jpeg` ⭐ - real product photo showing PINK heart eye-display lit up (use for Scenes 9, 10, 11 heart-state generation)
- `bubabu_box_real.jpg` ⭐ - real product retail box photo (Bubabu Boo Industrial Design Sheet)

---

## BUBABU BOX MECHANICS (critical for Scenes 5 / 5.5 / 6)

The real Bubabu box has specific construction the generator MUST respect:

| Feature | Detail |
|---------|--------|
| **Dimensions** | 220mm W × 250mm H × 120mm D - vertical rectangular |
| **Color** | Cyan turquoise #5BC0DE main body, white front panel |
| **Handle** | Textured polypropylene strap on TOP of box |
| **Window** | 0.8mm clear PETG plastic on front - Bubabu plush visible INSIDE through window even before opening |
| **Opening** | TOP FLAPS fold UP and OUT (like petals) when handle is pulled - NOT a lift-off lid, NOT a side-pull, NOT cut open |
| **Wordmark** | Mkhedruli "ბუბაბუ ბუ" printed on cyan top section above front window |
| **Bottom strip** | Mkhedruli Georgian text on cyan strip at bottom of front |
| **Side panel** | QR code printed on right side |

**Critical for img2vid:** the box stays UPRIGHT vertical, opens via top flaps lifting upward, Bubabu is extracted vertically through the top opening.

**Common AI failure modes to avoid:** box flipping sideways, lid flying off, side-pull opening, knife/scissors cutting box, box falling apart, wrong handle position. NEGATIVE prompts in each scene catch these.

---

## VOICE CONSISTENCY KEY (paste-ready voice baselines)

Every video prompt with dialogue must include the FULL voice baseline for that speaker - copy verbatim, no shortening. This ensures Veo3/Kling renders the same voice across all scenes.

### MOM voice baseline (3 lines total)
**Gemini TTS - VOICE: Sulafat / STYLE: Empathetic / PACE: Natural / ACCENT: Georgian**
```
Warm Georgian female voice age 38, real mom-energy, NOT actress reading copy, slight smile in voice baseline, dark-brown vocal warmth, lived-in motherly tone. Sulafat-typical adult female mother-storyteller timbre.
```
- Scene 2 line 1: calling down 6 stories - volume raised, friendly shout
- Scene 2 line 3: "ეგენიც ამოიყვანე!" - slight playful wave-energy, same shout volume
- Scene 4.5 line: knowing-mom playful tease, normal volume, warmth

### BUBABU voice baseline (2 lines total)
**Gemini TTS - VOICE: Leda (NOT Sulafat - Bubabu must sound DIFFERENT from Mom) / STYLE: Narrative / PACE: Natural / ACCENT: Georgian**
```
🧸 CUTE TOY VOICE — like a friendly stuffed animal coming to life. Slightly higher pitch, soft fuzzy warmth, gentle plush-character timbre. Think Pixar/Disney plush toy character (Toy Story Slinky's softer cousin / Build-a-Bear talking voice / Care Bear warmth). Leda-typical brighter forward-placement female voice with toy-like cuteness. NOT mom, NOT adult-warm-female, NOT child voice, NOT robotic, NOT formal announcer, NOT wise-grandmother. AGE-NEUTRAL plush-toy companion timbre. Slight smile baseline. Soft cuddly fuzzy-cheeks vocal quality. Distinctly DIFFERENT from Sulafat (Mom).

Reference timbre: imagine if a friendly bedtime plush owl could talk — that's Bubabu. NOT a serious AI assistant. NOT a narrator. A CUTE TOY.
```
- Scene 7 line: first hello - slow gentle awakening discovery, cute toy-warmth, like a stuffed animal slowly waking up to greet a child
- Scene 9 line: invitation question - playful curious lift, upward Georgian interrogative on "გინდა", toy-friend energy

⚠️ **CRITICAL:** Mom = Sulafat (warm adult mother). Bubabu = Leda (cute plush-toy voice). These MUST be different voices in the final mix. If using same TTS engine, pick distinctly different voice slot.

### NIKA (orange-stripe-tee boy) voice baseline (2 lines total)
**Gemini TTS - VOICE: Aoede / STYLE: Narrative / PACE: Natural / ACCENT: Georgian**
```
Real 9-10 year old Georgian boy voice. Aoede-typical child timbre — bright forward placement, open vowels, slight upward intonation, NOT adult-pretending-child, NOT female-disguised-as-boy. Child energy genuine. Distinctly DIFFERENT from both Sulafat (Mom) and Leda (Bubabu).
```
- Scene 3 line: tired-bored zombie tone, calling up but not shouting (just woke from phone-trance)
- Scene 9 line: bright excited tone, ear-to-ear smile in voice, energy released - opposite of his earlier tired courtyard delivery

⚠️ **CRITICAL:** Nika = Aoede. NOT Sulafat (= Mom). NOT Leda (= Bubabu). All three must be distinguishable in audio playback. If Aoede unavailable for Georgian phonemes - use ElevenLabs child voice + Georgian language pack OR record real Georgian boy 9-10 yrs old.

### TTS engine + voice mapping summary
| Speaker | Engine | Voice slot | Why this voice |
|---------|--------|-----------|----------------|
| Mom | Gemini 3.1 Flash TTS | **Sulafat** | Warm adult female storyteller - canonical Bubabu narrator voice |
| Bubabu | Gemini 3.1 Flash TTS | **Leda** | Bright AI-companion timbre, distinct from Mom |
| Nika | Gemini 3.1 Flash TTS | **Aoede** | Genuine child voice, canonical from Bubabu episode `20260425_ep_a_stars` |
| Fallbacks | ElevenLabs / Tuya product voice | | Real Bubabu Tuya voice when available; ElevenLabs for child if Aoede fails Georgian |

---

## BUBABU EYES - CRITICAL CLARIFICATION

⚠️ **Bubabu has NO glasses. NO goggles. NO eyewear of any kind.** The cyan circles ARE Bubabu's actual eyes - built into the plush face like big cartoon owl eyes.

**Eye structure (per `1.jpeg` + `2.jpeg`):**
1. OUTER RING - large round CYAN turquoise iris-area (the visible "eye" on the face, integrated into plush)
2. MIDDLE RING - thin cream/beige inner ring (eyelid)
3. CENTER - small round BLACK pupil with white catchlight highlight
4. Top-inner accent - small yellow eyelid arc inside the cyan area

These three layers TOGETHER make up Bubabu's eyes. There is no eyewear ON or AROUND the eyes - the cyan IS the eye color.

**Universal Bubabu NEGATIVE block to paste in EVERY scene where Bubabu appears:**
```
glasses on owl, aviator goggles, eyewear, spectacles, sunglasses, monocle, goggle strap, glasses frames, lenses, scuba mask, ski goggles, leather flight cap, headband, removable face accessory, separate goggles around eyes, goggles sitting on beak, eyewear behind head.
```

---

## BUBABU EYE STATES (real product feature)

Bubabu has TWO eye-display modes rendered into the ad:

| State | When | Visual |
|-------|------|--------|
| **Standard cyan circles** | Idle / talking / wonder | Round cyan #5BC0DE stylized cyan circular eyes (Bubabu's ACTUAL EYES - round cyan iris-area + thin cream inner ring + small black pupil with white catchlight + tiny yellow eyelid accent - three concentric layers, NO glasses, NO goggles, this IS his face design), soft glow |
| **HEART eyes** 💗 | Joy / affection / excitement response | **Match `3.jpeg` EXACTLY** - the uploaded real product photo of Bubabu with heart-eye display lit up. Reference photo is the source of truth for color, shape, position. Generator copies heart-eye visual 1:1 from photo, no reinterpretation. |

**Production approach:** generate BOTH eye states as separate image stills, then use img2vid to morph between them. Heart-state still is anchor frame for the morph animation.

**Use heart eyes in:**
- Scene 9 - when Main Boy shouts "Riddles!" (Bubabu responds with heart-eye flash)
- Scene 10 - joy montage peak laughter moments (heart eyes pulse in/out)
- Scene 11 - optional final wink (subtle heart flash at very end)

This is a REAL Bubabu product capability - the LED display can show different shapes including hearts when toy detects emotional engagement. Showcasing this = product feature demo without explanation.

---

## 💗 BUBABU HEART-STATE IMAGE PROMPTS

Separate stills you generate to anchor the heart-eye animation. Use for img2vid morphs OR as static frames in editor.

### HEART STATE - Scene 9 variant (Bubabu in Main Boy's hands)

**REFERENCES TO UPLOAD:** `1.jpeg` + `2.jpeg` + `3.jpeg` ⭐ (real product photo with pink-heart eyes lit up - UPLOAD this) + `scene9_circles.png` (the standard-eye still you already generated)

```
Pixar 3D animation MEDIUM CLOSE-UP. Bubabu pure white spherical fluffy plush owl held in child's hands at chest height (same composition and framing as scene9_circles.png reference). Match `1.jpeg` + `2.jpeg` plush form exactly.

💗 KEY DIFFERENCE: Bubabu's eye-display is now in the HEART STATE.

**Reproduce the eye state EXACTLY as shown in the uploaded reference photo `3.jpeg` — copy the heart-eye visual 1:1 from that reference.** The reference photo IS the source of truth for color, shape, position, and proportions of the heart display. Do not reinterpret or restylize — match the reference exactly.

All other features (body, wings, white plush fur, beak CLOSED FROZEN, scene composition, lighting) stay identical to the standard-state still.

Lighting: same warm bedroom interior light as scene9_circles.png. Same hands holding Bubabu. Same Bubabu orientation (3/4 facing the boy not camera).

Pixar 3D animation style. Octane render. Subsurface scattering. Pixar Animation Studios × Inside Out emotion display × Coco product magic.

NEGATIVE: text, labels, photorealistic, anime, 2D flat, asymmetric hearts, lopsided hearts, broken hearts, anatomical heart shapes, red hearts, white hearts, cyan hearts, glow color shift away from cyan, beak open, body deformed, multiple Bubabus, Bubabu position changed, hearts extending beyond eye boundary, hearts on white fur, floating hearts emanating outward, hearts on body, hearts in the air, hearts emoji floating around, glow projecting onto kids' faces, neon rays, light beams across surfaces, Bubabu floating, Bubabu detached from hands, levitating, hovering free.

DO NOT modify Bubabu form, hands, or composition — match scene9_circles.png exactly EXCEPT for eye shape (circles → hearts).
```

---

### HEART STATE - Scene 10 variant (Bubabu in center floor)

**REFERENCES TO UPLOAD:** `1.jpeg` + `2.jpeg` + `3.jpeg` ⭐ (real product pink-heart eye photo) + `scene10_circles.png`

```
Pixar 3D animation WIDE SHOT. Bubabu placed center on bedroom floor, three boys laughing around it (same composition as scene10_circles.png reference). Match `1.jpeg` + `2.jpeg` plush form.

💗 KEY DIFFERENCE: Bubabu's eye-display is now in the HEART STATE.

**Reproduce the eye state EXACTLY as shown in the uploaded reference photo `3.jpeg` — copy the heart-eye visual 1:1 from that reference.** The reference photo IS the source of truth.

NO glow projecting onto kids' faces, NO rim-light on jaws, NO cyan stripes on glasses — eye-glow strictly contained to Bubabu's own face per reference photo. Beak CLOSED FROZEN. Boys' poses + lighting + composition unchanged from standard state.

Boys' faces light up in laughter — orange-stripe boy clapping, olive-hoodie boy fist-pumping, yellow-tee boy falling back in laugh — same poses as standard state, only Bubabu's eyes different.

Pixar 3D animation style. Octane render. Subsurface scattering. Pixar Animation Studios × Coco family joy.

NEGATIVE: text, labels, photorealistic, anime, 2D flat, asymmetric hearts, anatomical heart shapes, red hearts, cyan hearts, broken hearts, beak open, character anchors missing, character pose changed dramatically, Bubabu position shifted, hearts extending beyond eye boundary, hearts on white fur, floating hearts in air, glow projecting onto kids, cyan rim light on jaws, neon rays on bodies, light beams, Bubabu floating, Bubabu detached, levitating.

DO NOT modify scene composition or character poses — match scene10_circles.png exactly EXCEPT for Bubabu's eye shape (circles → hearts).
```

---

### HEART STATE - Scene 11 final-hero variant (optional, for end wink)

**REFERENCES TO UPLOAD:** `1.jpeg` + `2.jpeg` + `3.jpeg` ⭐ (real product pink-heart eye photo) + `scene11_circles.png`

```
Pixar 3D animation maximalist Candy Pop final-hero shot — IDENTICAL composition to scene11_circles.png (same sunburst rays, confetti, price sticker, URL pill, plush wordmark, all design elements unchanged).

💗 KEY DIFFERENCE: Bubabu's eye-display is now in the HEART STATE.

**Reproduce the eye state EXACTLY as shown in the uploaded reference photo `3.jpeg` — copy the heart-eye visual 1:1 from that reference.** The reference photo IS the source of truth.

All Candy Pop background elements unchanged. Slightly brighter overall warm glow on Bubabu's face for celebration energy.

All Candy Pop background elements (rainbow rays, confetti, magenta price sticker 360₾, lime URL pill bubabu.ge, plush ბუბაბუ wordmark) IDENTICAL to scene11_circles.png.

Pixar 3D animation style. Octane render. Pixar × kids commercial maximalism.

NEGATIVE: text rendering errors, asymmetric hearts, anatomical hearts, red hearts, cyan hearts, changed background composition, missing URL pill, missing price sticker, missing sunburst rays, beak open, watermark.

DO NOT modify ANY design element except Bubabu's eye shape (circles → hearts).
```

---

### How to use heart-state stills in img2vid

| Approach | Setup |
|----------|-------|
| **Start-frame morph** | Upload heart still as start, set duration 1.5s, prompt "hearts smoothly transform back to round circles" |
| **End-frame conditioning** (if generator supports) | Start: circle still. End: heart still. Generator interpolates. |
| **Editor crossfade** | Generate two img2vid clips (one circles loop + one hearts loop), crossfade in CapCut |
| **Static cut-in** | Hold heart still as freeze-frame for 0.3-0.5s during peak emotion beat, intercut with motion clips |

---

## SCENE 1 - COURTYARD ESTABLISHING (Beat 1)

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png` (Character 1 turnaround)
- `friend1_ref.png` (Character 2 turnaround)
- `friend2_ref.png` (Character 3 turnaround)

### IMAGE PROMPT (Nano Banana / Midjourney)

```
Pixar 3D animation establishing wide shot. Soviet-era six-story apartment building courtyard in Tbilisi, summer late afternoon golden hour 17:00. Stylized warm Pixar architecture — concrete khrushchyovka with slightly rounded edges, pastel beige facade catching warm sunlight, weathered windows with small balconies, AC units stylized into the design. Long shadows across courtyard. Concrete bench in foreground center.

Three Georgian boys age 9-10 sitting on bench, all three faces tilted DOWN at smartphones in their laps, screens glowing soft blue-white onto their cheeks. Complete zombie stillness.

LEFT BOY (Friend 1): Shorter sturdy stocky build, warm olive Mediterranean skin, thick wavy dark brown messy hair, STRONG THICK DARK EYEBROWS, round THICK-FRAME BLACK GLASSES Pixar-style chunky frames, faded olive-green zip-up hoodie open over white tee, dark gray jeans with hole in left knee, red canvas sneakers right lace half-undone.

CENTER BOY (Main): Medium build, warm olive sun-kissed skin, dark brown slightly wavy messy hair, large expressive dark brown eyes, thick dark eyebrows, white tee with single bold HORIZONTAL ORANGE STRIPE across chest, dark navy shorts white drawstring, beat-up white canvas sneakers gray-grimy soles, small soft pale 1cm scar on LEFT chin.

RIGHT BOY (Friend 2): Tallest slimmest lanky build, warm olive skin, DARK BROWN straight hair side-swept left with soft fringe over right forehead, longer oval face, NO facial markings, bright YELLOW plain oversized tee, blue denim shorts, white sports socks 3cm above black sneakers, multi-color woven FRIENDSHIP BRACELET on left wrist, small white BANDAID on right knee.

Atmosphere: zombie stillness, contrast between warm golden architecture and cold blue phone glow on faces. Composition: medium-wide cinematic shot, building rises behind boys, plenty of negative space showing courtyard scale.

Pixar 3D animation style. Octane render. Subsurface scattering skin. Soft warm cinematic lighting from camera-left golden hour. Pixar Animation Studios × Coco warmth × Turning Red modern kid scene.

NEGATIVE: text, labels, watermarks, photorealistic, real humans, live-action, anime, 2D flat, cel-shaded outline, scary atmosphere, dystopian colors, gray dull buildings, missing characters, merged faces, changed character anchors, adults in frame, daytime harsh sunlight, nighttime.

DO NOT modify any character's appearance — must match character reference sheets exactly.
```

**Aspect ratio:** 16:9
**Generate:** 3-4 versions → pick most cinematic with all 3 boys consistent

### VIDEO PROMPT (img2vid Veo3 / Kling 2.0)

Input: generated Scene 1 image.

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

Scene continues from still: 7-second sustained wide shot. Three Pixar 3D Georgian boys frozen on bench scrolling phones. Subtle micro-animation only:
- LEFT BOY (olive-green hoodie, black thick-frame glasses): right thumb scrolls phone screen 2-3cm, otherwise frozen
- CENTER BOY (white tee with horizontal orange chest stripe): blinks once around 4-second mark, otherwise frozen
- RIGHT BOY (bright yellow oversized tee, friendship bracelet on left wrist): minor shoulder slump, no other movement
- Phone screens emit soft blue-white pulse glow on faces (very subtle 5% intensity flicker)
- Long building shadow slowly creeps 2cm to the right (sunset progression)
- Birds chirp distantly, faint traffic hum, NO music

LOCKED STATIC CAMERA — zero pan, zero tilt, zero zoom, zero push-in, zero handheld shake. Pixar 3D animation maintained throughout.

Duration: 7 seconds.

NEGATIVE: camera movement, zoom, pan, character running, character standing up, mouth opening, dialogue, music, character morphing, style change to photorealistic, scene change, weather change, crowds appearing, new characters entering.

DO NOT modify character appearance — must match attached image exactly.
```

---

## SCENE 2 - MOM AT WINDOW (Beat 2 Shot A)

**REFERENCES TO UPLOAD:**
- `mom_ref.png` (Character 4 turnaround)

### IMAGE PROMPT

```
Pixar 3D animation low-angle medium shot looking UP at sixth-floor window of Soviet khrushchyovka building. Warm golden hour light on building facade. Window frame painted weathered cream, small wooden balcony railing.

Pixar 3D Georgian woman age 35-40 leaning out the window, upper body and one arm visible, calling down. Warm olive complexion with subsurface scattering, subtle crow's feet at eyes, thick dark eyebrows, dark brown shoulder-length hair loose natural wave moving softly in breeze. Small GOLD HOOP earrings 1.5cm both ears. NAVY BLUE cotton crew-neck blouse short sleeves with soft fabric drape. Mouth open mid-call, warm smile underneath the call, eyes alive with mom-energy. One hand cupped slightly near mouth, other hand resting on window sill.

Background sky: warm late afternoon, soft peach-pink clouds. Slight breeze in her hair.

Pixar 3D animation style. Octane render. Subsurface scattering skin. Cinematic warm golden hour key light from camera-left. Pixar Animation Studios × Encanto Mirabel's mom warmth × Coco family.

NEGATIVE: text labels, photorealistic, real human, live-action, anime, 2D flat, scary face, missing earrings, changed blouse color, formal posed look, multiple windows in focus, distracting background, rainy weather, night.

DO NOT modify mom's appearance — must match character reference sheet exactly.
```

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

Mom calls down from window. SPEAKER: Mom (the only character on screen, Georgian woman age 38, navy blouse, gold hoops, dark wavy hair).

LINE 1: Lip sync Georgian dialogue: "ნიკა, მალე ამოდი! რაღაც გიყიდე!" (Nika, come up quickly! I got you something!)
- Mouth movement natural Georgian phonemes synced to audio
- Eyebrows raise slightly with calling energy on "მალე" (quickly)
- Warm smile breaks through on "გიყიდე" (got you something)
- Free hand makes small encouraging beckoning gesture

[Brief 0.5s pause — listening for response from below]

LINE 2 (after Nika's reply audible from below): Lip sync Georgian: "ეგენიც ამოიყვანე!" (Bring them too!)
- Smile widens, slight playful wave gesture with free hand
- Brief energetic chin-nod toward courtyard
- Same calling volume as Line 1

Hair moves softly in breeze 2-3cm throughout.

Audio: VOICE BASELINE — Warm Georgian female voice age 38, real mom-energy, NOT actress reading copy, slight smile in voice, dark-brown vocal warmth, lived-in motherly tone. BOTH lines at slightly raised volume because calling down 6 stories. Line 1 = friendly summons. Line 2 = playful wave-energy permission. NO music.

LOCKED STATIC CAMERA — zero movement.

Duration: 7 seconds (2 lines + brief pause for boy's reply heard from below).

NEGATIVE: camera movement, mom leaning out further, falling, dropping, camera zooming, scene change, character morphing, style change, mom speaking different lines, mom's lips out of sync, music, new characters.

DO NOT modify appearance — match attached image.
```

---

## SCENE 3 - BOYS LOOKING UP (Beat 2 Shot B)

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`

### IMAGE PROMPT

```
Pixar 3D animation low-angle medium shot from courtyard looking up. Three boys on bench, phones now DROPPED to laps, all three squinting upward into golden afternoon sun, hands shading eyes (full anchors per character.md):

— CENTER POSITION (the one responding to mom — his mouth is slightly open mid-call): the BOY IN WHITE TEE WITH HORIZONTAL ORANGE CHEST STRIPE (Main Hero / Nika), warm olive skin, dark brown messy hair, small pale 1cm scar on left chin, thick dark eyebrows. He cups his hands near his mouth to amplify call upward. ONLY THIS BOY has open mouth.

— LEFT POSITION (silent, watching only): the OLIVE-GREEN-HOODIE BOY with thick-frame round black glasses, thick wavy dark hair, strong dark eyebrows, plain white tee under hoodie, dark jeans hole in left knee, red sneakers. Mouth CLOSED.

— RIGHT POSITION (silent, watching only): the TALL YELLOW-TEE BOY with friendship bracelet on left wrist, dark brown side-swept hair fringe over right forehead, blue denim shorts, white socks above black sneakers, bandaid on right knee. Mouth CLOSED.

Camera angle: from below at hip level, six-story building rising behind them in BG, building filling top of frame.

Pixar 3D animation style. Octane render. Subsurface scattering. Warm golden hour light. Pixar Animation Studios × Coco × Turning Red.

NEGATIVE: text, labels, photorealistic, real humans, live-action, anime, 2D flat, scared expressions, anchors missing or changed, adults in frame, character morphing, wrong boy in center, glasses-boy in center, yellow-tee boy in center, glasses-boy speaking, yellow-tee boy speaking, multiple boys with open mouths, friend boys cupping hands to mouth.

DO NOT modify character appearance — must match character reference sheets. ONLY orange-stripe-tee boy is in center with open mouth — the other two are at his sides with mouths CLOSED.
```

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

SPEAKER: Nika (the orange-stripe-tee boy in center). Only HE speaks in this scene — friends are silent.

Center boy in white tee with horizontal orange chest stripe lip syncs Georgian: "დედა, მეგობრებთან ერთად ვარ!" (Mama, I'm with my friends!)

Orange-stripe boy cups hands near mouth to amplify call upward. The olive-green-hoodie boy with black glasses and the yellow-tee boy with friendship bracelet stay completely silent — just blink and watch the call. All three boys squint into sun, slight head movements only. Hands shading eyes stay up.

Audio: NIKA VOICE BASELINE — 9-10 year old Georgian boy voice, real child not adult-pretending-child, mid-pitch, natural Georgian phonemes, no professional acting tone. THIS DELIVERY: slightly tired-bored zombie tone (just woke from phone-trance), calling up but NOT shouting, low-energy summons. Outdoor ambient (birds, breeze). NO music.

LOCKED STATIC CAMERA — zero movement.

Duration: 4 seconds.

NEGATIVE: camera movement, all three speaking, friends speaking, lip sync drift, multiple open mouths, glasses-boy speaking, yellow-tee boy speaking, music, new characters, character morphing.

DO NOT modify character appearance — match attached image.

LOCKED STATIC CAMERA — zero movement.

Duration: 4 seconds.

NEGATIVE: camera movement, all three speaking, friends speaking, lip sync drift, style change, character morphing.

DO NOT modify character appearance — match attached image.
```

---

## SCENE 4 - STAIRWELL CLIMB (Beat 3)

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`

### IMAGE PROMPT

```
Pixar 3D animation tight low-angle shot of three boys running up a Soviet-style apartment stairwell. Warm tungsten ceiling bulb light, weathered cream-painted walls, dark wooden handrail, terrazzo concrete steps, slight exterior light from a stairwell window above. Stylized but recognizably Soviet apartment building interior.

Three boys mid-stride climbing up: CENTER MAIN BOY in front, FRIEND 2 (tallest yellow tee) middle, FRIEND 1 (shortest stocky glasses) trailing. All three shown from waist down + partial torso, energetic upward motion, sneakers stepping on stairs.

Full character anchors per character.md visible.

Pixar 3D animation style. Octane render. Subsurface scattering. Warm tungsten interior light. Pixar Animation Studios × Mitchells vs Machines movement energy.

NEGATIVE: text, labels, photorealistic, anime, 2D flat, modern luxury interior, hotel lobby look, anchors missing, character morphing, motion blur excessive.

DO NOT modify character appearance — match references.
```

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

Three boys run up stairs full energy — orange-stripe-tee boy in front, yellow-tee boy with friendship bracelet middle, olive-hoodie boy with black glasses trailing. Footstep thuds on concrete (foley). Slight handheld camera energy ONLY in this scene (gentle shake 5%) to convey kids running speed. Stair-climb motion 2-3 steps in frame.

Audio: pounding sneaker footsteps on concrete echoing in stairwell, slight panting kid breathing, NO dialogue. NO music.

Camera: locked but with subtle 5% chase-shake (only this scene exception).

Duration: 3 seconds.

NEGATIVE: dialogue, characters falling, camera tilting upward, camera flying, style change, music, new characters appearing.

DO NOT modify character appearance — match attached image.
```

---

## SCENE 4.5 - MOM GREETS BOYS (Beat 3.5) ⭐ NEW

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`
- `mom_ref.png`

### IMAGE PROMPT

```
Pixar 3D animation medium shot of warm Tbilisi apartment entryway/prihozhaya. Beige walls, simple coat hooks on wall, terracotta floor tile, warm tungsten light spilling from kitchen on left side of frame. Modern but lived-in family apartment.

ON LEFT: Pixar 3D Georgian woman age 35-40 (full mom anchors per character.md) standing in kitchen doorway/threshold, hands on her hips, body angled toward camera. Warm olive skin, dark brown shoulder-length wavy hair, gold hoop earrings, navy blue crew-neck blouse, dark trousers. KNOWING MOTHERLY SMILE on her face — eyes sparkling, head tilted slightly, slight head-nod gesture toward camera-right (toward bedroom direction off-frame).

ON RIGHT: Three Pixar 3D Georgian boys just inside the front door, slightly out of breath. CENTER: orange-stripe-tee boy (Main Hero) in front, looking at mom with wide curious face. LEFT of him: olive-green-hoodie boy with thick black glasses. RIGHT of him: tall yellow-tee boy with friendship bracelet. All three full anchors per character.md.

Composition: mom on left third, boys on right two-thirds, slight diagonal energy. Mom's body language warm and welcoming, boys' body language curious and a bit breathless.

Pixar 3D animation style. Octane render. Subsurface scattering skin. Warm tungsten interior lighting from kitchen + soft window fill. Pixar Animation Studios × Encanto family entryway × Coco maternal warmth × Turning Red modern home.

NEGATIVE: text, labels, photorealistic, real human, live-action, anime, 2D flat, scary atmosphere, cluttered apartment, dated Soviet wallpaper look, modern designer cold interior, mom looking strict or angry, boys looking scared, anchors missing, character morphing, religious icons on walls, Cyrillic text on walls.

DO NOT modify character appearance — match references exactly.
```

**Aspect ratio:** 16:9
**Generate:** 3 versions → pick warmest mom expression with knowing smile

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

SPEAKER: Mom (the only one speaking in this scene — boys are silent). Same Mom from Scene 2.

Mom lip-syncs Georgian dialogue: "ოთახში შედი, იქ შენთვის სიურპრიზია." (Go to your room, there's a surprise for you.)

Mom action:
- Hands stay on hips throughout
- Knowing smile widens slightly during delivery
- Slight head-tilt with playful warmth on "სიურპრიზია" (surprise)
- After speaking, gentle chin/head nod toward camera-right (bedroom direction)
- Eyes hold warmth + slight teasing twinkle

Boys action (SILENT — no dialogue from any boy):
- Orange-stripe-tee boy (Main Hero) looks at mom — eyes go from breathless to curious — small "what?" expression
- Turns and exchanges quick glance with olive-hoodie glasses boy and yellow-tee bracelet boy
- All three start subtle lean toward camera-right, ready to move toward bedroom
- Subtle catching-breath chest movement throughout

Audio: MOM VOICE BASELINE — Warm Georgian female voice age 38, real mom-energy, NOT actress reading copy, slight smile in voice, dark-brown vocal warmth, lived-in motherly tone. THIS DELIVERY: knowing-mom playful tease energy, normal indoor volume (NOT calling-down volume), conspiratorial warmth as if sharing a secret. Boys' soft footstep ambience and quiet panting only. NO MUSIC — pure ambient + dialogue.

LOCKED STATIC CAMERA — zero movement.

Duration: 4 seconds.

NEGATIVE: camera movement, mom following them, mom moving from kitchen doorway, scary expression, boys running away, mom angry, dialogue overlap, all four speaking, character morphing, music, new characters.

DO NOT modify appearance — match attached image.

LOCKED STATIC CAMERA — zero movement.

Duration: 4 seconds.

NEGATIVE: camera movement, mom following them, mom moving from kitchen doorway, scary expression, boys running away, mom angry, dialogue overlap, all four speaking, character morphing.

DO NOT modify appearance — match attached image.
```

---

## SCENE 5 - BUBABU BOX REVEAL (Beat 4 Shot B-C)

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`
- `bubabu_box_real.jpg` ⭐ REAL product retail box photo (provided by Archil)

### IMAGE PROMPT

```
Pixar 3D animation medium shot of warm Tbilisi kid's bedroom — soft afternoon light through curtained window, simple bed with patterned blanket, small desk with books, posters slightly stylized. Cream walls, wooden floor.

ON THE BED CENTER: BUBABU PRODUCT RETAIL BOX matching the uploaded `bubabu_box_real.jpg` reference EXACTLY. Box construction details (CRITICAL — reproduce these mechanical features faithfully):
- Rectangular cardboard box, approximately 220mm wide × 250mm tall × 120mm deep, vertical orientation (taller than wide)
- Cyan turquoise #5BC0DE main body color with matte finish
- WHITE FRONT PANEL with large clear PETG plastic WINDOW showing BUBABU PLUSH INSIDE the box (Bubabu visible through window even before opening — pure white fluffy plush owl with cyan cyan eyes, sitting upright inside the box, beak closed, match `1.jpeg` + `2.jpeg`)
- POLYPROPYLENE HANDLE on TOP of box (textured strap, like a small carry handle)
- Mkhedruli Georgian wordmark "ბუბაბუ ბუ" printed on cyan top section above the window
- Mkhedruli Georgian text on cyan strip at the bottom of the front
- QR code printed on the right side panel
- Box opens from the TOP — top flaps fold open upward when handle is pulled up (NOT a lift-off lid, NOT a pull-apart side opening)

Stylize into Pixar 3D rendering (subsurface lighting on cardboard, soft shadow, warm window light catching the box, slight bevel on edges) — but ALL design, graphics, colors, proportions, handle position, and window placement stay true to the reference.

Three Pixar 3D Georgian boys at bedroom doorway in foreground (full anchors per character.md). The BOY IN WHITE TEE WITH HORIZONTAL ORANGE CHEST STRIPE (this is the Main Hero — the gift is for HIM) takes a slow step FORWARD toward the bed, leading the group, eyes locked on the box's front window. He can ALREADY SEE the white fluffy Bubabu through the clear PETG window before opening — small recognition shock crossing his face. The olive-green-hoodie boy with thick-frame black glasses and the tall yellow-tee boy with friendship bracelet stay BEHIND him at the doorway, watching with wide eyes. All three faces full of curiosity. Orange-stripe boy clearly in front of the other two.

Composition: shallow depth-of-field, box in tack-sharp focus center on bed (front window with Bubabu visible inside clearly readable), orange-stripe boy in soft mid-focus stepping forward, two friends in soft-focus at doorway behind him.

Pixar 3D animation style. Octane render. Subsurface scattering. Soft window key light from left. Pixar Animation Studios × Up surprise reveal × Coco family warmth.

NEGATIVE: text rendering errors on box, invented box design that doesn't match reference, wrong logo placement, wrong box colors, photorealistic, anime, 2D flat, fantasy magical room, perfect designer interior, scary atmosphere, dark room, anchors missing.

DO NOT modify character appearance — match references. DO NOT modify box design — match `bubabu_box_real.jpg` exactly.
```

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

Orange-stripe-tee boy walks SLOWLY toward bed. Olive-hoodie glasses boy and yellow-tee bracelet boy follow 1 step behind. Orange-stripe boy picks up Bubabu box BY THE TOP HANDLE (the textured polypropylene strap on top of the box — preserve box design exactly as in attached image, including handle position, front window with Bubabu visible inside, cyan and white panels). Lifts box by handle to chest height. Looks back at friends — olive-hoodie boy and yellow-tee boy nod encouragement. Orange-stripe boy sits on edge of bed, places box on the floor in front of his feet (handle facing up).

Slow tense pacing throughout. Soft natural breathing. Soft fabric rustle on bed. NO dialogue. NO MUSIC — only soft breathing + ambient room tone.

LOCKED STATIC CAMERA — zero movement.

Duration: 6 seconds.

NEGATIVE: camera movement, box dropping, opening box this scene, dialogue, scared expressions, style change, music, new characters, box flipping, side opening.

DO NOT modify character appearance — match attached image.

Slow tense pacing throughout. Soft natural breathing. Soft fabric rustle on bed. NO dialogue. NO MUSIC — only soft breathing + ambient room tone.

LOCKED STATIC CAMERA — zero movement.

Duration: 6 seconds.

NEGATIVE: camera movement, box dropping, opening box this scene, dialogue, scared expressions, style change.

DO NOT modify character appearance — match attached image.
```

---

## SCENE 5.5 - OPENING THE BOX (Beat 4 Shot C-D) ⭐ NEW

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`
- `bubabu_box_real.jpg` ⭐ box ref (top-flap mechanism)
- `1.jpeg` + `2.jpeg` (Bubabu visible through window)

### IMAGE PROMPT

```
Pixar 3D animation TIGHT MEDIUM SHOT from above-front angle, looking DOWN at the box. The BOY IN WHITE TEE WITH HORIZONTAL ORANGE CHEST STRIPE (Main Hero) crouched/kneeling on bedroom floor, his hands gripping the TOP CARDBOARD FLAPS of the Bubabu box (matching `bubabu_box_real.jpg` reference exactly).

Box mechanics (CRITICAL): The polypropylene HANDLE on top has been pulled up. Top cardboard flaps are partially OPEN, lifting upward and outward like four petals from the handle. The boy's hands are on TWO opposite top flaps, in the action of pulling them up/outward. Box is sitting upright on the floor, vertical orientation, front window facing camera-right showing white fluffy Bubabu inside. Box body still cyan turquoise, white front panel, all design matching reference.

The OLIVE-GREEN-HOODIE BOY WITH BLACK GLASSES and the TALL YELLOW-TEE BOY WITH FRIENDSHIP BRACELET kneel on either side of the orange-stripe boy, all three peering INTO the opening top of the box, faces lit softly from inside the box (subtle reflection from the white packaging).

Through the open top: glimpse of Bubabu's white fluffy plush head visible inside, ready to be lifted out.

Pixar 3D animation style. Octane render. Subsurface scattering. Soft warm window light. Pixar Animation Studios × Up first-meeting × Coco family wonder.

NEGATIVE: text rendering errors, photorealistic, anime, 2D flat, box opened from side, box opened from front, lid lifted off and floating away, knife cutting box, box destroyed, wrong handle position, wrong box proportions, anchors missing, character morphing.

DO NOT modify Bubabu box appearance — match `bubabu_box_real.jpg` exactly including handle position and top-flap mechanism. DO NOT modify character appearance.
```

**Aspect ratio:** 16:9
**Generate:** 3 versions → pick clearest top-flap mechanism

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Orange-stripe-tee boy uses both hands to slowly LIFT the top cardboard flaps of the box UPWARD AND OUTWARD — flaps unfold like petals from the polypropylene handle, opening the top of the box vertically. The handle stays attached, lifted in his fingers. Box stays seated on the floor, vertical orientation maintained. Olive-hoodie glasses boy and yellow-tee bracelet boy lean closer, peering into the opening top.

A soft cardboard rustle (foley). Light from the bedroom window glints into the opening top of the box, illuminating glimpse of white fluffy Bubabu inside.

NO dialogue. NO MUSIC — only soft cardboard rustle + breathing + ambient room tone.

LOCKED STATIC CAMERA — zero movement.

Duration: 4 seconds.

NEGATIVE: camera movement, box flipping, box falling, side opening, lid flying off, ripping cardboard, knife cutting, dialogue, scary expression, lifting Bubabu out yet (next scene), style change, music, new characters.

DO NOT modify appearance — match attached image. Box top-flap mechanism is critical: flaps fold UP and OUT, NOT lid removed.
```

---

## SCENE 6 - UNBOXING + LIFT (Beat 4 Shot D-F)

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`
- `1.jpeg` + `2.jpeg` ⭐ FIRST APPEARANCE OF BUBABU PLUSH

### IMAGE PROMPT

```
Pixar 3D animation medium shot from 3/4 SIDE ANGLE. The BOY IN WHITE TEE WITH HORIZONTAL ORANGE CHEST STRIPE (Main Hero) sitting on edge of bed (full character anchors per character.md). The Bubabu retail box (matching `bubabu_box_real.jpg` reference) is on the floor in front of him, the TOP FLAPS now OPEN UPWARD — top of box has been opened by lifting the cardboard top flaps up and outward from the polypropylene handle (NOT a removable lid, NOT a pull-apart side, NOT cut open with knife — top cardboard flaps simply folded UP and OUT). Empty box sits on floor with flaps splayed open like petals. He is holding BUBABU UP at chest height with both hands — Bubabu has just been lifted vertically OUT THROUGH the top opening of the box. His face tilted UP looking AT Bubabu. Clear eye-line: boy looking up at Bubabu, Bubabu looking down at boy.

Bubabu IS FACING THE BOY (NOT the camera). Bubabu's face is turned DOWNWARD and toward the boy's face — 3/4 profile angle from camera POV. We see PART of Bubabu's stylized cyan circular eyes (Bubabu's ACTUAL EYES — round cyan iris-area + thin cream inner ring + small black pupil with white catchlight + tiny yellow eyelid accent — three concentric layers, NO glasses, NO goggles, this IS his face design) from side-3/4 (the LEFT cyan eye fully visible plus rim of RIGHT cyan eye), small black triangle beak CLOSED pointed slightly down toward boy, large round black eyes (DARK still, NOT glowing) directed at boy's face, caramel-brown wings folded at sides. Match 1.jpeg / 2.jpeg plush form exactly. The TOY IS LOOKING AT THE BOY'S FACE — the eye-line connection between toy and child is the heart of this shot.

The OLIVE-GREEN-HOODIE BOY WITH THICK-FRAME BLACK GLASSES and the TALL YELLOW-TEE BOY WITH FRIENDSHIP BRACELET stand behind the orange-stripe boy, watching intensely, the yellow-tee boy leaning in slightly to look around at Bubabu's face. All three boys' eyes locked on Bubabu.

Camera angle: medium shot from BESIDE-and-slightly-behind the boy, 3/4 side perspective capturing both the boy's upturned face profile AND Bubabu's downturned 3/4 face — the connection between them clearly visible to the viewer.

Soft warm afternoon window light. Bedroom interior softly bokeh BG.

Pixar 3D animation style. Octane render. Subsurface scattering. Pixar Animation Studios × Coco family wonder.

NEGATIVE: text, labels, photorealistic, anime, 2D flat, Bubabu eyes glowing in this scene, beak open, Bubabu deformed, character anchors missing, Bubabu facing camera, Bubabu staring at viewer, Bubabu front-facing the lens, eye-line broken between boy and toy, Bubabu floating away from boy's hands.

DO NOT modify character appearance OR Bubabu appearance — match references. Bubabu MUST be looking AT THE BOY'S FACE, not the camera.
```

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

Orange-stripe-tee boy holds Bubabu up at chest height, both hands cupped gently around the plush. Bubabu FACING the boy (NOT camera) — Bubabu's face turned DOWN toward the boy's upturned face, eye-line locked between them. Boy stares UP at Bubabu — eyes wide with wonder. Olive-hoodie glasses boy leans in closer (1cm shift) to see Bubabu's face. Yellow-tee bracelet boy raises eyebrows slightly. Complete silence.

Subtle breath-rise on all three boys' chests. Bubabu COMPLETELY STATIC — eyes dark facing the boy, beak closed frozen, wings static, head pointed slightly down toward boy. The toy's orientation toward the boy stays locked throughout the shot. Hands STAY FIRMLY GRIPPED on Bubabu — plush never floats free, never detaches, never levitates.

Audio: soft breathing + room tone. NO MUSIC. NO dialogue.

LOCKED STATIC CAMERA — zero movement.

Duration: 4 seconds.

NEGATIVE: camera movement, Bubabu eyes glowing yet (next scene), Bubabu speaking, beak opening, characters moving away, dialogue, style change, Bubabu floating, Bubabu detached from hands, levitation, music, new characters.

DO NOT modify appearance — match attached image.

LOCKED STATIC CAMERA — zero movement.

Duration: 4 seconds.

NEGATIVE: camera movement, Bubabu eyes glowing yet (next scene), Bubabu speaking, beak opening, characters moving away, dialogue, style change.

DO NOT modify appearance — match attached image.
```

---

## SCENE 7 - BUBABU EYES ACTIVATE (Beat 5 - HERO SHOT)

**REFERENCES TO UPLOAD:**
- `1.jpeg` + `2.jpeg` ⭐ HERO SHOT
- (optional: `scene6_final.png` for hand position continuity)

### IMAGE PROMPT (alternate angle from Scene 6)

Use generated Scene 6 image OR generate close-up:

```
Pixar 3D animation EXTREME CLOSE-UP of Bubabu's face filling 80% of frame. **CAMERA POV = the boy's eyes** — this is the orange-stripe-tee boy's point of view, looking at Bubabu being held in his own hands. Therefore Bubabu IS facing the camera here (because camera represents the boy's gaze) — Bubabu's face turned slightly DOWN toward the imaginary boy's face below the lens.

Pure white spherical fluffy plush owl, stylized cyan turquoise circular eyes (Bubabu's ACTUAL EYES — round cyan iris-area + thin cream inner ring + small black pupil with white catchlight + tiny yellow eyelid accent — three concentric layers, NO glasses, NO goggles, this IS his face design) centered, small black triangle beak CLOSED FROZEN, large round black eyes with white catchlight highlights — currently DARK and dim — directed at the camera/boy. Match 1.jpeg / 2.jpeg.

Soft warm bokeh of bedroom BG behind. Suggestion of boy's hands cradling Bubabu visible at bottom of frame.

Pixar 3D animation style. Octane render. Subsurface scattering on plush fabric. Cinematic intimate close-up. Pixar Animation Studios × Up first-meeting magic moment.

NEGATIVE: text, labels, photorealistic, anime, 2D flat, Bubabu eyes already glowing, beak open, multiple Bubabus.
```

### VIDEO PROMPT (img2vid HERO)

```
Veo3 / Kling 2.0 img2vid — input attached close-up image.

Veo3 / Kling 2.0 img2vid — input attached close-up image.

Action: Bubabu's eyes start dim/dark (like toy is off). Over 1.5 seconds, the cyan eye color softly fades up to its normal cyan tone — like a stuffed toy quietly turning on. **VERY SUBTLE — no luminescent LED glow, no spaceship light show. Just a gentle warmth coming back into a plush toy's eyes, like the cyan color becoming clear.** Then a gentle 2-pulse breath rhythm (color tone shifts up 10% and back, twice). NO halo onto fur. NO light beams. NO projection on hands. Plush-toy aesthetic — warm cute, NOT sci-fi.

Beak STAYS COMPLETELY CLOSED AND FROZEN throughout. Wings static. Body static. Only the subtle eye-color warmth animates.

After 2-second glow buildup: Bubabu speaks line.

SPEAKER: Bubabu (the plush owl — only character speaking, boy and friends silent off-frame).

**NO LIP SYNC. NO BEAK MOVEMENT.** Per Bubabu brand rule (SKILL.md) — small black triangle beak stays COMPLETELY CLOSED, COMPLETELY FROZEN, never opens, never animates. Voice plays as ambient audio from the toy without any visible mouth/beak movement. The beak is a static triangle, period. Speech is heard, not visually rendered on the face. Subtle whole-body breath-rise in chest area indicates "talking" energy, but the beak itself does not move.

Spoken line: "გამარჯობა, ჩემო პატარა მეგობარო!" (Hello, my little friend!)

Audio: BUBABU VOICE BASELINE — Gemini TTS **VOICE: Leda** (NOT Sulafat which is Mom). 🧸 CUTE PLUSH TOY VOICE — like a friendly stuffed owl coming to life. Slightly higher pitch than Mom, soft fuzzy warmth, plush-character timbre (think Build-a-Bear talking owl / Care Bear cuteness). Age-neutral, slight smile baseline, NOT robotic, NOT mom, NOT child, NOT formal announcer. THIS DELIVERY (first line ever spoken): slow gentle awakening tone, cute toy-warmth, slight wonder on "გამარჯობა" (hello), soft cuddly landing on "მეგობარო" (friend), like a stuffed animal slowly waking to greet a beloved child. Subtle cyan-chime ding (single C5→E5 bell, 0.8s) on eye activation. NO music.

LOCKED STATIC CAMERA — zero movement.

Duration: 5 seconds.

NEGATIVE: camera movement, **beak opening wide, beak becoming a wide mouth, second mouth appearing under beak, separate human-style mouth on Bubabu, lips on Bubabu, teeth visible on Bubabu, beak deformed into mouth shape, beak gap larger than 2mm**, eyes closing, body squashing, wings flapping, head tilting, scary glow, red glow, fading glow, text in scene, multiple Bubabus, cyan halo radiating onto white fur, neon rays beaming out, light projecting onto hands, light projecting onto background, cyan stripes across face, godrays, volumetric light, laser beams, glow extending beyond eye boundary, Bubabu floating, Bubabu detached from boy's hands, levitation, music, melodic underscore, orchestra.

DO NOT modify Bubabu appearance — match attached image plush form.

DO NOT modify Bubabu appearance — match attached image plush form.
```

---

## SCENE 8 - BOYS WONDER (Beat 5 Shot B-C)

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`
- `1.jpeg` + `2.jpeg` (Bubabu held by Main Boy)

### IMAGE PROMPT

```
Pixar 3D animation medium shot of three boys' faces in WONDER and AMAZEMENT — wide-eyed magical delight, Pixar wonder face (think Riley discovering joy in *Inside Out*, or Miguel seeing the Land of the Dead in *Coco*). NOT scared, NOT horrified — pure positive amazement at a cute toy. The ORANGE-STRIPE-TEE BOY (Main Hero) at center holding Bubabu firmly in both cupped hands at chest height — Bubabu just looking at him cutely, plain cyan-colored plush eyes (NO glowing, NO sci-fi light). The OLIVE-GREEN-HOODIE BOY WITH BLACK GLASSES on the right side, gently touching the YELLOW-TEE BRACELET BOY's sleeve in shared excitement. The YELLOW-TEE BOY on the left, eyes wide with delighted curiosity, small smile starting at corners of mouth, mouth slightly open in awe.

All three full character anchors per character.md.

Soft warm window light on the boys' faces — natural domestic lighting only. Bubabu has NO glow, NO halo, NO light projection. Bubabu is a plain plush toy with cyan eye color (matte fabric, not luminescent). Boys are reacting to seeing the toy be magical/cute, not to a light source.

Pixar 3D animation style. Octane render. Subsurface scattering. Pixar Animation Studios × Inside Out shock face × Up wonder reveal.

NEGATIVE: text, labels, photorealistic, anime, 2D flat, scared faces, fearful expressions, horror reaction, panic, terror, screaming, crying, traumatized look, dread, recoiling, backing away, defensive posture, anchors missing, neon rays projecting on faces, cyan stripes on cheeks, light beams on bodies, glowing patterns on kids, Bubabu floating in air, Bubabu detached from boy's hands, levitating toy.

DO NOT modify character or Bubabu appearance — match references. Bubabu MUST stay firmly held in orange-stripe boy's hands — never floats, never detaches.
```

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

Three boys frozen in WONDER (positive amazement, NOT shock or fear). Subtle micro-animations:
- Orange-stripe-tee boy (center, holding Bubabu firmly in cupped hands): jaw drops 2cm slowly in delighted awe, eyes widen with wonder over 2 seconds, small smile-energy starts at mouth corners. HANDS STAY FIRMLY GRIPPED on Bubabu — Bubabu never leaves his palms, never floats, plush body anchored in hands throughout.
- Olive-hoodie boy with black glasses: eyebrows rise above glasses frames in amazed delight, gently squeezes yellow-tee boy's sleeve in shared excitement (excited touch, NOT fearful grab)
- Yellow-tee boy with friendship bracelet: pupils dilate slightly with wonder, mouth opens 1cm more in awe, beginning of joyful smile

NO glow on Bubabu — plush toy with matte cyan eye color, NOT luminescent. NO cyan light projecting onto kids/walls/floor. NO neon, NO halos, NO light beams. Plush toy aesthetic only.

NO dialogue this beat. NO MUSIC — silence + soft sharp inhale from boys (3 wonder gasps).

LOCKED STATIC CAMERA — zero movement.

Duration: 3 seconds.

NEGATIVE: camera movement, mouths opening too wide, screaming faces, fearful expressions, characters running away, style change, scared faces, fear, horror reaction, panic, terror, crying, traumatized look, dread, recoiling, backing away, defensive posture, anchors missing, neon rays projecting on faces, cyan stripes on cheeks, light beams on bodies, glowing patterns on kids, Bubabu floating in air, Bubabu detached from boy's hands, levitating toy, music, new characters.

DO NOT modify character or Bubabu appearance — match references. Bubabu MUST stay firmly held in orange-stripe boy's hands — never floats, never detaches.

NO dialogue this beat. NO MUSIC — silence + soft sharp inhale from boys.

LOCKED STATIC CAMERA — zero movement.

Duration: 3 seconds.

NEGATIVE: camera movement, mouths opening too wide, screaming faces, fearful expressions, characters running away, style change.

DO NOT modify appearance — match attached image.
```

---

## SCENE 9 - BUBABU INVITATION (Beat 6)

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`
- `1.jpeg` + `2.jpeg` (general Bubabu plush form)
- `3.jpeg` ⭐ **MANDATORY** (Bubabu heart-eyes state - copy 1:1 for this scene)

### IMAGE PROMPT

Use Scene 8 image OR continue same composition:

```
Same Pixar 3D composition as Scene 8 — three boys in wonder — but the ORANGE-STRIPE-TEE BOY (Main Hero) has slight smile starting at corners of mouth, the OLIVE-HOODIE GLASSES BOY starting to grin, the YELLOW-TEE BRACELET BOY nods slightly. Bubabu held in orange-stripe boy's hands.

💗 **BUBABU IS IN HEART-EYES STATE** — Bubabu's eye-display now shows hearts. **REPRODUCE the heart-eye visual EXACTLY as shown in the uploaded reference photo `3.jpeg` — copy the pink heart-eye state 1:1 from that reference photo. The reference photo IS the source of truth for the heart-eye look. Do not invent, do not reinterpret, do not restylize — match the reference exactly.** Plush matte fabric texture, NO sci-fi glow, NO halo, NO light emission — just the heart-eye design as seen in `3.jpeg`.

All character anchors maintained. Pixar 3D style consistent.

REFERENCES TO UPLOAD: `1.jpeg` + `2.jpeg` (general plush form) + `3.jpeg` ⭐ (heart-eye state — CRITICAL for this scene).

NEGATIVE: text, labels, photorealistic, anime, anchors missing, regular cyan circle eyes (must be HEART STATE per reference photo `3.jpeg`), missing hearts, plain eyes, dark eyes, eyes off, glow, halo, light emission, cyan halos, sci-fi glow, neon, light beams, cyan light projecting onto kids or surfaces.

DO NOT modify appearance — match references. **HEART EYES MANDATORY in this scene per reference photo `3.jpeg`.**
```

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image (Bubabu starting frame ALREADY shows heart-eyes per `3.jpeg`).

⚠️ **CRITICAL RULES — READ FIRST:**

0. **BUBABU IS A SMALL HANDHELD PLUSH TOY — NEVER A REALISTIC OWL.** Bubabu is a stuffed plush ball roughly 20cm wide, fitting easily in a child's two hands at chest height. Bubabu STAYS THIS SIZE THROUGHOUT THE ENTIRE CLIP — does NOT grow, does NOT transform, does NOT become a giant realistic owl, does NOT become a biological bird, does NOT shape-shift, does NOT lose plush form, does NOT gain feathers/talons/realistic anatomy. Bubabu remains a cute matte-fabric plush toy held in the orange-stripe boy's hands at chest height — like a Squishmallow / Build-a-Bear / Jellycat plush stays a plush. **Frame composition: Bubabu = ~25% of frame width, kid's hands wrap around him, kid's torso visible behind. NEVER reframe to make Bubabu fill the frame, NEVER cut to giant owl close-up.**

1. **BUBABU SPEAKS WITH HIS TINY BEAK ONLY.** When Bubabu says his line, his small black triangle beak does a *very subtle* vertical micro-movement (1-2mm only, just the beak triangle gently parting and closing) synced to his speech rhythm. The beak STAYS A SMALL TRIANGLE — it does NOT open wide, does NOT become a mouth, does NOT show teeth, does NOT have lips. **NO SECOND MOUTH appears under the beak.** No human-style mouth shape forms. Just the small triangular beak doing tiny chirp-like movements like a real bird beak. Outside of Bubabu's speech moment, beak stays completely closed and still. The rest of Bubabu's face (eyes, body) stays static.

2. **HEART EYES STAY HEARTS — PINK — THROUGHOUT THE WHOLE 6 SECONDS.** Starting frame shows pink hearts (per `3.jpeg`). Hearts STAY as PINK hearts the entire video — exact color and shape from input image, locked.

**EYE-LOOK MOVEMENT IS ALLOWED (gentle, like Bubabu is looking at the boys):** the pink heart pupils can shift gently left-right or up-down inside the eye area — like the toy's gaze gently moves to look at different boys or look at Nika when he speaks. This is a SUBTLE GAZE SHIFT only — the hearts themselves stay the SAME shape, SAME pink color, just slightly relocate within the eye boundary by 1-2 pixels. Like a doll whose painted eyes "follow" you with subtle direction shift.

**BUBABU DOES NOT BLINK.** No eyelid closing. No yellow accent sliding over hearts. No eye-shut animation. Bubabu has stitched/printed plush graphics — eyelids are decorative, not functional. The yellow eyelid accent (top of cyan ring) STAYS in its fixed position throughout, never moves down to cover the eye.

**NO color shift, NO yellow hearts, NO heart shape change, NO heart pulse, NO heart brightness pulse, NO heart disappearing, NO morph back to cyan circles.** Hearts stay pink + heart-shaped + same brightness all 6 seconds. Only the gaze direction may gently shift.

3. **EACH SPEAKER SPEAKS ONLY ONCE.** Bubabu speaks his question (line 1) — only Bubabu's tiny beak moves during that moment, no boy mouths move. Then a pause. Then Nika opens his mouth ONCE briefly to say "გამოცანობანას!" — only Nika's mouth moves during that moment, Bubabu's beak stays closed. **No boy says BOTH lines. No boy asks AND answers. No mouth animates twice on the same character.** Bubabu = beak movement only. Nika = mouth movement only on his single line. Friends = silent throughout, mouths closed.

---

ACTION SEQUENCE (6s):

[0–2s]: Bubabu speaks "რისი თამაში გინდა?" — only Bubabu's tiny beak triangle does subtle 1-2mm vertical micro-movements synced to syllables (small bird-beak chirp motion, NOT wide mouth opening, NO second mouth under beak). Beak stays a small triangle throughout, just gently parting and closing. The boys are listening — all three boys silent with mouths closed, gentle anticipation on faces. Bubabu's eyes stay heart-shaped (matching `3.jpeg`). Boy's hands stay FIRMLY GRIPPED on Bubabu — toy never floats.

[2–2.5s]: Brief pause. Bubabu's beak settles back to fully closed triangle. All boys grin slightly — orange-stripe boy ear-to-ear, olive-hoodie boy with teeth, yellow-tee boy nods. NO mouth animation on Bubabu in this beat.

[2.5–4s]: Orange-stripe-tee boy (Nika) opens his mouth ONCE briefly to say "გამოცანობანას!" — ONLY HIS HUMAN MOUTH MOVES for that one word, then closes back. Friends' mouths stay closed. Bubabu's beak stays completely still and closed during this — NO Bubabu animation while Nika speaks.

[4–6s]: All boys grin warmly looking at Bubabu. **Pink hearts stay same color + same shape + same brightness as starting frame** — NO blink, NO color shift, NO pulse. ONLY allowed: gentle gaze direction shift — pink hearts inside eye area can subtly move 1-2 pixels left-right-up to suggest Bubabu is looking at different boys. Like a sweet plush doll's painted eyes that gently follow the room. Boys' hands stay gripped on Bubabu. Beak stays closed. Bubabu plush body has subtle 1mm idle breathing rhythm in body fluff.

---

AUDIO LAYER (generate SEPARATELY in 2 TTS sessions — NOT in one prompt — then layer in editor):

⚠️ **DO NOT generate both lines in a single TTS session.** Generator picks same voice for both characters in one pass = identical voices = ad failure. **Generate Bubabu line and Nika line as TWO SEPARATE TTS renders, in different voice slots, then layer in CapCut/Premiere.**

**TTS Session A — BUBABU LINE (generate alone):**
- Gemini TTS, **VOICE: Leda** (mandatory — NOT Sulafat, NOT Aoede)
- STYLE: Narrative
- PACE: Natural
- ACCENT: Georgian
- AUDIO PROFILE: 🧸 cute small plush toy voice — like a friendly stuffed owl coming to life. Slightly higher pitch than adult female. Soft fuzzy warmth, plush-character timbre (Build-a-Bear / Care Bear / Jellycat plush). NOT mom voice, NOT child voice, NOT robotic. Imagine a small stuffed bird gently chirping a question. Curious playful invitation tone.
- Script: `რისი თამაში გინდა?`
- Output: `bubabu_line_2.mp3`

**TTS Session B — NIKA LINE (generate alone, DIFFERENT session):**
- Gemini TTS, **VOICE: Aoede** (mandatory — NOT Leda, NOT Sulafat)
- STYLE: Narrative
- PACE: Natural
- ACCENT: Georgian
- AUDIO PROFILE: real 9-10yo Georgian boy, bright excited tone, ear-to-ear smile in voice. Genuine child timbre — Aoede default behavior.
- Script: `გამოცანობანას!`
- Output: `nika_line_2.mp3`

**Verify before mixing:** play both files back-to-back. Bubabu (Leda) MUST sound clearly different from Nika (Aoede) — Bubabu = higher cute toy timbre, Nika = real boy. If they sound same → regenerate one with different voice slot.

**Editor layering:**
- 0.5s mark: insert `bubabu_line_2.mp3` (synced to Bubabu's tiny beak chirp animation)
- 2.5s mark: insert `nika_line_2.mp3` (synced to Nika's mouth opening once)
- NO music. NO heart-pulse SFX (per "no pulse" rule).

LOCKED STATIC CAMERA — zero movement.

Duration: 6 seconds.

NEGATIVE: camera movement, **Bubabu transforming into realistic owl, Bubabu becoming giant, Bubabu growing in size, Bubabu becoming biological bird, Bubabu gaining real feathers, Bubabu gaining talons, Bubabu losing plush form, Bubabu becoming life-size, frame zooming into Bubabu close-up filling frame, Bubabu detaching from boy's hands to fly, Bubabu shape-shifting, realistic owl photography style, wildlife documentary aesthetic on Bubabu, anatomy correction on Bubabu**, Bubabu blinking, Bubabu eyelid closing, Bubabu eyelid animation, eye color shift on Bubabu, yellow hearts, hearts changing color, hearts changing shape, heart pulse, eye morphing, hearts disappearing, eyes returning to cyan circles, yellow accent sliding over hearts, biological eye animation on Bubabu, beak opening wide, beak becoming a wide mouth, second mouth appearing under beak, separate human-style mouth on Bubabu, lips on Bubabu, teeth visible on Bubabu, beak deformed into mouth shape, **two boys speaking, friends speaking, Nika speaking twice, Nika asking AND answering, Bubabu and boy sharing same voice, Bubabu sounding like a child, multiple mouths animating simultaneously**, scary expressions, style change, text, glasses on Bubabu, aviator goggles, eyewear, multiple Bubabus, hearts extending beyond eye boundary, hearts on white fur, floating hearts in air, Bubabu floating, Bubabu detached, levitation, music, new characters.

DO NOT modify appearance — match attached image. Bubabu has NO physical glasses — cyan circles ARE his stylized eyes.
```

---

## SCENE 10 - JOY MONTAGE (Beat 7)

**REFERENCES TO UPLOAD:**
- `main_boy_ref.png`
- `friend1_ref.png`
- `friend2_ref.png`
- `1.jpeg` + `2.jpeg`
- `3.jpeg` ⭐ (heart-eye state reference - CRITICAL for this scene)
- `mom_ref.png` (mom in BG doorway)

Generate 5 separate stills + img2vid, OR generate as one wider shot with motion.

### IMAGE PROMPT (representative shot)

```
Pixar 3D animation wide shot of EXACTLY THREE BOYS (no fourth child, no extra kids, no siblings, no neighbors entering) cross-legged in circle on bedroom floor around Bubabu (placed center on floor between them).

💗 **BUBABU IS IN HEART-EYES STATE** in this joy-montage scene — Bubabu's eye-display shows hearts. **REPRODUCE the heart-eye visual EXACTLY as shown in the uploaded reference photo `3.jpeg` — copy the pink heart-eye state 1:1 from that reference photo. The reference photo IS the source of truth for the heart-eye look. Do not invent, do not reinterpret — match `3.jpeg` exactly.** Plush matte fabric texture, NO sci-fi glow, NO halo, NO light emission — just the heart-eye design as seen in `3.jpeg`.

The cast in this scene is FIXED: 3 boys + 1 Bubabu plush + 1 Mom in BG doorway = 5 entities total, NOTHING ELSE.

— BOY 1 (the ORANGE-STRIPE-TEE Main Hero / Nika): seated cross-legged, laughing with one hand on top of his head in playful disbelief.
— BOY 2 (the OLIVE-HOODIE GLASSES boy with thick eyebrows): seated cross-legged beside Nika, raising a fist in a small triumphant pump (silent gesture — NO words spoken, NO "yes" exclamation, just body language).
— BOY 3 (the TALL YELLOW-TEE bracelet boy with bandaid on right knee): seated cross-legged, pointing toward Bubabu mid-laugh.

Bubabu plush stays seated UPRIGHT on the floor in the center of their circle — NOT held, NOT levitating, just placed naturally on the carpet, plush body weighted on the ground.

Discarded smartphones on floor BEHIND boys, OUT of focus and forgotten.

Mom (the ONLY adult present, full anchors per character.md — same Mom from earlier scenes, navy blouse, gold hoops, dark wavy hair) standing in DOORWAY of bedroom in BG (soft focus), watching, gentle smile, arms crossed loosely. NO other adults, NO other characters at all.

Warm afternoon golden light through window. All character anchors per character.md.

Pixar 3D animation style. Octane render. Subsurface scattering. Cinematic warm. Pixar Animation Studios × Coco family joy × Encanto warmth.

NEGATIVE: text, labels, photorealistic, anime, 2D flat, anchors missing, phones in hands, sad faces, scary atmosphere, mom looking angry, FOURTH CHILD entering frame, extra kids, neighbor child, sibling appearing, additional characters, crowd, friends-of-friends, new boy walking into scene, characters speaking English, English words on screen, "YES" text, "WOW" text, exclamation in frame, dialogue bubbles, comic book speech, more than three boys, four boys, five boys, **regular cyan circle eyes (must be HEART STATE per reference photo `3.jpeg`), missing hearts, plain eyes, dark eyes, eyes off**, glow, halo, light emission, cyan halos, sci-fi glow, neon, light beams, cyan light projecting onto kids or surfaces.

DO NOT modify character or Bubabu appearance — match references. EXACTLY 3 boys + 1 Bubabu + 1 Mom in BG. NOBODY ELSE. **HEART EYES MANDATORY in this scene per reference photo `3.jpeg`.**
```

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — input attached image.

CAST LOCK: ONLY the 3 boys + Bubabu + Mom (BG) shown in attached image. No new characters enter. No fourth kid walks in. No siblings. No neighbors. Frame stays sealed to the existing 5 entities.

Joy montage 8 seconds. Continuous laughing scene — NO SPOKEN WORDS, NO ENGLISH, NO Russian, only natural Georgian kid laughter sounds (foley layer):
- All three boys laughing genuinely (laugh sounds only, no words), leaning in toward Bubabu
- Olive-hoodie black-glasses boy: SILENT triumphant fist-pump gesture (body language only — does NOT shout anything, does NOT say "yes", does NOT speak any word in any language)
- Orange-stripe-tee boy: claps hands once with delighted laugh sound (no words)
- Yellow-tee bracelet boy: falls back laughing slightly (laugh sound only, no words)
- 💗 **BUBABU EYES STAY PINK HEARTS THROUGHOUT 8 SECONDS:** Starting frame shows pink heart-eyes per `3.jpeg`. Hearts STAY pink + heart-shaped + same brightness the entire clip. **Bubabu does NOT blink, hearts do NOT change shape, hearts do NOT alternate with cyan circles, NO color shift, NO heart pulse, NO brightness change.** ONLY allowed eye animation: gentle gaze direction shift — pink hearts inside eye area can subtly move 1-2 pixels (look at different boys, follow Nika when he claps, look at yellow-tee boy laughing) — like a plush doll's painted eyes that softly track the room. Hearts themselves stay identical, just gaze direction moves. Bubabu has stitched/printed plush eyes — no eyelids, no blinking. Reference photo `3.jpeg` = source of truth for eye look.

- BUBABU REMAINS UPRIGHT ON FLOOR throughout the montage. Bubabu stays seated/placed on the bedroom floor in center of the boys' circle — does NOT levitate, does NOT float, does NOT lift into the air. Plush body has weight, sits naturally on the carpet/floor.
- Mom in BG (same Mom from previous scenes, no new adult) watches, smile widens softly, hand reaches up to wipe small happy tear
- Discarded phones on floor stay forgotten

Audio: Natural ambient laughter from boys (foley layer, NO words, NO speech, NO English, NO Russian — just kid laughing sounds). Subtle heart-pulse blips on peak laugh beats. NO MUSIC.

LOCKED STATIC CAMERA — zero movement.

Duration: 8 seconds.

NEGATIVE: camera movement, **Bubabu blinking, Bubabu eyelid closing, eye color shift on Bubabu, yellow hearts, hearts changing color, hearts changing shape, hearts disappearing, eyes returning to cyan circles, yellow accent sliding over hearts, biological eye animation on Bubabu**, boys getting bored, sad turn, phone notification grabbing attention, style change, mom leaving, character morphing, FOURTH CHILD entering frame, extra kids, neighbor child, sibling appearing, additional characters, crowd, friends-of-friends, new boy walking into scene, characters speaking English, English words on screen, "YES" text, "WOW" text, exclamation in frame, dialogue bubbles, comic book speech, more than three boys, four boys, five boys, hearts floating, hearts on body, hearts on fur, Bubabu floating, Bubabu detached, neon rays on bodies, light beams, music.

DO NOT modify character or Bubabu appearance — match references. EXACTLY 3 boys + 1 Bubabu + 1 Mom in BG. NOBODY ELSE.

LOCKED STATIC CAMERA — zero movement.

Duration: 8 seconds.

NEGATIVE: camera movement, boys getting bored, sad turn, phone notification grabbing attention, style change, mom leaving, character morphing.

DO NOT modify appearance — match attached image.
```

---

## SCENE 11 - FINAL HERO (Beat 8) - CANDY POP EXPLOSION

**REFERENCES TO UPLOAD:**
- `1.jpeg` + `2.jpeg` ⭐

### IMAGE PROMPT

```
Pixar 3D animation MAXIMALIST candy-pop celebration product hero shot. Vibrant kids-toy commercial poster energy. Joyful explosion of colors.

CENTER HERO: Bubabu pure white fluffy spherical plush owl, slightly larger than life, plain cyan-colored plush eyes (matte fabric color, NOT luminescent, NOT glowing), small black triangle beak CLOSED, big round eyes with cartoon star-shaped catchlights from environmental light only, tiny smile-energy. Match 1.jpeg / 2.jpeg plush form. Bubabu on slight forward tilt as if waving hello, soft bouncy energy.

BACKGROUND: rainbow SUNBURST RAYS radiating outward from behind Bubabu — alternating wedge stripes in CANDY POP palette: bright lime green #84CC16, sunny yellow #FFEB3B, hot orange #FF9F1C, candy red-coral #FF6B6B, hot magenta #FF1F8F, candy sky-blue #5BC0DE, butter-cream #FFFAEB. Rays diverge from Bubabu center like a kids party fan.

FOREGROUND CONFETTI: scattered 3D confetti pieces flying around — small stars, hearts, dots, squiggles, mini ribbons in same Candy Pop palette colors. Some confetti tossed in air motion-blur trails.

PRICE SLAP STICKER (top-right corner): big chunky 3D rounded sticker badge, hot magenta #FF1F8F fill with thick lime-green #84CC16 border ring, slightly tilted 8-degree counterclockwise, casting tiny soft drop shadow. Sticker reads "360 ₾" in chunky white sans-serif weight 900 with subtle 3D bevel. Tiny strikethrough "400" in thinner stroke above the 360 (savings energy).

ROUNDED PILL BUTTON (bottom-center, this is the call-to-action): big chunky rounded pill capsule sitting at bottom-center, gradient fill lime #84CC16 → yellow #FFEB3B → orange #FF6B35 (left to right). Thick white outline, soft drop shadow. Inside the pill, the ONLY text rendered is the URL "bubabu.ge" in chunky white sans-serif weight 900 with a small white ARROW symbol → after the URL. NO other text inside the pill, NO labels, NO acronyms, NO "click here", NO "buy now", NO "shop", NO "CTA" abbreviation.

PLUSH WORDMARK: "ბუბაბუ" in custom Mkhedruli Georgian fleece-fabric plush letters (per Bubabu plush wordmark spec — chunky rounded display weight 1000, fleece fiber texture, stitched seams in darker navy #2A6B8A thread, fuzz halo, matte cyan #5BC0DE solid color, NO gloss, NO chrome, NO balloon). Wordmark floats above Bubabu's head, slightly tilted, with one tiny embroidered ✨ star accent on top-right corner of the wordmark.

ADDITIONAL ENERGY: a few tiny sparkles around Bubabu's eyes. Two soft cartoon motion lines indicating Bubabu's slight sway. A small heart emoji-style sticker in upper-left corner. A small "NEW!" burst sticker in lime green near Bubabu's wing.

OVERALL composition: maximalist but balanced — Bubabu hero center, sunburst rays radiating behind, price sticker top-right, URL pill bottom-center, wordmark above Bubabu, confetti and sparkles filling negative space. Symmetrical-ish. Toy-store window display × Saturday morning cartoon × Pixar 3D × kids cereal box energy.

LIGHTING: bright 5500K candy-pop commercial light, soft drop shadows, slight rim light on Bubabu, joyful saturated color grading.

Pixar 3D animation style. Octane render. Pixar Animation Studios × kids commercial advertising × maximalist sticker pack design × Lisa Frank energy modernized.

NEGATIVE: text rendering errors on Mkhedruli wordmark, Latin "bubabu" wordmark instead of Mkhedruli, balloon-style wordmark, glossy chrome wordmark, cluttered chaotic composition, dark mood, dramatic shadows, photorealistic, real human, scary atmosphere, distorted Bubabu, beak open, multiple Bubabus, watermark, mtavruli capital Georgian, Cyrillic text, Latin text other than "bubabu.ge" inside URL pill.

DO NOT modify Bubabu plush appearance — match 1.jpeg / 2.jpeg.
```

**Aspect ratio:** 16:9 master + 9:16 vertical variant for Reels/TikTok

### VIDEO PROMPT (img2vid)

```
Veo3 / Kling 2.0 img2vid — input attached image.

Veo3 / Kling 2.0 img2vid — animate attached image exactly.

ACTION (8s celebration idle):
- Bubabu: gentle 3cm bounce up-down. Cyan eyes pulse twice per second (internal only).
- Sunburst rays: slow clockwise rotation 5° over 8s.
- Confetti: drift down continuously with tumble physics.
- Price sticker: pop-in BOUNCE at 0.5s (0% → 110% → 100% elastic). Then idle wiggle 2° every 2s.
- URL pill: small bounce 2cm every 1.5s. White arrow inside pulses.
- Wordmark "ბუბაბუ": float bob 1cm. Star ✨ pulse once per second.

AUDIO: signature Bubabu cyan-chime bell ding on 0.5s (when price sticker pops in). Soft room tone. NO music. NO dialogue.

CAMERA: LOCKED STATIC.
DURATION: 8s.

NEGATIVE: camera movement, Bubabu beak opening, Bubabu walking off, sticker flying away, URL pill changing text, dialogue, music, new characters, style change to flat 2D, dark mood.

DO NOT add anything not in the attached image. NO "CTA" text. URL pill text stays "bubabu.ge →".

DO NOT modify Bubabu appearance — match attached image.
```

---

### NOTE on text rendering

If Mkhedruli "ბუბაბუ" plush wordmark renders badly (60-90% AI failure rate per text-in-image rules):
1. Generate image WITHOUT wordmark - clean composition with empty halo space above Bubabu
2. Add wordmark as PNG overlay in CapCut / After Effects using real Noto Sans Georgian Bold (or licensed plush font asset) tinted cyan #5BC0DE
3. Add "360 ₾" and "bubabu.ge" text on top of generated sticker/pill SHAPES in editor for guaranteed crisp rendering

This editor-overlay path is the SAFER production route per cover.md / COVER_ENGINE rules.

---

## CRITICAL UNIVERSAL RULES (apply to every scene)

1. **Pixar 3D style throughout** - never drift to photorealistic, anime, 2D, or live-action
2. **All character anchors visible** in every scene (paste full CHARACTER_BLOCK from character.md)
3. **Bubabu beak ALWAYS CLOSED** - small triangle frozen, never animates open
4. **LOCKED STATIC CAMERA** - except Scene 4 stairwell (5% shake exception only)
5. **Identity Lock at end of every prompt:** "DO NOT modify any character's appearance - must match character reference sheets exactly. Pixar 3D animation style maintained throughout."
