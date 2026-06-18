import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The broken Unsplash base URL
broken_base = 'https://images.unsplash.com/photo-1544490412-dc2ec29a65ee'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if broken_base in content:
        # Replace the parallax version (with w=1920)
        content = re.sub(
            r'https://images\.unsplash\.com/photo-1544490412-dc2ec29a65ee\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=1920&q=80',
            'assets/images/parallax_bg.png',
            content
        )
        
        # Replace the remaining standard img tag versions
        content = re.sub(
            r'https://images\.unsplash\.com/photo-1544490412-dc2ec29a65ee\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=\d+&q=80',
            'assets/images/certified_facility.png',
            content
        )

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")

print("All broken Facility image links replaced.")
