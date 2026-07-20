import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/dashboard.css";

const API = "https://jobportal-aver.onrender.com";

function SavedJobs() {
  const [jobs, setJobs] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchSavedJobs = async () => {
      const token = localStorage.getItem("token");

      if (!token) {
        setError("Please login first.");
        return;
      }

      try {
        const res = await axios.get(`${API}/candidate/saved-jobs`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        console.log("Saved jobs response:", res.data);

        // Important: jobs are inside res.data.jobs
        setJobs(res.data.jobs || []);

      } catch (err) {
        console.error(err);
        setError("Failed to load saved jobs");
      }
    };

    fetchSavedJobs();
  }, []);

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
            {jobs.map((job) => (
              <tr key={job.id}>
                <td>{job.title}</td>
                <td>{job.company}</td>
                <td>{job.location}</td>
                <td>
                  ₹{job.min_salary?.toLocaleString()} - ₹{job.max_salary?.toLocaleString()}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        !error && <p>No saved jobs yet.</p>
      )}
    </div>
  );
}

export default SavedJobs;