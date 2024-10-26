import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bardapi import Bard
import os

# Set the API key in the environment
os.environ["GEMINI_API_KEY"] = "AIzaSyA6BKVD7RLzoSOjDl-T-mB2XXELh_mdOZw"

def scrape_anchor_text(url):
    # Retrieve the API key from the environment
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    # Setup the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigate to the given URL
        driver.get(url)
        time.sleep(3)  # Allow time for the page to load

        # Extract all anchor tags that are not within the footer
        anchor_tags = driver.find_elements(By.XPATH, '//body//a[not(ancestor::footer)]')

        # Create a structured output
        print(f"{'Index':<5} {'Anchor Text':<100} {'Link'}")
        print("=" * 120)
        
        for index, anchor in enumerate(anchor_tags):
            anchor_text = anchor.text.strip()
            href = anchor.get_attribute('href')
            if anchor_text:  # Only print if the anchor text is not empty
                print(f"{index:<5} {anchor_text:<100} {href}")

        prompt = """The code output currently contains news headlines with links but also includes extra text that isn't part of the headline. Please filter this data and provide only the headlines along with their links, removing any non-headline text. Structure the results in a numbered list format, with each item containing just the headline followed by its link. Only include items that resemble a news headline or a press release headline, omitting any irrelevant or extraneous information."""

        # Use the API key to initialize Bard
        if gemini_api_key:
            print(Bard(token=gemini_api_key).get_answer(str(prompt))['content'])
        else:
            print("Error: GEMINI_API_KEY not found. Please set the environment variable.")

    finally:
        driver.quit()

if __name__ == "__main__":
    # Replace with the URL of the company press release page you want to scrape
    url = input("Enter the URL of the press release page: ")
    scrape_anchor_text(url)
