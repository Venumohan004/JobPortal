import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../services/api";

function EditJob() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [job, setJob] = useState({
    title: "",
    company: "",
    location: "",
    description: "",
    min_salary: "",
    max_salary: "",
    job_type: "Full Time",
    experience: "",
    skills: "",
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchJob();
  }, []);

  const fetchJob = async () => {
    try {
      const res = await api.get(`/jobs/${id}`);

      setJob({
        title: res.data.title || "",
        company: res.data.company || "",
        location: res.data.location || "",
        description: res.data.description || "",
        min_salary: res.data.min_salary || "",
        max_salary: res.data.max_salary || "",
        job_type: res.data.job_type || "Full Time",
        experience: res.data.experience || "",
        skills: res.data.skills || "",
      });
    } catch (err) {
      console.error(err);
      alert("Failed to load job");
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setJob({
      ...job,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await api.put(`/jobs/${id}`, job);

      alert("Job updated successfully!");

      navigate("/recruiter-dashboard");
    } catch (err) {
      console.error(err);
      alert(
        err.response?.data?.message || "Failed to update job"
      );
    }
  };

  if (loading) {
    return (
      <div className="container py-5">
        <p>Loading job...</p>
      </div>
    );
  }

  return (
    <div className="container py-5" style={{ maxWidth: "800px" }}>
      <div className="card shadow p-4">
        <h2 className="mb-4">Edit Job</h2>

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Job Title</label>
            <input
              type="text"
              name="title"
              className="form-control"
              value={job.title}
              onChange={handleChange}
              required
            />
          </div>

          <div className="row">
            <div className="col-md-6 mb-3">
              <label className="form-label">Company</label>
              <input
                type="text"
                name="company"
                className="form-control"
                value={job.company}
                onChange={handleChange}
                required
              />
            </div>

            <div className="col-md-6 mb-3">
              <label className="form-label">Location</label>
              <input
                type="text"
                name="location"
                className="form-control"
                value={job.location}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <div className="row">
            <div className="col-md-6 mb-3">
              <label className="form-label">Minimum Salary</label>
              <input
                type="number"
                name="min_salary"
                className="form-control"
                value={job.min_salary}
                onChange={handleChange}
              />
            </div>

            <div className="col-md-6 mb-3">
              <label className="form-label">Maximum Salary</label>
              <input
                type="number"
                name="max_salary"
                className="form-control"
                value={job.max_salary}
                onChange={handleChange}
              />
            </div>
          </div>

          <div className="row">
            <div className="col-md-6 mb-3">
              <label className="form-label">Job Type</label>
              <select
                name="job_type"
                className="form-select"
                value={job.job_type}
                onChange={handleChange}
              >
                <option>Full Time</option>
                <option>Part Time</option>
                <option>Internship</option>
                <option>Remote</option>
              </select>
            </div>

            <div className="col-md-6 mb-3">
              <label className="form-label">Experience</label>
              <input
                type="text"
                name="experience"
                className="form-control"
                value={job.experience}
                onChange={handleChange}
              />
            </div>
          </div>

          <div className="mb-3">
            <label className="form-label">Skills</label>
            <input
              type="text"
              name="skills"
              className="form-control"
              value={job.skills}
              onChange={handleChange}
            />
          </div>

          <div className="mb-4">
            <label className="form-label">Description</label>
            <textarea
              name="description"
              className="form-control"
              rows="5"
              value={job.description}
              onChange={handleChange}
              required
            />
          </div>

          <div className="d-flex gap-2">
            <button type="submit" className="btn btn-primary">
              Update Job
            </button>

            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => navigate("/recruiter-dashboard")}
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default EditJob;