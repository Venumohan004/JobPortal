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

      console.log("Apply response:", response.data);

      setMessage(response.data.message || "Applied successfully!");
      setApplied(true);

    } catch (err) {
        console.log("FULL ERROR:", err);

        if (err.response) {
          console.log("STATUS:", err.response.status);
          console.log("BACKEND DATA:", err.response.data);

          setMessage(
            err.response.data.message ||
            err.response.data.error ||
            "Apply failed"
          );
        } 
        else if (err.request) {
          console.log("No response from server");
          setMessage("Server timeout. Please try again.");
        } 
        else {
          setMessage(err.message);
        }
      }
    };

  if (loading) {
    return (
      <div className="container py-5 text-center">
        <h4>Loading job details...</h4>
      </div>
    );
  }

  if (!job) {
    return (
      <div className="container py-5 text-center">
        <div className="alert alert-danger">
          {message || "Job not found"}
        </div>
      </div>
    );
  }

  return (
    <div className="container py-5">
      <div className="card shadow-sm">
        <div className="card-body">
          <h2>{job.title}</h2>
          <h5 className="text-muted">{job.company}</h5>

          <hr />

          <p><strong>Location:</strong> {job.location}</p>
          <p>
            <strong>Salary:</strong> ₹{job.min_salary} - ₹{job.max_salary}
          </p>
          <p><strong>Experience:</strong> {job.experience}</p>
          <p><strong>Job Type:</strong> {job.job_type}</p>

          <h5 className="mt-4">Description</h5>
          <p>{job.description}</p>

          <h5 className="mt-4">Required Skills</h5>
          <p>{job.skills}</p>

            <button
                className={`btn mt-3 ${
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

              {message && (
                <div
                  className={`alert mt-3 ${
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