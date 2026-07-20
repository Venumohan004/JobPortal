import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/dashboard.css";

const API = "https://jobportal-aver.onrender.com";

function AdminDashboard() {
  const [stats, setStats] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchStats = async () => {
      const token = localStorage.getItem("token");

      if (!token) {
        setError("Please login first.");
        return;
      }

      try {
        const res = await axios.get(`${API}/admin/dashboard`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        console.log("Admin dashboard response:", res.data);
        setStats(res.data);

      } catch (err) {
        console.error(err);
        setError(err.response?.data?.msg || "Failed to load admin dashboard");
      }
    };

    fetchStats();
  }, []);

  return (
    <div className="dashboard-container">
      <h1>Admin Dashboard</h1>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {stats ? (
        <>
          {/* Statistics Cards */}
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Total Users</h3>
              <p>{stats.statistics.total_users}</p>
            </div>

            <div className="stat-card">
              <h3>Total Jobs</h3>
              <p>{stats.statistics.total_jobs}</p>
            </div>

            <div className="stat-card">
              <h3>Total Applications</h3>
              <p>{stats.statistics.total_applications}</p>
            </div>

            <div className="stat-card">
              <h3>Total Recruiters</h3>
              <p>{stats.statistics.total_recruiters}</p>
            </div>
          </div>

          {/* Recent Users */}
          <div className="jobs-section">
            <h2>Recent Users</h2>

            <table className="jobs-table">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Role</th>
                </tr>
              </thead>

              <tbody>
                {stats.latest_users.map((user) => (
                  <tr key={user.id}>
                    <td>{user.full_name}</td>
                    <td>{user.email}</td>
                    <td>{user.role}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Recent Jobs */}
          <div className="jobs-section">
            <h2>Recent Jobs</h2>

            <table className="jobs-table">
              <thead>
                <tr>
                  <th>Title</th>
                  <th>Company</th>
                  <th>Location</th>
                </tr>
              </thead>

              <tbody>
                {stats.latest_jobs.map((job) => (
                  <tr key={job.id}>
                    <td>{job.title}</td>
                    <td>{job.company}</td>
                    <td>{job.location}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      ) : (
        !error && <p>Loading...</p>
      )}
    </div>
  );
}

export default AdminDashboard;