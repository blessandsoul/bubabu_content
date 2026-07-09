# Bubabu Smart Gifts Shop - MVP Scope (1000₾ / 1 month = 40-50% of Phase 1)

> Phase 1 = the 20 "must-have for launch" items (brief §10). MVP carves the load-bearing transaction + Bubabu-story core. Hold this IN/OUT line against scope creep.

## Locked decisions (client-driven, 2026-06-13)
- **Engine = custom Next.js** (NOT Shopify/WordPress). Graft from FLORCA + ainow i18n + andrewaltair deploy.
- **Payment = real Georgian gateway (TBC/BoG) in MVP** - not COD. → Archil merchant creds = hard blocker (fallback: COD interim if creds slip).
- **Catalog = wait for Archil's final curated list + photoset** - engine built on temp seed (`product_catalog.md`) meanwhile.

## IN (MVP)
| # | Item | Brief §10 ref |
|---|------|---------------|
| 1 | GE + EN, mobile-first | #1, #2 |
| 2 | Bubabu hero landing/product page (full) | #3 |
| 3 | Homepage MVP blocks: Header(1) · Hero(2) · Bubabu Hero(3) · Shop-by-Age(4) · Featured Categories(6) · Best Sellers(7) · Trust icons(11) · Store locations simple(15) · Footer(16) | #4 |
| 4 | 3-4 category pages + listing + core filters (age/price/category) | #5, #8 |
| 5 | Product detail (photos/title/price/age/benefits/in-box/delivery/warranty/related) | #5 |
| 6 | Cart + mobile-first checkout (GE, no forced account, gift-message, delivery cost) + Order + confirmation email | #9 |
| 7 | **Real GE card payment (TBC/BoG)** sandbox→live | #10 |
| 8 | GA4 + Meta Pixel | #12 |
| 9 | ~15-30 SKU seeded (→ swap to Archil final) | §12 Step 4 |
| 10 | Minimal admin (product CRUD + order list) | partial #14 |
| 11 | Deploy VPS/Coolify (staging → bubabu.ge on sign-off) | - |

## OUT (→ full Phase 1 / Phase 2)
Promo/campaign logic (#16) · gift wrapping product (#15) · blog/gift-guides depth (#18) · full admin CMS banners/collections/SEO editor (rest of #14) · delivery-company API integration (#11 - MVP = flat/manual delivery rule) · occasion/budget/interest/recipient full gift-nav (#6/#7 partial) · Cinema-Heroes campaign · SEO-text blocks depth (#13) · store-locations rich (#19) · all 10 Phase-2 items (Gift Finder quiz, recommendations, loyalty, comparison, reviews/UGC, WhatsApp assistant, stand inventory sync, abandoned-cart, segmentation).

## Blockers from Archil (get in writing at start)
1. Merchant credentials TBC/BoG (or aggregator) - gates payment.
2. Final curated product list + photoset (30-60 SKU) - gates real catalog.
3. Domain/DNS + hosting access (or staging-first).
4. Legal: terms + privacy + GE tax-invoice requirement (aiNOW PAID-model contract for this scope).

## Premortem outcome (2026-06-13) - PLANNING ONLY, nothing built
Verdict = **CONDITIONAL PASS** (full: `../../premortem/content/20260613_bubabu_shop_mvp/transcript.md`).
- **Most likely failure:** both defining MVP features (live gateway + real catalog) are Archil-controlled and on the critical path → engine done, nothing demoable at month-end.
- **Most dangerous:** 1000₾ top-down quote vs ~4000₾ real work → unpaid overtime or thin ship, killing the P1/P2 upsell.
- **Repo finding:** FLORCA reuse is shallow (client `Product.price`/`category` absent from Prisma schema; `id` Int vs string; 2 clashing `CartItem`; no i18n). → reuse **UI only**, clean-build the domain (schema + Order + checkout).
- **Recommended build approach (apply WHEN/IF a build is greenlit):** COD/transfer checkout as the default shippable path behind a `PaymentProvider` interface + seed ~25 clean SKU now → demo NOT gated on Archil; real TBC/BoG + final catalog = swap-ins.
- **OPEN PLANNING DECISION (deferred by user):** COD-first decouple (recommended) vs keep gateway+catalog as hard MVP gates (then milestone date contingent on Archil week-1 delivery).
- **Not yet done (planning task):** bottom-up hour estimate (11 steps × solo-hours vs content/client load) → to replace the top-down 1000₾/1-month number.

**Status: PLAN ONLY. No repo, no code. Build starts only on explicit user go.**
