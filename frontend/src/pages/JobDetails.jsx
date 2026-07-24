import { useEffect, useState } from "react";
import { useParams, useNavigate, useLocation } from "react-router-dom";
import api from "../services/api";

function JobDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  const location = useLocation();

  const [job, setJob] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(true);
  const [applying, setApplying] = useState(false);
  const [applied, setApplied] = useState(false);

  useEffect(() => {
    fetchJob();
  }, [id]);

  const fetchJob = async () => {
    try {
      setLoading(true);

      const response = await api.get(`/jobs/${id}`);

      // Handle both possible response formats
      setJob(response.data.job || response.data);
    } catch (err) {
      console.error(err);

      if (err.response?.status === 404) {
        setMessage("Job not found");
      } else {
        setMessage("Failed to load job details");
      }
    } finally {
      setLoading(false);
    }
  };

  // =========================
  // Apply Job
  // =========================
  const applyJob = async () => {
    const token = localStorage.getItem("token");

    if (!token) {
      navigate("/login", {
        state: { from: location.pathname },
        replace: true,
      });
      return;
    }

    // Prevent double click
    if (applying || applied) return;

    setApplying(true);
    setMessage("");

    try {
      const response = await api.post(`/jobs/${id}/apply`);

      setMessage(
        response.data.message || "Application submitted successfully!"
      );

      setApplied(true);
    } catch (err) {
      console.log("FULL ERROR:", err);

      if (err.response) {
        setMessage(
          err.response.data.message ||
            err.response.data.error ||
            "Apply failed"
        );
      } else if (err.request) {
        setMessage("Server timeout. Please try again.");
      } else {
        setMessage(err.message);
      }
    } finally {
      setApplying(false);
    }
  };

  // =========================
  // Save Job
  // =========================
  const handleSaveJob = async () => {
    const token = localStorage.getItem("token");

    if (!token) {
      alert("Please login as candidate");
      navigate("/login");
      return;
    }

    try {
      const response = await api.post(`/jobs/${id}/save`);

      alert(response.data.message || "Job saved successfully!");
    } catch (err) {
      alert(err.response?.data?.message || "Failed to save job");
    }
  };

  // =========================
  // Loading State
  // =========================
  if (loading) {
    return (
      <div className="container py-5 text-center">
        <h4>Loading job details...</h4>
      </div>
    );
  }

  // =========================
  // Job Not Found
  // =========================
  if (!job) {
    return (
      <div className="container py-5 text-center">
        <div className="alert alert-danger">
          {message || "Job not found"}
        </div>
      </div>
    );
  }

  // =========================
  // Main UI
  // =========================
  return (
    <div className="container py-5">
      <div className="card border-0 shadow-lg rounded-4">
        <div className="card-body p-5">
          {/* Header */}
          <div className="d-flex justify-content-between align-items-start flex-wrap mb-4">
            <div>
              <h2 className="fw-bold mb-2">{job.title}</h2>
              <h5 className="text-primary mb-0">{job.company}</h5>
            </div>

            <span className="badge bg-primary fs-6 px-3 py-2">
              {job.job_type || "Full Time"}
            </span>
          </div>

          <hr />

          {/* Job Info */}
          <div className="row g-3 mb-4">
            <div className="col-md-6">
              <p className="mb-2">
                <strong>📍 Location:</strong> {job.location}
              </p>
            </div>

            <div className="col-md-6">
              <p className="mb-2">
                <strong>💼 Experience:</strong> {job.experience || "Not specified"}
              </p>
            </div>

            <div className="col-md-6">
              <p className="mb-2">
                <strong>💰 Salary:</strong> ₹{job.min_salary} - ₹{job.max_salary}
              </p>
            </div>

            <div className="col-md-6">
              <p className="mb-2">
                <strong>🕒 Job Type:</strong> {job.job_type || "Full Time"}
              </p>
            </div>
          </div>

          {/* Description */}
          <div className="mb-4">
            <h5 className="fw-bold mb-3">Job Description</h5>
            <p className="text-muted lh-lg">
              {job.description}
            </p>
          </div>

          {/* Skills */}
          <div className="mb-4">
            <h5 className="fw-bold mb-3">Required Skills</h5>
            <div className="d-flex flex-wrap gap-2">
              {(job.skills || "")
                .split(",")
                .map((skill, index) => (
                  <span
                    key={index}
                    className="badge bg-light text-dark border px-3 py-2"
                  >
                    {skill.trim()}
                  </span>
                ))}
            </div>
          </div>

          {/* Action Buttons */}
          <div className="d-flex gap-3 mt-4 flex-wrap">
            {/* Apply Button */}
            <button
              className={`btn px-4 py-2 rounded-pill ${
                applied ? "btn-secondary" : "btn-success"
              }`}
              onClick={applyJob}
              disabled={applying || applied}
            >
              {applying
                ? "Applying..."
                : applied
                ? "Already Applied"
                : "Apply Now"}
            </button>

            {/* Save Job Button */}
            <button
              className="btn btn-outline-primary px-4 py-2 rounded-pill"
              onClick={handleSaveJob}
            >
              Save Job
            </button>
          </div>

          {/* Message */}
          {message && (
            <div
              className={`alert mt-4 ${
                message.toLowerCase().includes("success")
                  ? "alert-success"
                  : message.toLowerCase().includes("already")
                  ? "alert-warning"
                  : "alert-danger"
              }`}
            >
              {message}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default JobDetails;