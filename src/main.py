import os
import shutil
from static_site import generate_pages_recursive


def main():
    # Clear public directory
    if os.path.exists('public'):
        shutil.rmtree('public')
    
    # Create public directory
    os.makedirs('public', exist_ok=True)

    # Copy static files
    if os.path.exists('static'):
        for item in os.listdir('static'):
            source = os.path.join('static', item)
            dest = os.path.join('public', item)
            if os.path.isfile(source):
                shutil.copy2(source, dest)
            else:
                shutil.copytree(source, dest)

    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == '__main__':
    main()