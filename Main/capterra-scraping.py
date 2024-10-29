import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def scrape_capterra(company_name):
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Format the search URL with the company name
        url = f"https://www.capterra.in/search/?q={company_name}"
        driver.get(url)
        time.sleep(3)  # Allow time for the page to load

        # Find all software result elements
        result_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "my-2")]')
        results = []

        # Iterate over result elements, extract software name, company name, and rating
        for result in result_elements:
            try:
                # Get the company name in the result to match with the input
                company_element = result.find_element(By.XPATH, './/span[@class="text-body fw-bold mx-lg-1 d-block d-lg-inline"]/em')
                result_company_name = company_element.text.strip()

                # Check for an exact match with the input company name (ignoring case)
                if result_company_name.lower() == company_name.lower():
                    # Get the software name
                    software_name_element = result.find_element(By.XPATH, './/span[@class="h4 fw-bold"]')
                    software_name = software_name_element.text.strip()
                    
                    # Get the rating (if present)
                    try:
                        rating_element = result.find_element(By.XPATH, './/span[@class="ms-1"]')
                        rating = rating_element.text.strip()
                    except NoSuchElementException:
                        rating = "No rating available"
                    
                    # Store the result
                    results.append((software_name, rating))
                    
                # Limit to 4 results
                if len(results) >= 4:
                    break
            except NoSuchElementException:
                # Skip this result if the company name or software name is not found
                continue

        # Display results
        if results:
            print("Top software results for company:", company_name)
            for idx, (software_name, rating) in enumerate(results, start=1):
                print(f"{idx}. Software Name: {software_name}, Rating: {rating}")
        else:
            print(f"No results found for company: {company_name}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Input company name from user
    company_name = input("Enter the company name to search on Capterra: ")
    scrape_capterra(company_name)
