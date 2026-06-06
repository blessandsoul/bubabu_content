# Brief — Bubabu Smart Gifts · Kiosk Category Stickers

**Date:** 2026-05-31 (Sun)
**Type:** Retail print collateral — glass-shelf category labels for the mall kiosk (Tbilisi Mall / Galleria stand format).
**Source request:** Archil's retail consultant gave an 8-category sticker system to fix the "messy mixed shelf" problem. This package is the **Bubabu-brand version** of that plan — his retail logic kept, his off-brand choices corrected.

---

## Why stickers at all

Kiosk reads as busy — product types mixed, customer cannot answer "what is where?" in 3 seconds. Shelf-edge category stickers create clear product zones WITHOUT covering products. Low cost, high clarity. Confirmed good call.

---

## 3 brand corrections to Archil's plan (locked-brand reasons)

| # | Archil proposed | Brand-correct version | Why |
|---|-----------------|------------------------|-----|
| 1 | Per-category colors incl. **purple, dark-blue, silver, gold, red** | Remapped every accent to the **LOCKED Bubabu palette** (cyan / magenta / lime / yellow / coral / orange + 1 deep-cyan tint) | Off-palette colors = brand drift on the physical stand. Palette is locked across all Bubabu surfaces. |
| 2 | **"Smart Surprises / ჭკვიანი სიურპრიზები"** for cheap impulse toys | **"სახალისო საჩუქრები / Fun Gifts"** (Archil's own honest fallback) | Brand anti-dilution lock: do not label fun/impulse items "smart" — weakens the smart-gift positioning. Archil flagged this himself. |
| 3 | 8 free-floating categories | Same 8, but **mapped onto the 5 locked retail zones** + one shared locked design system | Keeps stand IA consistent with the online shop + brand book. |

**Kept verbatim:** all of Archil's Georgian text (native-authored mkhedruli, zero Cyrillic — used as-is), his sizes (25–35 cm), one-sticker-per-shelf-section rule, front-glass-edge placement, "Bubabu is hero zone" priority, and his shelf-by-shelf image analysis (see `print_spec.md`).

---

## The 8-sticker system (customer-facing categories)

| # | Georgian (render verbatim) | English | Accent (locked) | Retail zone |
|---|----------------------------|---------|------------------|-------------|
| 1 | **ბუბაბუ AI მეგობარი** · საუბრობს • სწავლობს • თამაშობს | Bubabu AI Friend · Talks • Learns • Plays | Magenta `#FF1F8F` | Hero Bubabu |
| 2 | **მაგნიტური სათამაშოები** · ააწყე • შექმენი • ისწავლე | Magnetic Toys · Build • Create • Learn | Cyan `#5BC0DE` | Educational |
| 3 | **სასწავლო საჩუქრები** · ისწავლე თამაშით | Smart Learning Gifts · Learn Through Play | Lime `#84CC16` | Educational |
| 4 | **STEM & რობოტიკა** · ტექნოლოგია • ლოგიკა • აღმოჩენა | STEM & Robotics · Tech • Logic • Discovery | Deep teal-cyan `#2BA3C7` | Educational / Premium |
| 5 | **კრეატიული საჩუქრები** · დახატე • შექმენი • გააფერადე | Creative Gifts · Draw • Create • Imagine | Orange `#FF9F1C` | Educational / Creative |
| 6 | **სახალისო საჩუქრები** · პატარა სიხარული | Fun Gifts · Small Joys | Coral `#FF6B6B` | Small / Impulse |
| 7 | **საჩუქრის ნაკრებები** · მზად არის საჩუქრად | Gift Sets · Ready to Gift | Yellow `#FFEB3B` | Gift Sets |
| 8 | **ეკრანის გარეშე** · უსაფრთხო თამაში და სწავლა | Screen-Free Gifts · Safe Play • Smart Learning | Cyan `#5BC0DE` + Lime `#84CC16` duo | Cross-zone brand badge |

Sticker #8 (Screen-Free) is the **brand-philosophy badge** — Bubabu's core promise (AI without a screen). Place on the Hero zone + anywhere audio/storytelling toys sit. Reinforces #1.

---

## 2 Unified Elements — Арчил client directive (locked 2026-05-31)

Client Арчил reviewed v1 drafts and approved overall design («დანარჩენი ყველაფერი მაგარია» = «everything else is cool») BUT asked for 2 unifying elements across ALL 8 stickers so they read as one brand system, not 8 independent designs:

> «ხომ არ ჯობია, რომ bubabu.ge და თვითონ ბუბაბუ ყველგან ერთნაირი რომ იყოს? ბუბაბუს თავისი ცისარტყელა რომ მოყვებოდეს უკან, პატარაზე; bubabu.ge ყველგან ერთ ფონზე რომ იყოს? ეს ორი ელემენტი ყველგან ერთნაირი თუ გვექნება, გააერთიანებდა ყველა სტიკერს.»

Translation: «Wouldn't it be better if `bubabu.ge` and Bubabu himself looked the same everywhere? Bubabu with his own small rainbow behind him; `bubabu.ge` on one background everywhere? If these two elements are the same everywhere, it would unify all stickers.»

### Locked unifier #1 — Bubabu master visual (IDENTICAL across all 8)

Every sticker (hero + badge variants) ships with the SAME canonical Bubabu visual + pose + rainbow:

| Element | Locked value |
|---------|--------------|
| DNA persistent_features | round fluffy white plush owl + cyan goggle markings + cream inner ring + BLACK closed beak + caramel stubby wings + caramel feet w/ 3 orange toes + pure white ear tufts + soft light-grey outline. Match uploaded `1.jpeg` + `2.jpeg` plush form EXACTLY 1:1 |
| Expression | serene closed-mouth, calm warm friendly, head facing slight 3/4 right, eyes soft warm centered, beak closed |
| Rainbow behind | small soft Candy Pop 6-color rainbow arc (cyan / magenta / lime / yellow / orange / coral) scaled to ~120% of Bubabu body radius, tilted 5-10° behind right shoulder, soft kid-pastel saturation, NO body-glow |
| Scale flex | Sticker 1 hero = `visual_weight 0.9`, Stickers 2-8 badge = `visual_weight 0.12`. Style + form + pose + rainbow IDENTICAL — only scale differs |
| Ref upload | `1.jpeg` + `2.jpeg` MANDATORY per render (text-only DNA = drift risk across 8 separate renders) |

### Locked unifier #2 — `BUBABU.GE` butter-cream pill (IDENTICAL across all 8)

Per-category ribbon color (magenta/cyan/lime/teal/orange/coral/yellow/duo) DROPPED. Replaced with single unified pill across all 8:

| Element | Locked value |
|---------|--------------|
| Background | soft rounded pill capsule, butter-cream gradient `#FFFAEB` top → `#FFF6CC` bottom (matches Bubabu cover override + ad cover aesthetic) |
| Pill shape | radius = pill height / 2 (soft rounded ends, no harsh corners) |
| Text | `BUBABU.GE` uppercase, color = deep magenta `#FF1F8F` (brand primary, max contrast on butter-cream) |
| Shading | flat matte — NO drop shadow, NO border outline, NO gradient on text |
| Position | centered horizontally, bottom-third of sticker frame, IDENTICAL position across all 8 |

### What stays per-category (NOT unified)

- Per-category **headline accent color** (magenta/cyan/lime/teal/orange/coral/yellow/duo) — applied to the Georgian headline text only, NOT to the BUBABU.GE pill anymore
- Per-category **left icon** (magnetic balls / bulb / robot / paint brush / gift / etc) — category symbols
- Per-category **cloud silhouette shape** (organic blob unique per sticker)
- Sticker 1 hero Bubabu treatment kept (large center-left) — only visual identity + rainbow locked, not layout role

### Operator workflow per sticker render

1. Upload `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg` to Nano Banana 2 (MANDATORY).
2. Copy one JSON SPEC block from `image.md`, paste into NB2.
3. Render. Verify Bubabu visual matches reference (same plush form), rainbow present behind, BUBABU.GE pill butter-cream + magenta text at bottom.
4. If Bubabu drift between any 2 renders OR rainbow missing OR pill per-color → REJECT, re-render with stronger ref weighting.

**Print priority (Archil's order kept):** start with #1–#7. #8 is the strong optional 8th.

---

## Production path

- **PRIMARY (DIE-CUT, approved 2026-05-31):** render each category as a die-cut vinyl sticker — icon + text wrapped by a thick glossy white die-cut border + soft shadow, soft cloud-like organic shape — on a white background via Nano Banana 2. 8 paste-ready prompts in `image.md`. Each sticker is independent; shapes differ on purpose, the white border + palette + Bubabu owl + BUBABU.GE banner unify the set.
- **FALLBACK (Georgian mis-renders 3×):** render the sticker with icon + white border only (no letters), overlay the Georgian + English text in an editor over the die-cut shape.
- **Print:** cut along the white die-cut border (kiss-cut vinyl), matte anti-glare laminate (LED-safe), 300 DPI.

---

## Shared sticker DNA (unifies the varying shapes)

Die-cut sticker style: soft cloud-like organic shape (varies per category) wrapped by a thick glossy white die-cut border + soft drop shadow, on a pure white background · soft candy-pop 3D icon + text inside · accent color per category (border tint + ribbon banner + headline) · text order Georgian headline → Georgian benefit → small English subtitle · `BUBABU.GE` on an accent ribbon banner in white caps · tiny Bubabu owl (cyan goggles, closed beak) bottom-right. Unified by the white border + palette + owl + banner — NOT by an identical frame. Full prompts in `image.md`, physical spec in `print_spec.md`.

---

## Files
- `image.md` — the 8 die-cut sticker prompts (paste-ready into Nano Banana 2), brand-locked + per-category icon/text/color.
- `print_spec.md` — physical production spec (size, material, lamination, mounting, color hex list, shelf-by-shelf map, do/don't).
- `brief.md` — this file.

## Self-check
- [x] Locked Bubabu palette only (no purple/navy/silver/gold/red)
- [x] Georgian = Archil's verbatim mkhedruli, zero Cyrillic, no mtavruli caps
- [x] Anti-dilution respected ("Fun Gifts" not "Smart Surprises")
- [x] 8 categories mapped to 5 brand zones
- [x] Pixar candy-pop style, no photoreal
- [x] Draft-first (in `draft/`, moves to `content/` on user publish confirmation)
- [ ] Viewer/print test — PENDING (mockups not yet rendered; format checks only)
