import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Add d-flex flex-column to card-body in the Events section
    # The signature is:
    # <div class="card bg-color border border-secondary h-100">
    #     <div class="card-header bg-dark text-center border-bottom border-secondary py-3">
    # ...
    #     <div class="card-body p-4 text-center">
    
    content = re.sub(
        r'<div class="card-body p-4 text-center">',
        r'<div class="card-body p-4 text-center d-flex flex-column">',
        content
    )
    
    # Step 2: Add mt-auto to the button
    content = re.sub(
        r'<a href="#" class="btn btn-sm btn-secondary w-100">(Register Now|Join Waitlist)</a>',
        r'<a href="#" class="btn btn-sm btn-secondary w-100 mt-auto">\1</a>',
        content
    )

    # Note: wait, what if "card-body p-4 text-center" is used somewhere else?
    # Let's ensure the <p> tag also gets flex-grow-1 just in case, or we can leave it as mt-auto on the button pushes it to the bottom.

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Events alignment fixed.")
