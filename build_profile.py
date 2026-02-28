import json
import os
import urllib.parse
import time

def build_readme():
    config_path = 'profile_config.json'
    template_path = 'README.template.md'
    output_path = 'README.md'

    if not os.path.exists(config_path) or not os.path.exists(template_path):
        print("Missing config or template file.")
        return

    with open(config_path, 'r') as f:
        config = json.load(f)

    data = {}
    
    # Add cache bust
    data['cache_bust'] = str(int(time.time()))
    
    # User section - URL encode values potentially used in URLs
    for k, v in config.get('user', {}).items():
        encoded_val = urllib.parse.quote(str(v))
        data[f'user_{k}'] = v
        data[f'user_{k}_url'] = encoded_val
    
    # Theme section
    for k, v in config.get('theme', {}).items():
        data[f'theme_{k}'] = v
        
    # Widgets section
    for k, v in config.get('widgets', {}).items():
        data[f'widget_{k}'] = v

    # Current Focus - convert list to markdown list
    focus_list = config.get('current_focus', [])
    data['current_focus'] = "\n".join([f">  {item}" for item in focus_list])

    # Tech Arsenal - flatten nested dict
    tech = config.get('tech_arsenal', {})
    for k, v in tech.items():
        data[f'tech_{k}'] = v

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    output_content = template_content
    for key, value in data.items():
        placeholder = f"{{{{ {key} }}}}"
        output_content = output_content.replace(placeholder, str(value))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_content)

    print("README.md built successfully with advanced configuration.")

if __name__ == "__main__":
    build_readme()
