from fastapi import APIRouter
from typing import Dict
from scrapers.google_news_scraping import run_google_news_scraper
from scrapers.patents_desc import run_patents_scraper
from scrapers.capterra_scraping import run_capterra_scraper
from scrapers.press_release_scraping import run_press_release_scraper
from scrapers.clinicaltrials import run_clinical_trials_scraper

router = APIRouter()

@router.get("/search")
def search_company(company_name: str) -> Dict:
    """
    Process the search query and return results.
    Perform scraping or API calls to retrieve data.
    """
    print("Processing search for:", company_name)
    news_results = run_google_news_scraper(company_name)

    patents_results = run_patents_scraper(company_name)

    capterra_results = run_capterra_scraper(company_name)

    press_release_results = run_press_release_scraper(company_name)

    clinical_trials_results = run_clinical_trials_scraper(company_name)

    return {
        "company_name": company_name,
        "news": news_results,  # Structured news data returned from scraper
        "patents": patents_results,
        "capterra": capterra_results,
        "pressReleases": press_release_results,
        "clinicalTrials": clinical_trials_results,

    }
