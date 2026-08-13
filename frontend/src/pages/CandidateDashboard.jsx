import { useEffect, useState } from "react";
import api from "../api";
import { Link } from "react-router-dom";

function CandidateDashboard() {
  const [stats, setStats] = useState({
    applications: 0,
    savedJobs: 0,
    recentApplications: [],
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      setLoading(true);

      // Fetch candidate's own applications
      const appliedRes = await api.get("/my-applications");

      // Fetch saved jobs
      const savedRes = await api.get("/saved-jobs");

      console.log("Applications:", appliedRes.data);
      console.log("Saved jobs:", savedRes.data);

      const applications = appliedRes.data.applications || [];
      const savedJobs = savedRes.data.saved_jobs || [];

      setStats({
        applications: applications.length,
        savedJobs: savedJobs.length,
        recentApplications: applications.slice(0, 5),
      });

    } catch (err) {
      console.error("Dashboard error:", err);
      alert("Failed to load dashboard");
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container py-5 text-center">
        <h4>Loading dashboard...</h4>
      </div>
    );
  }

  return (
    <div className="container py-5">
      {/* Header */}
      <div className="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h2 className="fw-bold">Candidate Dashboard</h2>
          <p className="text-muted mb-0">
            Track your applications and saved jobs
          </p>
        </div>

        <Link to="/jobs" className="btn btn-primary">
          Browse Jobs
        </Link>
      </div>

      {/* Stats Cards */}
      <div className="row g-4 mb-5">
        <div className="col-md-6">
          <div className="card border-0 shadow-sm h-100">
            <div className="card-body text-center py-4">
              <h6 className="text-muted">Applied Jobs</h6>
              <h2 className="fw-bold text-primary">
                {stats.applications}
              </h2>
            </div>
          </div>
        </div>

        <div className="col-md-6">
          <div className="card border-0 shadow-sm h-100">
            <div className="card-body text-center py-4">
              <h6 className="text-muted">Saved Jobs</h6>
              <h2 className="fw-bold text-success">
                {stats.savedJobs}
              </h2>
            </div>
          </div>
        </div>
      </div>

      {/* Recent Applications */}
      <div className="card border-0 shadow-sm">
        <div className="card-header bg-white border-0 d-flex justify-content-between align-items-center">
          <h5 className="fw-bold mb-0">Recent Applications</h5>

          <Link
            to="/applied-jobs"
            className="btn btn-outline-primary btn-sm"
          >
            View All
          </Link>
        </div>

        <div className="card-body">
          {stats.recentApplications.length === 0 ? (
            <div className="text-center py-4">
              <p className="text-muted mb-3">
                You have not applied to any jobs yet.
              </p>

              <Link to="/jobs" className="btn btn-outline-primary">
                Explore Jobs
              </Link>
            </div>
          ) : (
            <div className="table-responsive">
              <table className="table align-middle">
                <thead>
                  <tr>
                    <th>Job</th>
                    <th>Company</th>
                    <th>Status</th>
                    <th>Applied At</th>
                  </tr>
                </thead>

                <tbody>
                  {stats.recentApplications.map((app) => (
                    <tr key={app.id}>
                      <td className="fw-semibold">
                        {app.job_title || "Job"}
                      </td>

                      <td>{app.company || "-"}</td>

                      <td>
                        <span className="badge bg-primary">
                          {app.status || "Applied"}
                        </span>
                      </td>

                      <td>
                        {app.created_at
                          ? new Date(app.created_at).toLocaleDateString()
                          : "Recently"}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default CandidateDashboard;