/* ============================================
   MOTIONNODEEDITS — Main JavaScript
   ============================================ */

// ── Portfolio Data (YouTube-based) ──
const defaultPortfolio = [
  { id:'1', title:'Luxury Perfume AI Ad', category:'ai-ads', youtubeId:'dQw4w9WgXcQ', desc:'AI-generated luxury fragrance commercial' },
  { id:'2', title:'Coffee Morning', category:'ai-ads', youtubeId:'ScMzIvxBSi4', desc:'Premium AI coffee commercial' },
  { id:'3', title:'Sweet Delights', category:'ai-ads', youtubeId:'LXb3EKWsInQ', desc:'AI candy brand showcase' },
  { id:'4', title:'Urban Fashion Reel', category:'ai-reels', youtubeId:'2Vv-BfVoq4g', desc:'Hyper-edited AI fashion reel' },
  { id:'5', title:'Tech Product Launch', category:'ai-reels', youtubeId:'jNQXAC9IVRw', desc:'Futuristic product reveal' },
  { id:'6', title:'AI Avatar Presenter', category:'ai-avatar', youtubeId:'dQw4w9WgXcQ', desc:'AI avatar business presentation' },
  { id:'7', title:'Digital Human Host', category:'ai-avatar', youtubeId:'ScMzIvxBSi4', desc:'Realistic AI avatar hosting' },
  { id:'8', title:'Modern Villa Tour', category:'real-estate', youtubeId:'LXb3EKWsInQ', desc:'Cinematic real estate walkthrough' },
  { id:'9', title:'Skyline Penthouse', category:'real-estate', youtubeId:'2Vv-BfVoq4g', desc:'Luxury property showcase' },
  { id:'10', title:'Color Grading Reel', category:'post-production', youtubeId:'jNQXAC9IVRw', desc:'Professional color grading demo' },
  { id:'11', title:'VFX Breakdown', category:'post-production', youtubeId:'dQw4w9WgXcQ', desc:'Visual effects compositing' },
  { id:'12', title:'Neon Night Drive', category:'ai-ads', youtubeId:'ScMzIvxBSi4', desc:'Cinematic night automotive ad' },
];

function getPortfolio() {
  const saved = localStorage.getItem('mne_portfolio');
  return saved ? JSON.parse(saved) : defaultPortfolio;
}

function getCategories() {
  const saved = localStorage.getItem('mne_categories');
  if (saved) return JSON.parse(saved);
  return [
    { slug: 'ai-ads', label: 'AI Ads' },
    { slug: 'ai-reels', label: 'AI Reels' },
    { slug: 'ai-avatar', label: 'AI Avatar Videos' },
    { slug: 'real-estate', label: 'Real Estate' },
    { slug: 'post-production', label: 'Post Production' }
  ];
}

function getCategoryLabel(slug) {
  const cats = getCategories();
  const found = cats.find(c => c.slug === slug);
  return found ? found.label : slug.replace(/-/g, ' ');
}

function getYouTubeThumb(videoId) {
  return `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`;
}

// ── Preloader ──
window.addEventListener('load', () => {
  setTimeout(() => {
    const pl = document.querySelector('.preloader');
    if (pl) pl.classList.add('hidden');
  }, 1800);
});

// ── Custom Cursor ──
(function initCursor() {
  if (window.innerWidth < 768) return;
  
  const cursor = document.getElementById('cursor') || document.querySelector('.custom-cursor');
  const cursorGlow = document.getElementById('cursorGlow');
  if (!cursor) return;

  let cursorX = 0, cursorY = 0, glowX = 0, glowY = 0;

  document.addEventListener('mousemove', (e) => {
    cursorX = e.clientX;
    cursorY = e.clientY;
    
    // Direct position update for the main cursor dot
    if (cursor.id === 'cursor') {
      cursor.style.left = cursorX + 'px';
      cursor.style.top = cursorY + 'px';
    }
  });

  function lerp() {
    // Smooth lerp for glow OR for .custom-cursor
    glowX += (cursorX - glowX) * 0.08;
    glowY += (cursorY - glowY) * 0.08;
    
    if (cursorGlow) {
      cursorGlow.style.left = glowX + 'px';
      cursorGlow.style.top = glowY + 'px';
    } else if (cursor.classList.contains('custom-cursor')) {
      cursor.style.left = glowX + 'px';
      cursor.style.top = glowY + 'px';
    }
    requestAnimationFrame(lerp);
  }
  lerp();

  const hoverEls = 'a, button, .video-card, .service-card, .filter-btn, .social-btn, .nav-cta, .btn-primary, .btn-secondary, input, select, textarea';
  document.addEventListener('mouseover', (e) => {
    if (e.target.closest(hoverEls)) cursor.classList.add('hover');
  });
  document.addEventListener('mouseout', (e) => {
    if (e.target.closest(hoverEls)) cursor.classList.remove('hover');
  });
})();

