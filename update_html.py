import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Top comment
top_comment = "<!-- Corrections applied: Stats fix, YouTube typo fix, Portfolio cards, Form connection, Scroll animations, Hero typography, SVG icons, OG meta tags -->\n"
if top_comment not in html:
    html = top_comment + html

# 1. Stats
stats_old = """<div class="stat-item reveal">
      <h3><span class="stat-num" data-count="50" data-suffix="+">0</span></h3>
      <p>Projects Delivered</p>
    </div>
    <div class="stat-item reveal reveal-delay-1">
      <h3><span class="stat-num" data-count="2" data-suffix="M+">0</span></h3>
      <p>Views Generated</p>
    </div>
    <div class="stat-item reveal reveal-delay-2">
      <h3><span class="stat-num" data-count="98" data-suffix="%">0</span></h3>
      <p>Client Retention</p>
    </div>
    <div class="stat-item reveal reveal-delay-3">
      <h3><span class="stat-num" data-count="48" data-suffix="hr">0</span></h3>
      <p>Turnaround Time</p>
    </div>"""

stats_new = """<div class="stat-item reveal reveal-delay-1">
      <h3><span class="stat-num" data-count="50" data-suffix="+">0</span></h3>
      <p>Projects Delivered</p>
    </div>
    <div class="stat-item reveal reveal-delay-2">
      <h3><span class="stat-num" data-count="10" data-suffix="M+">0</span></h3>
      <p>Views Generated</p>
    </div>
    <div class="stat-item reveal reveal-delay-3">
      <h3><span class="stat-num" data-count="95" data-suffix="%">0</span></h3>
      <p>Client Retention</p>
    </div>
    <div class="stat-item reveal reveal-delay-4">
      <h3><span class="stat-num" data-count="48" data-suffix="h">0</span></h3>
      <p>Turnaround Time</p>
    </div>"""

html = html.replace(stats_old, stats_new)

# 2. Meta tags
meta_old = """<meta name="description" content="MOTIONNODEEDITS — Premium cinematic AI creative agency specializing in AI video editing, ads, reels, and motion graphics.">"""
meta_new = """<!-- Open Graph / WhatsApp / Instagram link preview -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://motionnodeedits.com">
  <meta property="og:title" content="MOTIONNODEEDITS — Cinematic AI Creative Agency">
  <meta property="og:description" content="AI-powered video editing for creators and brands who refuse to be ignored. Reels, AI Ads, Avatar Videos and more. Based in Hyderabad.">
  <meta property="og:image" content="https://saiteja8342.github.io/test/image/logo.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="MOTIONNODEEDITS — Cinematic AI Creative Agency">
  <meta name="twitter:description" content="AI-powered video editing for creators and brands who refuse to be ignored.">
  <meta name="twitter:image" content="https://saiteja8342.github.io/test/image/logo.png">

  <!-- General SEO -->
  <meta name="description" content="MOTIONNODEEDITS — Premium AI video editing agency in Hyderabad. We create Reels, AI Ads, Avatar Videos, Motion Graphics and more.">
  <meta name="keywords" content="AI video editing, reels editing, YouTube shorts editing, AI ads, avatar videos, motion graphics, Hyderabad video agency">
  <meta name="author" content="MOTIONNODEEDITS">"""

if "og:title" not in html:
    html = html.replace(meta_old, meta_new)

# 3. Contact Form
form_old = """<form id="contactForm" class="contact-form reveal reveal-delay-2">
        <div class="form-group">
          <label>Name</label>
          <input type="text" name="user_name" placeholder="Your name" required>
        </div>
        <div class="form-group">
          <label>Email</label>
          <input type="email" name="user_email" placeholder="your@email.com" required>
        </div>
        <div class="form-group">
          <label>Message</label>
          <textarea rows="5" name="message" placeholder="Your message..." required></textarea>
        </div>
        <button type="submit">Send Message</button>
      </form>"""

