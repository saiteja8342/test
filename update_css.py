import re

with open('css/style.css', 'r') as f:
    content = f.read()

# Replace font import
content = re.sub(
    r"@import url\('https://fonts.googleapis.com/css2\?.*?'\);",
    "@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap');",
    content
)

# Body font
content = content.replace("font-family:'Plus Jakarta Sans',sans-serif;", "font-family:'DM Sans',sans-serif;")

# Headings font
headings_rule = "h1, h2, h3, h4, h5, h6 { font-family: 'Bebas Neue', sans-serif; font-weight: 400; letter-spacing: 2px; text-transform: uppercase; }\n\n"
if "h1, h2, h3, h4, h5, h6" not in content:
    content = content.replace("/* SECTION COMMON */", "/* SECTION COMMON */\n" + headings_rule)

# Remove Plus Jakarta Sans everywhere else and replace with Bebas Neue
content = content.replace("'Plus Jakarta Sans'", "'Bebas Neue'")

# Change portfolio scroll to grid
portfolio_scroll = """.portfolio-scroll { display:flex; gap:24px; overflow-x:auto; padding-bottom:24px; scroll-snap-type:x mandatory; scrollbar-width:none; }
.portfolio-scroll::-webkit-scrollbar { display:none; }
.video-card { flex:0 0 420px; aspect-ratio:9/16; border-radius:20px; overflow:hidden; position:relative; scroll-snap-align:start; cursor:none; border:1px solid var(--border); transition:transform .5s,box-shadow .5s; }"""

portfolio_grid = """.portfolio-grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:24px; padding-bottom:24px; }
@media(max-width: 1024px) { .portfolio-grid { grid-template-columns:repeat(2, 1fr); } }
@media(max-width: 600px) { .portfolio-grid { grid-template-columns:1fr; } }
.video-card { aspect-ratio:16/9; border-radius:20px; overflow:hidden; position:relative; cursor:none; border:1px solid var(--border); transition:transform .5s,box-shadow .5s; background:#111; }
.video-card:hover { z-index: 5; box-shadow: 0 0 40px var(--glow); }
.video-card-thumb { width:100%; height:100%; object-fit:cover; transition:transform .5s; }
.video-card:hover .video-card-thumb { transform:scale(1.05); }"""

content = content.replace(portfolio_scroll, portfolio_grid)

# Also fix the aspect-ratio for video-card if it got changed or wasn't there
if ".video-card { flex:0 0 420px; aspect-ratio:9/16;" in content:
    pass

# Add styles for Testimonials and CTA
new_styles = """

/* TESTIMONIALS */
.testimonials { background:var(--bg); }
.testimonials-grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:24px; max-width:1200px; margin:48px auto 0; }
.testimonial-card { background:var(--glass); backdrop-filter:blur(10px); border:1px solid var(--glass-border); border-radius:20px; padding:32px; display:flex; flex-direction:column; gap:16px; }
.testimonial-stars { color:#fbbf24; font-size:1.2rem; letter-spacing:2px; }
.testimonial-quote { font-family:'DM Sans',sans-serif; font-style:italic; font-size:1.05rem; color:var(--text); line-height:1.6; flex-grow:1; }
.testimonial-author { display:flex; flex-direction:column; gap:4px; margin-top:16px; }
.testimonial-name { font-weight:700; color:var(--text); font-size:1.1rem; text-transform:uppercase; font-family:'Bebas Neue',sans-serif; letter-spacing:1px; }
.testimonial-company { font-size:.85rem; color:var(--text2); text-transform:uppercase; letter-spacing:1px; }
@media(max-width:900px){ .testimonials-grid { grid-template-columns:1fr; } }

/* CTA SECTION */
.cta-section { background:var(--bg2); border-top:1px solid var(--border); text-align:center; position:relative; overflow:hidden; padding:100px 24px; }
.cta-glow { position:absolute; width:800px; height:800px; border-radius:50%; background:radial-gradient(circle, rgba(167,139,250,0.1), transparent 60%); top:50%; left:50%; transform:translate(-50%,-50%); pointer-events:none; }
.cta-content { position:relative; z-index:2; max-width:700px; margin:0 auto; display:flex; flex-direction:column; align-items:center; gap:32px; }
.cta-content h2 { font-size:clamp(3rem, 6vw, 5rem); margin:0; line-height:1; }
"""

if "/* TESTIMONIALS */" not in content:
    content += new_styles

with open('css/style.css', 'w') as f:
    f.write(content)

print("CSS updated successfully")
