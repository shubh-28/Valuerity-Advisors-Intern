# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import os

# # Function to retrieve Glassdoor rating and reviews
# def get_glassdoor_rating_and_reviews(company_name):
#     # Configure Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--ignore-certificate-errors")
#     chrome_options.add_argument("--ignore-ssl-errors")

#     # Initialize the WebDriver with options and service
#     driver = webdriver.Chrome(options=chrome_options)

#     try:
#         # Go to Google and search for "company_name Glassdoor Review"
#         driver.get("https://www.google.com")
#         search_box = driver.find_element(By.NAME, "q")
#         search_query = f"{company_name} Glassdoor Review"
#         search_box.send_keys(search_query)
#         search_box.send_keys(Keys.RETURN)
#         time.sleep(10)
        
#         # Click on the first search result
#         first_result = driver.find_element(By.XPATH, '(//h3)[1]')
#         first_result.click()
#         time.sleep(3)
        
#         # Locate the rating element on Glassdoor's page and extract its text
#         rating_element = driver.find_element(By.CSS_SELECTOR, 'div.rating-headline-average_ratingContainer__DdU7f p.rating-headline-average_rating__J5rIy')
#         rating = rating_element.text
#         print(f"The average rating for {company_name} on Glassdoor is: {rating}")
#         print("\n--- Top 5 Reviews ---\n")
        
#         # Locate the review list
#         review_list = driver.find_element(By.CLASS_NAME, 'ReviewsList_reviewsList__Qfw6M')
#         review_items = review_list.find_elements(By.TAG_NAME, 'li')[:5]  # Select the first 5 reviews

#         # Loop through each review and extract required details
#         for i, review in enumerate(review_items, start=1):
#             print(f"Review {i}:")
            
#             # Extract rating
#             rating = review.find_element(By.CSS_SELECTOR, "span[data-test='review-rating-label']").text
#             print(f"Rating: {rating}")
            
#             # Extract date
#             date = review.find_element(By.CLASS_NAME, "timestamp_reviewDate__dsF9n").text
#             print(f"Date: {date}")
            
#             # Extract title
#             title = review.find_element(By.CSS_SELECTOR, "h3[data-test='review-details-title'] span").text
#             print(f"Title: {title}")
            
#             # Extract subtitle (role or title of reviewer)
#             subtitle = review.find_element(By.CSS_SELECTOR, "span[data-test='review-avatar-label']").text
#             print(f"Role: {subtitle}")
            
#             # Extract employee type and location (if available)
#             tags = review.find_elements(By.CLASS_NAME, "text-with-icon_LabelContainer__xbtB8")
#             employee_type = tags[0].text if len(tags) > 0 else "N/A"
#             location = tags[1].text if len(tags) > 1 else "N/A"
#             print(f"Employee Type: {employee_type}")
#             print(f"Location: {location}")
            
#             # Extract pros
#             pros = review.find_element(By.CSS_SELECTOR, "span[data-test='review-text-PROS']").text
#             print(f"Pros: {pros}")
            
#             # Extract cons
#             cons = review.find_element(By.CSS_SELECTOR, "span[data-test='review-text-CONS']").text
#             print(f"Cons: {cons}")
            
#             print("\n" + "-" * 40 + "\n")

#     except Exception as e:
#         print("An error occurred:", e)
    
#     finally:
#         driver.quit()

# # Main function to ask for company name and call the Glassdoor scraping function
# def main():
#     company_name = input("Enter the company name: ")
#     get_glassdoor_rating_and_reviews(company_name)

# # Run the main function
# main()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Function to retrieve Glassdoor ratings and reviews
# def get_glassdoor_rating_and_reviews(company_name):
#     # Configure Chrome options (headless mode for background execution)
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--ignore-certificate-errors")
#     chrome_options.add_argument("--disable-web-security")
#     chrome_options.add_argument("--allow-running-insecure-content")
#     chrome_options.add_argument("--ignore-ssl-errors")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--window-size=1920,1080")

#     # Initialize the WebDriver with options
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     # driver = webdriver.Chrome(options=chrome_options)

#     try:
#         # Navigate to Google and search for "company_name Glassdoor Review"
#         driver.get("https://www.google.com")
#         search_box = driver.find_element(By.NAME, "q")
#         search_query = f"{company_name} Glassdoor Review"
#         search_box.send_keys(search_query)
#         search_box.send_keys(Keys.RETURN)
#         time.sleep(3)  # Wait for results to load

#         # Click on the first search result
#         first_result = driver.find_element(By.XPATH, '(//h3)[1]')
#         first_result.click()
#         time.sleep(5)  # Wait for the Glassdoor page to load

#         # Locate the Glassdoor rating
#         try:
#             rating_element = driver.find_element(By.CSS_SELECTOR, 'div.rating-headline-average_ratingContainer__DdU7f p.rating-headline-average_rating__J5rIy')
#             rating = rating_element.text.strip()
#         except Exception:
#             rating = "Rating not found."

#         # Locate and extract the top 5 reviews
#         reviews_data = []
#         try:
#             review_list = driver.find_element(By.CLASS_NAME, 'ReviewsList_reviewsList__Qfw6M')
#             review_items = review_list.find_elements(By.TAG_NAME, 'li')[:5]  # Limit to the first 5 reviews

#             for i, review in enumerate(review_items, start=1):
#                 review_data = {}
#                 review_data['Review Number'] = i

