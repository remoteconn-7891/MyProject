
from selenium.webdriver.chrome.service import Service  # Manages the Chrome WebDriver service.
from selenium.webdriver.chrome.options import Options  # Allows setting Chrome options, like headless mode.
from selenium import webdriver  # Provides WebDriver for controlling the browser.
from webdriver_manager.chrome import ChromeDriverManager  # Automatically downloads the ChromeDriver.

# Setup WebDriver options
options = Options()
options.headless = True  # Runs Chrome in headless mode (without opening a browser window).
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_peaktreeco():
    driver.get("https://www.peaktreeco.com/")  # Opens the specified URL in the browser.

    # Extract company name from the page title
    company_name = driver.title.split(" | ")[0]  # Splits the page title to get the company name before "|".

    # Set a default location based on the company name
    location = "Colorado Springs, CO" if "Peak Tree" in company_name else "Location not found"

    # Extract services offered by the company
    try:
        services_elements = driver.execute_script(
            '''
            let services = Array.from(document.querySelectorAll('li[role="menuitem"] > a > span.nav-item-text'));
            return services.map(el => el.innerText);
            '''
        )
        # Uses JavaScript to get all service items in the navigation menu.
        # `Array.from` creates an array from the elements selected by `querySelectorAll`.
        # `map` iterates over each element and extracts the text inside (`innerText`).

        # Exclude unwanted items from the services list
        exclude_items = {"Home", "Request an Estimate", "Gallery", "About", "Contact"}  # Services to exclude.
        filtered_services = [service for service in services_elements if service not in exclude_items]
        # List comprehension that keeps only services not in the exclude_items set.

        services = ", ".join(filtered_services) if filtered_services else "Services not found"
        # Joins the filtered services into a single string separated by commas.
    except Exception:
        services = "Services not found"  # Fallback in case of an error.

    return company_name, location, services  # Returns extracted data as a tuple.

def scrape_peaktreeco_reviews():
    driver.get("https://www.peaktreeco.com/tree-trimming")  # Opens the reviews page.

    # Extract the reviewer's name
    try:
        reviewer_name = driver.execute_script(
            'return document.querySelector("p.tmName")?.innerText || ""'
        )
        # Uses JavaScript to select the element with class `tmName` and return its text content.
        # `?.` is optional chaining, which prevents errors if the element is not found.
        # `|| ""` ensures it returns an empty string if the element doesn't exist.
    except Exception:
        reviewer_name = "Reviewer name not found"  # Fallback for any errors.

    # Extract the review text
    try:
        review_text = driver.execute_script(
            'return document.querySelector("p.tmBody")?.innerText || ""'
        )
        # Similar to the above, but targets the element with class `tmBody` for the review content.
    except Exception:
        review_text = "Review text not found"  # Fallback in case of an error.

    return reviewer_name, review_text  # Returns the reviewer's name and review text.

# Execute the scrapers
peaktreeco_data = scrape_peaktreeco()  # Scrapes company data.
peaktreeco_reviews = scrape_peaktreeco_reviews()  # Scrapes review data.

# create Python dictionary for scraped Pikes Peak Service
scraped_data = {
    "company": {
        "name": peaktreeco_data[0],
        "location": peaktreeco_data[1],
        "services": peaktreeco_data[2].split(", ")
    },
    "review": {
        "reviewer": peaktreeco_reviews[0],
        "review_text": peaktreeco_reviews[1]
    }
}

# Print the results in a readable format
print(f"Peaktreeco.com - Company: {peaktreeco_data[0]}, Location: {peaktreeco_data[1]}, Services: {peaktreeco_data[2]}")
print(f"Peaktreeco Reviews - Reviewer: {peaktreeco_reviews[0]}, Review: {peaktreeco_reviews[1]}")

# Close the WebDriver session
driver.quit()

