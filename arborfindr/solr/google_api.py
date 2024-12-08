import requests
from bs4 import BeautifulSoup

def fetch_additional_info(url):
    """
    Fetch additional data by scraping the given URL.
    :param url: Website URL
    :return: Dictionary with additional info
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example selectors for additional data
        city_state = soup.select_one(".city-state-selector").text if soup.select_one(".city-state-selector") else "N/A"
        types_of_service = [item.text for item in soup.select(".services-selector")] if soup.select(".services-selector") else []
        reviews = [{"reviewer": review.select_one(".reviewer").text,
                    "text": review.select_one(".review-text").text}
                   for review in soup.select(".review-selector")]

        return {
            "city_state": city_state,
            "types_of_service": types_of_service,
            "reviews": reviews
        }
    except Exception as e:
        print(f"Error fetching additional info from {url}: {e}")
        return {
            "city_state": "N/A",
            "types_of_service": [],
            "reviews": []
        }

def process_results(response):
    """
    Processes the JSON response from Google API into a usable format,
    with additional details scraped from the links.
    :param response: JSON response from Google API
    :return: List of processed results
    """
    results = []
    for item in response.get("items", []):
        url = item.get("link")
        additional_info = fetch_additional_info(url)  # Fetch additional data

        results.append({
            "title": item.get("title"),         # Company Name
            "link": url,                        # Website URL
            "description": item.get("snippet"), # Summary or snippet
            "city_state": additional_info["city_state"],  # City/State from the website
            "types_of_service": additional_info["types_of_service"],  # Services
            "reviews": additional_info["reviews"]  # Reviews
        })
    return results


