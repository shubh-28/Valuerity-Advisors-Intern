from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to scrape headlines from Google News
def scrape_google_news(company_name):
    # Set up Chrome options (headless mode)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Construct the Google News search URL
    url = f"https://news.google.com/search?q={company_name}"
    driver.get(url)

    # Allow some time for the page to load
    time.sleep(5)  # Adjust this time based on your internet speed

    # Use the correct class name to locate all headline anchors
    xpath_expression = '//a[@class="JtKRv"]'

    try:
        # Find all headline elements using the specified XPath
        headlines = driver.find_elements(By.XPATH, xpath_expression)

        # Check if headlines are found
        if headlines:
            print(f"Headlines for {company_name}:\n")
            for index, headline in enumerate(headlines, start=1):
                print(f"{index}. {headline.text}")  # Print the text of each headline with numbering
        else:
            print("No headlines found.")
    
    except Exception as e:
        print(f"Error while finding headlines: {e}")

    # Close the browser
    driver.quit()

# Get user input for the company name
company_name = input("Enter the company name: ")
scrape_google_news(company_name)
