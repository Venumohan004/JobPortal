import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function CreateJob() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    title: "",
    company: "",
    location: "",
    min_salary: "",
    max_salary: "",
    job_type: "Full Time",
    experience: "",
    skills: "",
    description: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setError("");
    setSuccess("");

    // Basic validation
    if (!formData.title || !formData.company || !formData.location) {
      setError("Please fill all required fields.");
      return;
    }

    if (
      formData.min_salary &&
      formData.max_salary &&
      Number(formData.min_salary) > Number(formData.max_salary)
    ) {
      setError("Minimum salary cannot be greater than maximum salary.");
      return;
    }

    try {
      setLoading(true);

      const payload = {
        ...formData,
        min_salary: formData.min_salary
          ? Number(formData.min_salary)
          : null,
        max_salary: formData.max_salary
          ? Number(formData.max_salary)
          : null,
      };

      const response = await api.post("/jobs", payload);

      console.log("Job created:", response.data);

      setSuccess("Job posted successfully!");

      // Reset form
      setFormData({
        title: "",
        company: "",
        location: "",
        min_salary: "",
        max_salary: "",
        job_type: "Full Time",
        experience: "",
        skills: "",
        description: "",
      });

      // Redirect after 2 seconds
      setTimeout(() => {
        navigate("/recruiter/dashboard");
      }, 2000);

    } catch (err) {
      console.error(err);

      setError(
        err.response?.data?.message ||
        err.response?.data?.error ||
        "Failed to create job"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-lg-8">

          <div className="card shadow border-0">
            <div className="card-header bg-primary text-white">
              <h2 className="mb-0">Post a New Job</h2>
            </div>

            <div className="card-body p-4">

              {error && (
                <div className="alert alert-danger">{error}</div>
              )}

              {success && (
                <div className="alert alert-success">{success}</div>
              )}

              <form onSubmit={handleSubmit}>

                {/* Job Title */}
                <div className="mb-3">
                  <label className="form-label fw-semibold">
                    Job Title *
                  </label>

                  <input
                    type="text"
                    name="title"
                    className="form-control"
                    placeholder="Python Backend Developer"
                    value={formData.title}
                    onChange={handleChange}
                    required
                  />
                </div>

                {/* Company & Location */}
                <div className="row">
                  <div className="col-md-6 mb-3">
                    <label className="form-label fw-semibold">
                      Company *
                    </label>

                    <input
                      type="text"
                      name="company"
                      className="form-control"
                      placeholder="ABC Technologies"
                      value={formData.company}
                      onChange={handleChange}
                      required
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label className="form-label fw-semibold">
                      Location *
                    </label>

                    <input
                      type="text"
                      name="location"
                      className="form-control"
                      placeholder="Bangalore"
                      value={formData.location}
                      onChange={handleChange}
                      required
                    />
                  </div>
                </div>

                {/* Salary */}
                <div className="row">
                  <div className="col-md-6 mb-3">
                    <label className="form-label fw-semibold">
                      Minimum Salary
                    </label>

                    <input
                      type="number"
                      name="min_salary"
                      className="form-control"
                      placeholder="500000"
                      value={formData.min_salary}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label className="form-label fw-semibold">
                      Maximum Salary
                    </label>

                    <input
                      type="number"
                      name="max_salary"
                      className="form-control"
                      placeholder="1200000"
                      value={formData.max_salary}
                      onChange={handleChange}
                    />
                  </div>
                </div>

                {/* Job Type & Experience */}
                <div className="row">
                  <div className="col-md-6 mb-3">
                    <label className="form-label fw-semibold">
                      Job Type
                    </label>

                    <select
                      name="job_type"
                      className="form-select"
                      value={formData.job_type}
                      onChange={handleChange}
                    >
                      <option>Full Time</option>
                      <option>Part Time</option>
                      <option>Internship</option>
                      <option>Contract</option>
                      <option>Remote</option>
                    </select>
                  </div>

                  <div className="col-md-6 mb-3">
                    <label className="form-label fw-semibold">
                      Experience
                    </label>

                    <input
                      type="text"
                      name="experience"
                      className="form-control"
                      placeholder="2+ years"
                      value={formData.experience}
                      onChange={handleChange}
                    />
                  </div>
                </div>

                {/* Skills */}
                <div className="mb-3">
                  <label className="form-label fw-semibold">
                    Required Skills
                  </label>

                  <input
                    type="text"
                    name="skills"
                    className="form-control"
                    placeholder="Python, Flask, PostgreSQL, React"
                    value={formData.skills}
                    onChange={handleChange}
                  />

                  <div className="form-text">
                    Separate skills with commas.
                  </div>
                </div>

                {/* Description */}
                <div className="mb-4">
                  <label className="form-label fw-semibold">
                    Job Description
                  </label>

                  <textarea
                    name="description"
                    className="form-control"
                    rows="6"
                    placeholder="Describe the job responsibilities, requirements, and benefits..."
                    value={formData.description}
                    onChange={handleChange}
                  />
                </div>

                {/* Buttons */}
                <div className="d-flex gap-3">
                  <button
                    type="submit"
                    className="btn btn-primary"
                    disabled={loading}
                  >
                    {loading ? "Posting..." : "Post Job"}
                  </button>

                  <button
                    type="button"
                    className="btn btn-outline-secondary"
                    onClick={() => navigate("/recruiter/dashboard")}
                  >
                    Cancel
                  </button>
                </div>

              </form>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}

export default CreateJob;