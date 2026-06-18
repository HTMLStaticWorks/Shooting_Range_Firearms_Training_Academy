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

# Read signup.html
with open('signup.html', 'r', encoding='utf-8') as f:
    signup_content = f.read()

# Extract old footer from signup.html
old_footer_match = re.search(r'<!-- Footer -->\s*<footer class="bg-dark text-white py-5 border-top">.*?</footer>', signup_content, re.DOTALL)
if not old_footer_match:
    print("Could not find footer in signup.html")
    exit(1)

# Replace old footer with full footer
signup_content = signup_content.replace(old_footer_match.group(0), full_footer)

# Write back to signup.html
with open('signup.html', 'w', encoding='utf-8') as f:
    f.write(signup_content)

print("Successfully updated footer in signup.html")
