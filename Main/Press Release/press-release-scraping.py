from googlesearch import search
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

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

def access_press_release_page(url):
    # Initialize Chrome WebDriver with WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the URL with Selenium
    driver.get(url)

    # Wait for a few seconds to ensure the page loads properly
    time.sleep(3)

    # Print the page title to confirm access
    print(f"Accessed page title: {driver.title}")
    
    # Optionally, print the page source or any specific content you want to scrape
    # Uncomment the following line to print the entire page's HTML
    # print(driver.page_source)
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    # Input: Company Name
    company_name = input("Enter the name of the company: ")
    
    # Step 1: Get the press release URL
    press_release_url = find_press_release_url(company_name)
    
    if press_release_url:
        print(f"Found Press Release URL: {press_release_url}")
        
        # Step 2: Access the press release page using Selenium
        access_press_release_page(press_release_url)
    else:
        print("No press release page found for this company.")
