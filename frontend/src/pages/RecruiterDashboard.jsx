import { useEffect, useState } from "react";
import api from "../services/api";
import "../styles/dashboard.css";
import { Link } from "react-router-dom";

function RecruiterDashboard() {
  const [profile, setProfile] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      setLoading(true);
      setError("");

      // Recruiter profile
      const profileRes = await api.get("/recruiter/profile");
      setProfile(profileRes.data);

      // Jobs with application counts
      const jobsRes = await api.get("/recruiter/jobs/applications");
      setJobs(jobsRes.data || []);

    } catch (err) {
      console.error(err);

      const status = err.response?.status;
      const message =
        err.response?.data?.message ||
        err.response?.data?.msg ||
        "Failed to load dashboard";

      if (status === 404) {
        setError(
          "Recruiter profile not found. Please create your recruiter profile first."
        );
      } else if (status === 403) {
        setError("Access denied. Please login as a recruiter.");
      } else if (status === 401) {
        setError("Session expired. Please login again.");
      } else {
        setError(message);
      }
    } finally {
      setLoading(false);
    }
  };

  // Calculate totals
  const totalJobs = jobs.length;
  const totalApplications = jobs.reduce(
    (sum, job) => sum + (job.applications || 0),
    0
  );

  if (loading) {
    return (
      <div className="dashboard-container">
        <h1>Recruiter Dashboard</h1>
        <p>Loading dashboard...</p>
      </div>
    );
  }

  return (
    <div className="dashboard-container">
      <h1>Recruiter Dashboard</h1>
          <Link to="/create-job" className="btn btn-primary">
            + Post New Job
          </Link>
      {error && (
        <div className="alert alert-warning">
          {error}
        </div>
      )}

      {profile && (
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
              <h3>Total Applications</h3>
              <p>{totalApplications}</p>
            </div>

            <div className="stat-card">
              <h3>Active Jobs</h3>
              <p>{totalJobs}</p>
            </div>
          </div>

          {/* Company Profile */}
          <div className="profile-card">
            <h2>{profile.company_name}</h2>

            <p>
              <strong>Email:</strong>{" "}
              {profile.company_email || "Not provided"}
            </p>

            <p>
              <strong>Location:</strong>{" "}
              {profile.company_location || "Not provided"}
            </p>

            <p>
              <strong>Website:</strong>{" "}
              {profile.company_website ? (
                <a
                  href={profile.company_website}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {profile.company_website}
                </a>
              ) : (
                "Not provided"
              )}
            </p>
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
      )}
    </div>
  );
}

export default RecruiterDashboard;