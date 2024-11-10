from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Function to retrieve Glassdoor rating and reviews
def get_glassdoor_rating_and_reviews(company_name):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")

    # Initialize the WebDriver with options and service
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Go to Google and search for "company_name Glassdoor Review"
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_query = f"{company_name} Glassdoor Review"
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        
        # Click on the first search result
        first_result = driver.find_element(By.XPATH, '(//h3)[1]')
        first_result.click()
        time.sleep(3)
        
        # Locate the rating element on Glassdoor's page and extract its text
        rating_element = driver.find_element(By.CSS_SELECTOR, 'div.rating-headline-average_ratingContainer__DdU7f p.rating-headline-average_rating__J5rIy')
        rating = rating_element.text
        print(f"The average rating for {company_name} on Glassdoor is: {rating}")
        print("\n--- Top 5 Reviews ---\n")
        
        # Locate the review list
        review_list = driver.find_element(By.CLASS_NAME, 'ReviewsList_reviewsList__Qfw6M')
        review_items = review_list.find_elements(By.TAG_NAME, 'li')[:5]  # Select the first 5 reviews

        # Loop through each review and extract required details
        for i, review in enumerate(review_items, start=1):
            print(f"Review {i}:")
            
            # Extract rating
            rating = review.find_element(By.CSS_SELECTOR, "span[data-test='review-rating-label']").text
            print(f"Rating: {rating}")
            
            # Extract date
            date = review.find_element(By.CLASS_NAME, "timestamp_reviewDate__dsF9n").text
            print(f"Date: {date}")
            
            # Extract title
            title = review.find_element(By.CSS_SELECTOR, "h3[data-test='review-details-title'] span").text
            print(f"Title: {title}")
            
            # Extract subtitle (role or title of reviewer)
            subtitle = review.find_element(By.CSS_SELECTOR, "span[data-test='review-avatar-label']").text
            print(f"Role: {subtitle}")
            
            # Extract employee type and location (if available)
            tags = review.find_elements(By.CLASS_NAME, "text-with-icon_LabelContainer__xbtB8")
            employee_type = tags[0].text if len(tags) > 0 else "N/A"
            location = tags[1].text if len(tags) > 1 else "N/A"
            print(f"Employee Type: {employee_type}")
            print(f"Location: {location}")
            
            # Extract pros
            pros = review.find_element(By.CSS_SELECTOR, "span[data-test='review-text-PROS']").text
            print(f"Pros: {pros}")
            
            # Extract cons
            cons = review.find_element(By.CSS_SELECTOR, "span[data-test='review-text-CONS']").text
            print(f"Cons: {cons}")
            
            print("\n" + "-" * 40 + "\n")

    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        driver.quit()

# Main function to ask for company name and call the Glassdoor scraping function
def main():
    company_name = input("Enter the company name: ")
    get_glassdoor_rating_and_reviews(company_name)

# Run the main function
main()

