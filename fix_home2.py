import re

file_path = "home-2.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the Unsplash link
content = content.replace(
    'https://images.unsplash.com/photo-1595590424283-b8f17842773f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
    'assets/images/beginner_fundamentals.png'
)

# Add z-index: 0 to hero-section to create a stacking context
content = content.replace(
    '<section class="hero-section vh-100 position-relative overflow-hidden">',
    '<section class="hero-section vh-100 position-relative overflow-hidden" style="z-index: 0;">'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed home-2.html")
