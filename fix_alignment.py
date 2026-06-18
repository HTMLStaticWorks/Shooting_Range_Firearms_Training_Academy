import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Make the card a flex column
    content = re.sub(
        r'<div class="military-card p-4 h-100">\s*<div class="d-flex text-warning mb-3">',
        r'<div class="military-card p-4 h-100 d-flex flex-column">\n                        <div class="d-flex text-warning mb-3">',
        content
    )
    
    # Make the paragraph grow and the bottom div mt-auto
    content = re.sub(
        r'<p class="fst-italic text-muted mb-4">(.*?)</p>\s*<div class="d-flex align-items-center">\s*<div class="rounded-circle bg-secondary',
        r'<p class="fst-italic text-muted mb-4 flex-grow-1">\1</p>\n                        <div class="d-flex align-items-center mt-auto">\n                            <div class="rounded-circle bg-secondary',
        content,
        flags=re.DOTALL
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Alignment fixed.")
