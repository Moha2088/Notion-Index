from dataclasses import dataclass

@dataclass
class JobPosting:
    position: str
    company_name: str
    job_posting_link: str
    search_query: str
    region: str