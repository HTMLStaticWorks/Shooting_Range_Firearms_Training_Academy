import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

scripts_block = """
  <!-- GSAP & AOS Scripts -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  
  <!-- Custom Scripts -->
  <script src="js/main.js"></script>
  <script src="js/animations.js"></script>
</body>
</html>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if "</body>" not in content and "</html>" not in content and "<script" not in content[-300:]:
        print(f"Fixing {file}...")
        # Make sure the file ends correctly
        content = content.strip()
        if content.endswith('</footer>'):
            content += "\n" + scripts_block
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done checking all files.")
