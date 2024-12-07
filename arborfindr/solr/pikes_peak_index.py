import pysolr
import json

# Connect to Solr server
solr = pysolr.Solr('http://localhost:8983/solr/core_arbor')

# Absolute path to the JSON file
JSON_FILE_PATH = r"C:\Users\corey james\Documents\CJProjects\treesbegone\NewProject\arborfindr\scraper\pikes_peak.json"

print("Looking for JSON file at:", JSON_FILE_PATH)

try:
    # Load and flatten JSON data
    with open(JSON_FILE_PATH, "r") as f:
        data = json.load(f)

    # Extract city and state from location
    city, state = data["company"]["location"].split(", ")

    # Flatten JSON data
    document = {
        "company_name": data["company"]["name"],  # company name
        "company_city": city,                     # extracted city from location
        "company_state": state,                   # extracted state
        "review_by_homeowner": data["review"]["review_text"],  # review comment
        "tree_services": ", ".join(data["company"]["services"]),  # joins services into single string
    }

    # Index the document
    solr.add([document])
    print("Document for Pikes Peak successfully indexed")

except FileNotFoundError:
    print(f"File not found: {JSON_FILE_PATH}")
except Exception as e:
    print(f"An error occurred: {e}")


