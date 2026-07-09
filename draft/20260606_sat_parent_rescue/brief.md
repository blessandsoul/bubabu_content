# BRIEF - Bubabu Story-Ad «Parent Rescue» (9 scenes)

**Type:** standalone hero story-ad (sells the Bubabu AI-owl itself, not a catalog SKU). NOT a SKU-pair, NOT the locked 3-scene Smart-Gifts ad.
**Date:** 2026-06-06 (sat) · **Status:** DRAFT in `agents/bubabu/draft/`, moves to `content/` only after the user confirms it is published.
**Deliverable:** a PROMPT PACKAGE. The user renders the 9 clips in Veo 3.1, records the Georgian voiceover, generates the Lyria 3 music, and composites in the editor. Claude does NOT render.

> 🔁 **RENDER-STYLE UPDATE 2026-06-06 - HYPERREAL 8K (replaced Pixar per user request: hyperreal 8K render, replace Pixar).** `video.md` + `cover.md` are now photoreal (Sony A1 / Portra / creamy bokeh, 8K). Child-safety: **children shown from-behind / faces hidden**, the mother's photoreal face carries the emotion, Bubabu = photoreal plush. Magic (flight + wonder-light) kept «as is» - **probe-gated** (render S1 + S3 first). **Needs Archil sign-off (brand-style break).** Pixar version recoverable via git. `voiceover.md` / `audio.md` / `post.md` unchanged (render-style-independent).

## Concept (one sentence)
A mother drowning in after-school chaos gets rescued by a little owl that flies in, calms the room with a story, and becomes the toy she phones a friend to recommend - sold entirely on the parent's relief, never on the toy's features.

## Why this exists
P2 PAIN + P4 SOCIAL PROOF pillar fusion. The user asked to "turn on the seller agent" - so the whole piece runs a Problem→Agitate→Solve→Proof→soft-CTA persuasion spine through a first-person mother voiceover. The result a parent buys is the calm, not the AI.

## Format deviations from the locked Bubabu ad (all deliberate, logged)
1. **9 scenes**, not the locked 3-scene REVEAL/PLAY/HOLD ad. Justified by the user's explicit 9-beat story. Distinct deliverable from the sibling 4-scene `20260606_sat_hero_ad_screenfree_friend`.
2. **First-person tired-MOM voiceover** (warm female Gemini TTS, voice **Sulafat**), NOT the Charon Storytime brand-narrator. A bu-narrator cannot say "my kids / my coffee" - the testimonial POV needs the mother's own voice. Scoped to THIS ad; Bubabu's Charon-narrator canon is unchanged. Logged in `voiceover.md` + `meta.md`.
3. **Humans on screen** (mom + 3 kids), which the zero-human locked ad never does. **HYPERREAL render:** the mother is photoreal with her face shown (adult, filter-safe, carries the emotion); the three children are photoreal but shown ONLY from behind / over-the-shoulder / faces hidden (long-sleeve + hair over neck) - AI photoreal of a clear child face trips the child-safety filter, so faces are never shown to camera. Always awake, daytime, clothed; never bed/nightwear/sleeping.
4. **Photoreal render replaces Pixar** (user choice) - breaks the Bubabu Pixar render-lock; the flying/glowing magic (S2/S3/S5) is kept in photoreal at accepted risk and must be probe-rendered first. Needs Archil sign-off.

## The 9-scene arc + seller map
| # | Beat | Location | var | Seller beat / cascade step |
|---|------|----------|-----|----------------------------|
| S1 | Living-room chaos, mother sunk on the couch, comic-overwhelmed | INT day | large | PROBLEM / BAB Before · Recognition |
| S2 | Bubabu on a cloud-tree branch sees the warm-lit home below, lifts off toward it | EXT day | medium | AGITATE · Curiosity |
| S3 | Curtains billow, Bubabu flies in, the whole room freezes | INT day | large | SOLVE-pivot / BAB Bridge · Pain→Hope |
| S4 | Close on the mother's face, the noise gone, a slow relieved smile | INT day | SMALL | SOLVE lands · Relief |
| S5 | The children sit in a circle, Bubabu tells a story (beak closed, wonder-light) | INT day | large | SOLVE in action · Desire |
| S6 | Mother stands watching, sips her coffee while it is still warm | INT day | medium | BAB After · Relief→Desire |
| S7 | All three children laugh together | INT day | SMALL | Social proof in pictures · Desire-peak |
| S8 | Mother on the phone, recommending it to a friend (diegetic line) | INT day | medium | RECOMMENDATION = proof · Action |
| S9 | The children play calmly, the mother watches, content | INT day | medium | RESOLUTION / soft close |

