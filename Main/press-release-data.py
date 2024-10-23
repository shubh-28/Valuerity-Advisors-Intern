import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def scrape_anchor_text(url):
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

    finally:
        driver.quit()

if __name__ == "__main__":
    # Replace with the URL of the company press release page you want to scrape
    url = input("Enter the URL of the press release page: ")
    scrape_anchor_text(url)
