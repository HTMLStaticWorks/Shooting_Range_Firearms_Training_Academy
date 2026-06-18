import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The HTML has: <button class="accordion-button collapsed bg-surface text-white shadow-none" ...>
    # or <button class="accordion-button bg-surface text-white shadow-none" ...>
    content = re.sub(
        r'class="accordion-button (.*?)text-white',
        r'class="accordion-button \1',
        content
    )
    # in case it's at the end or has multiple spaces
    content = content.replace('  ', ' ').replace(' shadow-none"', ' shadow-none"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("FAQ text color fixed in HTML.")
