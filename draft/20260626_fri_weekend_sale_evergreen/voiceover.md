# VOICEOVER: Bubabu Weekend Sale Promo, dated 3-5 July (explicit sale ad, off-screen)

> Per bible/GEMINI_TTS_GUIDE.md (Gemini TTS 7-field Settings) + bible/VOICEOVER_ENGINE.md (§6 off-screen voice = editor overlay) + bible/VIRAL_SCRIPT_ENGINE.md (VSE scoring pass below). EN MASTER only. The aired voiceover is GEORGIAN (ka-GE), written and recorded by the user (`voiceover_geo.md`). I write the English reference; the user writes the Georgian.
> USER OVERRIDE 2026-06-17 (carried): this is an EXPLICIT SALE AD for a grand store-wide sale, thirty percent off EVERYTHING. The offer + CTA go IN the voiceover, overriding the Bubabu default that keeps price/CTA out of narration. The deal is the message.
> THIS-WEEKEND DATES: the voiceover names the specific dates (July 3, 4 and 5). The VIDEO stays day-named (Friday, Saturday, Sunday) and reusable any weekend; only this VO is re-recorded with each weekend's dates. User directive 2026-06-29.
> OFF-SCREEN announcer: not shown in any frame. Veo renders every scene SILENT (`speech:null`). The voiceover is Gemini TTS, composited in the editor over the existing mom footage + the candy-pop tail.
> Format: short ad, 4 plain cues (~32 words, ~15s), simple everyday sale language. Numbers spoken as words (the on-screen plate shows the 30%).

## TTS Settings (paste into AI Studio Speaker Settings)
```
VOICE: Puck
AUDIO PROFILE: Speaks in NATIVE GEORGIAN (ka-GE), the Georgian script drives the language, NO English / American accent. Bright, friendly, upbeat sale presenter sharing a great weekend deal with a parent. LOUD, full volume, projected, energetic, clear, not breathy, not whispering, mic across the room. Punch the percent and the days. Warm and cheerful, never aggressive.
STYLE: Promo/Hype
PACE: Natural
ACCENT: native Georgian (ka-GE), NOT American. None of the English-accent presets fit; in AI Studio leave Accent at neutral/default and feed the Georgian text (it sets the language).
SCENE: a bright, friendly presenter at a sunlit shop counter sharing an exciting weekend deal with a parent, warm and upbeat, the kind of energy you lean toward.
SAMPLE CONTEXT: an upbeat weekend sale announcement for a kids gift shop.
```
Temperature 1.0. One pass.
VOICE note: Puck = upbeat male, pairs with Promo/Hype for a sale. ALT: Charon for the brand-warm storyteller (then pair STYLE Empathetic), or Zephyr for a bright female read.

## CUES (mapped to the edit)
## Cue 1 (T=0:01-0:04, hook, over the mom footage open)
This weekend Bubabu has a real sale. Thirty percent off everything.

## Cue 2 (T=0:05-0:09, over the mom footage)
Toys, gifts, and the Bubabu owl, all of it.

## Cue 3 (T=0:10-0:14, over the gift-rain)
Comment bubabu under the video and repost it.

## Cue 4 (T=0:15-0:22, over the day-board + the CTA card)
Come to Tbilisi Mall or Galleria. July 3, 4 and 5.

## FULL SCRIPT (paste-ready single TTS run)
This weekend Bubabu has a real sale. Thirty percent off everything. Toys, gifts, and the Bubabu owl, all of it. Comment bubabu under the video and repost it. Come to Tbilisi Mall or Galleria. July 3, 4 and 5.

## GEORGIAN (user-produced)
The Georgian master is the user's `voiceover_geo.md` (his own words, native ear). I do not auto-translate it. The English above is the reference for meaning, length, and the deal. The only date token to carry into the Georgian: «3, 4 და 5 ივლისს» (July 3, 4 and 5). Confirm the case by ear before recording.

## VIRAL SCORECARD (VSE pass, bible/VIRAL_SCRIPT_ENGINE.md)
Honest framing: this is a 15-second store-wide SALE announcer, not a narrative skit. The attention work is carried by the VISUALS (the mom emotional beat she already filmed + the candy-pop gift-rain + the owl), and the VO is the offer. The VO is scored as a sale read, not a story.

Attention ledger (the edit, not the VO alone):
| Beat | Cost (s) | Refund (mechanism) | Verdict |
|---|---|---|---|
| Mom sees the sale, lights up | ~5 | relatable parent emotion (social curiosity) | KEEP (her footage) |
| Gift-rain on Bubabu | ~5 | visual surprise + abundance (why all the gifts?) | KEEP |
| Day-board tap | ~3 | the when, named by day (curiosity closed) | KEEP |
| CTA card + wave | ~5 | the offer + where, warm close | KEEP |

| Axis | /10 | note |
|---|---|---|
| Hook | 6 | the mom emotional open + "real sale, 30% off everything" carries it; visuals do the lift |
| Curiosity | 6 | "why all the gifts?" gap held to the day-board |
| Escalation | 6 | emotion to abundance to offer to CTA |
| Comedy | n/a | warm sale ad, not a comedy beat |
| Memorability | 6 | the dates (July 3, 4, 5) + the owl in gift-rain |
| Shareability | 7 | the in-store mechanic (comment bubabu + repost) is built into the offer |
| Comment Potential | 6 | first-comment question in post.md carries it |
| Visual Density | 8 | something happens every beat, sound off (gift-rain, tap, wave) |
| Rewatch | 5 | low, it is an ad (acceptable for the format) |
| Ad Intrusiveness (inverse) | 5 | it IS an explicit sale ad by user directive; the warmth + the owl soften it |
Verdict: SHIP for an explicit branded sale (Ad-Intrusiveness veto waived, user directive 2026-06-17 makes the deal the message). Hook + Curiosity both at 6.

## CHECK (GEMINI_TTS 7-field + VOICEOVER + Bubabu)
- [x] 7 TTS Settings fields present (VOICE / AUDIO PROFILE / STYLE / PACE / ACCENT / SCENE / SAMPLE CONTEXT), fenced and paste-ready.
- [x] STYLE is one of the presets (Promo/Hype); PACE is one of the presets (Natural).
- [x] ACCENT = native Georgian (ka-GE), NOT American (the Bubabu winner-bug fix).
- [x] VOICE = a real voice name (Puck). Temperature 1.0, one pass, under 4000 bytes.
- [x] AUDIO PROFILE carries the performance direction (native ka-GE, LOUD, projected, punch the percent and the days), no whisper-triggering words.
- [x] §4 SCENE = intriguing storyteller (sunlit counter, lean-toward energy), zero banned depressive tokens.
- [x] §6 off-screen voice = editor overlay; no inline Speech tag; Veo renders silent (`speech:null`).
- [x] Numbers spoken as words (thirty percent); the plate carries the digit.
- [x] VO dated to this weekend (July 3, 4 and 5) per user directive 2026-06-29; the VIDEO plates stay day-named + reusable.
- [x] Cue bodies are plain complete sentences (Bubabu no-bracket, no-ellipsis rule).
- [x] VSE pass present (scorecard + ledger); calibration = SHIP for the sale-ad format, outcome pending real metrics.
- [x] No Cyrillic, no long dash. Georgian master = user's `voiceover_geo.md`.
