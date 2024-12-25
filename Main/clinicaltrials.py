from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def scrape_clinical_trials(keyword):
    # Configure Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 20)

    try:
        # Load the clinical trials homepage (using original URL)
        driver.get("https://clinicaltrials.gov/")
        
        # Wait for search box using original selector
        search_input = wait.until(
            EC.element_to_be_clickable((By.NAME, "advcond"))
        )
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.RETURN)

        # Allow time for results to load
        time.sleep(5)

        # Check for results using original selector
        try:
            results_text = driver.find_element(By.CSS_SELECTOR, "p.shown-range.font-body-md.ng-star-inserted").text
            total_studies = int(re.search(r'out of ([\d,]+) studies', results_text).group(1).replace(',', ''))
            if total_studies == 0:
                return {"message": "No studies found for the given keyword."}
        except Exception:
            return {"message": "No studies found or unable to retrieve results."}

        # Extract study data using original approach
        study_data = []
        nct_ids = set()  # Using set for efficiency
        max_attempts = 3

        for attempt in range(max_attempts):
            try:
                # Use original selector for study elements
                study_elements = driver.find_elements(By.CSS_SELECTOR, "div.nct-id")
                
                for elem in study_elements:
                    nct_id = elem.text.strip()
                    if nct_id and nct_id not in nct_ids:
                        nct_ids.add(nct_id)
                        study_details = scrape_study_details(driver, nct_id, keyword)
                        study_data.append(study_details)
                        
                        if len(study_data) >= 10:
                            return {"studies": study_data}
                
                if study_data:  # If we have any data, return it
                    return {"studies": study_data}
                    
            except Exception:
                if attempt == max_attempts - 1:  # Last attempt
                    if study_data:
                        return {"studies": study_data}
                    return {"message": "Failed to load study results"}
                time.sleep(3)  # Wait before retrying

        return {"studies": study_data} if study_data else {"message": "Failed to load study results"}

    finally:
        driver.quit()

def scrape_study_details(driver, nct_id, keyword):
    """Get detailed information for a single study"""
    study_url = f"https://clinicaltrials.gov/study/{nct_id}?cond={keyword}"
    
    try:
        # Open study in new tab for better stability
        driver.execute_script(f"window.open('{study_url}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)  # Wait for page load
        
        details = {
            "NCT-ID": nct_id,
            "URL": study_url,
            "Study Start": extract_detail(driver, "//div[contains(text(), 'Study Start')]/following-sibling::span"),
            "Primary Completion": extract_detail(driver, "//div[contains(text(), 'Primary Completion')]/following-sibling::span"),
            "Study Completion": extract_detail(driver, "//div[contains(text(), 'Study Completion')]/following-sibling::span"),
            "Enrollment": extract_detail(driver, "//div[contains(text(), 'Enrollment')]/following-sibling::div/span"),
            "Study Type": extract_detail(driver, "//div[contains(text(), 'Study Type')]/following-sibling::ctg-enum-value/span"),
            "Phase": extract_detail(driver, "//div[contains(text(), 'Phase')]/following-sibling::ctg-enum-value/span"),
        }
        
    except Exception as e:
        details = {
            "NCT-ID": nct_id,
            "URL": study_url,
            "Study Start": "N/A",
            "Primary Completion": "N/A",
            "Study Completion": "N/A",
            "Enrollment": "N/A",
            "Study Type": "N/A",
            "Phase": "N/A"
        }
        
    finally:
        # Close tab and switch back
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        
    return details

def extract_detail(driver, xpath):
    """Safely extract element text with original approach"""
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element.text.strip()
    except Exception:
        return "N/A"

if __name__ == "__main__":
    result = scrape_clinical_trials("Novartis")
    print(result)