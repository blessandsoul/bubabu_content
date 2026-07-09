# BUBABU CORPUS ANALYSIS - Georgian Kids YT Top Channels

**Built:** 2026-05-26
**Source corpus:** 29 transcripts (12 KA usable) from 2 Georgian kids YT channels
**Channels:**
- `@ძილისპირულიზღაპრები` (Sleep-Time Fairy Tales) - 10/10 KA transcripts ✓
- `@jirafijoze1` (Giraffe Joze) - 19/121 transcripts landed, 2 KA usable (rest = ro-auto/en-auto/disabled)
**Fetch method:** `youtube-transcript-api` (bypasses COPPA-block that defeated `yt-dlp`)
**Used by:** `bible/BUBABU_SCRIPT_ENGINE.md` (synthesized from this corpus)

---

## CORPUS STATS (12 KA transcripts)

| Metric | Min | Median | Max |
|--------|-----|--------|-----|
| Duration sec | 34 | 396 | 498 |
| Word count | 34 | 455 | 562 |
| Sentence count | 3 | 32 | 51 |
| WPM (words per minute) | 42.6 | 65.6 | 78.5 |
| Sentence length (words) | mean 14.3 / median 7 / 90th-pct 25 | | |

**Take-aways:**
- Standard sleep story = **~6-7 min** (median 396s)
- Word budget per story = **~450-560 words**
- Sentence median = **7 words** - SHORT, kid-comprehensible
- Narrator pace = **65 WPM** - SLOW (ALEKSO uses ~150 WPM for adult audience; kids halve that)
- **~32 sentences per 7-min episode** = ~12-13 sec per beat = matches kids attention span

---

## SIX HOOK ARCHETYPES (from 12 first-sentences)

| # | Archetype | Example (verbatim) | Use when |
|---|-----------|-------------------|----------|
| H1 | **SCENE-PAINT** | `ზამთარია, ცივა და ბუხართან მიკუნტულა ჩვენი დუდუ კურდღელი...` | Open with weather/place/character snapshot |
| H2 | **CHARACTER-ENTRY** | `ერთხელ ჟოზემ გადაწყვიტა, სახლში ჯდომას ჯობია, რომ წავიდე...` | Hero starts the adventure |
| H3 | **EMOTIONAL-NOTE** | `დღეს ჟირაფი ჟოზეს გულში სხვანაირად თბილა, რაღაც კარგზე მიანიშნებს მშვენიერი დილა` | A feeling opens the day |
| H4 | **TIME-ANCHOR** | `ერთ საღამოს, როცა იყო სკვერში ჯდომის ამინდი...` | Anchor a moment in time |
| H5 | **REMEMBER-OPENER** | `დავიწყდა, თუმცა ბევრს კარგად მახსოვს მე ისევ. ადრე კაცი ცხოვრობდა...` | Storyteller-frame folk tale |
| H6 | **DIRECT-INVITATION** | `ამ დებს დღემდე თუ არ იცნობთ, გაიცანით სანამ დროა` | Direct address to child viewer |

**Distribution (12 hooks):**
- H1 SCENE-PAINT: 2
- H2 CHARACTER-ENTRY: 3
- H3 EMOTIONAL-NOTE: 1
- H4 TIME-ANCHOR: 1
- H5 REMEMBER-OPENER: 1
- H6 DIRECT-INVITATION: 2
- Other (greeting / character-call): 2

**Universal hook traits:**
- Never starts with a question
- Never starts with negation ("not")
- Names a character, place, weather, or time within first 7 words
- Sets up rhyme cadence immediately (first sentence ends on a word that the next sentence rhymes with)

---

## CLOSING SECTION - REMOVED 2026-05-27

