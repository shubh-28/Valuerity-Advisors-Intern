from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to scrape patents
def scrape_patents(company_name):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Use ChromeDriverManager to install and manage ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Formulate the search URL
    url = f"https://patents.google.com/?assignee={company_name}&sort=new"

    # Open the webpage
    try:
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        # Extract patents' titles and dates
        patents = driver.find_elements(By.XPATH, '//article[@class="result style-scope search-result-item"]')
        
        structured_output = []
        for index, patent in enumerate(patents, start=1):
            try:
                title = patent.find_element(By.TAG_NAME, 'h3').text
                dates = patent.find_element(By.CLASS_NAME, 'dates').text
                structured_output.append(f"{index}. Title: {title}\n   Dates: {dates}\n")
            except Exception:
                continue  # Skip if any element is not found

    finally:
        driver.quit()

    # Return structured results or a fallback message
    return "\n".join(structured_output) if structured_output else "No patents found or unable to retrieve patents."

# Function for main script integration
def run_patents_scraper(company_name):
    return scrape_patents(company_name)
