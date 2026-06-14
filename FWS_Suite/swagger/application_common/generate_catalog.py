import os
import json
from typing import List, Dict

def generate_catalog(service_dir: str, output_file: str, category_name: str):
    catalog_items = []
    
    if not os.path.exists(service_dir):
        print(f"Directory {service_dir} not found.")
        return

    for filename in os.listdir(service_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(service_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    title = data.get('info', {}).get('title', filename)
                    summary = data.get('info', {}).get('x-summary', 'No summary available.')
                    
                    # Extract the first path to get the resource name
                    paths = data.get('paths', {})
                    base_path = next(iter(paths)) if paths else "N/A"
                    
                    catalog_items.append({
                        "name": filename.replace(".json", ""),
                        "title": title,
                        "summary": summary,
                        "base_path": base_path
                    })
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Write to Markdown
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {category_name} Service Catalog\n\n")
        f.write("| Service Name | Title | Summary | Base Path |\n")
        f.write("|--------------|-------|---------|-----------|\n")
        for item in sorted(catalog_items, key=lambda x: x['name']):
            f.write(f"| {item['name']} | {item['title']} | {item['summary']} | `{item['base_path']}` |\n")

if __name__ == "__main__":
    
    # Generate Common Catalog
    generate_catalog(
        "D:/HRD_TechCarrot_2/MasterAISuite/FusionWebServices/swagger/application_common/services",
        "D:/HRD_TechCarrot_2/MasterAISuite/FusionWebServices/swagger/application_common/common_catalog.md",
        "Fusion Applicatoin Common"
    )
