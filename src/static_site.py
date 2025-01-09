import os
import shutil
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    """
    Extract the h1 header from a markdown file.
    Args:
        markdown (str): The markdown content
    Returns:
        str: The title without the # and whitespace
    Raises:
        ValueError: If no h1 header is found
    """
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("No h1 header found in markdown content")

def generate_page(from_path, template_path, dest_path):
    """
    Generate an HTML page from markdown content and a template.
    Args:
        from_path (str): Path to the markdown file
        template_path (str): Path to the HTML template
        dest_path (str): Path where the generated HTML should be saved
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown content
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Read template
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Replace placeholders
    final_html = template_content.replace('{{ Title }}', title)
    final_html = final_html.replace('{{ Content }}', html_content)
    
    # Create destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the output
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Generate HTML pages from markdown files in a directory and its subdirectories.
    Args:
        dir_path_content (str): Path to the directory containing markdown files
        template_path (str): Path to the HTML template
        dest_dir_path (str): Path to the directory where the generated HTML should be saved
    """
    for item in os.listdir(dir_path_content):
        full_item_path = os.path.join(dir_path_content, item)
        full_dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(full_item_path):
            if full_item_path.endswith('.md'):
                generate_page(full_item_path, template_path, full_dest_path[:-3] + '.html')
        else:
            generate_pages_recursive(full_item_path, template_path, full_dest_path)