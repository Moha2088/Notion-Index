from random import randint
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from models.job_posting import JobPosting


query_strings = [
    "fullstack",
    "software+developer",
    "backend+developer",
    "software+udvikler",
]

excluded_keywords = [
    "senior",
    "lead",
    "principal",
    "manager",
    "director",
    "business",
    "student"
]

def scrape_job_posting():
    target_class = "PaidJob-inner"
    random_query_string = query_strings[randint(0, len(query_strings) - 1)]
    url = "https://www.jobindex.dk/jobsoegning/region-syddanmark?q=" + random_query_string

    html_response = wait_for_content(url)

    soup = BeautifulSoup(html_response, "html.parser")
    target_div = soup.find(class_=target_class)

    if(not target_div):
        return

    company_url = target_div.find("a")["href"]
    position = target_div.find("h4").text
    job_posting_url = target_div.find("h4").find("a")["href"]

    if(any(keyword in position.lower() for keyword in excluded_keywords)):
        print(f"Excluded job posting with position: {position}\nTrying again...")
        return scrape_job_posting()

    return JobPosting(
        position=position,
        company_link=company_url,
        job_posting_link=job_posting_url
    )


def wait_for_content(url: str):
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.wait_for_selector(".PaidJob-inner")
        html_response = page.content()
        browser.close()
    
    return html_response
