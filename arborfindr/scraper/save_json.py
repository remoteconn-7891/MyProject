import json
import os

# saved scraped/parsed data to JSON file
def save_json(data, filename='data.json'):

    # verifying directory for JSON file
    output_dir = os.path.join('C:', 'Users', 'corey james', 'Documents', 'CJProjects', 'treesbegone', 'data')

    os.makedirs(output_dir, exist_ok=True)

    # show full path
    file_path = os.path.join(output_dir,filename)

    # open the JSON file in write mode and save the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"data saved to {file_path}")