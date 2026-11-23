from dotenv.main import load_dotenv
load_dotenv()

from models.job_posting import JobPosting
from scraper.scraper import scrape_job_posting
from services.job_posting_service import create_job_posting_page
import asyncio
from config.logger import logger

async def main():
    job_posting: JobPosting = await scrape_job_posting()

    if job_posting is None:
        logger.error("No job posting found!")
        return

    await create_job_posting_page(job_posting)

if __name__ == "__main__":
    asyncio.run(main())