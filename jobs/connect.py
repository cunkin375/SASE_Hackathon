import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import List, Optional

conn_string = 'postgresql://neondb_owner:npg_zEbPwa1MH4yn@ep-quiet-art-ad4atrd6-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

engine = create_engine(conn_string)
Base = declarative_base()

class JobListing(Base):
    __tablename__ = 'job'
    job_id = Column(Integer, primary_key = True)
    company_name = Column(String)
    title = Column(String)
    max_salary = Column(String)
    pay_period = Column(String)
    job_location = Column(String)
    
Session = sessionmaker(bind=engine)

def get_job_listings(company: Optional[str] = None, title: Optional[str] = None) -> List[JobListing]:
    session = Session()
    try: 
        query = session.query(JobListing)
        if company:
            query = query.filter(JobListing.company_name.ilike(f"%{company}%"))
        if title:
            query = query.filter(JobListing.title.ilike(f"%{title}%"))
        return query.all()
    except psycopg2.OperationalError as error:
        print(f"Connection failed: {error}")
        raise error
    except Exception as error:
        print(f"Database error: {error}")
        raise error
    finally:
        session.close()
        
def get_jobs_by_salary_range(min_salary: Optional[int] = None, max_salaryu: Optional[int] = None) -> List[JobListing]:
    session = Session()
    try:
        query = session.query(JobListing).order_by(JobListing.max_salary.desc())
        return query.all()
    except psycopg2.OperationalError as error:
        print(f"Connection failed: {error}")
        raise error
    except Exception as error:
        print(f"Database error: {error}")
        raise error
    finally:
        session.close()

