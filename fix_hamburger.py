import glob

def fix_hamburger():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changed = False
        
        # Remove flex-nowrap from container-fluid (this breaks the collapse)
        if 'container-fluid flex-nowrap' in content:
            content = content.replace('container-fluid flex-nowrap', 'container-fluid')
            changed = True
        
        if changed:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Fixed: {file}')
        else:
            print(f'Skipped (no change needed): {file}')

if __name__ == '__main__':
    fix_hamburger()
