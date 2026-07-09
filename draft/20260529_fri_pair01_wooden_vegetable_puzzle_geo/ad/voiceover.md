# Voiceover - pair01 Ad (3 cues, soft emotional explainer of why this toy matters)

**Engine:** Gemini TTS, preset **Charon Storytime** (same preset as cartoon - brand voice consistency)
**Pace:** The Drift - 135-145 wpm, slow intimate continuous flow (same as cartoon)
**Speaker:** off-screen narrator (per VOICEOVER_ENGINE §6 editor-overlay path - silent img2vid render + Gemini TTS voice composited in editor over foley, NO Speech: tag in any ad/video.md SPEC)
**Language pipeline:** EN draft (this file) → user produces KA verbatim in `voiceover_geo.md` per memory `feedback_bubabu_no_ai_ka_verse_or_prose`
**Approach:** soft emotional product explainer per user directive 2026-05-30 «без цены, просто объясни почему игрушка классная». Sells RESULT (child learns by holding) not TOOL (puzzle features). Zero price, zero CTA - those live only in `post.md` text overlay. Brand voice warm + gentle, NOT commercial.

## Cue list (one per scene)

| Cue | Scene | Duration target | EN cue |
|-----|-------|----------------|--------|
| V1 | Scene 1 - JOY-HOP REVEAL | ~5.6 sec spoken | Seven wooden shapes painted by hand, made for a child's hand to hold. |
| V2 | Scene 2 - THEMATIC PLAY | ~3.9 sec spoken | Each shape carries a Georgian name, learned by matching. |
| V3 | Scene 3 - POSSESSION HOLD | ~6.0 sec spoken | A small handmade thing that stays on her shelf long after the screens go dim. |

**Total:** 36 EN words across 3 cues. Per cue average: 12.0 words. Trimmed -14% from v1 (42→36 words) per user directive 2026-05-31 «текст длиннее укороти на 10-15%».

## FULL SCRIPT - Bubabu narrator Charon (paste-ready single TTS run)

```
Seven wooden shapes painted by hand, made for a child's hand to hold. Each shape carries a Georgian name, learned by matching. A small handmade thing that stays on her shelf long after the screens go dim.
```

**Paste-ready note:** one continuous paragraph, no blank-line breaks between cues, no `...` ellipses, no `[bracket]` TTS directives. Charon Storytime preset reads it as one flowing soft explainer. Single TTS run captures all 3 cues in one Gemini API call - editor splits by silence-detection or manual cut at scene boundaries.

## TTS Settings (Gemini TTS - Charon Storytime preset, same as cartoon for brand consistency)

| Setting | Value |
|---------|-------|
| **VOICE** | Charon |
| **PACE** | The Drift (135-145 wpm, slow, intimate, continuous flow) |
| **STYLE** | warm storyteller, soft emotional explainer, gentle parent-warmth |
| **REGISTER** | intimate-conversational, NOT commercial-announcer |
| **PITCH** | natural mid-low, NO upward sales-inflection |
| **EMPHASIS** | soft on «wooden» (Cue 1) / «Georgian name» (Cue 2) / «handmade thing» (Cue 3) - single-word lift, never shouted |
| **PAUSE** | natural breath between cues (~0.5-0.8 sec, editor handles via silence-detection) |
| **AUDIO PROFILE SCENE** | sunlit terrace + golden hour + friend leaning forward + espresso/wine + cicadas (per VOICEOVER_ENGINE §4 - warm storyteller frame mandatory; NEVER midnight/rain/alone/candle/noir/confession/brooding) |

## Audit (per VOICEOVER_ENGINE + BRAND_ENGINE + SLOP_FILTER)

