from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    data = []
    with open(path, encoding="utf-8") as file:
        jobs = csv.DictReader(file, delimiter=",")

        for job in jobs:
            data.append(job)

    return data


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    types = []

    for job in jobs:
        if job["job_type"] in types:
            0
        else:
            types.append(job["job_type"])
    return types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    all_jobs_of_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            all_jobs_of_type.append(job)

    return all_jobs_of_type
