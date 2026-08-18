import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "../styles/dashboard.css";

const API = "https://jobportal-aver.onrender.com";

function AdminDashboard() {
  const navigate = useNavigate();

  const [stats, setStats] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // Show all jobs / applications
  const [showAllJobs, setShowAllJobs] = useState(false);
  const [allJobs, setAllJobs] = useState([]);

  const [showAllApplications, setShowAllApplications] = useState(false);
  const [allApplications, setAllApplications] = useState([]);

  // ============================================================
  // GET ADMIN DASHBOARD
  // ============================================================

  const fetchStats = async () => {
    const token = localStorage.getItem("token");

    if (!token) {
      setError("Please login first.");
      setLoading(false);
      return;
    }

    try {
      setLoading(true);
      setError("");

      const res = await axios.get(`${API}/admin/dashboard`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      console.log("Admin dashboard response:", res.data);

      setStats(res.data);
    } catch (err) {
      console.error("Admin dashboard error:", err);

      setError(
        err.response?.data?.message ||
          err.response?.data?.msg ||
          "Failed to load admin dashboard"
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStats();
  }, []);

  // ============================================================
  // SHOW ALL JOBS
  // ============================================================

  const handleShowAllJobs = async () => {
    const token = localStorage.getItem("token");

    if (!token) {
      alert("Please login first.");
      return;
    }

    try {
      setActionLoading(true);

      const response = await axios.get(`${API}/admin/jobs`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      console.log("All jobs response:", response.data);

      setAllJobs(response.data.jobs || []);
      setShowAllJobs(true);
    } catch (err) {
      console.error("Failed to load all jobs:", err);

      alert(
        err.response?.data?.message ||
          err.response?.data?.msg ||
          "Failed to load all jobs"
      );
    } finally {
      setActionLoading(false);
    }
  };

  // ============================================================
  // SHOW RECENT JOBS
  // ============================================================

  const handleShowRecentJobs = () => {
    setShowAllJobs(false);
  };

  // ============================================================
  // SHOW ALL APPLICATIONS
  // ============================================================

  const handleShowAllApplications = async () => {
    const token = localStorage.getItem("token");

    if (!token) {
      alert("Please login first.");
      return;
    }

    try {
      setActionLoading(true);

      const response = await axios.get(`${API}/admin/applications`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      console.log("All applications response:", response.data);

      setAllApplications(response.data.applications || []);
      setShowAllApplications(true);
    } catch (err) {
      console.error("Failed to load all applications:", err);

      alert(
        err.response?.data?.message ||
          err.response?.data?.msg ||
          "Failed to load all applications"
      );
    } finally {
      setActionLoading(false);
    }
  };

  // ============================================================
  // SHOW RECENT APPLICATIONS
  // ============================================================

  const handleShowRecentApplications = () => {
    setShowAllApplications(false);
  };

  // ============================================================
  // DELETE USER
  // ============================================================

  const handleDeleteUser = async (userId, role) => {
    if (role === "admin") {
      alert("Admin account cannot be deleted.");
      return;
    }

    const confirmed = window.confirm(
      "Are you sure you want to delete this user?"
    );

    if (!confirmed) {
      return;
    }

    const token = localStorage.getItem("token");

    try {
      setActionLoading(true);

      await axios.delete(`${API}/admin/users/${userId}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      alert("User deleted successfully.");

      await fetchStats();
    } catch (err) {
      console.error("Delete user error:", err);

      alert(
        err.response?.data?.message ||
          "Failed to delete user"
      );
    } finally {
      setActionLoading(false);
    }
  };

  // ============================================================
  // DELETE JOB
  // ============================================================

  const handleDeleteJob = async (jobId) => {
    const confirmed = window.confirm(
      "Are you sure you want to delete this job?\n\nAll applications for this job will also be deleted."
    );

    if (!confirmed) {
      return;
    }

    const token = localStorage.getItem("token");

    try {
      setActionLoading(true);

      await axios.delete(`${API}/admin/jobs/${jobId}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      // Remove from all-jobs list immediately
      setAllJobs((prevJobs) =>
        prevJobs.filter((job) => job.id !== jobId)
      );

      alert("Job deleted successfully.");

      // Refresh dashboard statistics/recent jobs
      await fetchStats();
    } catch (err) {
      console.error("Delete job error:", err);

      alert(
        err.response?.data?.message ||
          "Failed to delete job"
      );
    } finally {
      setActionLoading(false);
    }
  };

  // ============================================================
  // DELETE APPLICATION
  // ============================================================

  const handleDeleteApplication = async (applicationId) => {
    const confirmed = window.confirm(
      "Are you sure you want to delete this application?"
    );

    if (!confirmed) {
      return;
    }

    const token = localStorage.getItem("token");

    try {
      setActionLoading(true);

      await axios.delete(
        `${API}/admin/applications/${applicationId}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      // Remove from all-applications list immediately
      setAllApplications((prevApplications) =>
        prevApplications.filter(
          (application) => application.id !== applicationId
        )
      );

      alert("Application deleted successfully.");

      // Refresh dashboard statistics/recent applications
      await fetchStats();
    } catch (err) {
      console.error("Delete application error:", err);

      alert(
        err.response?.data?.message ||
          "Failed to delete application"
      );
    } finally {
      setActionLoading(false);
    }
  };

  // ============================================================
  // LOADING
  // ============================================================

  if (loading) {
    return (
      <div className="dashboard-container">
        <h1>Admin Dashboard</h1>
        <p>Loading dashboard...</p>
      </div>
    );
  }

  // ============================================================
  // ERROR
  // ============================================================

  if (error && !stats) {
    return (
      <div className="dashboard-container">
        <h1>Admin Dashboard</h1>

        <div className="alert alert-danger">
          {error}
        </div>

        <button
          className="btn btn-primary"
          onClick={fetchStats}
        >
          Retry
        </button>
      </div>
    );
  }

  // ============================================================
  // DASHBOARD
  // ============================================================

  return (
    <div className="dashboard-container">

      {/* ======================================================
          HEADER
      ====================================================== */}

      <div className="d-flex justify-content-between align-items-center mb-4">

        <div>
          <h1>Admin Dashboard</h1>

          <p className="text-muted">
            Manage users, jobs and applications
          </p>
        </div>

        <div className="d-flex gap-2">

          <button
            className="btn btn-outline-primary"
            onClick={fetchStats}
            disabled={actionLoading}
          >
            🔄 Refresh
          </button>

          <button
            className="btn btn-primary"
            onClick={() => navigate("/create-job")}
          >
            ➕ Add Job
          </button>

        </div>

      </div>

      {/* ======================================================
          ERROR MESSAGE
      ====================================================== */}

      {error && (
        <div className="alert alert-danger">
          {error}
        </div>
      )}

      {/* ======================================================
          STATISTICS
      ====================================================== */}

      {stats && (
        <>

          <div className="stats-grid">

            <div className="stat-card">
              <h3>Total Users</h3>
              <p>
                {stats.statistics.total_users}
              </p>
            </div>

            <div className="stat-card">
              <h3>Total Jobs</h3>
              <p>
                {stats.statistics.total_jobs}
              </p>
            </div>

            <div className="stat-card">
              <h3>Total Applications</h3>
              <p>
                {stats.statistics.total_applications}
              </p>
            </div>

            <div className="stat-card">
              <h3>Total Recruiters</h3>
              <p>
                {stats.statistics.total_recruiters}
              </p>
            </div>

          </div>

          {/* ==================================================
              USERS
          ================================================== */}

          <div className="jobs-section">

            <div className="d-flex justify-content-between align-items-center mb-3">

              <h2>Recent Users</h2>

              <span className="badge bg-primary">
                {stats.latest_users.length} users
              </span>

            </div>

            <div className="table-responsive">

              <table className="jobs-table">

                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Role</th>
                    <th>Action</th>
                  </tr>
                </thead>

                <tbody>

                  {stats.latest_users.length > 0 ? (

                    stats.latest_users.map((user) => (

                      <tr key={user.id}>

                        <td>
                          {user.id}
                        </td>

                        <td>
                          {user.full_name}
                        </td>

                        <td>
                          {user.email}
                        </td>

                        <td>
                          <span
                            className={`badge ${
                              user.role === "admin"
                                ? "bg-danger"
                                : user.role === "recruiter"
                                ? "bg-success"
                                : "bg-secondary"
                            }`}
                          >
                            {user.role}
                          </span>
                        </td>

                        <td>

                          {user.role === "admin" ? (

                            <button
                              className="btn btn-sm btn-secondary"
                              disabled
                            >
                              Protected
                            </button>

                          ) : (

                            <button
                              className="btn btn-sm btn-danger"
                              onClick={() =>
                                handleDeleteUser(
                                  user.id,
                                  user.role
                                )
                              }
                              disabled={actionLoading}
                            >
                              🗑 Delete
                            </button>

                          )}

                        </td>

                      </tr>

                    ))

                  ) : (

                    <tr>
                      <td
                        colSpan="5"
                        className="text-center"
                      >
                        No users found
                      </td>
                    </tr>

                  )}

                </tbody>

              </table>

            </div>

          </div>

          {/* ==================================================
              JOBS
          ================================================== */}

          <div className="jobs-section">

            <div className="d-flex justify-content-between align-items-center mb-3">

              <div className="d-flex align-items-center gap-3">

                <h2 className="mb-0">
                  {showAllJobs
                    ? "All Jobs"
                    : "Recent Jobs"}
                </h2>

                <span className="badge bg-primary">
                  {showAllJobs
                    ? `${allJobs.length} jobs`
                    : `${stats.latest_jobs.length} recent`}
                </span>

              </div>

              <div className="d-flex gap-2">

                {/* Show All / Recent */}

                {!showAllJobs ? (

                  <button
                    className="btn btn-outline-primary"
                    onClick={handleShowAllJobs}
                    disabled={actionLoading}
                  >
                    📋 Show All Jobs
                  </button>

                ) : (

                  <button
                    className="btn btn-outline-secondary"
                    onClick={handleShowRecentJobs}
                    disabled={actionLoading}
                  >
                    ↩ Show Recent Jobs
                  </button>

                )}

                {/* Add Job */}

                <button
                  className="btn btn-success"
                  onClick={() =>
                    navigate("/create-job")
                  }
                  disabled={actionLoading}
                >
                  ➕ Add Job
                </button>

              </div>

            </div>

            <div className="table-responsive">

              <table className="jobs-table">

                <thead>

                  <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Company</th>
                    <th>Location</th>
                    <th>Action</th>
                  </tr>

                </thead>

                <tbody>

                  {(showAllJobs
                    ? allJobs
                    : stats.latest_jobs
                  ).length > 0 ? (

                    (showAllJobs
                      ? allJobs
                      : stats.latest_jobs
                    ).map((job) => (

                      <tr key={job.id}>

                        <td>
                          {job.id}
                        </td>

                        <td>
                          {job.title}
                        </td>

                        <td>
                          {job.company}
                        </td>

                        <td>
                          {job.location}
                        </td>

                        <td>

                          <button
                            className="btn btn-sm btn-danger"
                            onClick={() =>
                              handleDeleteJob(
                                job.id
                              )
                            }
                            disabled={actionLoading}
                          >
                            🗑 Delete
                          </button>

                        </td>

                      </tr>

                    ))

                  ) : (

                    <tr>
                      <td
                        colSpan="5"
                        className="text-center"
                      >
                        No jobs found
                      </td>
                    </tr>

                  )}

                </tbody>

              </table>

            </div>

          </div>

          {/* ==================================================
              APPLICATIONS
          ================================================== */}

          <div className="jobs-section">

            <div className="d-flex justify-content-between align-items-center mb-3">

              <div className="d-flex align-items-center gap-3">

                <h2 className="mb-0">
                  {showAllApplications
                    ? "All Applications"
                    : "Recent Applications"}
                </h2>

                <span className="badge bg-primary">
                  {showAllApplications
                    ? `${allApplications.length} applications`
                    : `${stats.latest_applications?.length || 0} recent`}
                </span>

              </div>

              <div>

                {!showAllApplications ? (

                  <button
                    className="btn btn-outline-primary"
                    onClick={handleShowAllApplications}
                    disabled={actionLoading}
                  >
                    📋 Show All Applications
                  </button>

                ) : (

                  <button
                    className="btn btn-outline-secondary"
                    onClick={handleShowRecentApplications}
                    disabled={actionLoading}
                  >
                    ↩ Show Recent Applications
                  </button>

                )}

              </div>

            </div>

            <div className="table-responsive">

              <table className="jobs-table">

                <thead>

                  <tr>
                    <th>ID</th>
                    <th>Candidate ID</th>
                    <th>Job ID</th>
                    <th>Status</th>
                    <th>Action</th>
                  </tr>

                </thead>

                <tbody>

                  {(showAllApplications
                    ? allApplications
                    : stats.latest_applications || []
                  ).length > 0 ? (

                    (showAllApplications
                      ? allApplications
                      : stats.latest_applications || []
                    ).map((application) => (

                      <tr key={application.id}>

                        <td>
                          {application.id}
                        </td>

                        <td>
                          {application.candidate_id}
                        </td>

                        <td>
                          {application.job_id}
                        </td>

                        <td>
                          <span className="badge bg-info">
                            {application.status}
                          </span>
                        </td>

                        <td>

                          <button
                            className="btn btn-sm btn-danger"
                            onClick={() =>
                              handleDeleteApplication(
                                application.id
                              )
                            }
                            disabled={actionLoading}
                          >
                            🗑 Delete
                          </button>

                        </td>

                      </tr>

                    ))

                  ) : (

                    <tr>
                      <td
                        colSpan="5"
                        className="text-center"
                      >
                        No applications found
                      </td>
                    </tr>

                  )}

                </tbody>

              </table>

            </div>

          </div>

        </>
      )}

    </div>
  );
}

export default AdminDashboard;