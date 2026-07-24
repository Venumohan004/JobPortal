import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";

function SavedJobs() {
  const [savedJobs, setSavedJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSavedJobs();
  }, []);

  const fetchSavedJobs = async () => {
    try {
      const res = await api.get("/saved-jobs");

      console.log("Saved jobs response:", res.data);

      const savedList = res.data.saved_jobs || [];

      // Fetch full job details for each saved job
      const jobsWithDetails = await Promise.all(
        savedList.map(async (saved) => {
          try {
            const jobRes = await api.get(`/jobs/${saved.job_id}`);

            return {
              ...saved,
              job: jobRes.data.job || jobRes.data,
            };
          } catch (err) {
            console.error("Failed to fetch job", saved.job_id);
            return {
              ...saved,
              job: null,
            };
          }
        })
      );

      setSavedJobs(jobsWithDetails);
    } catch (err) {
      console.error(err);
      alert("Failed to load saved jobs");
    } finally {
      setLoading(false);
    }
  };

  const removeSavedJob = async (jobId) => {
    try {
      await api.delete(`/jobs/${jobId}/save`);

      setSavedJobs((prev) =>
        prev.filter((job) => job.job_id !== jobId)
      );
    } catch (err) {
      console.error(err);
      alert("Failed to remove saved job");
    }
  };

  if (loading) {
    return (
      <div className="container py-5 text-center">
        <h4>Loading saved jobs...</h4>
      </div>
    );
  }

  return (
    <div className="container py-5">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>Saved Jobs</h2>
        <span className="badge bg-primary fs-6">
          {savedJobs.length} saved
        </span>
      </div>

      {savedJobs.length === 0 ? (
        <div className="alert alert-info">
          You have not saved any jobs yet.
        </div>
      ) : (
        <div className="row g-4">
          {savedJobs.map((saved) => {
            const job = saved.job;

            return (
              <div className="col-md-6" key={saved.id}>
                <div className="card shadow-sm h-100 border-0">
                  <div className="card-body">
                    <h5 className="card-title">
                      {job?.title || "Job not found"}
                    </h5>

                    <p className="text-muted mb-2">
                      {job?.company || "Company"}
                    </p>

                    <p className="mb-2">
                      📍 <strong>{job?.location || "Location"}</strong>
                    </p>

                    <p className="mb-3 text-success fw-semibold">
                      ₹{job?.min_salary?.toLocaleString() || "N/A"} - ₹
                      {job?.max_salary?.toLocaleString() || "N/A"}
                    </p>

                    <div className="d-flex gap-2">
                      <Link
                        to={`/jobs/${saved.job_id}`}
                        className="btn btn-primary btn-sm"
                      >
                        View Details
                      </Link>

                      <button
                        className="btn btn-outline-danger btn-sm"
                        onClick={() => removeSavedJob(saved.job_id)}
                      >
                        Remove
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default SavedJobs;