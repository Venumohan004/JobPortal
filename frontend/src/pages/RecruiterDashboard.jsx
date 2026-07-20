import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/dashboard.css";

const API = "https://jobportal-aver.onrender.com";

function RecruiterDashboard() {
  const [profile, setProfile] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem("token");

      if (!token) {
        setError("Please login first.");
        return;
      }

      try {
        // Recruiter profile
        const profileRes = await axios.get(`${API}/recruiter/profile`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        setProfile(profileRes.data);

        // Recruiter jobs with application counts
        const jobsRes = await axios.get(
          `${API}/recruiter/jobs/applications`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        setJobs(jobsRes.data);

      } catch (err) {
        console.error(err);
        setError(err.response?.data?.msg || "Failed to load dashboard");
      }
    };

    fetchData();
  }, []);

  // Calculate totals
  const totalJobs = jobs.length;
  const totalApplications = jobs.reduce(
    (sum, job) => sum + job.applications,
    0
  );

  return (
    <div className="dashboard-container">
      <h1>Recruiter Dashboard</h1>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {profile ? (
        <>
          {/* Stats Cards */}
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Company</h3>
              <p>{profile.company_name}</p>
            </div>

            <div className="stat-card">
              <h3>Total Jobs</h3>
              <p>{totalJobs}</p>
            </div>

            <div className="stat-card">
              <h3>Applications</h3>
              <p>{totalApplications}</p>
            </div>

            <div className="stat-card">
              <h3>Active Jobs</h3>
              <p>{totalJobs}</p>
            </div>
          </div>

          {/* Profile */}
          <div className="profile-card">
            <h2>{profile.company_name}</h2>
            <p><strong>Email:</strong> {profile.email || "Not provided"}</p>
            <p><strong>Industry:</strong> {profile.industry || "Not provided"}</p>
            <p><strong>Website:</strong> {profile.website || "Not provided"}</p>
          </div>

          {/* Posted Jobs */}
          <div className="jobs-section">
            <h2>Posted Jobs</h2>

            {jobs.length > 0 ? (
              <table className="jobs-table">
                <thead>
                  <tr>
                    <th>Job Title</th>
                    <th>Company</th>
                    <th>Applications</th>
                  </tr>
                </thead>

                <tbody>
                  {jobs.map((job) => (
                    <tr key={job.job_id}>
                      <td>{job.title}</td>
                      <td>{job.company}</td>
                      <td>{job.applications}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <p>No jobs posted yet.</p>
            )}
          </div>
        </>
      ) : (
        !error && <p>Loading...</p>
      )}
    </div>
  );
}

export default RecruiterDashboard;