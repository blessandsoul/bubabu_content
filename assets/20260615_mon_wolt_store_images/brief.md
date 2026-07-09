# Bubabu - Wolt store images · brief

## What & why
Client (Saba, via Bubabu) is putting **Bubabu Smart Gifts** on **Wolt** (ვოლტი). Wolt's merchant store-listing UI needs four image slots. The client asked for **mockups without baked logo and without baked text** (`ლოგოს და წარწერების გარეშე`) - clean brand visuals, because Wolt overlays its own UI chrome (store name, logo badge, rating, delivery info) on top. Baked text/logo would clash with that chrome or get covered.

This aligns perfectly with the Bubabu house rule: every Bubabu image is rendered text-clean (`text_rendering.enabled:false`); the wordmark is always an editor overlay, never baked. So "no logo / no text" is the default, not a special ask.

## The 4 slots (client-specified, verbatim sizes)
| # | Slot | Size | Aspect | Export |
|---|------|------|--------|--------|
| 1 | Discovery/List Image (the card in the Wolt feed) | 2880×1620 | 16:9 | JPEG or PNG |
| 2 | Header (top banner on the store page) | 2880×1620 | 16:9 | JPEG or PNG |
| 3 | Product Photo / Menu Image | 2880×1620 | 16:9 | JPEG or PNG |
| 4 | Logo Image (below the header) | 1024×1024 | 1:1 | PNG (recommended) |

SPECs for all four: [images.md](images.md).

## Scope decisions (user, 2026-06-15)
- **Product/Menu (#3) = Bubabu hero toy only** - a clean product hero of the plush itself. The ~37 catalog SKU product photos are a **separate later batch** (each needs its own `sku_ref.jpg` upload).
- **Logo (#4) = clean mascot, NO wordmark** - the round plush owl IS the brand mark. No `BUBABU` text baked (matches "no inscriptions"). There is no separate logo file in the repo; the mascot is the logo.
- **Deliverable = SPEC prompts only.** No Magnific auto-render: house rule = no MCP generation until explicit "go", and the reference photos are client-side uploads not in the repo. Operator renders.

## How to render (operator)
1. Open [images.md](images.md). For each slot, copy the JSON SPEC block.
2. In **Nano Banana 2**, paste the SPEC and **upload `1.jpeg` + `2.jpeg`** (the standard cyan-goggle plush photos). **NEVER `3.jpeg`** (heart-eyes variant). The reference photo is the source of truth - match it exactly.
3. Slots 1-3: render at **16:9**, export **2880×1620**. Slot 4: render at **1:1**, export **1024×1024**. Save JPEG or PNG.
4. Generate 3-4 versions per slot; pick the warmest face + sharpest cyan goggles, full body not cropped.
5. Optional: I can render these via Magnific (Nano Banana 2 Flash, free) if you say **go** - but first hand me `1.jpeg` + `2.jpeg` (not in the repo), else a no-reference render risks identity drift.

## Brand locks applied (every SPEC)
Pure Pixar 3D (never photoreal) · Candy Pop palette (butter-cream #FFFAEB ground + cyan #5BC0DE goggles sacred + lime/yellow/orange/coral/magenta accents) · BLACK closed beak · cyan goggles matte (never lit) · WHITE body, caramel only on wings/feet · soft sunburst + candy confetti (NO hearts) · no second owl / no other owl toy (third-party conflation ban) · no baked text/logo · no Cyrillic, no mtavruli.

## Wolt-specific composition
- **#1 Discovery:** Bubabu front-and-center, inviting "tap me" storefront; clean bottom band (Wolt overlays store name + rating).
- **#2 Header:** Bubabu in the right third, left half + lower third kept airy/clean (Wolt overlays logo badge + name + delivery info) - most generous safe-zones.
- **#3 Product:** the plush toy itself, clean centered product hero, minimal props.
- **#4 Logo:** centered full-body mascot, legible at 96×96.

## Status
**Format checks pass - SPECs saved. Render + viewer test pending.**
- L1 FORMAT (grep gates: text-off, Pixar-lock, no photoreal fields, no Cyrillic, aspect per slot) - VERIFIED.
- L2 SPEC-CONFORMANCE (mirrors the proven 2026-06-13 `cover.md` + `avatar.md` templates field-for-field) - VERIFIED.
- L3 GENERATOR-CONVERGENCE (does NB2 produce on-brand clean Wolt art) - PENDING render.
- L4 VIEWER-TEST (does the listing read premium-playful + legible on-device in the Wolt app) - PENDING client review.
