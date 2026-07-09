# Voiceover - Bubabu «Parent Rescue» (first-person mother)

> Engine: `bible/GEMINI_TTS_GUIDE.md` (Gemini 3.1 Flash TTS - 7-field TTS Settings) + `bible/VOICEOVER_ENGINE.md`.
> First-person tired-then-relieved MOTHER, over all 9 silent Veo clips (video SPECs `speech:null`, foley only - only voice → zero drift). EN master draft → user produces KA verbatim in `voiceover_geo.md` (Bubabu EN-draft-only rule). Off-screen narrator overlay (VOICEOVER_ENGINE §6). NO price (locations = where-to-find only). CTA: a store-location invite WOVEN into the mother's closing line (cue 10) in her own voice, added per user request (overrides the default no-CTA-verb rule for this piece); brand CTA also on cover + `post.md`.
> **SPOKEN LANGUAGE = GEORGIAN (ka-GE).** The mother speaks GEORGIAN in every scene incl. the S8 phone line. TTS is fed the Georgian (`voiceover_geo.md` for cues 1-7/9 + the cue-10 connective, plus the LOCKED KA for cue 8 and the cue-10 store addresses). The EN lines in this file are a translation reference ONLY - never the audio. Gemini 3.1 TTS reads ka-GE natively when the input text is Georgian; tags stay English.

---

## TTS Settings

```
VOICE: Sulafat
AUDIO PROFILE: Speaks in NATIVE GEORGIAN (ka-GE) — the Georgian script drives the language; a natural Tbilisi mother's Georgian, NO English / American accent. First-person tired-then-relieved mother in her early thirties, confiding to a close friend across the table. Warmth builds scene to scene, from drained and overwhelmed at the open to soft relief and quiet pride by the end. Slow on the relief lines, a soft breath between cues. The phone line (cue 8) is lighter and present-tense, spoken aloud to a friend, not narrated. The relief line (cue 9) lands gentle and content, near a whisper; the closing invite (cue 10) lifts back to a warm, friendly tone, one mother to another. Never salesy, never an announcer.
STYLE: Empathetic
PACE: The Drift
ACCENT: native Georgian (ka-GE) — NOT American. None of the 7 English-accent presets fit; the Georgian script sets the language. In AI Studio leave Accent at neutral/default and feed Georgian text.
SCENE: A warm family living room at golden hour, the mother speaking softly and directly to one close friend, in Georgian.
SAMPLE CONTEXT:
```

Temperature 1.0 (Gemini 3.1 mandatory). Narrator cues (1-7, 9, 10) = one pass; the cue-8 phone line = a SEPARATE take (diegetic, synced to her mouth in S8; the narrator track ducks under it).

---

## FULL SCRIPT - narrator track, single Sulafat pass (cues 1-7 + 9 + 10, EN master → user KA)

```
Some afternoons the noise builds until I cannot hear myself think, and I sit there wondering how three small people fill a whole house this fast. [medium pause]

I used to wish someone could swoop in and give me five quiet minutes. [medium pause]

Then this little owl came into our home, and the whole room went still. [medium pause]

For the first time all day I felt my shoulders drop, and I caught myself smiling. [medium pause]

The children gathered around it, and it began telling them a story in their own language. [medium pause]

I finally drank my coffee while it was still warm, watching them stay curious instead of restless. [medium pause]

Hearing all three of them laugh together did something to my heart. [medium pause]

[whispering] Now our home has its calm back, and they are learning while they play. [medium pause]

And if your evenings ever feel the way mine did, you can meet this little owl for yourself, at Tbilisi Mall on the third floor in the food court, or at Galleria Tbilisi on the third floor right beside the elevator.
```

## DIEGETIC PHONE LINE - Scene 8 (mom SPEAKS this in-frame - Veo lip-sync per video.md S8)
> The SELLING beat (seller Mode L) - sells the EMOTION to the mom (she rests now, the kids are calm and happy, the evenings are hers again), NOT toy features. One tired mother to another on the phone. Present tense, warm, no price, no CTA verb.
> **Primary:** this Georgian line is set in the `video.md` S8 `speech` field - Veo renders the mother SPEAKING it in Georgian, lip-synced (S8 = 7s). **Fallback:** if Veo mangles ka-GE lip-sync on render, set S8 `speech:null` and composite this line as a separate Sulafat take, narrator ducks under it.

