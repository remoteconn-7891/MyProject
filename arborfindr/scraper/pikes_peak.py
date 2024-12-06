from selenium.webdriver.chrome.service import Service # manages Chrome Webdriver service
from selenium.webdriver.chrome.options import Options # Allows setting Chrome options, like headless mode
from selenium import webdriver # provides Webdriver for controlling the browser
from webdriver_manager.chrome import ChromeDriverManager # automatically downloads the ChromeDriver

# set up Webdriver options

options = Options()
options.headless = True # runs Chrome in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_peaktreeco():
    driver.get("https://www.peaktreeco.com/") # sends GET request to specified url

    # extract company name for the home page
    company_name = driver.title.split(" | ")[0] # split the page to get company name before "|"

    # set default location of company
    location = "Colorado Springs, CO" if "Peak Tree" in company_name else "Location not found"

    # extract services offered by the company
    try:
        services_elements = driver.execute_script(
            '''
            let services = Array.from(document.querySelectorAll('li[role="menuitem"] > a > span.nav-item-text'));
            return services.map(el => el.innerText);
            '''
        )

        # uses JavaScript to get all service items in navigation menu
        # 'Array.from' creates an array from the elements selected by 'querySelectorAll'
        # 'map' iterates over each element & extracts the text inside ('innerText')

        # excludes unnecessary items from the services list
        exclude_items = {"Home", "Request an Estimate", "Gallery", "About", "Contact"} # exclude texts

        # use list comprehension to keep only services that are not excluded
        filtered_services = [service for service in services_elements if service not in exclude_items]

        # joins the filtered services into one string separated by commas
        services = ", ".join(filtered_services) if filtered_services else "Services not found"
    except Exception:
        # exception in case of error
        services = "services not found"

        # since it is items, return extracted data as tuple
    return company_name, location, services

def scrape_peaktreeco_reviews():
    # sends GET request to Tree Trimming page where customer review is
    driver.get("https://www.peaktreeco.com/tree-trimming")

    # extracts reviewer's name
    try:
        reviewer_name = driver.execute_script(
            'return document.querySelector("p.tmName")?.innerText || ""'
        )

        # uses JavaScript to select the element with class 'tmName' and return its text content
        # `?.` is optional chaining, which prevents errors if the element isn't found
        # `|| ""` ensures it returns an empty string if the element doesn't exist

    except Exception:
        # exception for any errors
        reviewer_name = "Reviewer name not found"

    # extract review comment (text)

    try:
        review_text = driver.execute_script(
            'return document.querySelector("p.tmBody")?.innerText || ""'
        )

        # targets elements with class 'tmBody' for review comment

    except Exception:
        review_text = "review not found"

    # returns both the reviewer & review text
    return reviewer_name, review_text

# execute the scrapers to scrape data

# company name
peaktreeco_data = scrape_peaktreeco()

# review
peaktreeco_reviews = scrape_peaktreeco_reviews()

# create Python dictionary to convert to JSON and then save in JSON file
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

# prints the results of scraped data
print(f"Peaktreeco.com - {peaktreeco_data[0]}, Location: {peaktreeco_data[1]}, Services: {peaktreeco_data[2]}")
print(f"Peaktreeco Reviews - Reviewer: {peaktreeco_reviews[0]}, Review: {peaktreeco_reviews[1]}")

# close WebDriver session
driver.quit()