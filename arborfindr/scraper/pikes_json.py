import json

from scraper.pikes_peak import scraped_data

# serialize json
pikes_obj = json.dumps(scraped_data, indent=4)

with open("pikes_peak.json", "w") as outfile:
    outfile.write(pikes_obj)



