import re

file_path = 'gallery.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Video 1 placeholder
video1_old = '''<div class="ratio ratio-16x9 bg-dark d-flex align-items-center justify-content-center text-secondary">
              <div class="text-center">
                <i class="bi bi-play-btn fs-1 text-secondary"></i>
                <p class="small text-muted mt-2 mb-0">Tactical Pistol: Holster Draw & Fire</p>
              </div>
            </div>'''
video1_new = '''<div class="ratio ratio-16x9 bg-dark position-relative overflow-hidden cursor-pointer">
              <img src="assets/images/level2_marksman_1781806289798.png" alt="Video Thumbnail" class="w-100 h-100 object-fit-cover opacity-75">
              <div class="position-absolute top-50 start-50 translate-middle text-center text-white" style="z-index: 2;">
                <i class="bi bi-play-circle-fill" style="font-size: 4rem; text-shadow: 0 4px 8px rgba(0,0,0,0.5);"></i>
              </div>
            </div>'''
content = content.replace(video1_old, video1_new)

# Replace Video 2 placeholder
video2_old = '''<div class="ratio ratio-16x9 bg-dark d-flex align-items-center justify-content-center text-secondary">
              <div class="text-center">
                <i class="bi bi-play-btn fs-1 text-secondary"></i>
                <p class="small text-muted mt-2 mb-0">Carbine Basics: Safety Check & Recoil Control</p>
              </div>
            </div>'''
video2_new = '''<div class="ratio ratio-16x9 bg-dark position-relative overflow-hidden cursor-pointer">
              <img src="assets/images/level4_master_1781806312241.png" alt="Video Thumbnail" class="w-100 h-100 object-fit-cover opacity-75">
              <div class="position-absolute top-50 start-50 translate-middle text-center text-white" style="z-index: 2;">
                <i class="bi bi-play-circle-fill" style="font-size: 4rem; text-shadow: 0 4px 8px rgba(0,0,0,0.5);"></i>
              </div>
            </div>'''
content = content.replace(video2_old, video2_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated video thumbnails in gallery.html")
