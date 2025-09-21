import Button from './Button';
import "../App.css";

function JobInfo(props) {
    return (
        <div className={props.className}>
            <h2>Job: {props.title}</h2>
            <p>Company: {props.company}</p>
            <p>Location: {props.location}</p>
            <p>Salary: ${props.salary}</p>
            <p>Wage Type: {props.wageType}</p>

            <Button className="App-button" name="Description" />
        </div>
    )
}

export default JobInfo;