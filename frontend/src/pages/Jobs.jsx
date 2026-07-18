import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api
      .get("/jobs")
      .then((response) => {
        setJobs(response.data.jobs);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching jobs:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <h3>Loading jobs...</h3>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Available Jobs</h2>

      <div className="row">
        {jobs.map((job) => (
          <div className="col-md-4 mb-4" key={job.id}>
            <div className="card shadow-sm h-100">
              <div className="card-body">
                <h5>{job.title}</h5>

                <p className="text-muted">{job.company}</p>

                <p>📍 {job.location}</p>

                <p>
                  <strong>Experience:</strong> {job.experience}
                </p>

                <p>
                  <strong>Job Type:</strong> {job.job_type}
                </p>

                <p className="text-success fw-bold">
                  ₹{job.min_salary} - ₹{job.max_salary}
                </p>

                <Link
                  to={`/jobs/${job.id}`}
                  className="btn btn-primary w-100"
                >
                  View Details
                </Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Jobs;