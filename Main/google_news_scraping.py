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
    chrome_options.add_argument("--window-size=1920,1080")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Construct the Google News search URL
    url = f"https://news.google.com/search?q={company_name}"
    try:
        driver.get(url)

        # Allow some time for the page to load
        time.sleep(5)  # Adjust this time based on your internet speed

        # Use the correct class name to locate all headline anchors
        xpath_expression = '//a[@class="JtKRv"]'
        headlines = driver.find_elements(By.XPATH, xpath_expression)

        # Prepare and return the structured output
        structured_output = []
        for index, headline in enumerate(headlines, start=1):
            try:
                headline_text = headline.text.strip()
                headline_link = headline.get_attribute('href')
                if headline_text and headline_link:
                    structured_output.append(f"{index}. {headline_text}\n   Link: {headline_link}")
            except Exception:
                continue  # Skip problematic entries

    finally:
        driver.quit()

    # Return structured results or a fallback message
    return "\n".join(structured_output) if structured_output else "No news headlines found or unable to retrieve them."

# Function for main script integration
def run_google_news_scraper(company_name):
    return scrape_google_news(company_name)