The former «CANONICAL CLOSING RITUAL» section that lived here (the source-corpus 4-line lullaby + variants + bigram confirmations + «brand-loop signature» framing) was REMOVED per user directive 2026-05-27 + override memory `feedback_bubabu_no_sacred_closing_lullaby` (the override owns the explicit banned-token list). That source-channel signature does NOT transfer to Bubabu. Bubabu story closes on a story-specific warm prose landing line, never a fixed cultural lullaby. The lullaby + descriptors («sacred closing» / «closing ritual» / «brand-loop signature» / «4-gram closing lock» / «cultural lullaby») are BANNED across every Bubabu output.

---

## NARRATIVE ARC (5 beats - Bubabu canonical, post-2026-05-27)

| Beat | T range | Content | Sample |
|------|---------|---------|--------|
| **B1 - SCENE-OPEN** | 0-15% | Weather/setting/character intro | one of 6 hook archetypes (BUBABU_SCRIPT_ENGINE §1) |
| **B2 - PROBLEM** | 15-30% | Character has worry/wish/decision | situational setup |
| **B3 - JOURNEY** | 30-70% | Events unfold (3-5 sub-beats), dialogue-dense | events, encounters, `უთხრა` dialogue verb dominant |
| **B4 - RESOLUTION** | 70-90% | Problem solved, lesson learned | warm resolution |
| **B5 - CLOSE** | 90-100% | Story-specific warm prose landing line | varies per story - NEVER a fixed cultural lullaby |

**Total: ~30 sentences over ~6 minutes for long-form; ~8-10 sentences over ~60 sec for minute format default.**

---

## RHYMED VERSE LAW (sleep stories)

EVERY sleep story sentence is written as **rhyming couplet AA / BB**. Not prose. Two adjacent sentences end on words that rhyme phonetically.

Examples:
- `...ჯობია, რომ წავიდე, / ...მთელი ჩემი საქართველო მოვიარო` (ide/aro feels-rhyming via vowel)
- `უფროსი და თებროლეა, / უმცროსი და თანოა` (lea/oa)
- `ერთხელ კაცი ცხოვრობდა პროფესიით მეისრე / ბევრგვარია ისარიც და იმისი მისიაც` (eisre/isiats)
- `ჯარიც ისე ისროდა / ომს არასდროს აგებდა` (sroda/agebda)

**Rhyme drives the 65 WPM pace.** Verse reads slower than prose. Slow = sleep-inducing.

Bubabu daytime / educational scripts can use FLOWING PROSE (not rhymed verse), but sleep / nighttime / soothing scripts MUST be rhymed verse.

---

## TOP CONTENT VOCABULARY (12 KA transcripts, function-words excluded)

### Character names (proper nouns)
- ჟოზე (Joze) - 28
- პიო (Pio) - 23 (combined `პიოს` 13 + `პიო` 10)
- დუდუნა (Duduna) - 9
- თანო/თებრო (Tano/Tebro sisters) - present in 3 stories
- ნანა (Nana) - 10 (also lullaby marker)
- ჟოზეფინა (Josephina) - present in birthday episode

### Frequency markers (intensifiers / emotional warmth)
- სულ (always) - 26 - "სულ ყველაზე" = "always the most"
- უფრო (more) - 22
- ყველაზე (most) - 10
- კიდევ (still / more) - 12
- ძალიან (very) - 9

### Diminutive / warmth markers
- პატარა (little) - 11
- ტკბილი (sweet) - 9
- ლამაზ (beautiful) - 8

### Action verbs (the doing words)
- უთხრა (told) - 14 - most common dialogue verb
- ვითამაშეთ (we played) - 9
- მოვიდა (came) - 7
- თქვა (said) - 7
- გადაწყვიტა (decided) - pivotal verb

### Cultural / place anchors
- საქართველო (Georgia) - 8
- სახლი (home) - 9 (`სახლში` 9 + `სახლს`)

### Sleep / closure vocabulary
- ძილი/ძილიც/ძილია (sleep variants) - 16+ total (general sleep noun, OK in story body)
- ზღაპარი (fairy tale) - 7
- მეგობარო (friend, vocative) - 8 - Bubabu signature vocative anchor

