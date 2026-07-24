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

  // Delete job
  const handleDelete = async (jobId) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this job?"
    );

    if (!confirmDelete) return;

    try {
      await api.delete(`/jobs/${jobId}`);

      // Remove from UI instantly
      setJobs(jobs.filter((job) => job.job_id !== jobId));

      alert("Job deleted successfully!");
    } catch (err) {
      console.error(err);
      alert(
        err.response?.data?.message || "Failed to delete job"
      );
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
      {/* Header */}
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>Recruiter Dashboard</h1>

        <Link to="/create-job" className="btn btn-primary">
          + Post New Job
        </Link>
      </div>

      {/* Error */}
      {error && (
        <div className="alert alert-warning">
          {error}
        </div>
      )}

      {/* Main Content */}
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
                    <th>Actions</th>
                  </tr>
                </thead>

                <tbody>
                  {jobs.map((job) => (
                    <tr key={job.job_id}>
                      <td>{job.title}</td>
                      <td>{job.company}</td>
                      <td>{job.applications}</td>

                      <td>
                        {/* Edit */}
                        <Link
                          to={`/edit-job/${job.job_id}`}
                          className="btn btn-warning btn-sm me-2"
                        >
                          Edit
                        </Link>

                        {/* Applicants */}
                        <Link
                          to={`/job/${job.job_id}/applicants`}
                          className="btn btn-info btn-sm me-2"
                        >
                          Applicants
                        </Link>

                        {/* Delete */}
                        <button
                          className="btn btn-danger btn-sm"
                          onClick={() => handleDelete(job.job_id)}
                        >
                          Delete
                        </button>
                      </td>
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