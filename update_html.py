import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Hero video replacement
html = re.sub(
    r'<video class="hero-video" autoplay muted loop playsinline>\s*<source src="[^"]*" type="video/mp4">\s*</video>',
    '<video class="hero-video" autoplay muted loop playsinline>\n    <source src="assets/showreel.mp4" type="video/mp4">\n  </video>',
    html
)

# 2. Hero CTA addition
if 'Watch Our Reel' not in html:
    html = html.replace(
        '<a href="#contact" class="btn-primary">Contact Us</a>',
        '<a href="#contact" class="btn-primary">Contact Us</a>\n      <button class="btn-secondary" onclick="openVideoModal(\'dQw4w9WgXcQ\', \'Showreel\')">Watch Our Reel</button>'
    )

# 3. Stats section
html = html.replace('<span class="stat-num" data-count="150" data-suffix="+">0</span>', '<span class="stat-num" data-count="50" data-suffix="+">0</span>')
html = html.replace('<span class="stat-num" data-count="50" data-suffix="M+">0</span>', '<span class="stat-num" data-count="2" data-suffix="M+">0</span>')
# 98 is already 98
html = html.replace('<span class="stat-num" data-count="24" data-suffix="hr">0</span>', '<span class="stat-num" data-count="48" data-suffix="hr">0</span>')

# 4. Portfolio grid
html = html.replace('class="portfolio-scroll"', 'class="portfolio-grid"')

# 5. Services Icons
services_map = {
    '🎬': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect></svg>',
    '📢': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l18-5v12L3 14v-3z"></path><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"></path></svg>',
    '🤖': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>',
    '✨': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    '🔥': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>',
    '🏠': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>'
}
for emoji, svg in services_map.items():
    html = html.replace(f'<span class="service-icon">{emoji}</span>', f'<span class="service-icon">{svg}</span>')

# 6. Testimonials Section
testimonials_html = """
<!-- TESTIMONIALS -->
<section class="testimonials" id="testimonials">
  <div class="container">
    <p class="section-label reveal">Client Love</p>
    <h2 class="section-title reveal reveal-delay-1">Testimonials</h2>
    <div class="testimonials-grid">
      <div class="testimonial-card reveal">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-quote">"MOTIONNODEEDITS completely transformed our ad campaigns. The AI integrations allowed us to scale content faster than ever without losing that premium cinematic feel."</p>
        <div class="testimonial-author">
          <span class="testimonial-name">Sarah Jenkins</span>
          <span class="testimonial-company">CMO, TechNova</span>
        </div>
      </div>
      <div class="testimonial-card reveal reveal-delay-1">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-quote">"The 48-hour turnaround time is no joke. They delivered a breathtaking real estate showcase that helped us close a $4M property in days."</p>
        <div class="testimonial-author">
          <span class="testimonial-name">Marcus Cole</span>
          <span class="testimonial-company">Luxury Estates Group</span>
        </div>
      </div>
      <div class="testimonial-card reveal reveal-delay-2">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-quote">"Their AI avatar videos are indistinguishable from real human presenters. It gave our corporate training an entirely new, engaging dimension."</p>
        <div class="testimonial-author">
          <span class="testimonial-name">David L.</span>
          <span class="testimonial-company">HR Director, Apex</span>
        </div>
      </div>
    </div>
  </div>
</section>
"""

if 'class="testimonials"' not in html:
    html = html.replace('</section>\n\n<!-- PROCESS -->', '</section>\n' + testimonials_html + '\n<!-- PROCESS -->')


# 7. CTA Section
cta_html = """
<!-- NEW CTA SECTION -->
<section class="cta-section" id="cta">
  <div class="cta-glow"></div>
  <div class="container">
    <div class="cta-content reveal">
      <h2>Ready to Dominate?</h2>
      <a href="https://calendly.com/" target="_blank" class="btn-primary">Book a Free Strategy Call</a>
    </div>
  </div>
</section>
"""

if 'class="cta-section"' not in html:
    html = html.replace('</section>\n\n<!-- FOOTER -->', '</section>\n' + cta_html + '\n<!-- FOOTER -->')


# 8. Footer Youtube link
html = html.replace('youtube.com/@motionnodeedtis', 'youtube.com/@motionnodeedits')

# 9. EmailJS Script
emailjs_script = '<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>'
if 'emailjs/browser' not in html:
    html = html.replace('</head>', f'  {emailjs_script}\n</head>')

# Ensure id="contactForm" on the form
html = html.replace('<form class="contact-form reveal reveal-delay-2">', '<form id="contactForm" class="contact-form reveal reveal-delay-2">')
html = html.replace('<input type="text" placeholder="Your name">', '<input type="text" name="user_name" placeholder="Your name" required>')
html = html.replace('<input type="email" placeholder="your@email.com">', '<input type="email" name="user_email" placeholder="your@email.com" required>')
html = html.replace('<textarea rows="5" placeholder="Your message..."></textarea>', '<textarea rows="5" name="message" placeholder="Your message..." required></textarea>')


with open('index.html', 'w') as f:
    f.write(html)

print("HTML updated successfully")
