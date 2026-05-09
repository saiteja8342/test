import re

with open('js/main.js', 'r') as f:
    js = f.read()

js = js.replace("emailjs.init({ publicKey: 'YOUR_PUBLIC_KEY' });", "if (typeof emailjs !== 'undefined') { emailjs.init({ publicKey: 'YOUR_PUBLIC_KEY' }); }")
js = js.replace("emailjs.sendForm(", "if (typeof emailjs !== 'undefined') { emailjs.sendForm(")
js = js.replace("});\n    });", "});\n      } else { alert('EmailJS not loaded'); btn.textContent = originalText; }\n    });")

with open('js/main.js', 'w') as f:
    f.write(js)