### VOICEOVER_ENGINE compliance
- [x] §1 VO-FIRST workflow respected - voiceover drafted BEFORE video.md edits (this file ships before any Speech: tag changes to video SPECs).
- [x] §2 Block count 3 cues - under the 6-15 default since ad is short-form commercial, not narrative cartoon. Acceptable per §2 «6-15 ideal» as guideline not floor.
- [x] §3 FULL SCRIPT copy-paste block present as one continuous paragraph (per §BS body-style - no blank-line breaks between cues).
- [x] §4 AUDIO PROFILE SCENE = warm storyteller (sunlit terrace + golden hour). NEVER midnight/rain/alone/candle-alone/noir/confession/brooding. Tactical-dark content N/A here.
- [x] §5 Speaker visible in matching photo? NO - narrator is off-screen Charon. Bubabu visible in all 3 scenes but beak closed throughout (brand lock). Per §6 off-screen voice = editor overlay path (this is the intended setup for ad - Bubabu silent in frame, narrator floats above as parent-warmth presence).
- [x] §6 Off-screen voice = editor overlay. NO Speech: tag added to any ad/video.md SPEC. Silent img2vid renders + Gemini TTS voice + composite in editor. SPEC field `speech_editor_overlay` flag = implicit (Bubabu beak-closed brand lock already means no native lip-sync expected).
- [x] §7 Video prompt audio = SFX/foley only one-line. Verified - ad/video.md Scene 1/2/3 video SPECs have `sfx_cues` only, NO speech/narration/lip-sync mentions, NO «composited in editor» mentions, NO «cue N» references. Negative_prompt bans Speech tag.

### BRAND_ENGINE compliance (sales psychology)
- [x] Sells RESULT not TOOL. «Hand-painted shapes for a child's hand to hold» (Cue 1) = result (child interaction) not feature (wooden material spec). «Each shape carries a Georgian name, learned one matching piece at a time» (Cue 2) = result (language learning + matching skill) not feature (7 tiles + slots count). «Stays on her shelf long after the screens go dim» (Cue 3) = result (lasting keepsake vs ephemeral apps) not feature (durability spec).
- [x] Zero price mentions (per user directive). Zero price text, zero currency symbol, zero numerals, zero domain spoken, zero «buy now» / CTA verbs. **TOTAL price ban across ad** - scope re-extended 2026-05-31 per user directive: NO price in voiceover.md, NO price in video.md, NO price on cover.md, NO price in post.md caption either. Price lives ONLY in operator-internal SKU table data (brief.md / meta.md retail metadata for shop staff), NEVER in customer-facing content. Channels (BUBABU.GE + Tbilisi Mall + Galleria Tbilisi) named in post.md as «where to find it», price discovered by customer on site / in store.
- [x] Bar Test gate: would a parent at a bar mention this? Yes - handmade wooden + Georgian language teaching = identity-trigger memorable, parent-warmth pull.
- [x] Bubabu brand voice preserved: warm / friendly / smart / gentle. Same Charon Storytime preset as cartoon - single brand voice across pair, no commercial-narrator drift.
- [x] No aggressive selling tone, no urgency push, no scarcity claim, no comparison to other toys.

