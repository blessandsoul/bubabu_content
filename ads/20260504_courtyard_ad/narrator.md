# Narrator Voiceover - "ეზოს ბიჭები"

**Layer:** narrator track laid OVER silent scenes, in editor
**Engine:** Gemini 3.1 Flash TTS (`gemini-3.1-flash-tts-preview`)
**Voice:** Sulafat (same warm Georgian female baseline as Bubabu demo voiceover for brand consistency)
**Total narrator runtime:** ~22 seconds across 4 cuttable blocks
**Position:** layered ONLY on silent scenes (1, 5+5.5, 10, 11) - never overlaps with Mom / Bubabu / Nika dialogue

---

## Silent Window Map (where narrator can speak)

| Window | Time | Scene | Available | Narrator beat? |
|--------|------|-------|-----------|----------------|
| A | 0:00-0:07 | 1 - Pain courtyard | 7s | ✅ Beat 1 (5s) |
| B | 0:18-0:21 | 4 - Stairwell | 3s | ❌ skip - too short, let footsteps breathe |
| C | 0:25-0:40 | 5+5.5+6 - Approach + open + lift | 15s | ✅ Beat 2 (5s, placed 0:28-0:33) |
| D | 0:48-0:51 | 8 - Wonder | 3s | ❌ skip - let silence land the magic |
| E | 0:57-1:08 | 10 - Joy montage | 11s | ✅ Beat 3 (7s, placed 0:59-1:06) |
| F | 1:08-1:15 | 11 - Final hero | 7s | ✅ Beat 4 (5s, placed 1:09-1:14) |

---

## TTS Settings

```
VOICE: Sulafat
STYLE: Empathetic
PACE: Natural
ACCENT: American (Gen)
AUDIO PROFILE: Warm female storyteller, age 38, intimate mother-narrator energy. NOT documentary detached, NOT commercial pitch, NOT actress flat read. She has lived through screen-addicted parenting and found something that worked. Voice carries quiet wisdom, calm warmth, slight smile baseline. Real micro-breaths between sentences (audible inhale OK). Full emotional arc across 4 blocks:

BLOCK 1 (PAIN — over zombie courtyard): Lean in close, intimate confession tone, slow slight melancholy. "ყოველ საღამოს" almost whispered, weight of recognition. "ერთი და იგივე სცენა" lands with quiet shrug — every parent knows this.

BLOCK 2 (DISCOVERY — over bedroom approach): Voice lifts gently, conspiratorial wonder. "მაგრამ ერთ დღეს" warm rising tone, like sharing a secret with a friend. "რაღაც შეიცვალა" slow soft awe.

BLOCK 3 (VALUE PROP — over joy montage): Mother-pride awe. Slow proud landings on each beat. "ბუბაბუ" tender. "AI მეგობარი" warm wonder lift. "ბევრ ენაზე" gentle confident drop.

BLOCK 4 (CTA — over final hero): Warm invitation, trusted-friend send-off. "ბუბაბუ" gentle. "bubabu.ge" slow clear confident. "სამას სამოცი ლარი" simple landing without sales pitch energy.

GENERAL: Slight smile baseline. NEVER syrupy. NEVER announcer. NEVER infomercial. Voice should make the listener FEEL she has watched her own kid bond with this owl. Authentic mother discovery shared with one trusted friend across the table.
SCENE: Cozy Tbilisi evening, golden light, narrator reflecting on the moment unfolding on screen.
SAMPLE CONTEXT:
```

---

## BLOCK 1 - PAIN (0:00-0:05, ~5s)
**Layered over:** Scene 1 (zombie boys courtyard)
**Function:** parent-recognition hook

> ყოველ საღამოს ერთი და იგივე ხდება.

**Russian translation (for Archil approval):**
> Каждый вечер - одна и та же сцена.

**English translation (for international cut):**
> Every evening - the same scene.

**TTS direction:** quiet recognition tone, slight melancholy, soft exhale on "სცენა"

---

## BLOCK 2 - DISCOVERY (0:28-0:33, ~5s)
**Layered over:** Scene 5 (boys approach bedroom + see Bubabu box)
**Function:** turning-point setup before Bubabu reveal

> მაგრამ ერთხელაც... ყველაფერი შეიცვალა.

**Russian:**
> Но однажды - что-то изменилось.

