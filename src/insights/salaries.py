from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_salary = read(path)
    salaries = []

    for curr in jobs_salary:
        if len(curr["max_salary"]) > 1 and curr["max_salary"] != "invalid":
            salaries.append(int(curr["max_salary"]))

    return max(salaries)


def get_min_salary(path: str) -> int:
    jobs_salary = read(path)
    salaries = []

    for curr in jobs_salary:
        if len(curr["min_salary"]) > 1 and curr["min_salary"] != "invalid":
            salaries.append(int(curr["min_salary"]))

    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
            return True
        else:
            return False
    except (KeyError, TypeError, ValueError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    all_jobs_filtered = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                all_jobs_filtered.append(job)
        except (ValueError):
            0

    return all_jobs_filtered
