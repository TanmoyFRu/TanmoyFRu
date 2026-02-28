import json
import os

def build_readme():
    config_path = 'profile_config.json'
    template_path = 'README.template.md'
    output_path = 'README.md'

    # Ensure config and template exist
    if not os.path.exists(config_path) or not os.path.exists(template_path):
        print("Missing config or template file.")
        return

    # Load configuration
    with open(config_path, 'r') as f:
        config = json.load(f)

    data = {}
    
    # User section
    for k, v in config.get('user', {}).items():
        data[f'user_{k}'] = v
    
    # Theme section
    for k, v in config.get('theme', {}).items():
        data[f'theme_{k}'] = v
        
    # Widgets section
    for k, v in config.get('widgets', {}).items():
        data[f'widget_{k}'] = v

    # Load template
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Replace placeholders correctly
    # Placeholders are in format {{ user_name }}, {{ theme_primary_color }}, etc.
    output_content = template_content
    for key, value in data.items():
        placeholder = f"{{{{ {key} }}}}"
        output_content = output_content.replace(placeholder, str(value))

    # Write to README.md
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_content)

    print("README.md built successfully from config and template.")

if __name__ == "__main__":
    build_readme()
