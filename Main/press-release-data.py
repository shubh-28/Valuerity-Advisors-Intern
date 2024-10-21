import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# Placeholder for Google Gemini API Key
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

# Function to detect dates using regular expressions
def detect_date(text):
    date_patterns = [
        r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}",  # Month DD, YYYY
        r"\d{1,2}/\d{1,2}/\d{4}",  # MM/DD/YYYY
        r"\b\d{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}"  # DD Month YYYY
    ]
    
    for pattern in date_patterns:
        if re.search(pattern, text):
            return True
    return False

# Function to find headlines and dates
def scrape_headlines(driver):
    # Get the page source
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    headlines = []

    # Iterate through all elements (like divs, spans, etc.)
    for container in soup.find_all(['div', 'li', 'article', 'section']):
        # Check if there's a date in this container
        date_text = container.get_text(strip=True)
        if detect_date(date_text):
            # If date is found, look for a headline in the same container or nearby
            headline = None
            # Try to find an <a> or other headline tag within this container
            link = container.find('a')
            if link:
                headline = link.get_text(strip=True)
            else:
                # Try to find <div>, <span>, or <p> with headline-like text
                headline = container.find(['div', 'span', 'p'])
                if headline:
                    headline = headline.get_text(strip=True)
            
            # Add both date and headline to the list
            if headline:
                headlines.append(f"Date: {date_text} | Headline: {headline}")
    
    return headlines

# Function to send unstructured data to Gemini API
def send_to_gemini(unstructured_input):
    # URL endpoint for Gemini API (this is speculative and subject to change)
    gemini_api_url = "https://api.gemini.google.com/v1/your-endpoint"

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": f"Clean and structure the following press release data, remove any repetitive information, and return only the headlines and associated dates:\n\n{unstructured_input}",
        "max_tokens": 1500
    }

    response = requests.post(gemini_api_url, headers=headers, json=data)

    # Check for response status and return the output
    if response.status_code == 200:
        return response.json().get("choices")[0].get("text", "").strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

# Main function to scrape, process, and output structured data
def scrape_press_release_page(url):
    # Initialize Chrome WebDriver with WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the URL with Selenium
    driver.get(url)

    # Wait for the page to load
    time.sleep(3)

    # Scrape headlines and dates
    headlines = scrape_headlines(driver)

    # Combine scraped data into a single string
    unstructured_data = "\n".join(headlines)
    print("Unstructured Data Scraped:\n", unstructured_data)

    # Send the unstructured data to Gemini for processing
    structured_output = send_to_gemini(unstructured_data)
    print("\nStructured Output from Gemini:\n", structured_output)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    # Test the script by providing a URL for press release page
    url = input("Enter the press release URL: ")
    scrape_press_release_page(url)
