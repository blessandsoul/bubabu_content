/* BUBABU.GE - interactions */
document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', () => {
  const lang = document.documentElement.lang || 'ru';
  const t = {
    slide: { ru: 'Слайд ', ka: 'სლაიდი ', en: 'Slide ' },
    thanks: {
      ru: 'Спасибо! Проверьте почту.',
      ka: 'გმადლობთ! ფასდაკლებები მალე მოგივათ.',
      en: 'Thank you! Please check your email.'
    }
  };
  const getTranslation = (key) => (t[key] && t[key][lang]) || t[key]['ru'];

  // sticky header shadow
  const hdr = document.getElementById('hdr');
  if (hdr) addEventListener('scroll', () => hdr.classList.toggle('scrolled', scrollY > 8), { passive:true });

  // scroll reveal (staggered)
  const io = new IntersectionObserver((es) => {
    es.forEach((e) => {
      if (e.isIntersecting) {
        const sibs = [...e.target.parentElement.querySelectorAll('.reveal')];
        e.target.style.transitionDelay = (sibs.indexOf(e.target) % 5 * 70) + 'ms';
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { threshold: .12 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  // mobile nav
  const burger = document.getElementById('burger');
  const nav = document.getElementById('nav');
  if (burger && nav) burger.addEventListener('click', () => nav.classList.toggle('open'));
  if (nav) nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')));

  // cart drawer
  const scrim = document.getElementById('scrim');
  const drawer = document.getElementById('drawer');
  const openCart = () => { scrim.classList.add('open'); drawer.classList.add('open'); document.body.style.overflow='hidden'; };
  const closeCart = () => { scrim.classList.remove('open'); drawer.classList.remove('open'); document.body.style.overflow=''; };
  document.querySelectorAll('[data-cart-open]').forEach(b => b.addEventListener('click', openCart));
  document.querySelectorAll('[data-cart-close]').forEach(b => b.addEventListener('click', closeCart));
  if (scrim) scrim.addEventListener('click', closeCart);
  addEventListener('keydown', e => { if (e.key === 'Escape') closeCart(); });

  // add-to-cart -> bump badge + open drawer
  const badge = document.getElementById('cartCount');
  let count = 3;
  document.querySelectorAll('.add').forEach(b => b.addEventListener('click', (e) => {
    e.preventDefault(); count++; if (badge) badge.textContent = count; openCart();
  }));

  // gift finder option toggles
  document.querySelectorAll('.opts').forEach(group => {
    group.addEventListener('click', (e) => {
      const b = e.target.closest('button'); if (!b) return;
      group.querySelectorAll('button').forEach(x => x.classList.remove('on'));
      b.classList.add('on');
    });
  });

  // gift assistant -> reveal curated results
  const finderGo = document.getElementById('finderGo');
  const finderResults = document.getElementById('finderResults');
  if (finderGo && finderResults) finderGo.addEventListener('click', () => {
    finderResults.hidden = false;
    finderResults.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  // review filter chips (visual only in demo)
  document.querySelectorAll('.revfilter').forEach(g => g.addEventListener('click', (e) => {
    const b = e.target.closest('button'); if (!b) return;
    g.querySelectorAll('button').forEach(x => x.classList.remove('on'));
    b.classList.add('on');
  }));

  // hero slider
  const slider = document.getElementById('hslider');
  if (slider) {
    const slides = [...slider.querySelectorAll('.hslide')];
    const dotsWrap = document.getElementById('hdots');
    let idx = Math.max(0, slides.findIndex(s => s.classList.contains('on')));
    let timer;
    const dots = slides.map((_, i) => {
      const b = document.createElement('button');
      b.setAttribute('aria-label', getTranslation('slide') + (i + 1));
      b.addEventListener('click', () => go(i, true));
      dotsWrap && dotsWrap.appendChild(b);
      return b;
    });
    const paint = () => {
      slides.forEach((s, i) => s.classList.toggle('on', i === idx));
      dots.forEach((d, i) => d.classList.toggle('on', i === idx));
    };
    const go = (i, user) => { idx = (i + slides.length) % slides.length; paint(); if (user) restart(); };
    const restart = () => { clearInterval(timer); timer = setInterval(() => go(idx + 1), 5500); };
    const prev = document.getElementById('hprev');
    const next = document.getElementById('hnext');
    if (prev) prev.addEventListener('click', () => go(idx - 1, true));
    if (next) next.addEventListener('click', () => go(idx + 1, true));
    slider.addEventListener('mouseenter', () => clearInterval(timer));
    slider.addEventListener('mouseleave', restart);
    let sx = 0;
    slider.addEventListener('touchstart', e => { sx = e.touches[0].clientX; clearInterval(timer); }, { passive:true });
    slider.addEventListener('touchend', e => {
      const dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 40) go(idx + (dx < 0 ? 1 : -1), true); else restart();
    }, { passive:true });
    paint();
    if (slides.length > 1) restart();
  }

  // PDP interactions (product page only)
  const pdp = document.querySelector('.pdp');
  if (pdp) {
    const main = document.getElementById('galleryMain');
    document.querySelectorAll('.thumb').forEach(t => t.addEventListener('click', () => {
      document.querySelectorAll('.thumb').forEach(x => x.classList.remove('on'));
      t.classList.add('on');
      if (main && t.dataset.src) main.src = t.dataset.src;
    }));
    // swipe main gallery image on mobile to cycle photos
    const gmain = document.querySelector('.gallery__main');
    const thumbs = [...document.querySelectorAll('.thumb')];
    if (gmain && thumbs.length > 1) {
      let gx = 0;
      gmain.addEventListener('touchstart', e => { gx = e.touches[0].clientX; }, { passive:true });
      gmain.addEventListener('touchend', e => {
        const dx = e.changedTouches[0].clientX - gx;
        if (Math.abs(dx) < 40) return;
        let i = thumbs.findIndex(t => t.classList.contains('on'));
        if (i < 0) i = 0;
        i = (i + (dx < 0 ? 1 : -1) + thumbs.length) % thumbs.length;
        thumbs[i].click();
        thumbs[i].scrollIntoView({ inline:'center', block:'nearest' });
      }, { passive:true });
    }
    document.querySelectorAll('.vbtns, .swatches').forEach(group => group.addEventListener('click', e => {
      const b = e.target.closest('button'); if (!b) return;
      group.querySelectorAll('button').forEach(x => x.classList.remove('on'));
      b.classList.add('on');
    }));
    const qv = document.getElementById('qtyVal');
    document.querySelectorAll('.qty__btn').forEach(b => b.addEventListener('click', () => {
      const n = parseInt(qv.textContent, 10) + parseInt(b.dataset.q, 10);
      qv.textContent = Math.max(1, n);
    }));
    const sticky = document.getElementById('stickybuy');
    const buybox = document.getElementById('buybox');
    if (sticky && buybox) {
      new IntersectionObserver(es => es.forEach(e => {
        sticky.classList.toggle('show', !e.isIntersecting && e.boundingClientRect.top < 0);
      }), { threshold: 0 }).observe(buybox);
    }
  }

  // newsletter success state (both pages)
  document.querySelectorAll('.news form').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    f.innerHTML = '<p style="font-weight:700;color:var(--accent-deep);display:flex;align-items:center;gap:.5em"><i class="ph-fill ph-check-circle"></i> ' + getTranslation('thanks') + '</p>';
  }));
});
