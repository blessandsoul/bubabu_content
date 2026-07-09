# Voiceover - Bank of Georgia Cashback Weekend Ad (15s)

**Engine:** Gemini 3.1 Flash TTS (`gemini-3.1-flash-tts-preview`)
**Voice:** Sulafat (warm Georgian female, mom-energy, lived-in)
**Length:** ~12 seconds spoken, fits inside 15s video with breath room

---

## TTS Settings

```
VOICE: Sulafat
STYLE: Empathetic
PACE: Natural
ACCENT: American (Gen)
AUDIO PROFILE: Warm Georgian female age 38, real mom-energy, slight smile in voice, lived-in motherly tone. NOT actress reading copy. NOT salesman pushy. NOT urgency-screaming. THIS DELIVERY: warm trusted-friend telling you about a deal she just discovered. Slight excited lift on numbers ("30%!" / "252!") — genuine surprise energy, not infomercial. Confident landing on URL. Real micro-breaths between sentences.
SCENE: Cozy Tbilisi living room, mom calling a friend across the table to share a tip.
SAMPLE CONTEXT:
```

---

## SCRIPT (3 lines, ~12s spoken - numbers as WORDS per ABSOLUTE rule)

> მხოლოდ შაბათ-კვირას - Bubabu ოცდაათპროცენტიანი ქეშბექით. სამას სამოცი ლარის ნაცვლად - მხოლოდ ორას ორმოცდათორმეტი ლარად. გადაიხადე SOLO ბარათით საიტზე bubabu.ge.

**Russian translation (reference, not for TTS):**
> Только в субботу-воскресенье - Bubabu с тридцатипроцентным кэшбэком. Вместо трёхсот шестидесяти лари - всего двести пятьдесят два. Оплати картой SOLO на сайте bubabu.ge.

**English translation (reference, not for TTS):**
> This weekend only - Bubabu with thirty percent cashback. Just two hundred fifty-two lari instead of three hundred sixty. Pay with your SOLO card on bubabu.ge.

⚠️ **CRITICAL - ABSOLUTE rule per `feedback_numbers_words_voiceover.md`:** every number in TTS script written as WORDS, never digits. Digits in TTS field = inconsistent reading by Gemini (`30` may read as "სამი ნული" not "ოცდაათი"). Words = deterministic pronunciation. Captions / stickers / on-screen text follow Lang Architect "digits as digits" rule - that rule does NOT apply to voiceover.

---

## Delivery Notes

- **LINE 1** `მხოლოდ შაბათ-კვირას — Bubabu ოცდაათპროცენტიანი ქეშბექით`: warm intimate setup, conspiratorial like sharing a tip with a friend. Slight smile-lift on "ქეშბექით".
- **LINE 2** `სამას სამოცი ლარის ნაცვლად — მხოლოდ ორას ორმოცდათორმეტი ლარად`: clear price contrast. Slow on "ორას ორმოცდათორმეტი" - let the new low number land.
- **LINE 3** `გადაიხადე SOLO ბარათით საიტზე bubabu.ge`: action verb ("გადაიხადე" = "pay") + brand + URL close. Calm confident drop. "bubabu.ge" slow clear - like leaving a phone number with a trusted friend.

Total ~12s spoken - leaves 0:00 cyan-chime SFX room and 14-15s breath at end.

---

## FINAL SCRIPT (single-line concat for TTS field - paste this)

```
მხოლოდ შაბათ-კვირას — Bubabu ოცდაათპროცენტიანი ქეშბექით. სამას სამოცი ლარის ნაცვლად — მხოლოდ ორას ორმოცდათორმეტი ლარად. გადაიხადე SOLO ბარათით საიტზე bubabu.ge.
```

---

## TTS Notes

- "Bubabu" written in Latin within Georgian text - Sulafat may read in English; replace with `ბუბაბუ` if read awkwardly (text overlay still uses Latin "Bubabu" per AGENT LANG brand-name rule).
- ALL numbers spelled as Georgian words IN THE SCRIPT (never digits). Digits in TTS field = unreliable Gemini pronunciation. The script above contains: `ოცდაათპროცენტიანი` (30%), `სამას სამოცი` (360), `ორას ორმოცდათორმეტი` (252).
- "ქეშბექი" - established Georgian loanword for cashback (per Lang Architect).
- "გადაიხადე" - direct imperative "pay" - gives clear action.
- "SOLO" - read as "სოლო" (BoG product wordmark stays Latin).
- "bubabu.ge" - reads as "ბუბაბუ წერტილი ჯი" (bubabu dot gee).

Temperature: 1.0 (mandatory on 3.1).
Retry up to 3× if metallic / truncated.

---

## Compliance Check

- [x] All 7 TTS fields present
- [x] STYLE = Empathetic (1 of 6 presets)
- [x] PACE = Natural (1 of 4)
- [x] ACCENT = American Gen (1 of 7)
- [x] No pause tags inline
- [x] No emotion adjective tags inline
- [x] FINAL SCRIPT single-line concat
- [x] Georgian text, no Cyrillic, no mtavruli
- [x] **Numbers as WORDS** (ABSOLUTE per `feedback_numbers_words_voiceover.md` 2026-04-19) - `ოცდაათპროცენტიანი` / `სამას სამოცი` / `ორას ორმოცდათორმეტი`. NEVER digits in TTS script. Lang Architect "digits as digits" rule applies to ON-SCREEN text (captions/stickers), not VO.
- [x] "ქეშბექი" not "უკან"
- [x] Action verb "გადაიხადე" present
- [x] Under 4,000 bytes
- [x] Pre-save grep `\b\d+\b` on FINAL SCRIPT block = zero hits (only `bubabu.ge` URL allowed)
