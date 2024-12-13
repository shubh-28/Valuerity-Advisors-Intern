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

        # Use the correct class names to locate all headline anchors and their timestamps
        headline_xpath = '//a[@class="JtKRv"]'
        time_xpath = '//time[@class="hvbAAd"]'

        headlines = driver.find_elements(By.XPATH, headline_xpath)
        times = driver.find_elements(By.XPATH, time_xpath)

        # Prepare and return the structured output
        structured_output = []
        for i, headline in enumerate(headlines):
            try:
                headline_text = headline.text.strip()
                headline_link = headline.get_attribute('href')
                headline_time = times[i].text.strip() if i < len(times) else "Unknown"

                if headline_text and headline_link:
                    structured_output.append({
                        "title": headline_text,
                        "link": headline_link,
                        "time": headline_time
                    })
            except Exception:
                continue  # Skip problematic entries

    finally:
        driver.quit()

    # Return structured results or an empty list if no headlines found.
    return structured_output if structured_output else []

# Function for main script integration
def run_google_news_scraper(company_name):
    return scrape_google_news(company_name)
