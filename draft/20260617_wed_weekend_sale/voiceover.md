# VOICEOVER: Bubabu Weekend Sale Promo (explicit sale ad, off-screen)

> Per bible/GEMINI_TTS_GUIDE.md (Gemini 3.1 Flash TTS, 7-field TTS Settings) + bible/VOICEOVER_ENGINE.md (§6 off-screen voice = editor overlay). EN MASTER only. The aired voiceover is GEORGIAN (ka-GE), written and recorded by the user (`voiceover_geo.md`). I write the English reference; you write the Georgian.
> USER OVERRIDE 2026-06-17: this is an EXPLICIT SALE AD for a GRAND STORE-WIDE sale, thirty percent off EVERYTHING (the whole Bubabu Smart Gifts shop, not just the Bubabu owl). The price + offer + CTA go IN the voiceover, overriding the Bubabu default that keeps price/CTA out of narration. The deal is the message.
> OFF-SCREEN announcer: not shown in any frame. Veo renders every scene SILENT (`speech:null`). The voiceover is Gemini TTS, composited in the editor.
> Format: <30s ad, 4 short plain cues (~32 words, ~15s), simple everyday sale language, not literary. Numbers spoken as words (the on-screen plate shows the 30%).

## TTS Settings (bible/GEMINI_TTS_GUIDE.md, paste into AI Studio Speaker Settings)
```
VOICE: Puck
AUDIO PROFILE: Speaks in NATIVE GEORGIAN (ka-GE), the Georgian script drives the language, NO English / American accent. Bright, friendly, upbeat sale presenter sharing a great weekend deal with a parent. LOUD, projected, energetic, clear, not breathy. Punch the percent and the days. Warm and cheerful, never aggressive.
STYLE: Promo/Hype
PACE: Natural
ACCENT: native Georgian (ka-GE), NOT American. None of the 7 English-accent presets fit; in AI Studio leave Accent at neutral/default and feed the Georgian text (it sets the language).
SCENE: a bright, friendly presenter sharing an exciting weekend deal with a parent, warm and upbeat.
SAMPLE CONTEXT:
```
Temperature 1.0. One pass.
VOICE note: Puck = upbeat male, pairs with Promo/Hype for a sale. ALT: Charon for the brand-warm storyteller (then pair STYLE Empathetic), or Zephyr for a bright female read.

## CUES (mapped to the shots)
## Cue 1 (T=0:01-0:04, hook, over S1a + S1b)
Big weekend sale at Bubabu. Thirty percent off everything.

## Cue 2 (T=0:05-0:09, over S1b + S1c)
Toys, gifts, and the Bubabu owl, all of it.

## Cue 3 (T=0:10-0:15, over S2, the gifts rain)
Comment bubabu under the video and repost it.

## Cue 4 (T=0:16-0:24, over S1d the stand + S3 the CTA card)
Come to Tbilisi Mall or Galleria. Friday, Saturday, Sunday.

## FULL SCRIPT (paste-ready single TTS run)
Big weekend sale at Bubabu. Thirty percent off everything. Toys, gifts, and the Bubabu owl, all of it. Comment bubabu under the video and repost it. Come to Tbilisi Mall or Galleria. Friday, Saturday, Sunday.

## GEORGIAN (user-produced)
The Georgian master is the user's `voiceover_geo.md` (his own words, native ear). I do not auto-translate it. The English above is the reference for meaning, length, and the deal.

## CHECK (GEMINI_TTS_GUIDE 7-field + VOICEOVER + Bubabu)
- [x] 7 TTS Settings fields present (VOICE / AUDIO PROFILE / STYLE / PACE / ACCENT / SCENE / SAMPLE CONTEXT), fenced and paste-ready.
- [x] STYLE is one of the 6 presets (Promo/Hype); PACE is one of the 4 presets (Natural).
- [x] ACCENT = native Georgian (ka-GE), NOT American (the Bubabu winner-bug fix; American preset reads ka-GE with a US accent).
- [x] VOICE = a real 30-voice-table name (Puck). Temperature 1.0, one pass, under 4000 bytes.
- [x] AUDIO PROFILE carries the performance direction (native ka-GE, bright, projected, punch the percent and the days).
- [x] §6 off-screen voice = editor overlay; no inline Speech tag; Veo renders silent (`speech:null`).
- [x] Numbers spoken as words (thirty percent); the plate carries the digit. No `$15 online` line (dropped per user).
- [x] Inline tags Mode 1/2/4 only if used; cue bodies are plain (Bubabu no-bracket rule), pacing rides the periods.
- [x] Explicit grand store-wide sale: 30% off everything + comment-bubabu + repost + weekend + where-to-buy IN the narration (user override).
- [x] No Cyrillic, no long dash. Georgian master = user's `voiceover_geo.md`.
