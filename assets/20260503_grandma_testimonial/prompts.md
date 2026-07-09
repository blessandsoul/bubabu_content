# Bubabu - Grandma Testimonial (Nikusha + ბებო shot)

**Concept:** Modern grandmother + young grandson (Nikusha, age 7-9) testimonial shot for Bubabu demo video.
**Use:** Testimonial beat inside Bubabu demo video - placed AFTER UGC intro so viewer sees grandma+grandson as separate story unit, not linked to UGC kid.
**Spoken line:** "ნიკუშა ვერაფრით მოვწყვიტეთ ტიკტოკს, მერე ბუბაბუ ვიპოვეთ, ამის შემდეგ ტიკტოკი არც კი გახსენებია!"
**Disambiguation fix:** Grandson IN frame = viewer can't confuse him with UGC kid from intro.

---

## STEP 1 - PHOTO PROMPT (Nano Banana 2)

```
Photorealistic editorial portrait. Modern senior woman age 58-65 AND her young grandson age 7-9 sitting together on modern sofa, both facing camera.

GRANDMOTHER: Dark silver-streaked hair, chic layered cut below chin. Warm olive-beige complexion, high cheekbones, warm brown-hazel eyes, natural age lines. Soft natural makeup — groomed brows, neutral lip. Dark navy turtleneck OR bordeaux silk blouse, gold chain pendant, small earrings. Confident warm expression, gentle proud smile, one arm loosely around grandson.

GRANDSON: Young boy age 7-9, clearly her grandchild — family resemblance, warm olive skin, dark hair slightly wavy, bright curious eyes, small round face with natural child softness. Clean modern casual — plain white t-shirt OR simple color sweatshirt, no logos. Relaxed natural expression, slight smile, leaning slightly into grandma. Looks like a real modern city kid, primary school age — NOT baby, NOT toddler, NOT teenager.

INTERACTION: Natural, warm, unforced. Grandma arm loosely around small boy. Both angled very slightly toward each other but both looking at lens. Small boy noticeably smaller than grandma — scale difference clear, he fits under her arm comfortably.

SETTING: Bright contemporary urban apartment living room. Clean off-white walls, large window natural 5500K daylight from camera-left. Modern bookshelf background softly out of focus, books, small plant or ceramic. Clean minimal interior. NOT traditional ethnic decor, NOT cluttered, NO religious icons, NO lace, NO traditional textiles.

COMPOSITION: Medium close-up two-shot portrait. Eye-level camera. Frame mid-chest up, both subjects fully visible. Both faces tack-sharp. Background soft creamy bokeh. Both looking directly at lens.

CAMERA: Sony A7 IV, 85mm f/1.4 GM, f/2.8, 1/200s, ISO 400.
COLOR: Kodak Portra 400 warm natural tones, clean midtones.
LIGHTING: Soft natural window key light camera-left 45deg, gentle fill camera-right, both faces evenly lit.

STYLE: Annie Leibovitz intimate family editorial × Vogue Turkey lifestyle × Mediterranean contemporary family portrait. Real, warm, editorial-quality.

QUALITY: 8K, photorealistic, cinema-grade color, ultra-detail portrait photography.

NEGATIVE: cartoon, 3D render, illustration, AI plastic skin, multiple generations beyond two people, any toddlers, any babies, text overlays, watermark, blurry faces, deformed hands, extra fingers, traditional headscarf, ethnic folk costume, matronly cardigan, floral grandma dress, tight grey bun, frail look, cane, Soviet interior, lace doily, religious icons, cluttered old apartment, platinum blonde grandma, Northern European look, frozen Botox face, stiff formal posed look, identical twin faces, wrong age gap, grandson looking like adult man, grandson looking like small child under 6, teenager older than 12.
```

**Aspect ratio:** 16:9
**Generate:** 5-8 versions → pick warmest + most trust-worthy

---

## STEP 2 - TEXT STRIP PROMPT (optional, if text renders in photo)

Feed generated photo back into Nano Banana 2:

```
Reproduce this image EXACTLY — same composition, same people, same expressions, same lighting, same interior, same colors. THE ONLY CHANGE: remove any rendered text visible in the image and replace with clean background. Keep all people, faces, clothing, furniture, bokeh, lighting completely untouched. No new elements. No watermark.
```

---