form_new = """<!-- 
  HOW TO ACTIVATE THE CONTACT FORM:
  1. Go to https://formspree.io and sign up free
  2. Create a new form and copy your Form ID
  3. Replace YOUR_FORM_ID in the form action above with your real ID
  Done — you will receive emails directly to your inbox
-->
      <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" id="contactForm" class="contact-form reveal reveal-delay-2">
        <input type="hidden" name="_subject" value="New enquiry from MOTIONNODEEDITS website">
        <div class="form-group">
          <label>Name</label>
          <input type="text" name="user_name" placeholder="Your name" required>
        </div>
        <div class="form-group">
          <label>Email</label>
          <input type="email" name="user_email" placeholder="your@email.com" required>
        </div>
        <div class="form-group">
          <label>Message</label>
          <textarea rows="5" name="message" placeholder="Your message..." required></textarea>
        </div>
        <button type="submit">Send Message</button>
      </form>
      <div id="form-success" style="display:none; text-align:center; padding:40px 0;">
        <p style="font-size:28px; margin-bottom:12px;">🎬</p>
        <p style="font-size:20px; font-weight:700; color:#ffffff; margin-bottom:8px;">Message received.</p>
        <p style="font-size:15px; color:#888888;">We will respond within 24 hours.</p>
      </div>"""

html = html.replace(form_old, form_new)

# 4. Hero Title
hero_old = """<h1 class="reveal">Crafted in the <span class="highlight">DARK</span>.<br>Built to dominate the <span class="highlight">LIGHT</span>.</h1>"""
hero_new = """<h1 class="hero-title reveal">
  <span class="hero-thin">Crafted in the</span> DARK.<br>
  <span class="hero-thin">Built to dominate the</span> LIGHT.
</h1>"""
html = html.replace(hero_old, hero_new)

# 5. Service Icons
icon1_old = """<span class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect></svg></span>"""
icon1_new = """<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <rect x="2" y="6" width="15" height="12" rx="2"/><path d="m17 9 5-3v12l-5-3"/>
</svg>"""

icon2_old = """<span class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l18-5v12L3 14v-3z"></path><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"></path></svg></span>"""
icon2_new = """<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M3 11l19-9-9 19-2-8-8-2z"/>
</svg>"""

icon3_old = """<span class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span>"""
icon3_new = """<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/>
</svg>"""

icon4_old = """<span class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></span>"""
icon4_new = """<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M5 3l14 9-14 9V3z"/>
</svg>"""

icon5_old = """<span class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg></span>"""
icon5_new = """<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
</svg>"""

icon6_old = """<span class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg></span>"""
icon6_new = """<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M3 9.5L12 3l9 6.5V20a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9.5z"/><path d="M9 21V12h6v9"/>
</svg>"""

html = html.replace(icon1_old, icon1_new)
html = html.replace(icon2_old, icon2_new)
html = html.replace(icon3_old, icon3_new)
html = html.replace(icon4_old, icon4_new)
html = html.replace(icon5_old, icon5_new)
html = html.replace(icon6_old, icon6_new)

# 6. Portfolio replacement
portfolio_old = """  <div class="portfolio-header">
    <div>
      <p class="section-label reveal">Selected Work</p>
      <h2 class="section-title reveal reveal-delay-1">Cinematic Showcase</h2>
      <p class="section-desc reveal reveal-delay-2">Each project is a cinematic experience — crafted with AI precision and human artistry.</p>
    </div>
    <div class="portfolio-filters reveal reveal-delay-3">
      <!-- Filter buttons are dynamically generated from categories in main.js -->
    </div>
  </div>
  <div class="portfolio-grid" id="portfolioCards">
    <!-- Cards injected by JS -->
  </div>"""