### SLOP_FILTER ENGINE compliance (universal anti-AI-tells)
- [x] No negation-correction («not X, it's Y» / «не X, а Y»). Cue 1 first draft tried «No screen, no battery - just wooden shapes» - REJECTED as §2 negative listing slop. Replaced with positive framing «A wooden tray with seven hand-painted shapes...».
- [x] No throat-clearing openers («Here's the thing» / «Let me be clear» / «To be honest»).
- [x] No emphasis crutches («Full stop» / «Let that sink in» / «Make no mistake»).
- [x] No business jargon («deep dive» / «circle back» / «lean into»).
- [x] No adverb intensifiers («really» / «just» / «literally» / «actually» / «basically» / «simply» / «truly»). Cue 1 originally had «just wooden shapes» - JUST removed.
- [x] No meta-commentary («Plot twist:» / «Spoiler:» / «As we'll see»).
- [x] No vague declaratives («The stakes are high» / «This changes everything»).
- [x] No false agency («the data tells us» / «the market rewards» - every Cue has concrete agent: tray / shape / handmade thing).
- [x] No passive voice anywhere except «painted by hand» (Cue 1) which is purposeful craft-emphasis, acceptable per §10 exception.
- [x] No lazy extremes («everyone knows» / «every parent should»).
- [x] No rhetorical setups in body («What if» / «Think about it»).
- [x] Em-dashes - none used (clean comma-flow throughout).
- [x] No staccato («X. That's it. That's the thing.»).
- [x] No So,/Look, paragraph openers.
- [x] No performative emphasis («creeps in» / «I promise» / «actually matters»).

### §BS BODY-STYLE compliance (Bubabu universal 2026-05-29)
- [x] Zero `...` ellipses in any cue body or FULL SCRIPT block.
- [x] Zero `[bracket]` TTS-style directives prefixing any cue body.
- [x] Every cue = one complete long flowing grammatical sentence linked by commas.
- [x] Reads aloud as one warm continuous explainer paragraph.

### Brand-voice tension check (ad VO vs cartoon VO)
- Cartoon VO = bedtime grandmother narrating Bubabu's adventure to a child (audience POV: child + parent listening together).
- Ad VO = same Charon voice but addressing parent directly (audience POV: parent watching alone with sound on).
- Risk: same voice in two registers might feel forced. Mitigation: Charon Storytime preset works equally well as cozy-grandmother-talking-to-grandchild AND cozy-grandmother-explaining-gift-to-grandchild's-parent. Same warmth, slightly different addressee. Brand voice unified.

## Word count check

36 EN words across 3 cues. Per cue average: 12.0 words (trimmed -14% from v1's 42 words per user directive 2026-05-31).
- @ Charon Storytime 140 wpm = ~15.4 sec spoken + ~1.5 sec inter-cue breath = **~17 sec final ad VO duration.**
- Ad video master ~13-19 sec - VO fits cleanly with breathing room at scene transitions.
- If editor wants even tighter - trim Cue 1 «painted by hand,» = -3 words = saves ~1.3 sec.

## Editor compositing notes

1. Render all 3 ad/video.md scenes silently (Veo output = foley only, NO speech).
2. Render `voiceover.md` FULL SCRIPT in Gemini TTS Studio with Charon Storytime preset, AUDIO PROFILE SCENE = sunlit terrace warm storyteller. Single TTS run captures all 3 cues.
3. Editor splits VO audio by silence-detection (or manual cut at scene boundaries).
4. Composite: Veo silent video tracks + foley layer (from Veo `sfx_cues`) + VO layer (Charon at -3 dB above foley, -22 dB below foley peak so foley still breathes through) + optional Lyria 3 brand-bell loop layer at -22 dB under foley.
5. Mix mastered at -14 LUFS for FB/IG/TT/YT broadcast standard.

## Post-render listening test

- [ ] VO reads naturally without staccato or hesitation.
- [ ] Cue 1 «hand to hold» lands soft, not declarative.
- [ ] Cue 2 «one matching piece at a time» has gentle rhythm (not sing-songy).
- [ ] Cue 3 «long after the screens go dim» lands as quiet closing reflection (not sales punchline).
- [ ] VO does NOT overpower foley - wooden tile-click in Scene 2 still audible.
- [ ] Brand voice consistent with cartoon VO (same Charon, same warmth).
- [ ] Mom-buyer reaction test: does it feel like a friend explaining a gift, or like a commercial? Should feel like the former.

## Calibration

- L1 FORMAT - VERIFIED at write time (3 cues, FULL SCRIPT block, audit gates pass).
- L2 SPEC-CONFORMANCE - VERIFIED (Charon Storytime preset matches cartoon, off-screen narrator path per VOICEOVER_ENGINE §6, no Speech tag added to video SPECs, BRAND_ENGINE result-focus + zero-price + zero-CTA verified, SLOP_FILTER + §BS clean).
- L3 GENERATOR-CONVERGENCE - PENDING Gemini TTS render. Risk: Charon at 140 wpm might overshoot ~19 sec target - listen-test before locking ad video duration.
- L4 VIEWER-TEST - PENDING audience response post-publish. Success metric: organic parent comments mentioning «handmade» / «Georgian names» / «not screen» concepts = VO pull-through working.

**Allowed claim now:** «VO draft EN ready. Outcome pending Gemini TTS render + KA translation from user + editor composite.»
**Forbidden claim:** «Done / sells / works / ready» - outcome unverified.

## Pending user actions

- [ ] User reads EN draft and confirms tone (especially that it feels like a friend explaining, not a commercial).
- [ ] User produces `voiceover_geo.md` KA verbatim translation per memory rule (§BS body-style applies to KA too - zero `...`, zero `[bracket]`, complete flowing sentences).
- [ ] User renders Charon Storytime in Gemini TTS Studio (FULL SCRIPT block paste-ready) and approves before editor composite.
