import re

file_path = 'credentials.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add d-flex flex-column to the regular cards
content = content.replace(
    'class="card bg-surface border-0 h-100 text-center p-4 rounded-4 shadow-sm"',
    'class="card bg-surface border-0 h-100 text-center p-4 rounded-4 shadow-sm d-flex flex-column"'
)

# Add d-flex flex-column to the elite card
content = content.replace(
    'class="card bg-surface border-secondary border h-100 text-center p-4 rounded-4 shadow-sm position-relative"',
    'class="card bg-surface border-secondary border h-100 text-center p-4 rounded-4 shadow-sm position-relative d-flex flex-column"'
)

# Add mt-auto to the prerequisite badges
content = content.replace(
    '<span class="badge bg-dark text-white p-2">',
    '<span class="badge bg-dark text-white p-2 mt-auto">'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed alignment in credentials.html")
