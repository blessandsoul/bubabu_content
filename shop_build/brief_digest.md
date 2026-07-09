# Bubabu Smart Gifts Shop - Brief Digest (A-H)

> Source: 3 .docx in `C:\Users\User\Desktop\BUBABU\WEBSITE\` (dated 2026-06-08, from Archil via Telegram). Extracted 2026-06-13.
> HTML entities decoded. Where the 3 docs disagree, the discrepancy is flagged.

## A. Category architecture
**Main nav (Homepage doc - leanest 8-item, use for MVP):** Bubabu AI Friend · Smart Gifts · Gifts by Age · Gifts by Occasion · Gift Sets · Screen-Free Gifts · Cinema Heroes · Best Sellers. Utility: Search · Cart · Lang GE/EN(/RU later) · Contact/Messenger/WhatsApp · Store Locations.
**9 main categories** (Architecture doc §3; brief said ~7 - Creative Smart Play + Smart Comfort flagged "could be subcategory"):
1. **Bubabu AI Friend** - hero owl + versions + gift sets + accessories. Subs: Meet Bubabu / Gift Sets / How It Works / Safety & Privacy / Setup & Support / Reviews.
2. **Gift Sets** - birthday/NY/premium bundles + gift bag + card.
3. **Smart Learning Gifts** - educational/language/interactive books/learning tablets/logic.
4. **Screen-Free Gifts** - Bubabu + nightlights/projectors/audio story/creative non-screen. (strongest Bubabu positioning)
5. **STEM & Robotics** - robotics/coding/science/construction kits. ("second-wave if assortment small")
6. **Creative Smart Play** - drawing tablets/art kits/music/puzzle. (or subcat)
7. **Smart Comfort Gifts** - nightlights/lamps/sleep companions. (better as subcat initially)
8. **Smart Surprises** - small impulse / gifts under 50₾.
9. **Cinema Heroes** - Toy Story/Minions/PAW Patrol/Disney/Sonic licensed. (seasonal campaign)
**Gift routes:** by Age (3-5 / 6-8 / 9-12 / 13-17 / 18-30-later) · by Occasion · by Budget (under 50/100/200₾ + premium) · by Interest · by Recipient.
**Final sitemap (§14, 11 top sections):** Home · Bubabu AI Friend · Smart Gifts · Gifts by Age · Gifts by Occasion · Gifts by Budget · Gift Sets · Cinema Heroes · Gift Finder · Guides/Blog · Support.

## B. Homepage - 16 blocks (authoritative, Homepage doc §3/§14)
1 Header/nav · 2 Hero ("Bubabu Smart Gifts - smart, safe, meaningful gifts…") · 3 Bubabu Hero Product · 4 Shop by Age (4 cards) · 5 Shop by Occasion · 6 Featured Categories (6 cards) · 7 Best Sellers (6-8) · 8 Gift Sets · 9 Cinema Heroes/Seasonal · 10 New Arrivals · 11 Why Parents Choose (trust icons) · 12 Video/Demo · 13 Gift Finder (P1=static buttons, P2=quiz) · 14 Gift Guides · 15 Store Locations · 16 Footer.
**MVP subset (this build):** 1,2,3,4,6,7,11,15(simple),16.

## C. §7 Technical requirements
7.1 pages (home/Bubabu/shop/category/age/occasion/detail/cart/checkout/blog/FAQ/delivery-returns/warranty/safety/contact) · 7.2 homepage blocks · 7.3 category page (title+emotional intro+filters+cards+sort+SEO text) · 7.4 listing card (image/name/price/age/benefit/tag/stock/add-to-cart/badge) · 7.5 product detail (photos/video/title/price/age/benefits/why-kids/why-parents/tech/in-box/delivery/warranty/FAQ/related/cross-sell/reviews/gift-wrap) + Bubabu-specific (how it works/what kids can ask/languages/safety/screen-free/setup/use-cases/compare) · 7.6 filters (age/price/category/occasion/universal/educational/screen-free/character/type/new/bestseller/in-stock; GE/EN/RU search) · 7.7 gift nav (+Gift Finder quiz = P2) · 7.8 checkout (mobile-first/short/no forced account/GE/delivery cost early/card/COD/installment/promo/gift-message/gift-wrap/email-SMS confirm) · 7.9 admin CMS (products/categories/collections/homepage blocks/banners/prices/stock/campaigns/promo/gift-sets/blog/reviews/SEO/multilingual/badges/cross-sell) · 7.10 analytics (GA4/Meta Pixel/TikTok/GSC/conversion/add-to-cart/abandonment/UTM/source/retargeting).

## D. Product data model (§12 Step 3)
title · short title · category · age · occasion · price · images · video · description · benefits · technical info · safety info · stock · product badges · related products · SEO title/description.
**Badges:** Hero Gift · Screen-Free · Educational · Smart Gift · Best for 3-6 / 6-8 · Cinema Hero · New Arrival · Bestseller · Gift Pick.

## E. §10 - Phase split (KEY SCOPING LIST)
**Must-have for launch (Phase 1, 20):** 1 GE+EN · 2 mobile-first · 3 Bubabu hero page · 4 homepage structure · 5 category architecture · 6 gift by age · 7 gift by occasion · 8 product filters · 9 fast checkout · 10 payment integration · 11 delivery integration · 12 Meta Pixel+GA4 · 13 SEO-ready · 14 admin-editable banners/collections · 15 gift wrap/message · 16 promo/campaign logic · 17 badges · 18 blog/gift-guide · 19 store locations page · 20 warranty/delivery/FAQ/support pages.
**Phase 2 (10):** Gift Finder quiz · personalized recommendations · loyalty/birthday reminder · advanced cross-sell · product comparison · reviews/UGC · Messenger/WhatsApp assistant · inventory sync with stands · abandoned-cart automation · customer segmentation.

## F. §12 MVP definition (Step 4 "Build MVP store")
Bubabu + Bubabu gift sets + **5-8 categories** + **30-60 SKUs** + gift navigation + mobile-first checkout + analytics + campaign landing pages.

## G. Payment / logistics - "must verify" (§6, §12 Step 1)
GE payment gateway support · bank card processing · installment options · delivery company integrations · GE language · accounting/ERP export · inventory sync with physical stands · app costs · checkout localization · **manage GEL pricing · legal/tax invoice requirements**. Brief recommended Shopify "unless GE payment/logistics creates serious limitations" - **OVERRIDDEN: we build custom.**

## H. Benchmark stores (no URLs in brief - names only)
Top 3: **KiwiCo** (educational/STEM, age-based) · **Uncommon Goods** (gift discovery by recipient/occasion/budget) · **Wicked Uncle** (kids' gift by age, fast buy). Secondary: Fat Brain Toys · MoMA Design Store · Firebox. UX refs cited: Baymard, Shopify/Adobe 2026 trends.
> Archil also said he sent "design-example domains" - NOT found on disk (only Bubabu.ge + these 6 names). Pending: ask Archil to paste.
