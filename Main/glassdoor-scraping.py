from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Function to retrieve Glassdoor rating
def get_glassdoor_rating(company_name):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")

    # Initialize the WebDriver with options
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
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        driver.quit()

def get_glassdoor_salaries(company_name):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")

    # Initialize the WebDriver with options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Go to Google and search for "company_name Glassdoor Salaries"
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_query = f"{company_name} Glassdoor Salaries"
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        # Click on the first search result
        first_result = driver.find_element(By.XPATH, '(//h3)[1]')
        first_result.click()
        time.sleep(3)

        # Locate salary elements for the first two positions
        salary_elements = driver.find_elements(By.CSS_SELECTOR, "tr.salarylist_table-row__PHb9J")[:2]
        
        # Iterate over the first two elements to extract the required data
        for i, element in enumerate(salary_elements, start=1):
            # Extract the job title
            job_title = element.find_element(By.CSS_SELECTOR, "a.salarylist_job-title-link__MXnPX").text
            
            # Extract the total pay range
            total_pay_range = element.find_element(By.CSS_SELECTOR, "p.salarylist_total-pay-range__ECY78").text
            
            # Extract the base and additional pay
            
            #base_additional_pay = element.find_elements(By.CSS_SELECTOR, "p.salarylist_sub-data__Umf9l")[1].text
            
            print(f"Position {i}:")
            print(f"Job Title: {job_title}")
            print(f"Total Pay Range: {total_pay_range}")
            
            #print(f"Base | Additional Pay: {base_additional_pay}\n")

    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        driver.quit()

# Main function to ask for company name and call the scraping function
def main():
    company_name = input("Enter the company name: ")
    get_glassdoor_rating(company_name)
    get_glassdoor_salaries(company_name)

# Run the main function
main()
