import re, os, json
html = open("C:/Users/user/Documents/Landings/Smart/index.html", encoding="utf-8").read()

# 1. Remove all "SmartPrint" / "Smart" references (case insensitive) from visible text
# but keep the canonical URL and og:image - those are meta tags that should stay
# Actually the task says "remove all mention of Smart print" - let's be thorough

# Remove from title, h1, buttons, links text that say SmartPrint
# But keep the og:url and canonical - those are branding

# Let's just remove the word "SmartPrint" from visible UI text while keeping structure
# We'll replace occurrences but keep the domain references in meta tags

# First, let's find all occurrences
import html as html_mod
from html import escape

# Strategy: Replace "SmartPrint" in text content but preserve meta tags
# We'll do a careful replacement

output = html
# Remove from title
output = re.sub(r'(?i)<title>.*?</title>', '<title>PDV para Gráfica Rápida | Calculadora de Preço por m²</title>', output)
# Remove from og tags (but keep the domain - actually the task says remove all mention)
# Actually the task says "remova toda mencao de Smart print" - so remove everything

# Remove all og and twitter tags that reference smartprint
output = re.sub(r'(?i)<meta property="og:url" content="https?://www\\.smartprint\\.br"[^>]*>', '', output)
output = re.sub(r'(?i)<meta property="og:title" content="[^"]*SmartPrint[^"]*"[^>]*>', '', output)
output = re.sub(r'(?i)<meta property="og:description" content="[^"]*SmartPrint[^"]*"[^>]*>', '', output)
output = re.sub(r'(?i)<meta name="author" content="SmartPrint"[^>]*>', '', output)
output = re.sub(r'(?i)<meta name="keywords" content="[^"]*Smart[^"]*"[^>]*>', '', output)

# Remove "SmartPrint" from visible text but keep the structure
# Replace "SmartPrint" in anchor texts, spans, etc
output = re.sub(r'(?i)SmartPrint', 'Smart', output)

# Remove "smartprint.com.br" references from hrefs that are just tracking
# But keep the canonical - actually let's remove those too per the task
output = re.sub(r'(?i)https?://www\\.smartprint\\.br[^"\s>]*', '', output)

# Remove "Smart" from the eyebrow and other text
output = re.sub(r'(?i)Smart', 'PDV', output)

# Remove the logo text in footer
output = re.sub(r'(?i)SmartPrint', 'Smart', output)
output = re.sub(r'(?i)smartprint', 'smart', output)

# Save
with open("C:/Users/user/Documents/Landings/Smart/index_clean.html", "w", encoding="utf-8") as f:
    f.write(output)
print("saved index_clean.html")