**Removed 2026-05-27** (lullaby fillers that resurrect the banned cultural close): `იავ` / `ნანა` / `ნანი`. Per `feedback_bubabu_no_sacred_closing_lullaby`.

---

## VOCABULARY DON'T-LIST (kid-safe filter)

Words ABSENT from the corpus that signal adult content / inappropriate:
- No violence vocabulary (war/blood/kill - absent)
- No fear vocabulary (afraid/scared/horror - absent)
- No commercial vocabulary (buy/price/money - absent except K-008 art-school ad which was atypical)
- No screen/tech vocabulary (phone/tablet/internet - absent - kids stories don't mention screens)
- No competition/dominance (better-than/winner/loser - only collective triumph "ჩემპიონები ვართ" = "we are champions" plural)

---

## TOP BIGRAMS (recurring phrases - narrator's signature texture)

| Phrase | Count | Function |
|--------|-------|----------|
| `სულ ყველაზე` | 9 | "always the most" - superlative |
| `უფრო მეტი` | 6 | "even more" - escalation |
| `მეგობარო პატარა` | 5 | vocative + diminutive (signature vocative - Bubabu USES this) |
| `კარგად ვითამაშეთ` | 5 | "we played well" - collective triumph close |
| `ყველაზე უკეთესი` | 4 | "the best of all" |
| `ჩემპიონები ვართ` | 4 | "we are champions" - collective triumph |

**Removed 2026-05-27** (source-channel lullaby bigrams, NOT transferred to Bubabu - explicit banned-token list lives in `feedback_bubabu_no_sacred_closing_lullaby`).

---

## SOURCE-MATERIAL NOTES

### Channel 1: `@ძილისპირულიზღაპრები` (Sleep-Time Fairy Tales)
- 10 videos, all KA, all ~6-7 min rhymed verse sleep stories
- Source-channel closing pattern observed but NOT transferred to Bubabu (per user directive 2026-05-27 + `feedback_bubabu_no_sacred_closing_lullaby` - that close is the source channel's signature, not Bubabu's)
- Characters: Joze giraffe, Duduna rabbit, Pio, Mamini, Tebrole+Tano sisters, Josephina giraffe
- Story themes: friendship, family unity, kindness lessons, adventures, celebrations
- Narrator voice: warm female adult, calm pace, smile-in-voice
- Two videos open with "music only" segments (durations 28 + 30 min) - these are background music NOT stories, excluded from text analysis

### Channel 2: `@jirafijoze1` (Giraffe Joze)
- 121 videos total, mostly disabled/no-language for transcript extraction
- Many videos in `ro-auto` (Romanian dubs of Joze for Romanian market)
- 2 KA stories landed:
  - `0aWXp934fn4` "ისწავლე ხატვა" (Learn to draw) - 33-sec art school ad, atypical (commercial)
  - One full episode "ფეხბურთის დღე" (Football Day) - ~7 min collective-triumph closure
- Same character roster as ch1
- More energetic / educational than ch1 sleep stories

---

## CALIBRATION CAVEATS (L1-L4 per CLAUDE.md)

- **L1 FORMAT** ✓ - Corpus extracted, 12 KA transcripts parsed, frequencies counted
- **L2 SPEC-CONFORMANCE** ✓ - Patterns observed in corpus match the rules to be codified
- **L3 GENERATOR-CONVERGENCE** - engine derived will need viewer test (does Bubabu script in this style read warm to a Georgian parent reading aloud?)
- **L4 VIEWER-TEST** - PENDING. Engine ships at L2; viewer test = first user read-aloud + grandmother test

**Sample size:** 12 KA (very small). ALEKSO_TEXT_ENGINE v3.2 used 444 transcripts. This engine is **v1.0 with explicit small-corpus disclaimer**. Refresh when more KA subs land (try `youtube-transcript-api` again later - IpBlocked rate-limit may reset).

**Channel 2 IpBlocked 14 entries** - retry after 24h cooldown, can expand corpus to ~33 transcripts then.
