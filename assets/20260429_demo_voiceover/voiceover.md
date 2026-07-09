# Bubabu Demo Voiceover (Georgian)

**Engine:** Gemini 3.1 Flash TTS (`gemini-3.1-flash-tts-preview`)
**Language:** ka-GE (Preview)
**Total runtime:** ~33s · 5 cuttable blocks (Block 2 hero ~10s)
**Use:** cut by sentence in editor → layer over UGC b-roll

---

## TTS Settings

```
VOICE: Sulafat
AUDIO PROFILE: Warm female storyteller, 30s, expressive mother with full emotional range — NOT flat commercial read. She has LIVED through screen-addicted parenting nights and FOUND something that worked. Voice carries that real discovery energy. Full emotional arc across 5 blocks:

BLOCK 1 (HOOK): Lean in close, intimate confession tone. "ბუბაბუ უბრალო სათამაშო არ არის" — first half soft and slow, almost dismissive of "just a toy." Then on "ის ბავშვის პირველი მეგობარია" lift into warm wonder, like revealing a small miracle. End word "ინტელექტით" lands gentle, slight smile.

BLOCK 2 (PERSONALIZED DEMO): Two-voice feel within one read. "ბავშვი ეუბნება:" — set up gently, slightly higher pitch quote frame, like reading a memory. The quoted request "მომიყევი ისტორია ჩემზე და ჩემს მეგობრებზე — ლუკა, ნინი, გიო და მე, სანდრო" — warmer softer almost whisper, EACH NAME landing with tiny natural weight (not rushed list, not robotic — like a kid saying his real friends), names flow with affection. Then drop into "ბუბაბუ კი უგონებს ზღაპარს" — proud-mother awe, slow confident weight. "სახელებით" — lift with quiet wonder, THE hook word. "ცოცხალი საუბრით, ეკრანის გარეშე" — soft exhale of relief.

BLOCK 3 (100 LANGUAGES): Big bright energy lift, mother showing off something almost unbelievable. "სათამაშო ბავშვს" — soft setup. "ასამდე ენაზე" — emphasize "ასამდე" with subtle awe lift, like sharing a number that surprised her too when she first heard it. "ელაპარაკება და ხვდება" — confident drop with proud smile in voice. "ბუნებრივი ინტერაქცია ერთ თამაშში" — delight, mother bragging gently. "ინტერნეტისა და რეკლამების გარეშე" — drop firmness, slight protective edge.

BLOCK 4 (SAFETY): Most important emotional beat. Slow down. Mother-protector voice. "მშობელს თავად შეუძლია" — calm authority. "ზღაპრები, სიმღერები, შემეცნებითი კითხვები" — list with gentle reverence, like listing what childhood SHOULD be. "უსაფრთხოა" — quiet certainty, no salesman energy. "სამყაროს აფართოებს" — soft warmth, the emotional payoff line.

BLOCK 5 (CTA): Warm invitation, trusted friend send-off. "გაიგე მეტი" — gentle lift. "bubabu.ge" — slow, clear, confident drop, like leaving a phone number with someone you trust.

GENERAL: Slight smile baseline throughout. Real micro-breaths between sentences (audible inhale OK). NEVER syrupy. NEVER announcer. NEVER flat. Voice should make the listener FEEL she has held this owl, watched her own kid bond with it. Authentic mother discovery, not actress reading copy.
STYLE: Empathetic
PACE: Natural
ACCENT: American (Gen)
SCENE: Cozy Tbilisi living room mid-afternoon, golden window light, mom on couch leaning forward toward camera, kid asleep on her shoulder. Sharing real discovery with one trusted friend across the table. Slight emotional lift in chest from genuinely loving this thing.
SAMPLE CONTEXT:
```

**Why these settings:**
- **Sulafat** - warm intimate female, full emotional range, mother-storyteller energy
- **Empathetic** (changed from Vocal Smile) - gives deeper emotional warmth + gentle inflections, room for the full arc. Vocal Smile too brand-bright.
- **Natural pace** - 30s commercial cadence, not Drift (too slow) not Rapid Fire (too pushy)
- **American (Gen)** - default for ka-GE Preview; accent dropdown affects English emphasis only, Georgian phonetics handled by base voice

---

## BLOCK 1 - HOOK / IDENTITY (~6s)
**Function:** Introduce Bubabu, set warm tone

> ბუბაბუ უბრალო სათამაშო არ არის - ის ბავშვის პირველი მეგობარია, აღჭურვილი ხელოვნური ინტელექტით.

**Cut against:** UGC - kid hugs Bubabu / unboxing / first eye contact

---

## BLOCK 2 - PERSONALIZED STORY DEMO (~10s)
**Function:** Concrete demo - Bubabu uses YOUR kid's name + friends' names. Killer differentiator vs generic AI.

> ბავშვი ეუბნება: "მომიყევი ისტორია ჩემზე და ჩემს მეგობრებზე - ლუკა, ნინი, გიო და მე, სანდრო". ბუბაბუ კი უგონებს ზღაპარს, სადაც თითოეული მათგანი გმირია - სახელებით, ცოცხალი საუბრით, ეკრანის გარეშე.

