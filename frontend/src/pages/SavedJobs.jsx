import { useEffect, useState } from "react";
import api from "../services/api";
import "../styles/dashboard.css";

function SavedJobs() {
  const [jobs, setJobs] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSavedJobs = async () => {
      const token = localStorage.getItem("token");
      const role = localStorage.getItem("role");

      if (!token) {
        setError("Please login first.");
        setLoading(false);
        return;
      }

      // Saved jobs are only for candidates
      if (role !== "candidate") {
        setError("Saved jobs are available only for candidates.");
        setLoading(false);
        return;
      }

      try {
        const res = await api.get("/saved-jobs");

        console.log("Saved jobs response:", res.data);

        // Backend returns { count, saved_jobs }
        setJobs(res.data.saved_jobs || []);
      } catch (err) {
        console.error(err);

        if (err.response?.status === 403) {
          setError("Access denied. Please login as a candidate.");
        } else {
          setError("Failed to load saved jobs.");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchSavedJobs();
  }, []);

  if (loading) {
    return (
      <div className="dashboard-container">
        <h1>Saved Jobs</h1>
        <p>Loading saved jobs...</p>
      </div>
    );
  }

  return (
    <div className="dashboard-container">
      <h1>Saved Jobs</h1>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {jobs.length > 0 ? (
        <table className="jobs-table">
          <thead>
            <tr>
              <th>Title</th>
              <th>Company</th>
              <th>Location</th>
              <th>Salary</th>
            </tr>
          </thead>

          <tbody>
            {jobs.map((savedJob) => {
              // savedJob may contain nested job object
              const job = savedJob.job || savedJob;

              return (
                <tr key={savedJob.id}>
                  <td>{job.title}</td>
                  <td>{job.company}</td>
                  <td>{job.location}</td>
                  <td>
                    ₹{job.min_salary?.toLocaleString()} - ₹{job.max_salary?.toLocaleString()}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      ) : (
        !error && <p>No saved jobs yet.</p>
      )}
    </div>
  );
}

export default SavedJobs;