import { Link } from "react-router-dom";

function JobCard({ job }) {
  return (
    <div className="card shadow-sm h-100">
      <div className="card-body d-flex flex-column">
        <h5 className="card-title">{job.title}</h5>
        <h6 className="card-subtitle mb-2 text-muted">{job.company}</h6>

        <p className="mb-1">
          <strong>Location:</strong> {job.location}
        </p>

        <p className="mb-1">
          <strong>Salary:</strong> ₹{job.min_salary} - ₹{job.max_salary}
        </p>

        <p className="mb-3">
          <strong>Type:</strong> {job.job_type}
        </p>

        <Link
          to={`/jobs/${job.id}`}
          className="btn btn-primary mt-auto"
        >
          View Details
        </Link>
      </div>
    </div>
  );
}

export default JobCard;