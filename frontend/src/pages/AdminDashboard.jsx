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

      const res = await axios.get(
        `${API}/admin/dashboard`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      console.log(
        "Admin dashboard response:",
        res.data
      );

      setStats(res.data);

    } catch (err) {
      console.error(
        "Admin dashboard error:",
        err
      );

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

      await axios.delete(
        `${API}/admin/users/${userId}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      alert("User deleted successfully.");

      await fetchStats();

    } catch (err) {

      console.error(
        "Delete user error:",
        err
      );

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

      await axios.delete(
        `${API}/admin/jobs/${jobId}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      alert("Job deleted successfully.");

      await fetchStats();

    } catch (err) {

      console.error(
        "Delete job error:",
        err
      );

      alert(
        err.response?.data?.message ||
        "Failed to delete job"
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

      <div
        className="d-flex justify-content-between align-items-center mb-4"
      >

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

            <div
              className="d-flex justify-content-between align-items-center mb-3"
            >
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

            <div
              className="d-flex justify-content-between align-items-center mb-3"
            >

              <h2>Recent Jobs</h2>

              <button
                className="btn btn-success"
                onClick={() =>
                  navigate("/create-job")
                }
              >
                ➕ Add Job
              </button>

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

                  {stats.latest_jobs.length > 0 ? (

                    stats.latest_jobs.map((job) => (

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

            <h2>Recent Applications</h2>

            <div className="table-responsive">

              <table className="jobs-table">

                <thead>

                  <tr>
                    <th>ID</th>
                    <th>Candidate ID</th>
                    <th>Job ID</th>
                    <th>Status</th>
                  </tr>

                </thead>

                <tbody>

                  {stats.latest_applications?.length > 0 ? (

                    stats.latest_applications.map(
                      (application) => (

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

                        </tr>

                      )
                    )

                  ) : (

                    <tr>
                      <td
                        colSpan="4"
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