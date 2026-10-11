"""Builds docs/index.html: playable-packer.html wrapped as a complete page for static hosting (GitHub Pages).

playable-packer.html has no doctype, charset or viewport (claude.ai artifacts add them at publish time).
Run after editing it:  python3 make-standalone.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "playable-packer.html")
TARGET = os.path.join(HERE, "docs", "index.html")

with open(SOURCE, encoding="utf-8") as f:
    body = f.read()

page = (
    "<!doctype html>\n"
    '<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    "<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n"
    "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
)

os.makedirs(os.path.dirname(TARGET), exist_ok=True)
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(page)
print("Wrote", os.path.relpath(TARGET, os.getcwd()))
