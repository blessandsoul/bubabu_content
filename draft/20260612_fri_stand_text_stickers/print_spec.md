# Print Spec - Stand Text Stickers (18 pcs: 9 GE + 9 EN)

## Typography (locked - rev 2026-06-12: UNIFORM LETTER HEIGHT)
- **Georgian:** Noto Sans Georgian, weight **600 (SemiBold)** - *rev 2026-06-12 ×2 «ცოტა დავათხელოთ» → «еще тоньше»: 900 → 700 → 600 default; preview switcher now 400-900, final weight = client visual pick* - **MTAVRULI** (Ა-forms, U+1C90 block) - every letter exactly the same height, no ascenders/descenders. Letter height = **65 mm** for ALL letters (client range 6-7 cm). *Client directive 2026-06-12 «all letters one height» - explicitly overrides the default mkhedruli-only sign rule for this set.*
- **English:** Noto Sans, weight **600 (SemiBold, same switcher logic)**, **ALL CAPS**, cap height = **32 mm** (≈ half of GE per brief) - uniform too.
- **Weight floor recommendation: 500.** At 400 the EN 32 mm caps drop to ~2.5-3 mm stroke - starts to wash out under mall LED from 5 m+. GE 65 mm survives 400, but keep the set on ONE weight; don't go below 500 without an on-stand distance test.
- GE + EN always SAME weight - never mix weights inside the set.
- Letter-spacing ≈ +2.5% (uniform-height/caps text needs slight air; never tight-merged at Black weight).
- **NO shadow, NO outline, NO stroke.** On white, shadow blurs the edge and reads WORSE from distance. Weight carries visibility.

## Color (FINAL - rev 2026-06-12 client «ჯობია ყველაფერი შავად ეწეროს»)
| Element | Color | Print |
|---|---|---|
| **ALL letters, all 18 stickers** | Black `#000000` | **100% K** (single ink, crispest edge, no registration halo) |
| **Rainbow underline bar - every sticker** (restored 2026-06-12 «верни цвет линию») | Gradient `#5BC0DE → #FF1F8F → #84CC16 → #FFEB3B → #FF9F1C → #FF6B6B` | Candy Pop 6-color, left→right, fully rounded ends |

Underline bar: height **9 mm** (GE) / **5 mm** (EN), gap below letters ~7 mm, length = exact text width.
No magenta brand word, no red promo word - those stay killed. Letters = black only; the bar is the single color element.

## Sticker list - FINAL print strings (copy verbatim; verify widths in `stickers_preview.html` labels)
Strip height ≈ 11 cm (GE) / 6 cm (EN) - uniform letters, no asc/desc overshoot. Side quiet zone ≈ 22 mm (GE) / 12 mm (EN).

| # | GE text - Mtavruli, 65 mm letters | ≈ GE width | EN text - ALL CAPS, 32 mm | ≈ EN width |
|---|---|---|---|---|
| 1 | ᲑᲣᲑᲐᲑᲣ - ᲘᲓᲔᲐᲚᲣᲠᲘ ᲡᲐᲩᲣᲥᲐᲠᲘ | 152 cm | BUBABU - THE PERFECT GIFT | 67 cm |
| 2 | ᲞᲠᲔᲛᲘᲣᲛ ᲡᲐᲩᲣᲥᲠᲔᲑᲘ | 102 cm | PREMIUM GIFTS | 39 cm |
| 3 | ᲡᲐᲡᲬᲐᲕᲚᲝ ᲡᲐᲩᲣᲥᲠᲔᲑᲘ | 113 cm | EDUCATIONAL GIFTS | 50 cm |
| 4 | ᲢᲔᲥᲜᲝ ᲡᲐᲩᲣᲥᲠᲔᲑᲘ | 93 cm | TECH GIFTS | 28 cm |
| 5 | ᲡᲐᲮᲐᲚᲘᲡᲝ ᲡᲐᲩᲣᲥᲠᲔᲑᲘ | 113 cm | FUN GIFTS | 26 cm |
| 6 | ᲐᲡᲐᲬᲧᲝᲑᲘ ᲡᲐᲩᲣᲥᲠᲔᲑᲘ | 108 cm | BUILD & CREATE GIFTS | 54 cm |
| 7 | ᲛᲐᲒᲜᲘᲢᲣᲠᲘ ᲡᲐᲗᲐᲛᲐᲨᲝᲔᲑᲘ | 130 cm | MAGNETIC TOYS | 40 cm |
| 8 | ᲭᲙᲕᲘᲐᲜᲘ ᲡᲐᲩᲣᲥᲠᲔᲑᲘ | 100 cm | SMART GIFTS | 32 cm |
| 9 | ᲐᲥᲪᲘᲐ | 32 cm | SPECIAL OFFER | 36 cm |

