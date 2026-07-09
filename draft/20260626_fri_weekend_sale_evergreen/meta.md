# META: Bubabu Weekend Sale Promo, EVERGREEN (candy-pop refresh)

## What
A reusable weekend-sale promo. The sale window is named by DAY (Friday, Saturday, Sunday), never by a date number, so the asset runs ANY weekend. This is a candy-pop REFRESH of the proven `20260617_wed_weekend_sale`: the user reuses his existing MOM footage and only needs the candy-pop Bubabu prompts new, with the calendar-of-dates beat swapped for a day-board.

## Offer (client-set, same as the proven promo)
- A grand store-wide sale: 30% off EVERYTHING (the whole Bubabu Smart Gifts shop, all products, not just the Bubabu owl), every Friday / Saturday / Sunday.
- Participation mechanic: comment the brand word "bubabu" under the video + repost the video, then come to the store and show it is shared (the Georgian mechanic is in `post_geo.md` + the video end-plate).
- Online orders: message us on Facebook.
- The offer (30% + the three day-names) appears in the caption + the editor text plates + the cover AND in the off-screen voiceover (explicit sale ad, user directive 2026-06-17). NO date numbers anywhere (evergreen).

## Render note (LOCKED, Pixar lock INTACT, no Archil gate)
- The MOM photoreal beat (home, the stand, she gives Bubabu to her daughter) = REUSE the existing footage from the prior weekend-sale render. NOT re-prompted here.
- The candy-pop Bubabu tail (Scene A gift-rain, Scene B the -30% sign, Scene C the weekend day-board, Scene D the CTA card) is the only NEW generation: all candy-pop Pixar, matte goggles no-glow, beak closed, rigid, silent.
- Because no photoreal human is in the NEW prompts, the standing BUBABU_PIXAR_LOCK is INTACT, so NO Archil sign-off is required (unlike the prior mixed-render version).
- Scene 0 = a green-screen text HOOK card on chroma green #00B140 (the offer line "30% off everything", baked in Georgian, see video.md Scene 0), the silent scroll-stop for sound-off viewers, keyed and overlaid on the open. White text + magenta outline (green-de-spill-safe per the chroma rule). Baked Georgian, regenerate until clean; editor-typed title is the reliable fallback.

## The days-not-numbers change (the whole point)
- Scene C reworked: the prior "POINTS AT THE DATES" candy-pop June calendar with baked date numbers (19 20 21) is replaced by a candy-pop WEEKEND BOARD with three circled day-slots. Per user directive 2026-06-26 the three Georgian day-names (Friday / Saturday / Sunday) are BAKED into the photo (`text_rendering.enabled:true`), one per slot. Regenerate until the Mkhedruli reads clean; fallback is blank slots + an editor plate if it garbles. Either way: no date numbers (evergreen).
- The Scene D end-card plate + the caption already use the three day-names. The voiceover already says "Friday, Saturday, Sunday".
- Zero date numbers in the whole package. The percent (30%) stays, it is the offer.

## Channels + objective
- GEO: Tbilisi / Georgia, parents 25-55, lean female, Georgian language.
- Objective: Messages + in-store footfall + shares (the comment + repost mechanic).
- Format: 9:16 vertical master. Crops 1:1 + 16:9 in editor if needed.
- Per-platform: FB feed + IG Reels + TikTok + Stories = the 9:16 master. FB/IG carry the caption (`post_geo.md`) + first comment.

## Editor composite (layer order)
1. The green-screen text HOOK (Scene 0) keyed (#00B140 out) over the first ~1.5-2s of the open as the silent scroll-stop, then the existing MOM photoreal clips + the 4 new silent candy-pop Veo clips (Scene A to B to C to D). MOM beat to HARD CUT (photoreal to candy-pop) to the candy-pop tail to the end-card.
2. Foley per scene `sfx_cues`.
3. Off-screen presenter VO (`voiceover.md`) leads; ONE Lyria 3 track (`audio.md`) is the music bed, ducked under the VO and ~3 dB above the gift-rain foley.
4. Burn the KA text plates per scene + the end-card (Noto Sans Georgian, warm-cream gradient). Master -14 LUFS.

## Editor text plates + store addresses
The verbatim Georgian plates + the two store addresses live in `video.md` (SCENE C + SCENE D EDITOR PLATE blocks) and `post_geo.md` (do NOT retranslate). Treatment: Noto Sans Georgian, warm-cream gradient. Scene B = the baked «-30%» sign. Scene C = the three day-names baked into the photo via text_rendering (fallback: editor plate if garbled). Scene D / end-card = the offer stack + the day-names + the two store addresses + a small `BUBABU.GE` pill (uppercase Latin, the one allowed Latin element).

## Refs to upload at render (candy-pop scenes only)
- Scene A + B + C + D + cover: `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg`. NEVER `3.jpeg`.
- Cover stamp: the `BUBABU.GE` logo as a reference image (9:16, logo not described in words).
- The mom / consultant / daughter / stand refs are NOT needed (that footage is reused, not regenerated).

## Files
brief? (none, see this meta) · video.md (candy-pop only) · voiceover.md · post.md · post_geo.md · cover.md · audio.md · meta.md · safety_scan.json (+ user-produced voiceover_geo.md)

## Ad setup (reuse)
Same as the proven promo's `ads_boost_setup.md`: an Engagement Auction campaign, ~$15/day, broad Tbilisi 25-55, Advantage+ placements, Use existing post. Runnable any weekend (evergreen). The comment + repost wording is mild engagement-bait, watch day-1 reach.

## Validator status (honest)
- video.md: candy-pop scenes carry populated Pixar fields (style_anchor + Pixar virtual camera + ≥15 negatives); SET-EQUALITY ∅ per scene; 0 of 4 SMALL. Engine-override header documents the 4-scene ad density + the intentional baked «-30%» sign. Pixar lock intact (no Archil gate).
- post_geo.md: DRAFT, dates swapped to day-names, flagged for the user's grammar confirm.
- character.md not regenerated (the mom + consultant + daughter live in the reused footage; Bubabu identity = `1.jpeg` + `2.jpeg` referenced inline in every scene).

## Calibration (CLAUDE.md ABSOLUTE 2026-05-12)
- L1 FORMAT: VERIFIED (files written, no em-dash, no Cyrillic, no date numbers, Pixar fields populated).
- L2 SPEC-CONFORMANCE: VERIFIED (candy-pop-only render, set-equality ∅, day-names editor-overlay, offer in plates + VO per user override, Bubabu locks present).
- L3 GENERATOR-CONVERGENCE: PENDING (a real render must confirm candy-pop Bubabu reads clean, the -30% sign and the blank day-board generate without garble, the editor day-name plate sits right).
- L4 VIEWER-TEST: PENDING (does the day-named evergreen version convert + share like the dated original).
- Allowed claim: "Candy-pop prompts written, mom footage reused, dates swapped to day-names, outcome pending render." NOT "done / shipped / converts".

## Status
DRAFT. Stays in agents/bubabu/draft/. Moves to content/ only on user publish confirmation.
