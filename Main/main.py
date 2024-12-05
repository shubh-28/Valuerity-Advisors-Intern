from press_release_scraping import run_press_release_scraper
from patents_desc import run_patents_scraper
from google_news_scraping import run_google_news_scraper
from glassdoor_scraping import run_glassdoor_scraper
from capterra_scraping import run_capterra_scraper

def main():
    # Dictionary to store outputs from all scrapers
    scraper_results = {}
    company_name = input("Enter the company name for press releases: ")

    print("Running press release scraper...")
    scraper_results['press_release'] = run_press_release_scraper(company_name)

    # print("Running patents scraper...")
    # scraper_results['patents'] = run_patents_scraper(company_name)

    # print("Running Google News scraper...")
    # scraper_results['google_news'] = run_google_news_scraper(company_name)

    # print("Running Glassdoor scraper...")
    # scraper_results['glassdoor'] = run_glassdoor_scraper(company_name)

    # print("Running Capterra scraper...")
    # scraper_results['capterra'] = run_capterra_scraper(company_name)

    # Output the results
    for scraper_name, results in scraper_results.items():
        print(f"\nResults from {scraper_name}:")
        print(results)

if __name__ == "__main__":
    main()