portfolio_new = """  <div class="portfolio-header">
    <div>
      <p class="section-label reveal">Selected Work</p>
      <h2 class="section-title reveal reveal-delay-1">Cinematic Showcase</h2>
      <p class="section-desc reveal reveal-delay-2">Each project is a cinematic experience — crafted with AI precision and human artistry.</p>
    </div>
  </div>
  
  <div class="portfolio-tabs reveal reveal-delay-3" style="display:flex; gap:12px; margin-bottom:32px; overflow-x:auto; padding-bottom:12px;">
    <button class="tab-btn active" data-tab="reels">Reels & Shorts</button>
    <button class="tab-btn" data-tab="ads">AI Ads</button>
    <button class="tab-btn" data-tab="avatar">AI Avatar</button>
    <button class="tab-btn" data-tab="aireels">AI Reels</button>
    <button class="tab-btn" data-tab="post">Post-Production</button>
  </div>

  <div class="portfolio-lanes reveal reveal-delay-4">
    <!-- Lane: Reels & Shorts -->
    <div class="portfolio-lane active" id="lane-reels">
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>SHORT-FORM · REEL</span>
          <h4>Creator Brand Reel Vol.1</h4>
          <p style="color:#888; font-size:13px; margin:0;">3.2M views · Cinematic lifestyle cut</p>
        </div>
      </div>
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>SHORT-FORM · YOUTUBE SHORT</span>
          <h4>Viral Education Short</h4>
          <p style="color:#888; font-size:13px; margin:0;">1.8M views · Hook-first structure</p>
        </div>
      </div>
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>SHORT-FORM · REEL</span>
          <h4>Fitness Brand Montage</h4>
          <p style="color:#888; font-size:13px; margin:0;">4.5M views · High-energy edit</p>
        </div>
      </div>
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>SHORT-FORM · REEL</span>
          <h4>Product Launch Teaser</h4>
          <p style="color:#888; font-size:13px; margin:0;">900K views · Premium feel</p>
        </div>
      </div>
    </div>

    <!-- Lane: AI Ads -->
    <div class="portfolio-lane" id="lane-ads">
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>AI · ADVERTISEMENT</span>
          <h4>SaaS Product Launch Ad</h4>
          <p style="color:#888; font-size:13px; margin:0;">AI-assisted full production</p>
        </div>
      </div>
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>AI · E-COMMERCE</span>
          <h4>Fashion Brand Campaign</h4>
          <p style="color:#888; font-size:13px; margin:0;">AI visuals + cinematic edit</p>
        </div>
      </div>
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>AI · PERFORMANCE AD</span>
          <h4>Real Estate Promo</h4>
          <p style="color:#888; font-size:13px; margin:0;">AI voiceover + motion</p>
        </div>
      </div>
    </div>

    <!-- Lane: AI Avatar -->
    <div class="portfolio-lane" id="lane-avatar">
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>AI AVATAR · REEL</span>
          <h4>Digital Human Spokesperson</h4>
          <p style="color:#888; font-size:13px; margin:0;">AI avatar for tech brand</p>
        </div>
      </div>
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>AI AVATAR · EXPLAINER</span>
          <h4>Course Creator Avatar</h4>
          <p style="color:#888; font-size:13px; margin:0;">Multilingual AI presenter</p>
        </div>
      </div>
    </div>

    <!-- Lane: AI Reels -->
    <div class="portfolio-lane" id="lane-aireels">
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>AI-GENERATED · SHORT</span>
          <h4>Generative Brand Reel</h4>
          <p style="color:#888; font-size:13px; margin:0;">100% AI-generated visuals</p>
        </div>
      </div>
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>AI-GENERATED · CINEMATIC</span>
          <h4>Sora-Style Narrative</h4>
          <p style="color:#888; font-size:13px; margin:0;">Next-gen AI video production</p>
        </div>
      </div>
    </div>

    <!-- Lane: Post-Production -->
    <div class="portfolio-lane" id="lane-post">
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>POST-PRODUCTION · LONG-FORM</span>
          <h4>Documentary Edit — 45 min</h4>
          <p style="color:#888; font-size:13px; margin:0;">Full post-production pipeline</p>
        </div>
      </div>
      <!-- Replace dQw4w9WgXcQ with your real YouTube video ID -->
      <div class="video-card" onclick="openVideoModal('dQw4w9WgXcQ')">
        <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Thumbnail" class="video-card-thumb">
        <div class="play-icon"></div>
        <div class="video-card-overlay">
          <span>POST-PRODUCTION · COLOR</span>
          <h4>Cinematic Color Grade</h4>
          <p style="color:#888; font-size:13px; margin:0;">Nolan-grade color pipeline</p>
        </div>
      </div>
    </div>
  </div>"""

html = html.replace(portfolio_old, portfolio_new)
html = html.replace('youtube.com/@motionnodeedtis', 'youtube.com/@motionnodeedits')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if top_comment not in css:
    css = "/* Corrections applied: Stats fix, YouTube typo fix, Portfolio cards, Form connection, Scroll animations, Hero typography, SVG icons, OG meta tags */\n" + css

