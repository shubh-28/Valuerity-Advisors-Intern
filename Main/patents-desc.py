from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to scrape patents
def scrape_patents(company):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Use ChromeDriverManager to install and manage chromedriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Formulate the search URL
    url = f"https://patents.google.com/?assignee={company}&sort=new"

    # Open the webpage
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Extract patents' titles and dates
    patents = driver.find_elements(By.XPATH, '//article[@class="result style-scope search-result-item"]')

    for index, patent in enumerate(patents, start=1):
        title = patent.find_element(By.TAG_NAME, 'h3').text
        dates = patent.find_element(By.CLASS_NAME, 'dates').text

        # Print the structured output
        print(f"{index}. Title: {title}")
        print(f"   Dates: {dates}")

    driver.quit()

# Get input from the user
company_name = input("Enter the company name: ")

# Call the function to scrape patents
scrape_patents(company_name)
