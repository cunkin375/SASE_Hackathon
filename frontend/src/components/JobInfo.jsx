import Button from './Button';
import "../App.css";

function JobInfo(job) {
    return (
        <div className={job.className}>
            <h2>Job: {job.title}</h2>
            <p>Company: {job.company}</p>
            <p>Location: {job.location}</p>
            <p>Salary: ${job.salary}</p>
            <p>Wage Type: {job.wageType}</p>

            <Button className="App-button" name="Description" />
        </div>
    )
}

export default JobInfo;