## STEP 3 - VIDEO PROMPT (Kling / Veo3 img2vid)

Feed final photo into img2vid:

```
KLING / VEO3 IMG2VID — GRANDMOTHER TALKING + GRANDSON BESIDE HER

Input: uploaded reference still (modern grandmother with young grandson on sofa).

SPOKEN LINE (lip sync this exact text):
"ნიკუშა ვერაფრით მოვწყვიტეთ ტიკტოკს, მერე ბუბაბუ ვიპოვეთ, ამის შემდეგ ტიკტოკი არც კი გახსენებია!"

AUDIO: Georgian female voice age 60, warm intimate tone, genuine not actress. Emotional arc across sentence — first half "ნიკუშა ვერაფრით მოვწყვიტეთ ტიკტოკს" delivered with tired-loving confession energy, slight exhale weight of a real memory. Brief natural pause. "მერე ბუბაბუ ვიპოვეთ" — voice lifts with warm relief, discovery energy. "ამის შემდეგ ტიკტოკი არც კი გახსენებია!" — genuine warm smile in voice, quiet amazed pride, trailing upward with delight. NOT announcer, NOT actress reading script — real grandmother sharing real discovery with trusted friend. Subtle ambient living room room tone underneath voice, no music.

GRANDMOTHER LIP SYNC + FACE ANIMATION:
- Realistic natural mouth open/close perfectly synced to speech throughout
- "ნიკუშა ვერაფრით მოვწყვიტეთ ტიკტოკს" — slight tired-loving eyebrow raise, very subtle head shake left-right 2mm (nothing worked energy), eyes warm and direct at lens
- Natural beat pause — face resets, slight breath
- "მერე ბუბაბუ ვიპოვეთ" — eyes soften with relief, slight forward lean 3mm
- "ამის შემდეგ ტიკტოკი არც კი გახსენებია!" — genuine warm smile breaks, eye crinkles, slight nod of satisfaction, smile lingers after final word
- Natural jaw and cheek movement throughout, NOT robotic, NOT over-exaggerated

GRANDSON ANIMATION (secondary, silent):
- Sits quietly beside grandma, natural still child presence
- Small natural fidget — slight shoulder shift, blinks
- At "ბუბაბუ ვიპოვეთ" — slight recognising smile flickers, like he knows this story
- One brief glance up at grandma then soft eyes back to camera
- Natural lean into grandma side throughout

CAMERA: LOCKED static tripod. Zero pan, zero tilt, zero zoom, zero push-in, zero shake.

ENVIRONMENT: Very subtle soft window light gentle flicker 2-3% brightness variation. BG bokeh completely static.

Duration: 8 seconds.

NEGATIVE: camera movement, zoom, pan, tilt, handheld shake, frozen face with no lip movement, mouth closed while speaking, robotic mechanical mouth, mouth too wide open, teeth bared aggressively, grandson speaking, grandson reacting dramatically, new people entering frame, background changing, lighting dramatic shift, style change from reference image, cartoon bleed, face artifacts, deformed mouth, double face, text overlay appearing in video, watermark, abrupt cut.
```

---

## STEP 4 - STANDALONE TTS (backup if Veo3 audio качество слабое)

**Engine:** Gemini 3.1 Flash TTS (`gemini-3.1-flash-tts-preview`)

```
VOICE: Sulafat
STYLE: Empathetic
PACE: Natural
ACCENT: American (Gen)
AUDIO PROFILE: Georgian grandmother age 60, warm intimate tone. Arc: tired-loving confession → relief → proud delight. NOT flat, NOT announcer. Real person discovery energy.
SCENE: Living room, speaking to trusted friend across table.
SAMPLE CONTEXT:
```

**FINAL SCRIPT:**
```
ნიკუშა ვერაფრით მოვწყვიტეთ ტიკტოკს, მერე ბუბაბუ ვიპოვეთ, ამის შემდეგ ტიკტოკი არც კი გახსენებია!
```

---

## Production flow

1. Nano Banana 2 → photo (5-8 versions, pick best)
2. Kling/Veo3 → img2vid with video prompt above (8 sec clip)
3. If Veo3 audio weak → Gemini TTS standalone → layer in editor
4. Cut clip into demo video testimonial beat
5. Optional: use photo as static thumbnail for FB/IG testimonial card
