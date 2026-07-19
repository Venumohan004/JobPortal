import { useEffect, useState } from "react";
import api from "../services/api";
import JobCard from "../components/jobs/JobCard";

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchJobs();
  }, []);

  const fetchJobs = async () => {
    try {
      setLoading(true);

      const response = await api.get("/jobs");

      // Your backend returns { jobs: [...], total_jobs: ... }
      setJobs(response.data.jobs || []);
    } catch (err) {
      console.error(err);
      setError("Failed to load jobs");
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container py-5 text-center">
        <h4>Loading jobs...</h4>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container py-5 text-center">
        <div className="alert alert-danger">{error}</div>
      </div>
    );
  }

  return (
    <div className="container py-5">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>Available Jobs</h2>

        <span className="badge bg-primary fs-6">
          {jobs.length} Jobs
        </span>
      </div>

      {jobs.length === 0 ? (
        <div className="alert alert-info">
          No jobs available.
        </div>
      ) : (
        <div className="row g-4">
          {jobs.map((job) => (
            <div className="col-md-6 col-lg-4" key={job.id}>
              <JobCard job={job} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Jobs;