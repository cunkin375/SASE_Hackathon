from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
from typing import Literal, List
from backend.connect import get_job_listings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"], # Vite default port
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

# ---------- Get API Declarations ----------

@app.get("/")
async def read_root():
    return {"message": "Welcome to the job search API!"}

@app.get("/jobs/search")
async def search_jobs(company: str = None, title: str = None,
                      pay_period: str = None, min_wage: int = None,
                      location: str = None, limit: int = 10
                      ) -> List[JobOutput]:
    try:
        jobs = get_job_listings(company = company, title = title,
                                pay_period = pay_period, min_wage = min_wage,
                                location = location, limit = limit)
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

@app.get("/health")
async def health_check():
    try:
        from backend.connect import Session, Company, JobListing
        session = Session()
        company_count = session.query(Company).count()
        job_listing_count = session.query(JobListing).count()
        session.close()
        return { "Status" : "healthy",
                 "companies_count": company_count,
                 "job_listings": job_listing_count }
    except Exception as error:
        raise HTTPException(status_code = 500, detail = f"Database connection failed: {error}")

# ---------- Set API Declarations ----------

@app.post("/jobs/")
async def create_job(job: JobInput) -> List[JobOutput]:
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

