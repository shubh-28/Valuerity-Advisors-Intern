# Updated press_release_scraping.py
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googlesearch import search
import google.generativeai as genai
from dotenv import load_dotenv

# Load the environment variables for the GEMINI API key
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to find press release URL
def find_press_release_url(company_name):
    query = f"{company_name} press releases"
    urls = []
    for url in search(query, num_results=5):  # Adjust num_results if needed
        if 'press' in url or 'news' in url:  # Filter for likely press release URLs
            urls.append(url)
        time.sleep(random.uniform(5, 10))
    return urls[0] if urls else None

# Function to scrape anchor text
def scrape_anchor_text(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    stored_output = ""
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//body//a[not(ancestor::footer)]'))
        )

        anchor_tags = driver.find_elements(By.XPATH, '//body//a[not(ancestor::footer)]')

        for anchor in anchor_tags:
            anchor_text = anchor.text.strip()
            href = anchor.get_attribute('href')
            if anchor_text:  # Only add if anchor text is not empty
                line = f"{anchor_text} {href}\n"
                stored_output += line

    finally:
        driver.quit()

    return stored_output

# Function to filter and process the scraped output
def process_output(output_text):
    # Setup model configuration
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    prompt = """This code output currently contains news headlines with respective dates and links but also includes extra text that isn't part of the headline. Please filter this data and provide only the headlines, date (also very important) and their links, removing any non-headline text. Structure the results in a numbered list format, with each item containing just the headline and its date followed by its link. Only include items that resemble a news headline or a press release headline having its date, omitting any irrelevant or extraneous information."""

    # Generate the filtered output
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(output_text + " " + prompt)

    return response.text

# Main function to integrate into the primary script
def scrape_press_releases(company_name):
    # Step 1: Get the press release URL
    press_release_url = find_press_release_url(company_name)

    if not press_release_url:
        return "No press release page found for this company."

    # Step 2: Scrape the anchor text from the press release page
    output_text = scrape_anchor_text(press_release_url)

    # Step 3: Process and filter the output through the AI model
    filtered_output = process_output(output_text)

    return filtered_output

# Wrapper function for integration
def run_press_release_scraper(company_name):
    return scrape_press_releases(company_name)
