from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
from typing import Literal, List
from backend.connect import get_job_listings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

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
async def search_jobs(company: str = None, title: str = None,pay_period: str = None, min_wage: int = None ) -> List[JobOutput]:
    """TEMP: Search for jobs by company or title"""
    try:
        jobs = get_job_listings(company=company, title=title,pay_period=pay_period,min_wage=min_wage)
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
    

# @app.post("/jobs/")
# async def create_job(job: JobInput) -> List[JobOutput]:
#     try:
#         jobs = get_job_listings()
#         return [JobOutput(
#             job_id = job.job_id,
#             company_name = job.company.company_name,
#             title = job.title,
#             max_salary = job.max_salary,
#             pay_period = job.pay_period,
#             job_location = job.job_location
#         ) for job in jobs]
#     except Exception as error:
#         raise HTTPException(status_code = 500, detail = str(error))
