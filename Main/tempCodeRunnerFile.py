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

def scrape_clinical_trials(keyword):
    # Configure Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Base URL for clinical trials search
    base_url = "https://clinicaltrials.gov/"

    try:
        # Load the clinical trials homepage
        driver.get(base_url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "advcond"))
        )

        # Enter the search keyword and press Enter
        search_input = driver.find_element(By.NAME, "advcond")
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

        # Allow some time for results to load
        time.sleep(5)

        # Check if any studies are found
        try:
            results_text = driver.find_element(By.CSS_SELECTOR, "p.shown-range.font-body-md.ng-star-inserted").text
            total_studies = int(re.search(r'out of ([\d,]+) studies', results_text).group(1).replace(',', ''))
            if total_studies == 0:
                return {"message": "No studies found for the given keyword."}
        except Exception:
            return {"message": "No studies found or unable to retrieve results."}

        # Extract study IDs and details, limiting to 10 results
        study_data = []
        nct_ids = []
        for _ in range(10):
            try:
                study_elements = driver.find_elements(By.CSS_SELECTOR, "div.nct-id")
                for elem in study_elements:
                    nct_id = elem.text.strip()
                    if nct_id and nct_id not in nct_ids:
                        nct_ids.append(nct_id)
                        study_details = scrape_study_details(driver, nct_id, keyword)
                        study_data.append(study_details)
                        if len(study_data) == 10:
                            break
                if len(study_data) == 10:
                    break
            except Exception:
                continue

        return {"studies": study_data}

    finally:
        driver.quit()

# Helper function to scrape individual study details
def scrape_study_details(driver, nct_id, keyword):
    study_url = f"https://clinicaltrials.gov/study/{nct_id}?cond={keyword}"
    driver.get(study_url)
    time.sleep(3)
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
    return details

# Helper function to extract specific detail
def extract_detail(driver, xpath):
    try:
        return driver.find_element(By.XPATH, xpath).text.strip()
    except Exception:
        return "N/A"

# Run the scraper
if __name__ == "__main__":
    result = scrape_clinical_trials("Novartis")
    print(result)


