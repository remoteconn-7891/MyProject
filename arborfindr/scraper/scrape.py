from scraper.save_json import save_json
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_peaktreeco():
    driver.get("https://www.peaktreeco.com/")

    # Company Name and Location
    company_name = driver.title.split(" | ")[0]
    location = "Colorado Springs, CO" if "Peak Tree" in company_name else "Location not found"

    # Services
    try:
        services_elements = driver.execute_script(
            '''
            let services = Array.from(document.querySelectorAll('li[role="menuitem"] > a > span.nav-item-text'));
            return services.map(el => el.innerText).join(", ");
            '''
        )
        services = services_elements if services_elements else "Services not found"
    except Exception:
        services = "Services not found"

    return company_name, location, services

def scrape_peaktreeco_reviews():
    driver.get("https://www.peaktreeco.com/tree-trimming")

    # Reviewer Name
    try:
        reviewer_name = driver.execute_script(
            'return document.querySelector("p.tmName")?.innerText || ""'
        )
    except Exception:
        reviewer_name = "Reviewer name not found"

    # Review Text
    try:
        review_text = driver.execute_script(
            'return document.querySelector("p.tmBody")?.innerText || ""'
        )
    except Exception:
        review_text = "Review text not found"

    return reviewer_name, review_text

# Execute the scrapers
peaktreeco_data = scrape_peaktreeco()
peaktreeco_reviews = scrape_peaktreeco_reviews()

# Print the results

print(f"Peaktreeco.com - Company: {peaktreeco_data[0]}, Location: {peaktreeco_data[1]}, Services: {peaktreeco_data[2]}")
print(f"Peaktreeco Reviews - Reviewer: {peaktreeco_reviews[0]}, Review: {peaktreeco_reviews[1]}")

# Close the driver
driver.quit()
