# BRIEF: Bubabu Weekend Sale Promo (mom photoreal + gifts-on-Bubabu candy-pop)

## What we are making
A short vertical promo (~28s, 9:16) for the Bubabu weekend sale. The mom beat in 3 home angles + a stand redemption (she shows her phone to a consultant who hands her the toy), the gifts payoff, plus a CTA end-card. Standalone promo ad (NOT a SKU cartoon+ad pair).

## The offer (client-set, weekend)
- A GRAND store-wide sale: 30% off EVERYTHING (the whole Bubabu Smart Gifts shop, all products, not just the Bubabu owl) on Friday, Saturday, Sunday.
- Participation mechanic: comment bubabu under the VIDEO + repost the video, then come to the store (Tbilisi Mall / Galleria) Fri-Sun and show it is shared.
- Online orders: message us on Facebook. (The "$15" from the original brief is the user's online price note, kept in his caption, NOT pushed in the ad, it confused the store-wide 30% message.)
- Price + the offer live in the CAPTION (`post_geo.md`, user verbatim) + the editor text plates + the cover AND in the off-screen voiceover (explicit sale ad, user directive 2026-06-17). The in-store share mechanic (comment + share) stays in the caption.

## Render split (LOCKED per user 2026-06-17, Bubabu candy-pop + mom photoreal)
- Scenes 1a/1b/1c (mom) = PHOTOREAL Georgian, the proven hero-ad look (Sony A1 / Kodak Portra), the mom beat in 3 camera angles. Breaks the Pixar lock, so it needs an engine-override + Archil sign-off before publish.
- Scene 2 + Scene 3 (Bubabu) = Pixar Candy-Pop stylized, full brand lock.
- The two styles never share a frame: the photoreal real world is S1a/b/c/d (home + the stand, where the consultant hands over the REAL Bubabu plush); the candy-pop mascot is only the S2 gift-payoff and the S3 card.

## Shot arc (9 shots: mom in 3 home angles + stand redemption + home daughter-payoff + 4 candy-pop)
1. MOM, 3 angle-shots (~11s total, PHOTOREAL). A warm Georgian mom in a cozy Tbilisi apartment: S1a eye-level medium, she sits on the sofa scrolling her phone; S1b over-the-shoulder, the Bubabu sale appears on her screen and her face lights up, happy; S1c wider, she rises and heads eagerly to the door to go buy. The phone stays in her hand the whole time, never set down (no bag).
2. S1d, STAND REDEMPTION (~5s, PHOTOREAL hyperreal). At the Bubabu Smart Gifts stand, the mom holds up her phone (the shared post) to a friendly consultant, who hands her a Bubabu plush. Both warm and happy. You supply the stand photo as `stand_ref.jpg`; the consultant is photoreal Georgian, the plush is the real one (1.jpeg/2.jpeg).
3. S1e, HOME, DAUGHTER GETS BUBABU (~5s, PHOTOREAL hyperreal). Back home, the mom gives the Bubabu plush to her school-age daughter, who lights up and hugs it. The mom is warm (watching her child's joy), the daughter is the delighted one (fixes the earlier "grown woman over-excited about a toy" oddness). Optional `daughter_ref.png`. Daytime, clothed, living room, moderation-safe.
4. S2, GIFTS RAIN ON BUBABU (~7s, CANDY-POP). Wrapped gift boxes fall from a candy-pop sky onto a joyful Bubabu, who catches one in his wing. The "30% off everything" abundance, made visible.
5. S2b, BUBABU HOLDS THE 30% SIGN (~3s, CANDY-POP). Bubabu proudly lifts a bright sale sign with «-30%» baked into the photo prompt (text_rendering).
6. S2c, BUBABU POINTS AT THE DATES (~3s, CANDY-POP). Bubabu points at a candy-pop June calendar with the numbers 19, 20, 21 circled, baked into the photo prompt (text_rendering "19 20 21").
7. S3, CTA END-CARD (~5s, CANDY-POP). Bubabu waves, holding one gift, with negative space for the editor plates: 30% / Fri-Sat-Sun / comment "bubabu" / repost / store addresses / BUBABU.GE.

## Mood
Warm, joyful, generous, gift-day excitement. Bubabu = Cozy-Excited. The mom = relatable real-parent delight. Candy-Pop palette on the Bubabu scenes (butter-cream, magenta, lime, yellow, coral, sky-blue, orange).

## Audio
Off-screen Charon voiceover (`voiceover.md`, you record the Georgian) + Lyria 3 upbeat-warm music bed + SFX + on-screen text. The voiceover announces the deal (30% / weekend / $15 online / where to buy); the plates + caption carry it too.

## Hard locks
- Bubabu: beak CLOSED, cyan goggles matte (no glow), body rigid (no squash), static camera, silent (`speech:null`). Refs `1.jpeg` + `2.jpeg` only, NEVER `3.jpeg`.
- Mom: Georgian (dark hair, warm brown eyes, olive skin); photoreal but no subsurface-scattering field on the human; face from `mom_ref.png` if uploaded, else a one-off (she is in S1 only, no cross-scene lock needed).
- Gift boxes named in the S2 image SPEC first (PHOTO_VIDEO_FIDELITY); the video only animates the fall.
- No Cyrillic anywhere. No long dash anywhere. English social body (user translates). Georgian caption = user verbatim.

## Files
brief.md · character.md · video.md · voiceover.md · post.md · post_geo.md · cover.md · audio.md · meta.md

## Calibration (per CLAUDE.md ABSOLUTE 2026-05-12)
L1 FORMAT + L2 SPEC = will be VERIFIED at write. L3 RENDER + L4 VIEWER-TEST = PENDING (Archil sign-off on the photoreal S1 + a real render). Do not claim "done/works" on format alone.
