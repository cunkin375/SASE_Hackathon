import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload
from typing import List, Optional

conn_string = 'postgresql://neondb_owner:npg_zEbPwa1MH4yn@ep-quiet-art-ad4atrd6-pooler.c-2.us-east-1.aws.neon.tech/relational?sslmode=require&channel_binding=require'

engine = create_engine(conn_string)
Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    company_id = Column(Integer, primary_key=True)
    company_name = Column(String)
    job_listings = relationship("JobListing", back_populates="company")

class JobListing(Base):
    __tablename__ = 'job_listings'
    job_id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.company_id'))
    title = Column(String)
    max_salary = Column(String)
    pay_period = Column(String)
    job_location = Column(String)
    company = relationship("Company", back_populates="job_listings")
    
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def get_job_listings(company: Optional[str] = None, title: Optional[str] = None) -> List[JobListing]:
    session = Session()
    try: 
        query = session.query(JobListing).options(joinedload(JobListing.company))
        if company:
            query = query.join(Company).filter(Company.company_name.ilike(f"%{company}%"))
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
        
def get_jobs_by_salary_range(min_salary: Optional[int] = None, max_salary: Optional[int] = None) -> List[JobListing]:
    session = Session()
    try:
        query = session.query(JobListing).options(joinedload(JobListing.company))
        # TODO: Add actual salary filtering logic here if needed
        # if min_salary:
        #     query = query.filter(JobListing.max_salary >= min_salary)
        # if max_salary:
        #     query = query.filter(JobListing.max_salary <= max_salary)
        return query.all()
    except psycopg2.OperationalError as error:
        print(f"Connection failed: {error}")
        raise error
    except Exception as error:
        print(f"Database error: {error}")
        raise error
    finally:
        session.close()
