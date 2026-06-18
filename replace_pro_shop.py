import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_url = 'https://images.unsplash.com/photo-1584283866205-0810db338a06?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
new_url = 'assets/images/pro_shop.png'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_url in content:
        content = content.replace(old_url, new_url)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Replacement complete.")
