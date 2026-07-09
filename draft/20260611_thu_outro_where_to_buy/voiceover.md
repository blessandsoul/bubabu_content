# BUBABU OUTRO VO - "WHERE TO BUY" (render ONCE, reuse in every episode)

Voice: **Charon - Storytime preset** (locked Bubabu brand narrator, same voice as cartoons + ads). Pace ~135 wpm, warm and unhurried. One TTS run per language, saved as `bubabu_outro_vo_ka.mp3` / `bubabu_outro_vo_en.mp3`, reused forever.

AUDIO PROFILE SCENE: Warm toy boutique at golden hour. A friendly storyteller stands at the open door, smiling, pointing a family the way inside. Shelves of soft toys glow in butter light. He is glad they came.

Length: ~27 EN words ≈ 11-12 sec at 135 wpm. Video master = 8 sec motion + last-frame freeze to ~12 sec (see meta.md).

No price anywhere. Locations are a "where to find it" line, not a sales pitch (per `memory/reference_bubabu_retail_locations.md`).

---

## Cue map - EN master

## Cue B01 (T=0:00-0:04)
Find Bubabu at Tbilisi Mall, third floor, in the food court.

## Cue B02 (T=0:04-0:08)
At Galleria Tbilisi, third floor, next to the elevator.

## Cue B03 (T=0:08-0:12)
Or online, at BUBABU.GE.

## FULL SCRIPT - EN (Charon Storytime, single TTS run)
Find Bubabu at Tbilisi Mall, third floor, in the food court. At Galleria Tbilisi, third floor, next to the elevator. Or online, at BUBABU.GE.

---

## Cue map - KA draft (USER FINALIZES - assembled from your verbatim lines, only the opening verb is mine)

## Cue B01 (T=0:00-0:04)
ბუბაბუს იპოვით თბილისი მოლში, მესამე სართულზე, კვების სივრცეში.

## Cue B02 (T=0:04-0:08)
გალერია თბილისში, მესამე სართულზე, ლიფტის მიმდებარედ.

## Cue B03 (T=0:08-0:12)
ან საიტზე, ბუბაბუ წერტილი ჯი.

## FULL SCRIPT - KA (single TTS run)
ბუბაბუს იპოვით თბილისი მოლში, მესამე სართულზე, კვების სივრცეში. გალერია თბილისში, მესამე სართულზე, ლიფტის მიმდებარედ. ან საიტზე, ბუბაბუ წერტილი ჯი.

Pronunciation hint: the domain is spoken exactly as written above - «ბუბაბუ წერტილი ჯი» (never «წერტილი გე», never Latin `bubabu.ge` inside the KA TTS body). «მე-3» from the on-screen text is spelled out as «მესამე» for TTS only.

---

## Notes
- Complete flowing sentences, zero ellipsis, zero bracket directives in cue bodies (Bubabu TTS law). Pauses = sentence breaks.
- Numbers as words in VO («მესამე» / "third"); the digit form «მე-3» lives only in the editor overlay text (meta.md).
- KA cues B01-B02 use the user's location lines verbatim; B03 verbatim. Only «ბუბაბუს იპოვით» is glue - confirm or replace it when finalizing (per `feedback_bubabu_no_ai_ka_verse_or_prose`).
- This VO is an editor overlay over the silent Veo render (VOICEOVER_ENGINE §6) - no Speech tag in video.md, Bubabu beak stays closed.
