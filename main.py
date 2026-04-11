from models.job_posting import JobPosting
from scraper.scraper import scrape_job_posting
from services.job_posting_service import create_job_posting_page


def main():
    job_posting: JobPosting = scrape_job_posting()

    print("Scraped job posting:")
    print(job_posting)

    create_job_posting_page(job_posting)

if __name__ == "__main__":
    main()