**Cut against:** UGC - kid leans in, whispers names to Bubabu / cyan eyes light up / cut to dreamy story-illustration b-roll with kid's name floating in / kid's face lights up hearing own name

**TTS direction:** Block 2 needs DOUBLE-VOICE feel:
- Kid request line (`ბავშვი ეუბნება: "..."`) - soft warmer slightly higher pitch, almost whisper, like quoting child's curiosity
- Bubabu response setup (`ბუბაბუ კი უგონებს...`) - drop into proud-mother awe, slow on names ლუკა, ნინი, გიო, სანდრო - let each name LAND with tiny half-beat between (no pause tags, just natural phrasing weight)
- "სახელებით" - lift with quiet wonder, this is the hook word

---

## BLOCK 3 - UP TO 100 LANGUAGES (~7s)
**Function:** Massive multilingual capability, no internet

> სათამაშო ბავშვს ასამდე ენაზე ელაპარაკება და ხვდება. ეს არის ბუნებრივი ინტერაქცია ერთ თამაშში - ინტერნეტისა და რეკლამების გარეშე.

**Cut against:** UGC - kid speaking different languages, fast montage of language tags flashing globe-style: 🇬🇪 KA / 🇬🇧 EN / 🇷🇺 RU / 🇪🇸 ES / 🇨🇳 ZH / 🇫🇷 FR / 🇩🇪 DE / 🇯🇵 JA / 🇮🇹 IT / etc - quick flicker conveying "many many languages"

---

## BLOCK 4 - SAFE & STORYTELLER (~7s)
**Function:** Parent-curated content + safety

> მშობელს თავად შეუძლია შეარჩიოს შინაარსი: ზღაპრები, სიმღერები თუ შემეცნებითი კითხვები. ბუბაბუ უსაფრთხოა, ის ეკრანს კი არ ცვლის, არამედ ბავშვის სამყაროს აფართოებს.

**Cut against:** UGC - evening warm light, kid in bed with Bubabu, parent in BG, sleep mode

---

## BLOCK 5 - CTA / CLOSE (~3s)
**Function:** URL close

> გაიგე მეტი: bubabu.ge

**Cut against:** Bubabu hero shot, fade to logo + bubabu.ge text overlay

---

## FINAL SCRIPT (single line for TTS paste)

```
ბუბაბუ უბრალო სათამაშო არ არის — ის ბავშვის პირველი მეგობარია, აღჭურვილი ხელოვნური ინტელექტით. ბავშვი ეუბნება: "მომიყევი ისტორია ჩემზე და ჩემს მეგობრებზე — ლუკა, ნინი, გიო და მე, სანდრო". ბუბაბუ კი უგონებს ზღაპარს, სადაც თითოეული მათგანი გმირია — სახელებით, ცოცხალი საუბრით, ეკრანის გარეშე. სათამაშო ბავშვს ასამდე ენაზე ელაპარაკება და ხვდება. ეს არის ბუნებრივი ინტერაქცია ერთ თამაშში — ინტერნეტისა და რეკლამების გარეშე. მშობელს თავად შეუძლია შეარჩიოს შინაარსი: ზღაპრები, სიმღერები თუ შემეცნებითი კითხვები. ბუბაბუ უსაფრთხოა, ის ეკრანს კი არ ცვლის, არამედ ბავშვის სამყაროს აფართოებს. გაიგე მეტი: ბუბაბუ წერტილი ჯი
```

---

## Production Workflow

1. **AI Studio setup:** Open Google AI Studio → Gemini 3.1 Flash TTS Preview → paste TTS Settings into Speaker panel field-by-field (Voice dropdown = Sulafat, Style = Vocal Smile, Pace = Natural, Accent = American Gen, Scene + Audio Profile as free text)
2. **Temperature:** **1.0** (mandatory on 3.1, lower causes stalling)
3. **Paste FINAL SCRIPT** into text field
4. **Generate** - if metallic/truncated → retry with same input (30-40% truncation rate)
5. **Cut in editor** at sentence boundaries → 5 clean blocks
6. **Layer over UGC** - no music under voiceover, or very low ambient pad (-30dB)
7. **Optional foley:** soft room tone under blocks 1-4, gentle bell swell on block 5 CTA

## Compliance Check

- [x] All 7 TTS fields present (VOICE + AUDIO PROFILE + STYLE + PACE + ACCENT + SCENE + SAMPLE CONTEXT)
- [x] STYLE = one of 6 presets (Vocal Smile)
- [x] PACE = one of 4 presets (Natural)
- [x] ACCENT = one of 7 presets (American Gen)
- [x] No pause tags inline (per `feedback_no_pause_tags_in_voiceover.md` - ABSOLUTE)
- [x] No emotion adjective tags inline (Mode 3 trap)
- [x] FINAL SCRIPT single-line concat present (per `feedback_voiceover_consolidated_final_line.md` - ABSOLUTE)
- [x] Georgian text + English-only tags rule honored (no tags used here at all)
- [x] No CAPS on Georgian Mkhedruli (no case in script)
- [x] Under 4,000 bytes ✅ (~700 chars)
