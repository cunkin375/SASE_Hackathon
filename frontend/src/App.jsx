import "./App.css";
import { useState } from "react";
import { jobsAPI } from './services/JobsAPI';
import Button from './components/Button';
import InputBox from './components/InputBox';
import JobInfo from './components/JobInfo';

function App() {
    const [title, setTitle] = useState("");
    const [salary, setSalary] = useState("");
    const [location, setLocation] = useState("");
    const [company, setCompany] = useState("");
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchJobs = async (searchParams = {}) => {
        setLoading(true);
        setError(null);
        try {
            const jobsData = await jobsAPI.searchJobs(searchParams);
            setJobs(jobsData);
        } catch (error) {
            setError('Failed to fetch jobs');
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log('Searching with:', { title, salary, location, company });

        const searchParams = {};
        if (title.trim()) searchParams.title = title.trim();
        if (company.trim()) searchParams.company = company.trim();
        if (salary.trim()) searchParams.min_wage = parseInt(salary);
        await fetchJobs(searchParams);
    };

    const loadAllJobs = async () => {
        await fetchJobs();
    }

    return (
        <div>
            <h1 className="App-header">
                J*b Elephant
            </h1>

            <form onSubmit={handleSubmit}>
                <InputBox 
                    className="App-inputBox"
                    htmlFor="job-search" 
                    type="text" 
                    placeholder="Job Role" 
                    onChange={(event) => setTitle(event.target.value)} 
                />
                <InputBox 
                    className="App-inputBox" 
                    htmlFor="salary-search" 
                    type="text" 
                    placeholder="Salary" 
                    onChange={(event) => setSalary(event.target.value)} 
                />
                <InputBox 
                    className="App-inputBox" 
                    htmlFor="location-search" 
                    type="text" 
                    placeholder="Location" 
                    onChange={(event) => setLocation(event.target.value)} 
                />
                <InputBox 
                    className="App-inputBox" 
                    htmlFor="company-search" 
                    type="text" placeholder="Company" 
                    onChange={(event) => setCompany(event.target.value)} 
                />

                <button className="App-button" type="submit">
                    Search Jobs
                </button>

            </form>

            {loading && <div>Loading jobs...</div>}
            {error && <div>Error: {error}</div>}

            <div>
                {jobs.length === 0 && !loading ? (
                    <p>No jobs found.</p> 
                ) : (
                    jobs.map((job) => (
                        <JobInfo
                            key={job.job_id}
                            className="App-jobInfo"
                            title={job.title}
                            company={job.company_name}
                            location={job.job_location}
                            salary={job.max_salary}
                            wageType={job.pay_period}
                        />
                    ))
                )}
            </div>

            <Button 
                className="App-button" 
                name="Load More Jobs" 
                onClick={loadAllJobs}
            />
        </div>
    )
}

export default App