**KA - LOCKED (user-supplied, speak VERBATIM, do NOT retranslate):**
```
ახლა მართლა ვისვენებ. ბავშვები მშვიდად და ბედნიერად არიან, საღამოები კი, როგორც იქნა, ჩემთვის მრჩება
```
**EN gloss (reference only, NOT spoken):** Now I really rest. The kids are calm and happy, and the evenings, finally, are mine again.

~160 EN words total. Numbers as words («three», «five»). No em-dash. No slop. Sells the RESULT (calm, story in their language, the evening back), zero price. The store locations are WOVEN into the mother's closing invite (cue 10), in her own voice, not a separate tacked-on tag.

### Cue 10 · locked KA store tokens (weave these VERBATIM into her closing line; do NOT retranslate the place names):
```
თბილისი მოლი მე-3 სართული, კვების სივრცეში
გალერია თბილისი, მე-3 სართული, ლიფტის მიმდებარედ
```
Cue 10 is the mother's warm closing invite (the FULL SCRIPT above is the EN master). You author the KA connective in her voice, then drop in the two locked KA store tokens above verbatim. Same Sulafat pass, warm and content, NOT a whisper, never salesy. NO price (locations = "where to find it"). No domain (BUBABU.GE stays on cover/post).

---

## Cue → scene map (for the editor)

| Cue | Lands over | Beat |
|-----|-----------|------|
| 1 «Some afternoons the noise builds…» | Scene 1 | chaos / problem |
| 2 «I used to wish someone could swoop in…» | Scene 2 | the wish / agitate |
| 3 «Then this little owl came into our home…» | Scene 3 | arrival / turn |
| 4 «For the first time all day…» | Scene 4 | relief |
| 5 «The children gathered around it…» | Scene 5 | story circle / desire |
| 6 «I finally drank my coffee…» | Scene 6 | the evening back |
| 7 «Hearing all three of them laugh…» | Scene 7 | joy peak |
| 8 «ახლა მართლა ვისვენებ… საღამოები კი ჩემთვის მრჩება» (mom SPEAKS in-frame, Veo ka-GE lip-sync; composite = fallback) | Scene 8 | the sell (mom's emotion / free time back) |
| 9 «[whispering] Now our home has its calm back…» | Scene 9 | resolution |
| 10 «…you can meet this little owl at თბილისი მოლი… / გალერია თბილისი…» (WOVEN into the pass, mother's warm invite) | Scene 9 tail / end-card | where to find it (woven CTA) |

---

## KA hand-off (user)
User writes `voiceover_geo.md` - KA of cues 1-7 + 9 + 10 in ONE Sulafat pass, plus the separate cue-8 diegetic take. Keep English tags inside Georgian text (`[medium pause]` / `[whispering]`). **Cue 8 (phone line) KA is user-supplied + LOCKED above - copy verbatim. Cue 10 = the mother's woven closing invite: you author the warm KA connective in her voice, then drop in the two LOCKED KA store tokens verbatim (do NOT retranslate the place names).** BUBABU.GE not voiced here (cover/post only).

---

## Checklist (GEMINI_TTS_GUIDE)
- [x] All 7 TTS Settings fields present (VOICE / AUDIO PROFILE / STYLE / PACE / ACCENT / SCENE / SAMPLE CONTEXT).
- [x] STYLE = preset (Empathetic) · PACE = preset (The Drift) · ACCENT = native Georgian ka-GE (NOT American - Georgian text sets the language; no English-accent preset applies) · VOICE = warm-female (Sulafat) per voice table.
- [x] SPOKEN LANGUAGE = Georgian (ka-GE) in all scenes incl. S8 diegetic. EN in this file = translation reference only, never the audio.
- [x] AUDIO PROFILE has detailed performance direction (emotional arc, breathing, whisper-drop, diegetic-line note).
- [x] Inline tags Mode 2/4 safe only (`[medium pause]`, `[whispering]`), ≤2 per paragraph, English.
- [x] Numbers as words. No CAPS on Georgian (KA by user). Script under 4,000 bytes; single chunk. Temperature 1.0.
- [x] One narrator voice over silent clips (VOICEOVER_ENGINE §6); video `speech:null`; S8 diegetic = separate synced take.
- [x] No price (cue-10 locations = where-to-find only). Store-location CTA WOVEN into the mother's closing invite (cue 10), her own voice, not a separate tag. EN master; cue-10 KA store tokens user-supplied verbatim. No em-dash in spoken script. No slop lazy-extreme.