// ── Navbar Scroll ──
(function initNavbar() {
  const nav = document.querySelector('.navbar');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 50);
  });
  // Hamburger
  const ham = document.querySelector('.hamburger');
  const links = document.querySelector('.nav-links');
  if (ham && links) {
    ham.addEventListener('click', () => {
      ham.classList.toggle('active');
      links.classList.toggle('open');
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        ham.classList.remove('active');
        links.classList.remove('open');
      });
    });
  }
})();

// ── Particle System ──
function initParticles(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let w, h;
  const particles = [];
  const count = 60;

  function resize() {
    w = canvas.width = canvas.parentElement.offsetWidth;
    h = canvas.height = canvas.parentElement.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  for (let i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * w, y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.3, vy: (Math.random() - 0.5) * 0.3,
      r: Math.random() * 1.5 + 0.5, a: Math.random() * 0.3 + 0.1
    });
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x = w; if (p.x > w) p.x = 0;
      if (p.y < 0) p.y = h; if (p.y > h) p.y = 0;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${p.a})`;
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  draw();
}

// ── Scroll Reveal ──
function initReveal() {
  const els = document.querySelectorAll('.reveal, .reveal-left');
  if (!els.length) return;
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { threshold: 0.15 });
  els.forEach(el => obs.observe(el));
}

// ── Stats Counter ──
function initCounters() {
  const counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target;
      const target = parseInt(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      const duration = 2000;
      const start = performance.now();
      function step(now) {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.floor(target * eased) + suffix;
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
      obs.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(c => obs.observe(c));
}

// ── Portfolio Cards ──
function renderPortfolio(containerId, filter) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const data = getPortfolio();
  const filtered = filter && filter !== 'all' ? data.filter(v => v.category === filter) : data;
  container.innerHTML = '';
  filtered.forEach(v => {
    const card = document.createElement('div');
    card.className = 'video-card';
    card.dataset.videoId = v.youtubeId;
    card.innerHTML = `
      <img class="video-card-thumb" src="${getYouTubeThumb(v.youtubeId)}" alt="${v.title}" loading="lazy">
      <div class="video-card-overlay">
        <span class="video-card-category">${getCategoryLabel(v.category)}</span>
        <span class="video-card-title">${v.title}</span>
      </div>
      <div class="video-card-play"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
    `;
    card.addEventListener('click', () => openVideoModal(v.youtubeId, v.title));
    container.appendChild(card);
  });
}

// ── Video Modal ──
function openVideoModal(videoId, title) {
  const modal = document.getElementById('videoModal');
  const iframe = document.getElementById('modalIframe');
  if (!modal || !iframe) return;
  iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0&modestbranding=1`;
  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeVideoModal() {
  const modal = document.getElementById('videoModal');
  const iframe = document.getElementById('modalIframe');
  if (!modal || !iframe) return;
  modal.classList.remove('open');
  iframe.src = '';
  document.body.style.overflow = '';
}

