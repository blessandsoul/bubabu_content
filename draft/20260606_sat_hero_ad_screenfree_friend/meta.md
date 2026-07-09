# Meta - Bubabu Hero Ad «Screen-Free Friend» (AI HYPERREAL 8K)

**Date:** 2026-06-07 · **Agent:** /bubabu (hero ad) · **Folder:** `agents/bubabu/draft/20260606_sat_hero_ad_screenfree_friend/`
**Purpose:** creative for the $1/day Meta test (`agents/growth/content/20260606_sat_bubabu_strategy/ads.md`). AI hyper-real, Moxie-cloned arc. Fully AI-generated (NOT a real shoot).

## FILE SET
| File | What it is |
|---|---|
| `brief.md` | what + why |
| `character.md` | ONE full prompt per character (Bubabu / Child / Parent), reuse + swap `[expression]` |
| `video.md` | 4 standalone AI hyperreal scene prompts (KEYFRAME + VEO MOTION each) |
| `voiceover.md` | one Charon narrator track over the cut |
| `post.md` | EN caption (no price) |
| `meta.md` | this |

## Render route (per scene, 1→2→3→4)
1. NB2: paste Scene N `[KEYFRAME PROMPT]` + upload `1.jpeg`+`2.jpeg` (+ `child_ref.png` / `parent_ref.png`) → 8K still.
2. Veo: that still + Scene N `[VEO MOTION]` → clip (SILENT).
3. Grab the clip's last frame → seeds Scene N+1 keyframe (img2img ~70%). Chain = clips flow as one.
4. Generate `child_ref.png` + `parent_ref.png` FIRST (see character.md §3) for face consistency.

## Editor composite
4 silent clips → foley → ONE Charon narrator track (`voiceover.md`, −3 dB above foley) → optional Lyria bell → BUBABU.GE end-card. Master −14 LUFS. Final 4K/8K video upscale = paid, ask first.

## Channels
FB feed · IG Reels · TikTok (trim hashtags) · YT Shorts. Objective = ThruPlay (no pixel yet).

## Hand-off (user)
`voiceover_geo.md` (KA of cues) + `post_geo.md` (KA caption) - user produces KA.

## Status
DRAFT. Render → edit → Archil OK (Pixar-lock broken: AI photoreal) → once published, moves to content/. Child face shown - if the generator blocks it, soft 3/4 framing.