#                 # Extract individual review details
#                 try:
#                     review_data['Rating'] = review.find_element(By.CSS_SELECTOR, "span[data-test='review-rating-label']").text
#                 except Exception:
#                     review_data['Rating'] = "N/A"
#                 try:
#                     review_data['Date'] = review.find_element(By.CLASS_NAME, "timestamp_reviewDate__dsF9n").text
#                 except Exception:
#                     review_data['Date'] = "N/A"
#                 try:
#                     review_data['Title'] = review.find_element(By.CSS_SELECTOR, "h3[data-test='review-details-title'] span").text
#                 except Exception:
#                     review_data['Title'] = "N/A"
#                 try:
#                     review_data['Role'] = review.find_element(By.CSS_SELECTOR, "span[data-test='review-avatar-label']").text
#                 except Exception:
#                     review_data['Role'] = "N/A"
#                 try:
#                     tags = review.find_elements(By.CLASS_NAME, "text-with-icon_LabelContainer__xbtB8")
#                     review_data['Employee Type'] = tags[0].text if len(tags) > 0 else "N/A"
#                     review_data['Location'] = tags[1].text if len(tags) > 1 else "N/A"
#                 except Exception:
#                     review_data['Employee Type'] = "N/A"
#                     review_data['Location'] = "N/A"
#                 try:
#                     review_data['Pros'] = review.find_element(By.CSS_SELECTOR, "span[data-test='review-text-PROS']").text
#                 except Exception:
#                     review_data['Pros'] = "N/A"
#                 try:
#                     review_data['Cons'] = review.find_element(By.CSS_SELECTOR, "span[data-test='review-text-CONS']").text
#                 except Exception:
#                     review_data['Cons'] = "N/A"

#                 # Append structured review data
#                 reviews_data.append(review_data)

#         except Exception:
#             reviews_data = [{"Error": "Reviews not found or unable to retrieve reviews."}]

#     finally:
#         driver.quit()

#     # Return formatted output
#     structured_output = f"Glassdoor Rating for {company_name}: {rating}\n\n--- Top Reviews ---\n"
#     for review in reviews_data:
#         for key, value in review.items():
#             structured_output += f"{key}: {value}\n"
#         structured_output += "-" * 40 + "\n"

#     return structured_output

# # Function for main script integration
# # def run_glassdoor_scraper(company_name):
# print(get_glassdoor_rating_and_reviews("Oracle"))


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import time


# Function to add realistic delays
def realistic_delay(min_seconds=2, max_seconds=5):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


# Function to simulate human-like scrolling
def human_like_scroll(driver, height=300, step=50):
    for i in range(0, height, step):
        driver.execute_script(f"window.scrollBy(0, {step});")
        realistic_delay(0.1, 0.3)


# Function to retrieve Glassdoor rating and reviews
def get_glassdoor_rating_and_reviews(company_name):
    # Configure Chrome with undetected_chromedriver
    options = uc.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    # Initialize undetected Chrome WebDriver
    driver = uc.Chrome(options=options)
    action = ActionChains(driver)

    try:
        # Open Google and search for the company
        driver.get("https://www.google.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
        search_box = driver.find_element(By.NAME, "q")
        search_query = f"{company_name} Glassdoor Review"
        search_box.send_keys(search_query)
        realistic_delay(2, 4)  # Human-like pause
        search_box.send_keys(Keys.RETURN)

        # Wait for search results and click the first link
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//h3)[1]'))
        )
        first_result = driver.find_element(By.XPATH, '(//h3)[1]')
        action.move_to_element(first_result).click().perform()
        realistic_delay(3, 6)

        # Check if captcha is encountered
        if "captcha" in driver.current_url.lower():
            print("Captcha encountered! Please solve it manually.")
            while "captcha" in driver.current_url.lower():
                time.sleep(5)  # Wait until the captcha is solved
            print("Captcha solved. Resuming scraping...")

        # Wait for the Glassdoor page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.rating-headline-average_ratingContainer__DdU7f")
            )
        )

        # Scrape rating
        rating_element = driver.find_element(
            By.CSS_SELECTOR, "p.rating-headline-average_rating__J5rIy"
        )
        rating = rating_element.text
        print(f"The average rating for {company_name} on Glassdoor is: {rating}")
        print("\n--- Top 5 Reviews ---\n")

        # Scrape reviews
        review_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "ReviewsList_reviewsList__Qfw6M")
            )
        )
        review_items = review_list.find_elements(By.TAG_NAME, "li")[:5]

        for i, review in enumerate(review_items, start=1):
            print(f"Review {i}:")

            # Extract review details
            rating = review.find_element(
                By.CSS_SELECTOR, "span[data-test='review-rating-label']"
            ).text
            date = review.find_element(By.CLASS_NAME, "timestamp_reviewDate__dsF9n").text
            title = review.find_element(
                By.CSS_SELECTOR, "h3[data-test='review-details-title'] span"
            ).text
            subtitle = review.find_element(
                By.CSS_SELECTOR, "span[data-test='review-avatar-label']"
            ).text

            tags = review.find_elements(By.CLASS_NAME, "text-with-icon_LabelContainer__xbtB8")
            employee_type = tags[0].text if len(tags) > 0 else "N/A"
            location = tags[1].text if len(tags) > 1 else "N/A"

            pros = review.find_element(By.CSS_SELECTOR, "span[data-test='review-text-PROS']").text
            cons = review.find_element(By.CSS_SELECTOR, "span[data-test='review-text-CONS']").text

            # Print review details
            print(f"Rating: {rating}")
            print(f"Date: {date}")
            print(f"Title: {title}")
            print(f"Role: {subtitle}")
            print(f"Employee Type: {employee_type}")
            print(f"Location: {location}")
            print(f"Pros: {pros}")
            print(f"Cons: {cons}")
            print("\n" + "-" * 40 + "\n")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()


# Main function
def main():
    company_name = input("Enter the company name: ")
    get_glassdoor_rating_and_reviews(company_name)


# Run the script
if __name__ == "__main__":
    main()
