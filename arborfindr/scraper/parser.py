from bs4 import BeautifulSoup
import re
import json

def parse_html(html):
    """Parse the HTML content using BeautifulSoup and extract desired information."""

    soup = BeautifulSoup(html, 'html.parser')

    # Extract company name from meta description
    meta_descrip = soup.find('meta', attrs={'name': 'description'})
    company_name = 'Company unknown'  # Default value

    if meta_descrip:
        description = meta_descrip.get('content', '')
        print(f"Meta Description: {description}")

        # Attempt to find company name in description
        match = re.search(r'([A-Za-z\s]+ Tree Service)', description)
        if match:
            company_name = match.group(0)

    # Extract services (assuming services are in a <ul> with role="menu")
    services = []
    service_items = soup.find('ul', role="menu")

    if service_items:
        service_items = service_items.find_all('li', role='menuitem')
        for service in service_items:
            service_name = service.find('a').text.strip()
            services.append(service_name)

    # Extract location (city and state) from <script> tag with type="application/ld+json"
    location = {}
    script_tag = soup.find('script', type='application/ld+json')
    if script_tag:
        try:
            # Extract JSON data from the script tag
            json_data = json.loads(script_tag.string)  # Parse the JSON string in the script tag

            if isinstance(json_data, list):
                for item in json_data:
                    if 'address' in item and 'addressLocality' in item['address']:
                        city = item['address']['addressLocality']
                        state = item['address']['addressRegion']
                        location = {'city': city, 'state': state}
                        print(f"Location: {city}, {state}")
            elif isinstance(json_data, dict) and 'address' in json_data:
                city = json_data['address']['addressLocality']
                state = json_data['address']['addressRegion']
                location = {'city': city, 'state': state}
                print(f"Location: {city}, {state}")
        except json.JSONDecodeError:
            print("Error parsing JSON from <script> tag")

    # Return parsed data including company name, services, and location
    return {
        'company_name': company_name,
        'services': services,
        'location': location
    }