**English:**
> But one day - something changed.

**TTS direction:** soft conspiratorial lift on "ერთ დღეს", slow warm awe on "შეიცვალა"

---

## BLOCK 3 - VALUE PROP (0:59-1:06, ~7s)
**Layered over:** Scene 10 (joy montage peak laughter)
**Function:** product positioning - what Bubabu IS

> Bubabu - ბავშვის პირველი AI მეგობარი. ლაპარაკობს, უსმენს, ეთამაშება - ბევრ ენაზე.

**Russian:**
> Bubabu - первый AI-друг ребёнка. Говорит, слушает, играет - на многих языках.

**English:**
> Bubabu - your child's first AI friend. Speaks, listens, plays - in many languages.

**TTS direction:**
- "ბუბაბუ" - tender warm landing
- "პირველი AI მეგობარი" - lift with quiet wonder, this is the hook phrase
- "ეუბნება, უსმენს, თამაშობს" - three-beat rhythm, each verb half-beat between
- "ბევრ ენაზე" - gentle confident drop, mother-pride

---

## BLOCK 4 - CTA (1:09-1:14, ~5s)
**Layered over:** Scene 11 (final hero CTA)
**Function:** URL + price close

> Bubabu - bubabu.ge - 360 ლარი.

**Russian:**
> Bubabu - bubabu.ge - триста шестьдесят лари.

**English:**
> Bubabu - bubabu.ge - three hundred sixty lari.

**TTS direction:**
- "ბუბაბუ" - gentle warm
- "bubabu.ge" - slow clear, confident drop, like leaving a phone number with a trusted friend
- "სამას სამოცი ლარი" - simple landing, no sales pitch energy, just the number

---

## FINAL SCRIPT (single line for one TTS render - cut by sentence in editor)

```
ყოველ საღამოს ერთი და იგივე ხდება. მაგრამ ერთხელაც... ყველაფერი შეიცვალა. Bubabu — ბავშვის პირველი AI მეგობარი. ლაპარაკობს, უსმენს, ეთამაშება — ბევრ ენაზე. Bubabu — bubabu.ge — 360 ლარი.
```

**Note on TTS rendering:**
- "Bubabu" in Latin within Georgian text - Sulafat may pronounce it as English. If TTS reads it awkwardly, replace with `ბუბაბუ` (Mkhedruli) in the TTS input - the text overlay still uses Latin "Bubabu" / "bubabu.ge".
- "ბევრ ენაზე" stays as text - no digit conversion needed.
- "360 ლარი" - TTS reads `სამას სამოცი ლარი`.

---

## Mix Notes

- **Narrator volume:** -14 dB (front-most layer above music)
- **Music ducks:** -8 dB during narrator beats
- **Foley:** stays at -18 dB underneath narrator (footsteps, room tone audible)
- **Diegetic dialogue:** narrator MUST NOT overlap with Mom / Bubabu / Nika lines - 0.5s clean gap before/after every diegetic line
- **Reverb:** very light room tone reverb on narrator (sounds like she's in same intimate space, not voiceover booth)

---

## Production Workflow

1. **Generate full TTS** in Gemini AI Studio - paste FINAL SCRIPT, set Sulafat + Empathetic + Natural + American Gen
2. **Temperature:** 1.0 (mandatory on 3.1 model)
3. **Cut by sentence** in editor → 4 clean blocks
4. **Layer over silent scene windows** per timing map above
5. **Verify no overlap** with diegetic dialogue (Scenes 2, 3, 4.5, 7, 9)
6. **Duck music** -8dB during each narrator beat

---

## Compliance Check

- [x] All 7 TTS fields present (VOICE + AUDIO PROFILE + STYLE + PACE + ACCENT + SCENE + SAMPLE CONTEXT)
- [x] STYLE = one of 6 presets (Empathetic)
- [x] PACE = one of 4 presets (Natural)
- [x] ACCENT = one of 7 presets (American Gen)
- [x] No pause tags inline
- [x] No emotion adjective tags inline
- [x] FINAL SCRIPT single-line concat present
- [x] Georgian text + English-only tags rule honored
- [x] No CAPS on Mkhedruli
- [x] Under 4,000 bytes
- [x] No overlap with diegetic dialogue scenes
- [x] Total narrator time ~22s of 70s = doesn't dominate visuals
