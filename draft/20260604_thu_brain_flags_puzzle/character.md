# CHARACTER - Bubabu Brain Remedy · World Flags Puzzle

Per `bible/CHARACTER_ENGINE.md` (CHE$1 STATIC/DYNAMIC split, CHE$9 self-check) + Bubabu `character_bubabu.md` canon + SKILL NO-APPEARANCE-DUMP rule (refs attached → SPEC body uses reference-only line, not prose dump).

---

## 1 · BUBABU (constant hero - silent)

**Refs uploaded to EVERY render:** `agents/bubabu/1.jpeg` + `agents/bubabu/2.jpeg`. NEVER `3.jpeg` (heart-eyes).

### Canonical IDENTITY BLOCK (reference only - NOT pasted into SPEC bodies)
> Held here as source-of-truth. In JSON SPECs, Bubabu appearance is carried by `character_dna.heritage = "match uploaded 1.jpeg + 2.jpeg EXACTLY 1:1"` + 3 anchor `persistent_features` - never re-described in prose (per `feedback_no_appearance_dump_when_refs_uploaded`).

Bubabu is a round fluffy plush owl mascot, ball-shaped body almost spherical, pure white snowy fluffy fur over entire body, face AND top of head. Two tiny pointed PURE WHITE ear tufts (same white as body, NEVER brown). Signature cyan-turquoise circular eye-goggle markings (built-in aviator goggles) with cream-beige inner ring. Bright yellow upper eyelid arcs inside the cyan rings. Large round black eyes, single white highlight. Small triangular black beak between goggles - **STAYS CLOSED, never animates**. Two small caramel-brown stubby wings (wings ONLY caramel). Two small caramel-brown feet, three orange toes each (feet ONLY caramel). Round chunky snowball body. Soft kawaii calm-wise expression.

**COLOR LOCK:** WHITE = body + face + ears + head. CARAMEL-BROWN = ONLY wings + feet.

### Abbreviated SPEC anchor set (paste into persistent_features - exactly 3)
```
"match attached 1.jpeg + 2.jpeg EXACTLY 1:1 — do NOT describe or invent Bubabu's appearance, the uploaded photos are the sole source"
```
- `heritage`: `"match uploaded 1.jpeg + 2.jpeg EXACTLY 1:1"` - **reference-only, Bubabu NEVER described in a SPEC** (user 2026-06-04: stop describing Bubabu - any appearance text spawns owl/bird drift; the uploaded photos are the sole source). The full prose block above is a HUMAN reference only, never pasted into SPECs.
- `bone_structure`: `"delicate"` (round plush form)
- `face_id_strength`: `0.95` · `outfit_consistency`: `"locked"` · `speech`: `null`

### Bubabu hard locks (every scene)
- Beak BLACK CLOSED - only expression bracket changes (`[expression: gentle calm]` / `[expression: soft wonder]` / `[expression: warm proud]`).
- Cyan goggles = matte printed fabric. **NEVER glow / pulse / illuminate.**
- Body rigid-translates - NO squash-and-stretch.
- Static camera - no zoom / dolly / pan.
- No `3.jpeg` heart-eyes variant.

---

## 2 · THE CHILD (one per episode - Pixar-stylized, moderation-safe) - NEW: a boy

> **MODERATION LOCK (`feedback_bubabu_never_child_in_bed_in_nightwear`):** AWAKE · DAYTIME · CLOTHED · daytime indoor play-nook. NEVER bed / pyjamas / nightwear / under-blanket / eyes-closed-sleeping. Combo trips Veo/NB2/Meta/TT CSAM filter.
> **PIXAR-DNA LOCK (`feedback_bubabu_pixar_render_lock_no_photoreal_spec_fields`):** stylized only. NO real-age number, NO skin-tone hex, NO freckle/dimple/SSS tokens in persistent_features.
> **MOUTH LOCK (`feedback_bubabu_veo_child_mouth_motion_equals_speaks_drift`):** child mouth FIRMLY SEALED CLOSED across ALL scenes - cheek-lift only, never a lip-parting smile (Veo reads mouth-shape-change as "speaks" drift).
> **Fresh from ep1** (ep1 = girl, dark pigtails, mustard sweater). Ep2 = a boy, for cast diversity.

CHARACTER_BLOCK:
```
STATIC: Pixar stylized 3D young boy character, Russell (Up) + Miguel (Coco) DNA — large
        expressive stylized Pixar eyes, soft rounded simplified short tousled dark hair with
        a soft cowlick, round soft cheeks, small button nose, soft Pixar 3D skin shader
        (NOT photoreal), toy-like rounded body proportions, small stature.
        ANCHORS: short tousled dark hair with a soft cowlick · a small front-tooth gap ·
        a slightly-too-big leaf-green zip hoodie.
DYNAMIC: oversized leaf-green zip hoodie over a cream tee, soft denim shorts, white crew socks,
        mustard-yellow sneakers (daytime indoor play).
[expression: ...]  ← per-shot only field that changes (curious / focused / delighted / proud-calm).
```
- `bone_structure`: `"delicate"` · `face_id_strength`: `0.9` · `outfit_consistency`: `"locked"`
- persistent_features (Pixar DNA - paste exactly, zero real-anatomy tokens):
```
"Pixar stylized 3D young boy, Russell + Miguel DNA, large stylized Pixar eyes"
"short tousled dark hair with a soft cowlick"
"oversized leaf-green zip hoodie, soft Pixar 3D skin shader not photoreal, toy-like proportions"
```
- Speech: child is silent by default (narrator carries). This episode = **zero child speech** (pure narrator). If a line were ever needed → ONE Speech tag that scene, child mouth animates, Bubabu beak closed bracket (Veo 3.1 one-speech rule §5.2.1). Here: zero - mouth FIRMLY SEALED CLOSED every scene.

