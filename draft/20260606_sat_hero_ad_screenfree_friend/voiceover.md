# Voiceover - Bubabu Hero Ad «Screen-Free Friend»

> Engine: `bible/GEMINI_TTS_GUIDE.md` (Gemini 3.1 Flash TTS - 7-field TTS Settings) + `bible/VOICEOVER_ENGINE.md`.
> EN draft mirror of the user-authored Georgian master `voiceover_geo.md` (KA is authoritative - 2026-06-07). ONE Charon narrator over all 5 silent Veo clips (`speech:null`, foley only → only voice → zero drift). Off-screen narrator overlay (VOICEOVER_ENGINE §6).
> ⚠️ The user added a soft CTA + the spoken domain in cue 5 - this OVERRIDES the Bubabu ad "no CTA / domain-not-voiced" default for THIS ad (user choice). Domain voiced in KA as «ბუბაბუ წერტილი ჯი» (.ge = ჯი).

## TTS Settings

```
VOICE: Charon
AUDIO PROFILE: Warm gentle male storyteller, 40s, speaking softly to one parent like a trusted friend. Calm wonder, never salesy. Slow on the emotional lines, a soft breath between cues, the cue-4 line near a whisper, the closing cue 5 warm and inviting (the call to the site).
STYLE: Empathetic
PACE: The Drift
ACCENT: American (Gen)
SCENE: A cozy warm living room at golden hour, speaking gently and directly to one parent.
SAMPLE CONTEXT:
```
Temperature 1.0. One pass.

## FULL SCRIPT - single Charon pass (EN draft → KA master in voiceover_geo.md)

```
Six hours a day on a screen, a worry every parent knows. [medium pause]

So here is a completely different kind of friend, one with no screen at all. [medium pause]

The children simply play, while Bubabu talks to them in up to a hundred languages, listens and teaches. [medium pause]

[whispering] A friend that helps them grow, not a screen that holds them in one place. [medium pause]

Give your child a happy childhood. You can get it on BUBABU.GE.
```

~62 EN words. Numbers as words. No em-dash. (Cue 1 «every parent knows» = the user's verbatim Georgian phrasing «ყველა მშობლისთვის ნაცნობია» - kept on purpose, overrides the SLOP lazy-extreme guard for this user-authored line.)

## Cue → scene map (for the editor)

| Cue | Lands over | Beat |
|-----|-----------|------|
| 1 «Six hours a day on a screen…» | Scene 1 (0-7s) | problem |
| 2 «So here is a completely different kind of friend…» | Scene 2 (7-15s) | arrival |
| 3 «The children simply play, while Bubabu talks… up to a hundred languages…» | Scene 3 (15-24s) | benefit |
| 4 «[whispering] A friend that helps them grow…» | Scene 4 (24-31s) | resolution |
| 5 «Give your child a happy childhood. You can get it on BUBABU.GE.» | Scene 5 (31-37s) | CTA / Bubabu waves to the site |

## KA hand-off
KA master = `voiceover_geo.md` (user-authored, DONE). Same Charon TTS Settings. Spoken domain «ბუბაბუ წერტილი ჯი» in cue 5 only.

## Checklist (GEMINI_TTS_GUIDE)
- [x] 7 TTS Settings fields present; STYLE/PACE/ACCENT = presets; VOICE Charon.
- [x] AUDIO PROFILE has performance direction (arc, whisper-drop, inviting close).
- [x] Inline tags Mode 2/4 safe only (`[medium pause]`, `[whispering]`), ≤2 per paragraph, English.
- [x] Numbers as words. Script under 4,000 bytes; single chunk. Temperature 1.0.
- [x] One voice over 5 silent clips (VOICEOVER_ENGINE §6); video `speech:null`.
- [x] CTA + voiced domain = user override, logged. KA master authoritative.