Strip heights (incl. 8 mm quiet margin + 9/5 mm rainbow bar): **GE ≈ 13 cm · EN ≈ 8 cm.**
Mkhedruli reference originals (client brief wording, for cross-check only - NOT for print): ბუბაბუ - იდეალური საჩუქარი · პრემიუმ საჩუქრები · სასწავლო საჩუქრები · ტექნო საჩუქრები · სახალისო საჩუქრები · ასაწყობი საჩუქრები · მაგნიტური სათამაშოები · ჭკვიანი საჩუქრები · აქცია

**Widths above are MEASURED from the rendered PDF at weight 600** (the `stickers_print.pdf` build), not estimates. Heavier weight = wider; if the client picks a different weight, re-run the PDF and the widths update.

⚠️ **Width flag:** #1 GE ≈ 1.58 m, #7 ≈ 1.30 m at 65 mm letters. Confirm stand fascia width BEFORE print - if a strip doesn't fit, reduce letter height on the long ones (e.g. #1 header at 50 mm) or stack in two lines (client decision).

## Print-ready PDF
`stickers_print.pdf` - **18 pages, one sticker per page, each page at its true 1:1 physical size** (page = sticker size, e.g. p01 = 158×13 cm). Pages 1-9 = Georgian Mtavruli, 10-18 = English CAPS, in the order above. Black letters weight 600 + Candy Pop rainbow underline, white background, no crop marks (page edge = trim). Hand this straight to the large-format/vinyl printer. Regenerate with `python scratch/bubabu_stickers_pdf.py` (change `WEIGHT` to re-bake at another thickness).

## Material & finish
- White adhesive vinyl (opaque), digital large-format print.
- **Matte anti-glare lamination - MANDATORY** (mall LED gloss hotspot kills distance legibility).
- Cut: rectangle strips with rounded corners (R ≈ 10 mm). Optional premium: contour kiss-cut hugging the letter cluster (~10 mm offset) - white-on-white stand makes the difference subtle; rectangle is cheaper and fine.
- Adhesive: removable (stand gets re-merchandised).
- 300 DPI at final size if rasterized; better: ask the print shop to typeset live text from this spec (font free on Google Fonts) and export vector.

## Scale QA (mandatory before mass print)
1. Print ONE test strip (#4 ᲢᲔᲥᲜᲝ ᲡᲐᲩᲣᲥᲠᲔᲑᲘ - shortest full-format GE).
2. Measure ANY letter height = **65 mm ± 2 mm** (uniform Mtavruli - every letter must measure the same). Off → rescale, reprint test.
3. Stick on the stand, step back 5 m under mall lighting: text must read instantly, no glare.
4. Variant B: rainbow bar must NOT pull attention before the text at 5 m (it shouldn't - 9 mm vs 65 mm letters).
5. Zero Cyrillic look-alike glyph corruption in GE strings (compare against this file char-by-char).

## Status
Format checks pass. Client review pending: variant A/B pick + stand-width confirmation for #1/#7. Print test pending.
