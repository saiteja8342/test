import re

with open('js/main.js', 'r') as f:
    js = f.read()

# Limit defaultPortfolio to 6 items
# The easiest way is to modify the getPortfolio function
js = js.replace('return saved ? JSON.parse(saved) : defaultPortfolio;', 'return saved ? JSON.parse(saved) : defaultPortfolio.slice(0, 6);')

# Add EmailJS setup inside DOMContentLoaded
email_js_code = """
  // Contact Form Setup with EmailJS
  emailjs.init({ publicKey: 'YOUR_PUBLIC_KEY' });
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const btn = this.querySelector('button[type="submit"]');
      const originalText = btn.textContent;
      btn.textContent = 'Sending...';
      
      emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
        .then(() => {
            btn.textContent = 'Message Sent!';
            this.reset();
            setTimeout(() => btn.textContent = originalText, 3000);
        }, (error) => {
            console.error('FAILED...', error);
            btn.textContent = 'Failed to Send (Check Keys)';
            setTimeout(() => btn.textContent = originalText, 3000);
        });
    });
  }
"""

if 'emailjs.init' not in js:
    js = js.replace("initLenis();\n", "initLenis();\n" + email_js_code)


with open('js/main.js', 'w') as f:
    f.write(js)

print("JS updated successfully")