// ── Portfolio Filter (Dynamic from categories) ──
function initFilters() {
  const filterContainer = document.querySelector('.portfolio-filters');
  if (!filterContainer) return;

  // Dynamically build filter buttons from stored categories
  const cats = getCategories();
  filterContainer.innerHTML = '';

  // "All" button first
  const allBtn = document.createElement('button');
  allBtn.className = 'filter-btn active';
  allBtn.dataset.filter = 'all';
  allBtn.textContent = 'All';
  filterContainer.appendChild(allBtn);

  cats.forEach(cat => {
    const btn = document.createElement('button');
    btn.className = 'filter-btn';
    btn.dataset.filter = cat.slug;
    btn.textContent = cat.label;
    filterContainer.appendChild(btn);
  });

  // Attach click handlers
  const btns = filterContainer.querySelectorAll('.filter-btn');
  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderPortfolio('portfolioCards', btn.dataset.filter);
    });
  });
}

// ── Booking Form Multi-step ──
function initBookingForm() {
  const form = document.getElementById('bookingForm');
  if (!form) return;
  let step = 0;
  const steps = form.querySelectorAll('.booking-step');
  const indicators = form.querySelectorAll('.booking-step-indicator');
  const nextBtns = form.querySelectorAll('.btn-next');
  const prevBtns = form.querySelectorAll('.btn-prev');

  function showStep(n) {
    steps.forEach((s, i) => { s.classList.toggle('active', i === n); });
    indicators.forEach((ind, i) => {
      ind.classList.toggle('active', i === n);
      ind.classList.toggle('done', i < n);
    });
  }

  nextBtns.forEach(b => b.addEventListener('click', () => { if (step < steps.length - 1) { step++; showStep(step); } }));
  prevBtns.forEach(b => b.addEventListener('click', () => { if (step > 0) { step--; showStep(step); } }));
  showStep(0);
}

// ── GSAP Animations ──
function initGSAP() {
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;
  gsap.registerPlugin(ScrollTrigger);

  // Hero text animation
  gsap.from('.hero-content h1', { y: 80, opacity: 0, duration: 1.4, delay: 2, ease: 'power4.out' });
  gsap.from('.hero-subtitle', { y: 40, opacity: 0, duration: 1, delay: 2.4, ease: 'power3.out' });
  gsap.from('.hero-buttons', { y: 30, opacity: 0, duration: 1, delay: 2.7, ease: 'power3.out' });

  // Section titles
  gsap.utils.toArray('.section-title').forEach(el => {
    gsap.from(el, {
      scrollTrigger: { trigger: el, start: 'top 85%' },
      y: 60, opacity: 0, duration: 1, ease: 'power3.out'
    });
  });

  // Service cards stagger
  gsap.utils.toArray('.service-card').forEach((el, i) => {
    gsap.from(el, {
      scrollTrigger: { trigger: el, start: 'top 85%' },
      y: 50, opacity: 0, duration: 0.8, delay: i * 0.1, ease: 'power3.out'
    });
  });

  // Process timeline
  const processLine = document.querySelector('.process-line-fill');
  if (processLine) {
    gsap.to(processLine, {
      height: '100%',
      scrollTrigger: {
        trigger: '.process-timeline',
        start: 'top 70%',
        end: 'bottom 30%',
        scrub: 1
      }
    });
  }

  // Process steps
  gsap.utils.toArray('.process-step').forEach((el, i) => {
    gsap.from(el, {
      scrollTrigger: { trigger: el, start: 'top 80%' },
      x: -40, opacity: 0, duration: 0.8, delay: i * 0.15,
      ease: 'power3.out',
      onComplete: () => el.classList.add('active')
    });
  });
}

// ── Lenis Smooth Scroll ──
function initLenis() {
  if (typeof Lenis === 'undefined') return;
  const lenis = new Lenis({ duration: 1.2, easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)), smooth: true });
  function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
  requestAnimationFrame(raf);
  // Sync with GSAP ScrollTrigger
  if (typeof ScrollTrigger !== 'undefined') {
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(time => lenis.raf(time * 1000));
    gsap.ticker.lagSmoothing(0);
  }
}

// ── Init All ──
document.addEventListener('DOMContentLoaded', () => {
  initReveal();
  initCounters();
  initParticles('heroParticles');
  renderPortfolio('portfolioCards', 'all');
  initFilters();
  initBookingForm();
  initGSAP();
  initLenis();

  // Modal close
  const modal = document.getElementById('videoModal');
  if (modal) {
    modal.addEventListener('click', e => { if (e.target === modal) closeVideoModal(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeVideoModal(); });
  }
});
