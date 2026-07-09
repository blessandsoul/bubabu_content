# Voiceover - Bubabu Hero Ad «Screen-Free Friend v2» (Charon narrator)

> Engine: `bible/GEMINI_TTS_GUIDE.md` (Gemini 3.1 Flash TTS - 7-field TTS Settings) + `bible/VOICEOVER_ENGINE.md`.
> ONE Charon narrator over all 5 silent Veo clips (`speech:null`, foley only → only voice → zero drift). Off-screen narrator overlay (VOICEOVER_ENGINE §6). Bubabu is NEVER voiced (user 2026-06-09).
> ⚠️ **SPOKEN LANGUAGE = GEORGIAN (ka-GE).** The narrator speaks GEORGIAN. The EN lines below are a translation reference ONLY - never the audio. The user authors the KA master in `voiceover_geo.md` (Bubabu EN-draft-only rule). Cue-5 store tokens are user-supplied + LOCKED - copy verbatim, do NOT retranslate.
> ⚠️ **ACCENT = native ka-GE, NOT American.** Fixes the winner's `ACCENT: American (Gen)` bug (`feedback_georgian_tts_accent_not_american` - American preset reads Georgian with a US accent → «она на англ базарит»). Feed Georgian text; leave Accent neutral/default in AI Studio; the Georgian text sets the language.

## TTS Settings

```
VOICE: Charon
AUDIO PROFILE: Speaks in NATIVE GEORGIAN (ka-GE) — the Georgian script drives the language, NO English / American accent, a natural Tbilisi narrator's Georgian. Warm gentle male storyteller, 40s, speaking softly to one parent like a trusted friend. Calm wonder, never salesy. Slow on the emotional lines, a soft breath between cues, the cue-4 line near a whisper, the closing cue 5 warm and inviting (the call to message and visit).
STYLE: Empathetic
PACE: The Drift
ACCENT: native Georgian (ka-GE) — NOT American. None of the 7 English-accent presets fit; the Georgian script sets the language. In AI Studio leave Accent at neutral/default and feed Georgian text.
SCENE: A cozy warm living room at golden hour, speaking gently and directly to one parent, in Georgian.
SAMPLE CONTEXT:
```
Temperature 1.0. One pass.

## FULL SCRIPT - single Charon pass (EN draft → KA master in voiceover_geo.md)

```
Six hours a day on a screen. A worry every parent knows. [medium pause]

So here is a different kind of friend, one with no screen at all. [medium pause]

Your child just plays, while Bubabu talks, listens and teaches in up to a hundred languages. [medium pause]

[whispering] A friend that helps them grow, not a screen that holds them still. [medium pause]

Come and meet it. Message us, or find us at Tbilisi Mall and Galleria Tbilisi.
```

~58 EN words. Numbers as words. No em-dash. (Cue 1 «a worry every parent knows» = the winner's verbatim Georgian phrasing «ყველა მშობლისთვის ნაცნობია» - kept on purpose, overrides the SLOP lazy-extreme guard for this user-authored line.)

### Cue 5 · locked KA store tokens (weave these VERBATIM into the closing line; do NOT retranslate the place names):
```
თბილისი მოლი მე-3 სართული, კვების სივრცეში
გალერია თბილისი, მე-3 სართული, ლიფტის მიმდებარედ
```
Cue 5 is the narrator's warm closing invite - «message us» + the two store locations. NO price (locations = where-to-find only). Small `BUBABU.GE` stays on the cover/end-card, not necessarily voiced.

## Cue → scene map (for the editor)

| Cue | Lands over | Beat |
|-----|-----------|------|
| 1 «Six hours a day on a screen. A worry every parent knows.» | Scene 1 (0-7s) | problem |
| 2 «So here is a different kind of friend, one with no screen at all.» | Scene 2 (7-15s) | arrival |
| 3 «Your child just plays, while Bubabu talks, listens and teaches in up to a hundred languages.» | Scene 3 (15-24s) | benefit |
| 4 «[whisper] A friend that helps them grow, not a screen that holds them still.» | Scene 4 (24-31s) | resolution |
| 5 «Come and meet it. Message us, or find us at Tbilisi Mall and Galleria Tbilisi.» | Scene 5 (31-37s) | CTA / Bubabu waves |

## KA hand-off (user)
User writes `voiceover_geo.md` - KA of cues 1-5 in ONE Charon pass, native ka-GE. Keep English tags inside Georgian text (`[medium pause]` / `[whispering]`). Cue-5 store tokens = LOCKED above, copy verbatim; author the warm KA connective around them in the narrator's voice. BUBABU.GE not voiced here (cover/end-card only).

## Checklist (GEMINI_TTS_GUIDE)
- [x] 7 TTS Settings fields present; STYLE/PACE = presets; VOICE Charon; ACCENT = native ka-GE (NOT American - winner-bug fix).
- [x] AUDIO PROFILE has performance direction (arc, whisper-drop, inviting close) + explicit no-English-accent direction.
- [x] Inline tags Mode 2/4 safe only (`[medium pause]`, `[whispering]`), ≤2 per paragraph, English.
- [x] Numbers as words. Script under 4,000 bytes; single chunk. Temperature 1.0.
- [x] One voice over 5 silent clips (VOICEOVER_ENGINE §6); video `speech:null`. Bubabu never voiced.
- [x] CTA = message + store tokens (user override, logged). KA master authoritative. No price. No em-dash, no slop.
