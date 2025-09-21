import "./App.css";
import { useState } from "react";
import Jobs from "./sample_jobs.json";
import Button from './components/Button';
import InputBox from './components/InputBox';
import JobInfo from './components/JobInfo';

function App() {
  const [title, setTitle] = useState("");
  const [salary, setSalary] = useState("");
  const [location, setLocation] = useState("");
  const [company, setCompany] = useState("");

  const jobInfo = [];

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(title, salary, location, company);
  }

  return (
    <div>
      <h1 className="App-header">
        J*b Finding
      </h1>

      <form onSubmit={handleSubmit}>
        <InputBox className="App-inputBox" label="Search Jobs: " htmlFor="job-search" type="text" placeholder="Enter job title" onChange={(e) => setTitle(e.target.value)} />
        <InputBox className="App-inputBox" label="Salary: " htmlFor="salary-search" type="text" placeholder="Enter salary" onChange={(e) => setSalary(e.target.value)} />
        <InputBox className="App-inputBox" label="Location: " htmlFor="location-search" type="text" placeholder="Enter location" onChange={(e) => setLocation(e.target.value)} />
        <InputBox className="App-inputBox" label="Company: " htmlFor="company-search" type="text" placeholder="Enter company name" onChange={(e) => setCompany(e.target.value)} />

        <button className="App-button" type="submit">
          Submit
        </button>
      </form>

      <div>
        {Jobs.map((job) => (
          <JobInfo
            className="App-jobInfo"
            title={job.title}
            company={job.company_name}
            location={job.job_location}
            salary={job.max_salary}
            wageType={job.pay_period}
          />
        ))
        }
      </div>

      <Button className="App-button" name="Load More Jobs" />
    </div>
  )
}

export default App
