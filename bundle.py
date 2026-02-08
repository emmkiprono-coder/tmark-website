#!/usr/bin/env python3
"""
bundle.py – Reads index.html, css/style.css, and js/main.js, then produces
a single self-contained HTML file (tmark-bundled.html) with CSS and JS inlined.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Read source files ---
with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

with open(os.path.join(BASE_DIR, "css", "style.css"), "r", encoding="utf-8") as f:
    css = f.read()

with open(os.path.join(BASE_DIR, "js", "main.js"), "r", encoding="utf-8") as f:
    js = f.read()

# --- Inline the CSS ---
css_link = '<link rel="stylesheet" href="css/style.css">'
css_inline = f"<style>\n{css}\n    </style>"
html = html.replace(css_link, css_inline, 1)

# --- Inline the JS ---
js_link = '<script src="js/main.js"></script>'
js_inline = f"<script>\n{js}\n    </script>"
html = html.replace(js_link, js_inline, 1)

# --- Write bundled output ---
out_path = os.path.join(BASE_DIR, "tmark-bundled.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Bundled file written to: {out_path}")
