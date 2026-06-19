import glob

def fix_navbars():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add flex-nowrap to container-fluid
        content = content.replace('<div class="container-fluid">', '<div class="container-fluid flex-nowrap">')
        
        # Add ms-auto to navbar-toggler
        content = content.replace('<button class="navbar-toggler"', '<button class="navbar-toggler ms-auto"')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
if __name__ == '__main__':
    fix_navbars()
    print("Fixed navbars in all HTML files.")
