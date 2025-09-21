from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import Literal, List
from connect import get_job_listings

app = FastAPI()

class JobInput(BaseModel):
    role: str
    company: str
    location: str
    wage_type: Literal["HOURLY","YEARLY"]
    wage: int
    
class JobOutput(BaseModel):
    job_id: int
    company_name: str
    title: str
    max_salary: str
    pay_period: str
    job_location: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the job search API!"}

@app.get("/jobs/search")
async def search_jobs(company: str = None, title: str = None) -> List[JobOutput]:
    """TEMP: Search for jobs by company or title"""
    try:
        jobs = get_job_listings(company=company, title=title)
        return [JobOutput(
            job_id = job.job_id,
            company_name = job.company.company_name,
            title = job.title,
            max_salary = job.max_salary,
            pay_period = job.pay_period,
            job_location = job.job_location
        ) for job in jobs]
    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
    
@app.post("/jobs/")
async def create_job(job: JobInput) -> List[JobOutput]:
    """Get all job listings"""
    try:
        jobs = get_job_listings()
        return [JobOutput(
            job_id = job.job_id,
            company_name = job.company.company_name,
            title = job.title,
            max_salary = job.max_salary,
            pay_period = job.pay_period,
            job_location = job.job_location
        ) for job in jobs]
    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