---

## 3 · THE WONDER-BRAIN (ENCOUNTER_BLOCK - the cute brain)

Per CHE$4. The "brain" is shown as a friendly Pixar prop inside a soft dream-bubble - never a medical organ.

ENCOUNTER_BLOCK:
```
A small soft rounded Pixar-stylized "wonder-brain" — gently glowing pastel coral-pink
plush-soft brain shape with smooth rounded folds (toy-like, NOT anatomical), floating
inside a translucent soap-bubble of warm light. Tiny constellation sparkles drift across
its surface; specific soft regions warm up cyan / butter-gold / coral as a skill wakes.
Friendly, cute, calm — like a sleepy creature waking up. NEVER realistic, NEVER clinical,
NEVER wet/wrinkled/medical, NEVER scary.
```
- Region-glow semantics: **cyan** = perception/pattern · **butter-gold** = focus/attention · **coral** = solving-joy/independence.
- Glow is on the BRAIN PROP inside the bubble only - NEVER on Bubabu's body or goggles.

---

## 4 · THE PUZZLE (SKU - reference-only, never described)
Per `feedback_no_sku_appearance_dump_when_ref_uploaded`. The SKU is the **Wooden World Flags Puzzle** (`4860129139007`) - its appearance (flags, countries, wood, piece-count, labels, dimensions) is carried SOLELY by the uploaded photo, never typed into a SPEC.
- `sku_ref.jpg` uploaded to every render alongside `1.jpeg` + `2.jpeg`.
- persistent_features (paste exactly - the ONE reference line):
```
"match attached sku_ref.jpg 1:1, do not invent shape colors or labels — use uploaded photo as sole appearance source"
```
- `heritage`: `"Wooden World Flags Puzzle, uploaded sku_ref.jpg"` · `bone_structure`: `"delicate"` · `face_id_strength`: `0.85` · locked · speech `null`.
- Interaction/action words may use GENERIC play nouns only - "puzzle pieces" / "a piece" / "the puzzle board" / "the frame" / "the finished puzzle" - NEVER "flags" / country names / "wooden" / colors / piece-count.

---

## 5 · STYLE ANCHOR (paste verbatim into every image + video SPEC)
```
Ultra-detailed Pixar feature-film 3D final-render — Disney/Pixar studio polish grade, sharp clean geometry, crisp edge separation between subjects and background, high-frequency detail on plush fur weave and knit-hoodie texture, vivid saturated Candy Pop kid-toy palette (NOT muted, NOT washed out, NOT desaturated), bright clear studio-polish lighting with warm key + soft fill + gentle rim. Reference quality bar: Boo close-up sharpness from Monsters Inc + Carl Fredricksen warm-render quality from Up + Miguel character detail from Coco. Stylized toy-like proportions. NEVER muddy, NEVER soft-focused, NEVER cheap-3D, NEVER photoreal, NEVER live-action, NEVER cinematic film camera grade.
```

## 6 · UNIVERSAL NEGATIVE TAIL (every SPEC negative_prompt)
```
no glow on Bubabu body, no glow on goggles, no goggle illumination, no LED eyes, no open beak,
no 3.jpeg heart-eyes variant, no second Bubabu, no scary owl, no realistic owl, no brown ears,
no caramel body, no squash-and-stretch, no camera zoom,
no photoreal, no live-action, no DSLR, no real-skin SSS, no real-lens DOF, no film grain, no HDR cinema,
no ARRI, no Sony, no Sigma, no Canon, no realistic child, no photoreal kid, no live-action child,
no realistic human anatomy, no child in bed, no pyjamas, no nightwear, no sleeping child,
no clinical brain, no anatomical brain, no medical imagery, no wet wrinkled organ,
no second puzzle, no duplicate puzzle, no extra toy,
text artifacts, watermark, deformed hands, extra fingers, blurry, low quality
```

## CHE$9 self-check
- [x] Bubabu block byte-identical (carried by refs + 3 anchors, never re-described) across SPECs
- [x] Child STATIC byte-locked; DYNAMIC wardrobe single daytime outfit (no silent drift); NEW boy distinct from ep1 girl
- [x] ≥3 anchors each (Bubabu 3 · child 3 · puzzle reference-only)
- [x] No personality words in STATIC/DYNAMIC (calm/wise live in expression brackets / notes only)
- [x] No character names inside generation prompts (names live here + facebook only)
- [x] Moderation lock honored (child awake/daytime/clothed, mouth sealed closed)
- [x] Wonder-brain = cute prop, never clinical
- [x] SKU reference-only (no flags/countries/wood/count described anywhere)