css_additions = """
/* NEW PORTFOLIO CSS */
.tab-btn {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 9px 22px;
  border-radius: 100px;
  border: 1px solid rgba(255,255,255,0.15);
  background: transparent;
  color: #888888;
  cursor: pointer;
  transition: all 0.25s;
}
.tab-btn.active {
  background: #ffffff;
  color: #000000;
  border-color: #ffffff;
}

.portfolio-lane {
  display: none;
  overflow-x: auto;
  gap: 20px;
  padding-bottom: 24px;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
  scrollbar-color: rgba(255,255,255,0.15) transparent;
}
.portfolio-lane.active {
  display: flex;
}

.hero-title {
  font-size: clamp(48px, 8vw, 100px);
  font-weight: 800;
  line-height: 1.0;
  letter-spacing: -0.03em;
  text-transform: uppercase;
  clip-path: inset(0 0 100% 0);
  animation: clipReveal 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.4s forwards;
}
.hero-thin {
  font-weight: 200;
  font-style: italic;
  color: #666666;
  text-transform: none;
  font-size: 0.75em;
}
@keyframes clipReveal {
  from { clip-path: inset(0 0 100% 0); }
  to   { clip-path: inset(0 0 0% 0); }
}

.service-icon {
  width: 32px;
  height: 32px;
  color: #ffffff;
  margin-bottom: 20px;
  display: block;
  opacity: 0.85;
}
"""

if ".tab-btn" not in css:
    css += css_additions

# Need to update .video-card styling to match user's prompt
video_card_old = """.video-card { aspect-ratio:16/9; border-radius:20px; overflow:hidden; position:relative; cursor:none; border:1px solid var(--border); transition:transform .5s,box-shadow .5s; background:#111; }
.video-card:hover { z-index: 5; box-shadow: 0 0 40px var(--glow); }"""
video_card_new = """.video-card {
  flex: 0 0 320px;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  cursor: pointer;
  transition: transform 0.4s cubic-bezier(0.16,1,0.3,1), border-color 0.3s;
}
.video-card:hover {
  transform: translateY(-8px) scale(1.02);
  border-color: rgba(255,255,255,0.2);
  z-index: 5;
}"""

css = css.replace(video_card_old, video_card_new)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

if "/* Corrections applied: " not in js:
    js = "/* Corrections applied: Stats fix, YouTube typo fix, Portfolio cards, Form connection, Scroll animations, Hero typography, SVG icons, OG meta tags */\n" + js

js = js.replace('@motionnodeedtis', '@motionnodeedits')

js_additions = """
// ── Custom Portfolio Tabs & Modal ──
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.portfolio-lane').forEach(l => l.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('lane-' + btn.dataset.tab).classList.add('active');
  });
});

// ── Contact Form Formspree ──
const newContactForm = document.querySelector('form[action*="formspree"]');
if (newContactForm) {
  newContactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = new FormData(newContactForm);
    const response = await fetch(newContactForm.action, {
      method: 'POST',
      body: data,
      headers: { 'Accept': 'application/json' }
    });
    if (response.ok) {
      newContactForm.style.display = 'none';
      document.getElementById('form-success').style.display = 'block';
    } else {
      alert('Something went wrong. Please WhatsApp us directly.');
    }
  });
}

// ── Reveal Scroll Animations ──
const revealEls = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
revealEls.forEach(el => revealObserver.observe(el));
"""

# replace old emailjs handler to avoid conflict, or just remove the old event listener logic
js_email_old = """  // Contact Form Setup with EmailJS
  if (typeof emailjs !== 'undefined') { emailjs.init({ publicKey: 'YOUR_PUBLIC_KEY' }); }
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const btn = this.querySelector('button[type="submit"]');
      const originalText = btn.textContent;
      btn.textContent = 'Sending...';
      
      if (typeof emailjs !== 'undefined') { emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
        .then(() => {
            btn.textContent = 'Message Sent!';
            this.reset();
            setTimeout(() => btn.textContent = originalText, 3000);
        }, (error) => {
            console.error('FAILED...', error);
            btn.textContent = 'Failed to Send (Check Keys)';
            setTimeout(() => btn.textContent = originalText, 3000);
        });
      } else { alert('EmailJS not loaded'); btn.textContent = originalText; }
    });
  }"""
js = js.replace(js_email_old, "")

# the initCounters might have a conflict with the new countUp if we append? 
# The prompt provided a `countUp` logic:
count_up_logic = """const countUp = (el, target, suffix, duration) => {
  let start = null;
  const step = (timestamp) => {
    if (!start) start = timestamp;
    const progress = Math.min((timestamp - start) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.floor(ease * target) + suffix;
    if (progress < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
};"""
# Actually, the existing `initCounters()` in `js/main.js` already does EXACTLY what the prompt requested for counting up!
# I will just leave it be, as I already modified index.html to use data-count="50" data-suffix="+" etc.

if "document.querySelectorAll('.tab-btn')" not in js:
    js += js_additions

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

