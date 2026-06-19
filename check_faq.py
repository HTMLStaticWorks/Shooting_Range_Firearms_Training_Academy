import glob, re
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(r'<button class="accordion-button.*?>(.*?)</button>', content, re.DOTALL)
    if matches:
        print(f'--- {file} ---')
        for m in matches:
            print(m.strip())
