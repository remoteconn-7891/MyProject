from selenium.webdriver.chrome.service import Service # manages Chrome Webdriver service
from selenium.webdriver.chrome.options import Options # Allows setting Chrome options, like headless mode
from selenium import webdriver # provides Webdriver for controlling the browser
from webdriver_manager.chrome import ChromeDriverManager # automatically downloads the ChromeDriver

# set up Webdriver options

options = Options()
options.headless = True # runs Chrome in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_treewizardco():
    driver.get("https://arborwizard.com/")