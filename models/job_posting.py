from dataclasses import dataclass

@dataclass
class JobPosting:
    position: str
    company_link: str
    job_posting_link: str
    search_query: str
    region: str