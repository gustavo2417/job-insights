from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    all_industries = read(path)
    industries = []

    for indus in all_industries:
        if indus["industry"] not in industries and len(indus["industry"]) > 1:
            industries.append(indus["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    all_jobs_industry = []
    for job in jobs:
        if job["industry"] == industry:
            all_jobs_industry.append(job)

    return all_jobs_industry
