import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

function JobDetails() {
  const { id } = useParams();
  const [job, setJob] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  api
    .get(`/jobs/${id}`)
    .then((response) => {
      console.log("Job Response:", response.data);
      setJob(response.data);
      setLoading(false);
    })
    .catch((error) => {
      console.error("API Error:", error.response?.status);
      console.error("API Data:", error.response?.data);
      setLoading(false);
    });
}, [id]);

  if (loading) {
    return (
      <div className="container mt-5">
        <h3>Loading...</h3>
      </div>
    );
  }

  if (!job) {
    return (
      <div className="container mt-5">
        <h3>Job Not Found</h3>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">
        <h2>{job.title}</h2>

        <h5 className="text-primary">{job.company}</h5>

        <p>
          <strong>Location:</strong> {job.location}
        </p>

        <p>
          <strong>Experience:</strong> {job.experience}
        </p>

        <p>
          <strong>Job Type:</strong> {job.job_type}
        </p>

        <p>
          <strong>Salary:</strong>
          ₹{job.min_salary} - ₹{job.max_salary}
        </p>

        <p>
          <strong>Skills:</strong> {job.skills}
        </p>

        <p>
          <strong>Description:</strong>
        </p>

        <p>{job.description}</p>

        <button className="btn btn-success">
          Apply Now
        </button>
      </div>
    </div>
  );
}

export default JobDetails;