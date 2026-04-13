from dotenv import load_dotenv
from notion_client import Client, AsyncClient
from models.job_posting import JobPosting
import os


load_dotenv()

NOTION_INTEGRATION_SECRET = os.getenv("NOTION_INTEGRATION_SECRET")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")

notionClient = AsyncClient(auth=NOTION_INTEGRATION_SECRET)
 
async def create_job_posting_page(job_posting: JobPosting):
    position, company_url, job_posting_url, search_query, region = job_posting.position, job_posting.company_link, job_posting.job_posting_link, job_posting.search_query, job_posting.region

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
                "type": "url",
                "url": company_url
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