import requests
from scraper.parser import parse_html  # Absolute import
from scraper.save_json import save_json  # Absolute import

def scrape_data():
    """Scrape data from the website and parse it."""
    url = "https://www.peaktreeco.com/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }

    # Requesting data from the website
    response = requests.get(url, headers=headers)

    if response.status_code == 200:  # Check if the request was successful
        # Parse the HTML using the function from parser.py
        parsed_data = parse_html(response.text)

        # Save the parsed data to a JSON file
        save_json(parsed_data)
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_data()