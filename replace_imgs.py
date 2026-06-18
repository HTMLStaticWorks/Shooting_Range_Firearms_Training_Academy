import re

files = [
    "index.html",
    "courses.html",
    "gallery.html"
]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Instructor Card
    content = re.sub(
        r'<div class="glass-panel p-5 h-100 military-card border-0">\s*<i class="bi bi-person-badge fs-1 mb-4" style="color: var\(--secondary-color\);"></i>\s*<h3 class="h4 mb-3">Certified Instructors</h3>\s*<p class="text-white-50">(.*?)</p>\s*</div>',
        r'''<div class="glass-panel h-100 military-card border-0 overflow-hidden d-flex flex-column">
                        <img src="assets/images/instructor.png" alt="Certified Instructors" class="w-100" style="height: 220px; object-fit: cover;">
                        <div class="p-4 flex-grow-1">
                            <i class="bi bi-person-badge fs-2 mb-3" style="color: var(--secondary-color);"></i>
                            <h3 class="h4 mb-3">Certified Instructors</h3>
                            <p class="text-white-50">\1</p>
                        </div>
                    </div>''',
        content,
        flags=re.DOTALL
    )

    # Facilities Card
    content = re.sub(
        r'<div class="glass-panel p-5 h-100 military-card border-0">\s*<i class="bi bi-building fs-1 mb-4" style="color: var\(--secondary-color\);"></i>\s*<h3 class="h4 mb-3">Modern Facilities</h3>\s*<p class="text-white-50">(.*?)</p>\s*</div>',
        r'''<div class="glass-panel h-100 military-card border-0 overflow-hidden d-flex flex-column">
                        <img src="assets/images/facilities.png" alt="Modern Facilities" class="w-100" style="height: 220px; object-fit: cover;">
                        <div class="p-4 flex-grow-1">
                            <i class="bi bi-building fs-2 mb-3" style="color: var(--secondary-color);"></i>
                            <h3 class="h4 mb-3">Modern Facilities</h3>
                            <p class="text-white-50">\1</p>
                        </div>
                    </div>''',
        content,
        flags=re.DOTALL
    )

    # Safety Card
    content = re.sub(
        r'<div class="glass-panel p-5 h-100 military-card border-0">\s*<i class="bi bi-shield-check fs-1 mb-4" style="color: var\(--secondary-color\);"></i>\s*<h3 class="h4 mb-3">Safety-First Culture</h3>\s*<p class="text-white-50">(.*?)</p>\s*</div>',
        r'''<div class="glass-panel h-100 military-card border-0 overflow-hidden d-flex flex-column">
                        <img src="assets/images/safety.png" alt="Safety-First Culture" class="w-100" style="height: 220px; object-fit: cover;">
                        <div class="p-4 flex-grow-1">
                            <i class="bi bi-shield-check fs-2 mb-3" style="color: var(--secondary-color);"></i>
                            <h3 class="h4 mb-3">Safety-First Culture</h3>
                            <p class="text-white-50">\1</p>
                        </div>
                    </div>''',
        content,
        flags=re.DOTALL
    )

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Replacement complete.")
