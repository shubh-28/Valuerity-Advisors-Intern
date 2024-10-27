import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googlesearch import search

def find_press_release_url(company_name):
    # Perform Google search query
    query = f"{company_name} press releases"
    urls = []
    
    # Search for relevant press release URLs (filtering for press-related keywords)
    for url in search(query, num_results=5):  # Adjust num_results if needed
        if 'press' in url or 'news' in url:  # Filter for likely press release URLs
            urls.append(url)
        time.sleep(random.uniform(5, 10))
    
    if urls:
        return urls[0]  # Return the first valid URL
    else:
        return None

def scrape_anchor_text(url):
    # Setup the Chrome driver with headless options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    stored_output = ""  # Initialize variable to store output as text
    
    try:
        # Navigate to the given URL
        driver.get(url)
        
        # Use explicit wait to ensure the page loads fully
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//body//a[not(ancestor::footer)]'))
        )

        # Extract all anchor tags that are not within the footer
        anchor_tags = driver.find_elements(By.XPATH, '//body//a[not(ancestor::footer)]')

        # Create a structured output
        header = f"{'Index':<5} {'Anchor Text':<100} {'Link'}\n" + "=" * 120 + "\n"
        print(header)
        stored_output += header  # Store the header in the output variable
        
        for index, anchor in enumerate(anchor_tags):
            anchor_text = anchor.text.strip()
            href = anchor.get_attribute('href')
            if anchor_text:  # Only print if the anchor text is not empty
                line = f"{index:<5} {anchor_text:<100} {href}\n"
                print(line)
                stored_output += line  # Store each line of output in the variable

    finally:
        driver.quit()
    
    return stored_output  # Return the stored output as text

if __name__ == "__main__":
    # Replace with the URL of the company press release page you want to scrape
    
    company_name = input("Enter the name of the company: ")
    
    # Step 1: Get the press release URL
    press_release_url = find_press_release_url(company_name)
    
    if press_release_url:
        print(f"Found Press Release URL: {press_release_url}")
        
        # Step 2: Scrape anchor text and store output
        output_text = scrape_anchor_text(press_release_url)
        print("\nStored Output:\n", output_text)
    else:
        print("No press release page found for this company.")
