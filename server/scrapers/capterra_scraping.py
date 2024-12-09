
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Function to scrape software details from Capterra
def scrape_capterra(company_name):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Construct the Capterra search URL
    url = f"https://www.capterra.in/search/?q={company_name}"

    try:
        # Open the search page
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        # Locate software results
        result_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "my-2")]')
        structured_output = []

        # Extract software details
        for result in result_elements:
            try:
                # Extract software name
                software_name_element = result.find_element(By.XPATH, './/span[@class="h4 fw-bold"]')
                software_name = software_name_element.text.strip()

                # Extract rating, if available
                try:
                    rating_element = result.find_element(By.XPATH, './/span[@class="ms-1"]')
                    rating = rating_element.text.strip()
                except NoSuchElementException:
                    rating = "No rating available"

                # Append structured results
                structured_output.append({
                    "name": software_name,
                    "rating": rating
                })

                # Stop after collecting 4 results
                if len(structured_output) >= 4:
                    break
            except NoSuchElementException:
                continue  # Skip incomplete results

    finally:
        # Close the browser
        driver.quit()

    # Return results or fallback message
    return structured_output if structured_output else [{"name": f"No results for {company_name}", "rating": "N/A"}]

# Function for main script integration
def run_capterra_scraper(company_name):
    return scrape_capterra(company_name)
