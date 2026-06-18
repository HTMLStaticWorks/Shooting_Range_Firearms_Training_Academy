import re

file_path = 'facilities.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Indoor Range placeholder
content = content.replace(
    '<div class="ratio ratio-16x9 bg-dark rounded-4 shadow-sm d-flex align-items-center justify-content-center text-muted">\n            <i class="bi bi-bullseye" style="font-size: 4rem;"></i>\n          </div>',
    '<div class="ratio ratio-16x9 bg-dark rounded-4 shadow-sm overflow-hidden">\n            <img src="assets/images/indoor_range.png" alt="25-Yard Indoor Range" class="w-100 h-100 object-fit-cover">\n          </div>'
)

# Replace Outdoor Range placeholder
content = content.replace(
    '<div class="ratio ratio-16x9 bg-dark rounded-4 shadow-sm d-flex align-items-center justify-content-center text-muted">\n            <i class="bi bi-tree" style="font-size: 4rem;"></i>\n          </div>',
    '<div class="ratio ratio-16x9 bg-dark rounded-4 shadow-sm overflow-hidden">\n            <img src="assets/images/outdoor_range.png" alt="100-Yard Outdoor Tactical Bay" class="w-100 h-100 object-fit-cover">\n          </div>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated facilities.html with range images")
