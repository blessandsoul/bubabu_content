# CHARACTER: Bubabu Weekend Sale Promo (Ad subjects)

> Engine: bible/CHARACTER_ENGINE.md · Status: DRAFT 2026-06-17 · Refs: Bubabu = `1.jpeg` + `2.jpeg` (NEVER `3.jpeg`); Mom = optional `mom_ref.png`
> Two subjects, never in the same frame: Bubabu (S2 + S3, candy-pop) · Mom (S1 only, photoreal Georgian).

---

## STEP 0, PICK BLOCK MODE

| Subject | Refs uploaded? | Block mode |
|---|---|---|
| Bubabu | YES (`1.jpeg` + `2.jpeg`) | ABBREVIATED, zero appearance words, the photo is the source of truth. |
| Mom | Optional (`mom_ref.png`) | If uploaded: ABBREVIATED + match. If not: FORENSIC + generate the turnaround sheet first. |

---

## 1. CHARACTER_BLOCK (per subject)

### BUBABU (S2 + S3) , ABBREVIATED (refs uploaded, skip the sheet, the photo IS the turnaround)
```
CHARACTER_BLOCK (Bubabu):
STATIC: Bubabu plush owl mascot, match attached 1.jpeg + 2.jpeg plush form EXACTLY 1:1.
        Matte printed cyan-turquoise goggle fabric, NOT illuminated. Black felt triangular beak, CLOSED. Round rigid plush body.
DYNAMIC: none (no costume; a held gift is a scene prop, not worn).
[expression: ...]  ← per shot only.
```
Scene-reuse line (every Bubabu scene + upload `1.jpeg` + `2.jpeg`): `the Bubabu plush from 1.jpeg + 2.jpeg, matte goggles (no glow), beak closed. [expression: ...]`

### MOM (S1 only) , FORENSIC if no ref · ABBREVIATED if `mom_ref.png` uploaded
Photoreal but NO subsurface-scattering field on the human (Bubabu SKILL human-field rule + approved plan). She is in S1 only, so the turnaround is for face consistency within that single scene; if you already have a mom face you like, upload it as `mom_ref.png` and skip the sheet.

TURNAROUND SHEET (no-ref case, generate first then save `mom_ref.png`):
```
A professional character design board / turnaround reference sheet on a pure white background, landscape, no text, no labels, no logos, no watermark.
CHARACTER: a real Georgian mother, early thirties, warm brown eyes, dark-brown hair in a loose low bun, olive-warm skin, soft natural face with real pores and a gentle catchlight in the eyes, slim friendly build; wardrobe: mustard-cream knit cardigan over a plain cream tee, dark slim jeans, simple stud earrings, plain flat shoes.
LAYOUT: full-body three-view turnaround (front, left side, back) in a neutral standing pose with arms hanging naturally, plus six head angles (front, three-quarter left, three-quarter right, left profile, right profile, slight high angle), plus six detail close-ups (eyes, hair bun, cardigan knit texture, earring, hands, shoes). Exact facial and wardrobe consistency across every panel. Photoreal, natural daylight, no plastic skin, no CGI.
```
Scene-reuse line (S1, upload `mom_ref.png` if generated): `the same Georgian mother from mom_ref.png, loose low bun, mustard-cream cardigan, face shown. [expression: warm, brightening into a happy smile]`

---

## 2. IDENTITY LOCK (append to the LAST line of every prompt)
- Bubabu (reference-image): `Match attached 1.jpeg + 2.jpeg plush form exactly as the single source of truth. Do not modify the plush, goggles, beak, or proportions. No glow, no open beak, no second plush.`
- Mom (photo lock): `Real Georgian woman, photoreal, face fully visible and natural; match mom_ref.png if uploaded. No plastic skin, no CGI, no morphing.`

---

## 3. REFERENCE SHEET PROTOCOL (CHE$3)
- Bubabu: refs uploaded (`1.jpeg` + `2.jpeg`) , the product photo IS the turnaround. Skip the sheet, use the scene-reuse line.
- Mom: no ref by default , generate the §1 turnaround sheet FIRST, save `mom_ref.png`, upload it in S1. If a face is already chosen, upload it as `mom_ref.png` and skip the sheet.

---

## 4. EXPRESSION LIBRARY (the only thing that changes between scenes)
- Mom S1: `[expression: a little tired and idle, then her face lights up into a warm happy smile]`
- Bubabu S2: `[expression: bright excited wonder, eyes wide and joyful]`
- Bubabu S3: `[expression: warm friendly, gentle inviting wave]`
- spare: `[expression: cozy content]`
- spare: `[expression: delighted, looking up]`

---

## 5. ENCOUNTER_BLOCK (recurring props/creatures)
> none recurring. Gift boxes in S2/S3 are generic wrapped candy-pop gift boxes (varied colors, ribbons, bows), described inline in the scene SPEC, not a locked character. They are scene props.

---

## 6. CROSS-EPISODE LOCK
> Single-use weekend promo, n/a. The Bubabu STATIC block is the standing brand lock (matches `1.jpeg` + `2.jpeg` always); the mom is a one-off, no cross-scene or cross-episode hold needed.

---

## 7. GENERATOR-SPECIFIC COMPILE
- Bubabu (Nano Banana 2 + Veo, reference-upload): abbreviated block + upload `1.jpeg` + `2.jpeg` every scene. No appearance re-dump in the prompt body.
- Mom (Nano Banana 2, photoreal): if `mom_ref.png` uploaded, abbreviated + match; else paste the forensic turnaround prompt to build the face, then upload `mom_ref.png` for S1.

---

## 8. CHE$9 SELF-CHECK
- [x] STEP 0 mode correct per subject (Bubabu abbreviated, zero appearance dump; mom forensic/ref).
- [x] CHARACTER_BLOCK paste-diff = zero across scenes (only `[expression]` differs).
- [x] STATIC visual + behavioral only, no personality/role words; DYNAMIC = wardrobe (mom) / none (Bubabu).
- [x] Identity Lock present per subject.
- [x] Reference Sheet section present (Bubabu = uploaded photo; mom = turnaround prompt provided).
- [x] Mom no-ref case has a FULL turnaround (front/side/back + 6 head angles + 6 detail close-ups).
- [x] Anchors: Bubabu (matte cyan goggles · closed black beak · round rigid plush) · mom (low bun · warm brown eyes with catchlight · mustard-cream cardigan).
- [x] No character names inside image/video prompts (names live here + social only).
- [x] No Cyrillic. No long dash. Bubabu silent, `speech:null`, refs `1.jpeg` + `2.jpeg`, never `3.jpeg`.
