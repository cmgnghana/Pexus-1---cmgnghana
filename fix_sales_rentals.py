import os
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Generic replaces
    content = content.replace("Car Rental", "")
    content = content.replace("Vehicle Sales", "")
    content = content.replace("Rentals", "")
    content = content.replace("rentals", "")
    content = content.replace("vehicle sales", "")
    content = content.replace("Vehicle sales", "")
    content = content.replace("Car Rentals", "")
    content = content.replace("car rentals", "")
    content = content.replace("car sales", "")

    # Write back
    with open(filepath, 'w') as f:
        f.write(content)

for root, dirs, files in os.walk('src'):
    for file in files:
        if file.endswith('.tsx') or file.endswith('.ts'):
            process_file(os.path.join(root, file))

