import React, { useState, useEffect } from 'react';
import { jobsAPI } from '../services/JobsAPI';
import JobInfo from './JobInfo';

const JobList = () => {
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

    // Fetch every job on component mount
    useEffect(() =>  {
        fetchJobs();
    }, []);

    if (loading) return <div>Loading jobs...</div>;
    if (error) return <div>Error: {error}</div>

    return (
        <div>
            {jobs.length === 0 ? (
                <p>No jobs found!</p>
            ) : (
                jobs.map((job) => (
                    <JobInfo
                        key={job.job_id}
                        className="App-jobInfo"
                        title={job.title}
                        company={job.company}
                        location={job.location}
                        salary={job.max_salary}
                        wageType={job.pay_period}
                    />
                ))
            )}
        </div>
    );
};