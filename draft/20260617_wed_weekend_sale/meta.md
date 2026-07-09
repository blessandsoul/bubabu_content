# META: Bubabu Weekend Sale Promo

## What
Standalone weekend-sale promo (NOT a SKU cartoon+ad pair). ~38s, 9:16. The mom beat in 3 home angles + a stand redemption + a home moment where she gives Bubabu to her daughter, the gifts payoff, Bubabu holding the 30% sign + pointing at the June 19-20-21 dates, plus a CTA end-card.

## Offer (client-set)
- A GRAND store-wide sale: 30% off EVERYTHING (the whole shop, all products, not just the Bubabu owl), Friday / Saturday / Sunday.
- Participation mechanic: comment bubabu under the video + repost the video, then come to the store and show it is shared (the Georgian mechanic is in post_geo.md + the video end-plate).
- Online orders: message us on Facebook. (The "$15" online figure stays in the user's caption only, not pushed in the ad.)
- Price / offer appear in the caption + the editor text plates + the cover AND in the off-screen voiceover (this is an explicit sale ad, user directive 2026-06-17, the voiceover announces the deal).

## Render split (LOCKED 2026-06-17, user directive: Bubabu candy-pop, mom photoreal)
- S1a-e = PHOTOREAL Georgian (Sony A1 / Kodak Portra, no subsurface-scattering on humans): the mom in 3 home angles + the stand redemption (consultant + real plush) + the home payoff where she gives Bubabu to her school-age daughter. Breaks the Pixar lock.
- S2 / S2b / S2c / S3 Bubabu = Pixar Candy-Pop (gifts rain, the 30% sign, the calendar, the CTA card; matte goggles no-glow, beak closed, rigid, silent).
- The two render styles never share a frame.
- ARCHIL SIGN-OFF REQUIRED before publish (the photoreal S1 breaks the standing BUBABU_PIXAR_LOCK). Same gate as the proven Jun-9 hero ad.

## Channels + objective
- GEO: Tbilisi / Georgia, parents 25-55, lean female, Georgian language.
- Objective: Messages (matches the "message us on Facebook" online-buy mechanic) + in-store footfall.
- Format: Advantage+ / 9:16 vertical master. Crops 1:1 + 16:9 in editor if needed.
- Per-platform: FB feed + IG Reels + TikTok + Stories = the 9:16 master. FB/IG carry the caption (post_geo.md) + first comment.

## Editor composite (layer order)
1. 9 silent Veo clips (S1a-e photoreal · S2 / S2b / S2c / S3 candy-pop), S1a-e coverage cuts, S1e to S2 hard cut, S2-S2b-S2c-S3 candy-pop cuts.
2. Foley per scene sfx_cues.
3. Off-screen Charon VO (voiceover.md) leads; ONE Lyria 3 track (audio.md) is the music bed, ducked under the VO and ~3 dB above the gift-rain foley.
4. Burn the KA text plates per scene + the end-card. Master -14 LUFS.

## Editor text plates + store addresses
The verbatim Georgian plates and the two store addresses live in video.md (SCENE 3 EDITOR PLATE block) and post_geo.md (do NOT retranslate). Treatment: Noto Sans Georgian, warm-cream gradient. S1b = a small "-30%" badge + the discount word as the offer appears on the phone. S3 / end-card = the offer stack + the two store addresses + a small BUBABU.GE pill (uppercase Latin, the one allowed Latin element).

## Refs to upload at render
- S1a-e: mom_ref.png (optional, same mom face). S1d also: stand_ref.jpg (your photo of the real stand) + 1.jpeg/2.jpeg. S1e also: daughter_ref.png (optional, school-age Georgian girl) + 1.jpeg/2.jpeg. Consultant (S1d) = photoreal one-off (or a ref).
- S2 + S3 + cover: agents/bubabu/1.jpeg + agents/bubabu/2.jpeg. NEVER 3.jpeg.
- Cover stamp: the BUBABU.GE logo as a reference image.

## Files
brief.md · character.md · video.md · voiceover.md · post.md · post_geo.md · cover.md · audio.md · meta.md (+ user-produced voiceover_geo.md)

## Validator status (honest)
- video.md: all PROMPT_ENGINE_DETAIL_FLOOR field gates pass (candy-pop scenes carry stylized-but-populated LUT / Kelvin / lens / motion-blur values; S1a-e photoreal under the documented engine-override). SET-EQUALITY empty per scene. Motion floors met (0 of 9 SMALL).
- ONE known false-positive remains: SCENE_DENSITY_FLOOR flags "only 9 scenes (floor 10)". That floor is a narrative-video rule (80-90s alekso-style). This is a ~38s ad at 9 shots (mom in 3 home angles + the stand redemption + the home daughter-payoff + 4 candy-pop), not a narrative; one short of the floor, but padding it just to hit 10 would hurt the ad. Kept at 9 by design, documented in the video.md override header. Overrides are not yet code-honored, so the flag persists harmlessly.
- character.md / cover.md / audio.md / voiceover.md / post.md / post_geo.md / brief.md: clean.

## Calibration (CLAUDE.md ABSOLUTE 2026-05-12)
- L1 FORMAT: VERIFIED (files written, field gates pass, no em-dash, no Cyrillic).
- L2 SPEC-CONFORMANCE: VERIFIED (render split applied per scene, set-equality empty, Bubabu locks present, offer in plates not narration).
- L3 GENERATOR-CONVERGENCE: PENDING (a real render must confirm candy-pop Bubabu does not drift photoreal from the populated LUT/Kelvin fields, and the photoreal mom reads natural).
- L4 VIEWER-TEST: PENDING (Archil sign-off on the photoreal S1 + does the gift-rain + offer convert).
- Allowed claim: "Specs written, field gates pass, outcome pending render + Archil sign-off." Not "done / shipped / converts".

## Status
DRAFT. Stays in agents/bubabu/draft/. Moves to content/ only on user publish confirmation.
