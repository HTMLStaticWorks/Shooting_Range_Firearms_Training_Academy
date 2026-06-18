import re

file_path = 'facilities.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Rental 1
content = content.replace(
    '<img src="https://images.unsplash.com/photo-1595590424283-b8f17842773f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Rental 1"',
    '<img src="assets/images/rental1.png" alt="Rental 1"'
)

# Replace Rental 2
content = content.replace(
    '<img src="https://images.unsplash.com/photo-1584283866205-0810db338a06?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Rental 2"',
    '<img src="assets/images/competition_skills.png" alt="Rental 2"'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated rentals images in facilities.html")
