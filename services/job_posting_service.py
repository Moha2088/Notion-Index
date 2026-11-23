from notion_client import AsyncClient
from models.job_posting import JobPosting
from config.logger import logger
import os
import sys
from services.messaging_service import send_message

NOTION_INTEGRATION_SECRET = os.getenv("NOTION_INTEGRATION_SECRET")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")
NOTION_DATA_SOURCE_ID = os.getenv("NOTION_DATA_SOURCE_ID")
NOTION_DB_URL = os.getenv("NOTION_DB_URL")

if NOTION_INTEGRATION_SECRET is None or NOTION_DB_ID is None or NOTION_DATA_SOURCE_ID is None:
    logger.critical("secrets are missing!")
    sys.exit(1)

notionClient = AsyncClient(auth=NOTION_INTEGRATION_SECRET)

async def create_job_posting_page(job_posting: JobPosting):
    position, company_name, job_posting_url, search_query, region = job_posting.position, job_posting.company_name, job_posting.job_posting_link, job_posting.search_query, job_posting.region
    
    logger.info("Job Posting scraped: %s", job_posting.position) 

    await notionClient.pages.create(
        parent={"database_id": NOTION_DB_ID},
        properties={
            "Position": {
                "title": [
                    {
                        "text": {
                            "content": position,
                            
                        }
                    }
                ]
            },

            "Company": {
                "type": "rich_text",
                "rich_text": [
                    {
                        "text": {
                            "content": company_name
                        }
                    }
                ]
            },

            "JobPostingLink": {
                "type": "url",
                "url": job_posting_url
            },
            
            "SearchQuery": {
                "type": "rich_text",
                "rich_text": [
                    {
                        "text": {
                            "content": f'{search_query} | {region}'
                        }
                    }
                ]
            }
        },
        icon={
            "type": "emoji",
            "emoji": "💼"
        }
    )

    send_message(f'New job_posting has been scraped:\nPosition: {position}\nCompany: {company_name}\n\nUrl: {NOTION_DB_URL}')