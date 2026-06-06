# Audio — "ეზოს ბიჭები"

**Engine:** Suno AI (music) + Gemini 3.1 Flash TTS (dialogue) + foley library + custom SFX
**Total runtime:** 70 seconds
**Style DNA:** Pixar warm family commercial — *Coco* tenderness × *Encanto* ukulele warmth × *Up* "Married Life" intimacy × Pixar product brand sting

---

## Music Arc Map

| Time | Beat | Music state | Instruments | BPM | Key |
|------|------|------------|-------------|-----|-----|
| 0:00–0:07 | Pain courtyard | Near-silence, uncomfortable | Tiny low cello drone -30dB | — | A minor sus |
| 0:07–0:16 | Mom calls window | Curiosity enters | Soft pizzicato strings | 80 | C major |
| 0:16–0:25 | Stairs + mom greets | Anticipation builds | Pizzicato + light piano | 95 | C major |
| 0:25–0:36 | Bedroom approach + box opening | Suspense | Single piano notes, sparse | 90 | C major sus |
| 0:36–0:40 | Lift Bubabu | Held breath | Soft pad only, near-silent | — | — |
| 0:40–0:48 | Eyes activate + first hello | **MAGIC** | Warm string swell + cyan-chime | 70 → 90 | F major |
| 0:48–0:51 | Wonder | Sustained | Held warm chord | — | F major |
| 0:51–0:57 | Invitation + "Riddles!" | Playful warmth | Ukulele + light strings | 100 | F major |
| 0:57–1:08 | Joy montage | **TRIUMPH** | Full ensemble — ukulele + strings + piano + light percussion | 115 | G major |
| 1:08–1:15 | Final hero CTA | Resolution | Warm sustained chord + signature bell chime | — | G major |

**Music duck:** -12dB under all dialogue lines. Foley sits on top of music at -18dB.

---

## Suno Prompt

```
Warm uplifting Pixar-style family brand commercial music. Instrumental only. No lyrics. 70 seconds total. Style: Coco gentleness × Encanto ukulele warmth × Up Married Life intimacy. Light orchestral with ukulele undertone, gentle strings, soft piano, subtle percussion. NEVER folk-dance, NEVER epic cinematic, NEVER aggressive — just intimate kid-magic family commercial.

[0:00-0:07] Near-silence. Tiny low cello drone, uncomfortable A minor sus, -30dB barely there.

[0:07-0:16] Soft pizzicato strings enter, curious warm C major, 80 BPM, light and tentative.

[0:16-0:25] Pizzicato + light piano notes build, 95 BPM, anticipation rising, still warm.

[0:25-0:36] Drop to sparse single piano notes, suspense, near-silence, 90 BPM C major sus, breath held.

[0:36-0:40] Soft warm pad only, near-silent, sustained, breath of wonder approaching.

[0:40-0:48] **MAGIC MOMENT** — warm string swell rises slowly, F major, 70 BPM softening to 90. Single bright bell chime accents the awakening. Tender, like a heart waking up.

[0:48-0:51] Sustained warm F major chord, held, gentle, like watching wonder cross a child's face.

[0:51-0:57] Ukulele enters playful, light strings counter-melody, F major, 100 BPM, warm invitation energy.

[0:57-1:08] Full ensemble — ukulele rhythm + warm strings + soft piano + light percussion shaker + glockenspiel sparkle, G major, 115 BPM, triumphant family-joy peak. Pure Pixar-finale energy. Builds without aggression.

[1:08-1:15] Resolves to warm sustained G major chord, ukulele settles, single signature bell chime closes, soft fade out 2 seconds.

Genre: orchestral commercial / kid family Pixar score. Mood: warm, hopeful, intimate, magical. Mix: clean, no reverb wash, dialogue-friendly.
```

---

## Dialogue (Gemini TTS)

| Line | Speaker | Voice | Style |
|------|---------|-------|-------|
| "ნიკა, მალე ამოდი! რაღაც გიყიდე!" | Mom (Sulafat) | Warm Georgian female 38, real mom-energy | Empathetic, raised volume |
| "დედა, მეგობრებთან ერთად ვარ!" | Nika (child voice or library) | 9-10 yo Georgian boy | Tired-bored zombie tone |
| "ეგენიც ამოიყვანე!" | Mom (Sulafat) | Same as above | Playful wave-energy |
| "ოთახში შედი, იქ შენთვის სიურპრიზია." | Mom (Sulafat) | Same | Knowing playful tease |
| "გამარჯობა, ჩემო პატარა მეგობარო!" | Bubabu (Tuya / Sulafat backup) | AI companion age-neutral | Slow gentle awakening |
| "რისი თამაში გინდა?" | Bubabu | Same | Playful inviting question |
| "გამოცანობანას!" | Nika | Same boy voice | Bright excited |

---

## Foley List

| SFX | Source | Use |
|-----|--------|-----|
| Birds chirping | Library — sparse Mediterranean | Scenes 1-3 (courtyard) |
| Distant traffic hum | Library | Scenes 1-3 |
| Kid sneaker footsteps on concrete | Custom or library | Scene 4 (stairwell) |
| Apartment door open/close | Library | Scene 4 → 4.5 |
| Kitchen room tone | Library — warm domestic | Scenes 4.5–10 |
| Bed fabric rustle | Custom | Scene 5 |
| Cardboard flap rustle | Custom | Scene 5.5 |
| Soft plush lift | Custom | Scene 6 |
| Wonder gasps × 3 | Voice ADR | Scene 8 |
| Group kid laughter | Voice recording | Scene 10 |
| Hand clap × 1 | Library | Scene 10 |
| Fist pump fabric snap | Library | Scene 10 |
| **Bubabu cyan-chime bell** ⭐ | Custom synth — C5→E5 ascending bell, 0.8s, 200ms decay, soft attack | Scenes 7 + 11 |
| **Bubabu heart-pulse blip** 💗 | Custom synth — heartbeat-like soft blip, 0.3s, warm synth | Scenes 9 + 10 |

---

## Mix Notes

- **Master format:** stereo, -16 LUFS for Facebook/Instagram, -14 LUFS for TikTok
- **Dialogue:** -12 dB, mono center, light de-esser
- **Music:** -18 dB baseline, ducks to -22 dB under dialogue (-12 dB ducking)
- **Foley:** -18 dB to -22 dB, stereo wide
- **Ambient:** -28 dB to -32 dB, subtle bed
- **Bubabu chime/blips:** -16 dB, slight reverb tail
- **Total runtime:** 70 seconds + 0.5s tail fade

---

## Production Workflow

1. **Generate Suno track** using prompt above. Aim for full 70s in one render. Retry if structure off.
2. **Generate TTS dialogue** in Gemini AI Studio per `voiceover.md` settings — separate clip per line.
3. **Foley library pull + custom record** — group laughter and wonder gasps need real kid voices recorded.
4. **Mix in Premiere/CapCut/DaVinci:**
   - Layer 1: Music (Suno)
   - Layer 2: Dialogue (TTS, ducked music auto)
   - Layer 3: Foley + ambient
   - Layer 4: Bubabu product SFX (chime + heart blips)
5. **Final master:** -16 LUFS for FB/IG, -14 LUFS TikTok cut.
