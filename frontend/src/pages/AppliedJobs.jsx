import { useEffect, useState } from "react";
import api from "../api";
import { Link } from "react-router-dom";

function AppliedJobs() {
  const [applications, setApplications] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchApplications();
  }, []);

    const fetchApplications = async () => {
    try {
      const res = await api.get("/my-applications");

      console.log("My Applications:", res.data);

      setApplications(res.data.applications || []);

    } catch (err) {
      console.error(
        "Failed to load applications:",
        err.response?.data || err.message
      );

      alert("Failed to load applications");
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container py-5">
        <p>Loading applications...</p>
      </div>
    );
  }

  return (
    <div className="container py-5">
      <h2 className="mb-4">Applied Jobs</h2>

      {applications.length === 0 ? (
        <div className="alert alert-info">
          You have not applied to any jobs yet.
        </div>
      ) : (
        <div className="row g-4">
          {applications.map((app) => (
            <div key={app.id} className="col-md-6">
              <div className="card h-100 shadow-sm border-0">
                <div className="card-body">
                  <h5 className="card-title">{app.job_title}</h5>

                  <p className="text-muted mb-2">
                    <strong>{app.company}</strong>
                  </p>

                  <p className="mb-2">
                    <strong>Location:</strong> {app.location}
                  </p>

                  <p className="mb-3">
                    <strong>Status:</strong>{" "}
                    <span className="badge bg-success">Applied</span>
                  </p>

                  <Link
                    to={`/jobs/${app.job_id}`}
                    className="btn btn-outline-primary"
                  >
                    View Job
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default AppliedJobs;