import re

with open('js/main.js', 'r') as f:
    js = f.read()

# Fix the broken code block
bad_code = """      a.addEventListener('click', () => {
        ham.classList.remove('active');
        links.classList.remove('open');
      });
      } else { alert('EmailJS not loaded'); btn.textContent = originalText; }
    });"""

good_code = """      a.addEventListener('click', () => {
        ham.classList.remove('active');
        links.classList.remove('open');
      });
    });"""

js = js.replace(bad_code, good_code)

with open('js/main.js', 'w') as f:
    f.write(js)

print("Syntax error fixed")
