from random import randint
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from models.job_posting import JobPosting


query_strings = [
    "full+stack",
    "software+developer",
    "backend+developer",
    "software+udvikler",
    "developer",
    ".NET",
    "C#",
    "React",
    "TypeScript",
    "Next.js"
]

regions = [
    "region-syddanmark",
    "region-hovedstaden",
    "region-midtjylland"
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

async def scrape_job_posting():
    random_query_string = query_strings[randint(0, len(query_strings) - 1)]
    random_region = regions[randint(0, len(regions) - 1)]
    
    target_class = "PaidJob-inner"
    print(random_query_string)
    url = f'https://www.jobindex.dk/jobsoegning/{random_region}?q={random_query_string}'
    print(url)

    html_response = await wait_for_content(url)

    soup = BeautifulSoup(html_response, "html.parser")
    target_divs = soup.find_all(class_=target_class)

    if target_divs.__len__() == 0:
        return

    target_div = target_divs[randint(0, target_divs.__len__() - 1)]

    company_url = target_div.find("a")["href"]
    position = target_div.find("h4").text
    job_posting_url = target_div.find("h4").find("a")["href"]

    if any(keyword in position.lower() for keyword in excluded_keywords):
        print(f"Excluded job posting with position: {position}\nTrying again...")
        return scrape_job_posting()

    return JobPosting(
        position=position,
        company_link=company_url,
        job_posting_link=job_posting_url,
        search_query=random_query_string,
        region=random_region
    )


async def wait_for_content(url: str):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        await page.wait_for_selector(".PaidJob-inner")
        html_response = await page.content()
        await browser.close()
    
    return html_response
