# Bubabu - Wolt store images · meta

## Slot → SPEC map
| Wolt slot | Size | Aspect | SPEC | Composition intent |
|-----------|------|--------|------|--------------------|
| Discovery/List Image | 2880×1620 | 16:9 | images.md §1 | Storefront card, Bubabu front-and-center, clean bottom band for Wolt name+rating |
| Header | 2880×1620 | 16:9 | images.md §2 | Wide banner, Bubabu right-third, clean left half + lower third for Wolt logo/name/delivery |
| Product Photo / Menu Image | 2880×1620 | 16:9 | images.md §3 | Clean product hero of the Bubabu plush toy itself |
| Logo Image | 1024×1024 | 1:1 | images.md §4 | Centered mascot badge, no wordmark, legible at 96×96 |

## Reference uploads (every render)
`agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg` → Nano Banana 2. **NEVER `3.jpeg`** (heart-eyes). These are client-side photos, not committed in the repo - operator supplies at render time.

## Render checklist (operator)
- [ ] Slot 1 - 16:9, export 2880×1620, bottom band clean
- [ ] Slot 2 - 16:9, export 2880×1620, left half + lower third clean
- [ ] Slot 3 - 16:9, export 2880×1620, product-forward
- [ ] Slot 4 - 1:1, export 1024×1024, full-body badge legible at 96×96
- [ ] All: full body not cropped · cyan goggles · black closed beak · no baked text/logo · no hearts
- [ ] Export JPEG or PNG (PNG preferred for the logo)

## Pre-save grep-gate results (this folder, 2026-06-15)
- Cyrillic `[U+0400–U+04FF]` → 0 hits (Bubabu no-Russian absolute) - PASS
- Photoreal fields `Kelvin|aperture|lens.*mm|SSS|hdr_mode|motion_blur|dynamic_range|noise_reduction|contrast|roughness|reflections` in SPECs → 0 - PASS
- Real-camera `camera.model` `ARRI|Sony|Sigma|Canon|RED|Blackmagic|Kodak|DSLR|ISO` → 0 (camera.model = "Pixar virtual") - PASS
- `text_rendering.enabled:false` in all 4 SPECs · `style_anchor` present in all 4 · negative_prompt 23-25 each - PASS
- `aspect_ratio`: §1-§3 "16:9", §4 "1:1" - PASS

> Note: `meta.quality:"3d_render_octane"` is the schema's only 3D enum value and matches the validated 2026-06-13 templates; the `REAL_CAMERA_BRAND_BANNED` gate is scoped to `camera.model`, which carries `"Pixar virtual"`, so the Octane quality token is clean.

## Lineage
Mirrors `agents/bubabu/assets/20260613_sat_smart_gifts_social_rebrand/` (`cover.md` 16:9 banner + `avatar.md` 1:1 badge) - same clean-render, text-off, Candy Pop, Pixar-lock law, re-composed for Wolt's four slots + reserved Wolt UI safe-zones.

## Channel
Bubabu Smart Gifts merchant listing on Wolt (ვოლტი). First Wolt asset set - greenfield, no prior Wolt work.

## Status
SPECs saved - render + viewer test pending (see brief.md L1-L4 calibration).
