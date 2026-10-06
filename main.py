from models.job_posting import JobPosting
from scraper.scraper import scrape_job_posting
from services.job_posting_service import create_job_posting_page
import asyncio
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

async def main():
    job_posting: JobPosting = await scrape_job_posting()

    if job_posting is None:
        logging.error("No job posting found!")
        return


    await create_job_posting_page(job_posting)

    logger.info("Job Posting scraped: %s", job_posting.position)

if __name__ == "__main__":
    asyncio.run(main())