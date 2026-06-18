import re

file_path = 'credentials.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Level 1
content = content.replace(
    '<div class="mb-4">\n              <i class="bi bi-shield text-muted" style="font-size: 3rem;"></i>\n            </div>',
    '<div class="mb-4">\n              <img src="assets/images/level1_safety.png" alt="Level I Safety" class="img-fluid rounded-circle shadow-sm" style="width: 100px; height: 100px; object-fit: cover;">\n            </div>'
)

# Replace Level 2
content = content.replace(
    '<div class="mb-4">\n              <i class="bi bi-shield-check text-primary" style="font-size: 3rem;"></i>\n            </div>',
    '<div class="mb-4">\n              <img src="assets/images/level2_marksman.png" alt="Level II Marksman" class="img-fluid rounded-circle shadow-sm" style="width: 100px; height: 100px; object-fit: cover;">\n            </div>'
)

# Replace Level 3
content = content.replace(
    '<div class="mb-4">\n              <i class="bi bi-shield-fill-check text-danger" style="font-size: 3rem;"></i>\n            </div>',
    '<div class="mb-4">\n              <img src="assets/images/level3_tactical.png" alt="Level III Tactical" class="img-fluid rounded-circle shadow-sm" style="width: 100px; height: 100px; object-fit: cover;">\n            </div>'
)

# Replace Level 4
content = content.replace(
    '<div class="mb-4 mt-2">\n              <i class="bi bi-patch-check-fill text-secondary" style="font-size: 3rem;"></i>\n            </div>',
    '<div class="mb-4 mt-2">\n              <img src="assets/images/level4_master.png" alt="Level IV Master" class="img-fluid rounded-circle shadow-sm" style="width: 100px; height: 100px; object-fit: cover;">\n            </div>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated credentials.html with level images")
