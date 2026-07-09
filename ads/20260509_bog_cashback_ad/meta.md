# Meta Ads Placement & Targeting Spec - Bank of Georgia Cashback Weekend

**Campaign objective:** Conversions (purchase) on bubabu.ge
**Pixel event:** Purchase
**Budget:** ~150 GEL/day for May 7-10 = ~600 GEL total ad spend
**Window:** Live May 7 (warmup) → May 9-10 peak → off May 11 morning

---

## Placement Map (one 15s master, 3 crops)

| Placement | Crop | Why |
|-----------|------|-----|
| **IG Reels** | 9:16 master | Highest engagement, sound-off tolerant |
| **IG Stories** | 9:16 master | Skip-protected, high recall |
| **FB Feed (mobile)** | 1:1 | Largest reach mid-funnel |
| **FB Feed (desktop)** | 16:9 | Desktop conversion (parents on laptop) |
| **IG Feed** | 1:1 | Visual-first, parent demo strong |
| **Audience Network** | 9:16 master | Cheap reach if performing |

Skip: FB Stories (low conversion for this product), Marketplace (wrong audience).

All placements use the SAME 15-second video - just different aspect-ratio crops from the master. One source video, no separate cuts.

---

## Targeting

### Ad Set 1 - Cold (KA, broad)
- Geo: Georgia (Tbilisi + 50km radius around all major cities)
- Age: 25-55
- Gender: All
- Interests: Parenting, Kids toys, AI/Tech, Bank of Georgia
- Languages: Georgian
- Estimated reach: ~250K

### Ad Set 2 - Cold (RU, expat)
- Geo: Georgia (Tbilisi only - expats concentrated)
- Age: 28-50
- Languages: Russian
- Interests: Parenting, Kids toys, Russian-speaking parents, Tbilisi expat groups
- Estimated reach: ~80K

### Ad Set 3 - Warm Retargeting
- Audiences:
  - Visited bubabu.ge last 90 days (didn't purchase)
  - Engaged with Bubabu IG/FB last 60 days
  - Watched any Bubabu video 50%+
- Geo: Georgia + neighbouring CIS expats
- Languages: All
- Estimated reach: ~10-30K

### Ad Set 4 - Lookalike
- Source: Bubabu past purchasers (if pixel data sufficient, ≥100 events)
- Lookalike: 1-3% in Georgia
- Estimated reach: ~50K

---

## Budget Split

| Ad set | Daily | Days | Total |
|--------|-------|------|-------|
| Cold KA | 50 GEL | 4 | 200 GEL |
| Cold RU | 30 GEL | 4 | 120 GEL |
| Warm retargeting | 50 GEL | 4 | 200 GEL |
| Lookalike | 20 GEL | 4 | 80 GEL |
| **Total** | **150 GEL** | **4** | **600 GEL** |

Reserve another 200 GEL for scaling winning variants on May 9-10.

---

## KPI Targets

| Metric | Target | Stretch |
|--------|--------|---------|
| CTR | ≥ 2% | 3.5% |
| CPC | ≤ 1.5 GEL | 0.8 GEL |
| CPA (purchase) | ≤ 30 GEL | 15 GEL |
| ROAS | ≥ 2.0× | 3.5× |
| Frequency cap | 4 max | - |

---

## Pixel Events to Track

- ViewContent (bubabu.ge product page view)
- AddToCart
- InitiateCheckout
- Purchase (with `value` parameter for ROAS calculation)
- Custom event: `bog_cashback_redeemed` (if feasible from order data)

---

## Creative Rotation

One 15s creative × 3 crops × 4 ad sets × 3 language variants on **headline/primary-text** copy = 12 variant combinations in Meta Ads Manager. The video itself is the same - only the surrounding ad copy varies (KA / RU / EN per `facebook.md`).

Day 1 (May 7): all variants live, low budget per ad
Day 2 (May 8): pause bottom 50% by CTR, scale top 30% by CPA
Day 3-4 (May 9-10): only top 4 variants running, full budget on weekend peak

---

## Landing Page Requirements

bubabu.ge product page MUST display before May 9:
- Banner at top: "30% ქეშბექი საქართველოს ბანკის SOLO ბარათით - 9-10 მაისს"
- Countdown timer to May 11 0:00
- Bank of Georgia logo prominent on payment options
- "Effective price 252 ₾" callout next to 360 ₾ price
- Mobile-first layout (most ads click from mobile)

---

## Compliance Check

- [x] No misleading claims ("only days this year" - verify with Bank of Georgia contract)
- [x] No competitor mentions
- [x] No religious symbolism
- [x] No Cyrillic baked into video frames (only in toggle subtitle track)
- [x] No mtavruli capital Georgian
- [x] Bank of Georgia logo usage approved (verify with bank co-marketing agreement)
- [x] Pixar 3D style consistent with brand
- [x] Cyan eyes (NOT glasses) on Bubabu in all assets
- [x] Sound-off compatible (burned-in captions)

---

## Post-Campaign Report (template - fill May 11)

| Metric | Result | vs Target |
|--------|--------|-----------|
| Total spend | TBD | / 600 GEL |
| Total reach | TBD | / 380K |
| Total purchases | TBD | / 30 |
| ROAS | TBD | / 2.0× |
| Best variant CTR | TBD | / 2% |
| Best variant CPA | TBD | / 30 GEL |
| Bank of Georgia cashback redemptions | TBD | / 80 |

Wiki ingest: after campaign, ingest results into `wiki/centaur/selling_patterns.md` Proof Arsenal section + Bubabu campaign log.
