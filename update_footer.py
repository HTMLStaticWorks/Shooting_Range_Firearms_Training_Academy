import re

# Read gallery.html to get the full footer
with open('gallery.html', 'r', encoding='utf-8') as f:
    gallery_content = f.read()

# Extract footer block from gallery.html
footer_match = re.search(r'<!-- Footer -->\s*<footer class="bg-dark text-white py-5 border-top".*?</footer>', gallery_content, re.DOTALL)
if not footer_match:
    print("Could not find footer in gallery.html")
    exit(1)

full_footer = footer_match.group(0)

# Read contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    contact_content = f.read()

# Extract old footer from contact.html
old_footer_match = re.search(r'<!-- Footer -->\s*<footer class="bg-dark text-white py-5 border-top">.*?</footer>', contact_content, re.DOTALL)
if not old_footer_match:
    print("Could not find footer in contact.html")
    exit(1)

# Replace old footer with full footer
contact_content = contact_content.replace(old_footer_match.group(0), full_footer)

# Write back to contact.html
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_content)

print("Successfully updated footer in contact.html")