**SMALL count = 2/9 (22%)** - under the 30% VYALO cap. Every non-SMALL clip carries 3-5 sequenced actions, motion_bucket_id ≥90, peak intensity ≥0.6, LF≠FF.

## Seller arc baked in (BRAND_ENGINE BE$1 + storytelling_for_sales PAS/BAB + psychology_engine 8-step cascade)
- **Sell RESULT not TOOL:** the voiceover names the calm, the story in their own language, the warm coffee, the evening back - never "AI / offline speech engine / specs". Bar Test passes (you could not swap a generic toy in without losing the specific calm being sold).
- **8-step emotional cascade** runs S1→S9: Recognition → Curiosity → Pain-reactivation → Hope → (skepticism dissolved by) Relief → Desire → Action.
- **The recommendation IS the social proof** - S7-S8 peak-end: the mother phoning a friend is the testimonial.

## TOTAL price ban (customer-facing) + CTA placement
- ZERO price / currency / numerals-as-price in `voiceover.md`, `video.md`, `cover.md`, `post.md`.
- ZERO CTA verbs in the narration. The only CTA is the soft "where to find it" channel line - **BUBABU.GE · Tbilisi Mall · Galleria Tbilisi** - which lives in `post.md` + the cover wordmark only.
- **Price = operator-internal only.** Bubabu hero-unit price lives on the current BUBABU.GE listing / shop staff sheet, never in any customer file. (No price number is written in this package by design.)

## Characters (full blocks in `video.md`)
- **Bubabu** - refs `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg` uploaded to every Bubabu render (NEVER `3.jpeg`). **Photoreal plush** (visible fibers + seams); beak black + closed always; goggles matte printed fabric (no glow). Appears S2/S3/S5/S6/S7/S8/S9.
- **Mom** - photoreal adult woman, face shown (the emotional carrier). Render Scene 4 first, save as the mother-reference plate for cross-scene consistency. Appears S1/S3/S4/S6/S8/S9.
- **Kid1 / Kid2 / Kid3** - photoreal children shown ONLY from behind / faces hidden, distinct from-behind silhouettes (hair + wardrobe). Appear S1/S3/S5/S7/S9.

## Audio pipeline (standard, composited)
9 SILENT Veo clips (foley only, `speech:null` everywhere) + ONE warm-female Georgian voiceover the user records + ONE separate Georgian phone line for S8 (synced to the mother's mouth) + Lyria 3 music bed. Editor composites. See `meta.md` for layer order.

## Language
EN draft only in this package. The user produces `voiceover_geo.md` + `post_geo.md` (KA verbatim). The cover headline is proposed in Georgian, flagged for the user to confirm the native form. BUBABU.GE is always UPPERCASE in written copy. No Cyrillic anywhere.

## File inventory
`brief.md` · `voiceover.md` · `video.md` · `audio.md` · `cover.md` · `post.md` · `meta.md` (+ user-produced `voiceover_geo.md` / `post_geo.md`).

## Calibration (per CLAUDE.md ABSOLUTE 2026-05-12)
- **L1 FORMAT** - verifiable now (7 files, dual JSON SPECs, SMALL=2/9, set-equality per scene, grep gates).
- **L2 SPEC-CONFORMANCE** - verifiable now (every scene maps to a cascade step, Bubabu locks applied each scene, kids daytime-awake-clothed, price/CTA bans held, deviations logged).
- **L3 GENERATOR-CONVERGENCE** - PENDING render (child-mouth speaks-drift, KA S8 sync, human cross-scene consistency, moderation classifier pass).
- **L4 VIEWER-TEST** - PENDING publish (hold-rate, the recommendation beat landing, client accepting the mom-narrator deviation).

**Allowed claim now:** "Format + spec design complete; Bubabu locks, VYALO, FF/LF chain, set-equality, price/CTA bans satisfied at the spec layer. Generator-convergence + viewer outcome pending render + test."
**Forbidden:** "done / works / ready / shipped".
