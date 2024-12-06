import pysolr
import json

# connect to Solr server
solr = pysolr.Solr('http://localhost:8983/solr/core_arbor')

# load & flatten JSON data
with open("pikes_peak.json", "r") as f:
    data = json.load(f)

# extract city and state from location
city,state = data["company"]["location"].split(", ")

# flattens JSON data
document = {
    "company_name": data["company"]["name"], # company name
    "company_city": city, # extracted city from location
    "company_state": state, # extracted state
    "review_by_homeowner": data["review"]["review_text"], # review comment
    "tree_services": ", ".join(data["company"]["services"]), # joins services into single string
}

# index the document
solr.add([document])

print("Document for Pikes Peak successfully indexed")
