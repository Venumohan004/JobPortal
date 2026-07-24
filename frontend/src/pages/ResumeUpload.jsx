import { useState, useEffect } from "react";
import api from "../services/api";

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [resumeInfo, setResumeInfo] = useState(null);
  const [loading, setLoading] = useState(false);

  const candidateId = localStorage.getItem("user_id");

  useEffect(() => {
    fetchResume();
  }, []);

  const fetchResume = async () => {
    if (!candidateId) return;

    try {
      const res = await api.get(`/resume/${candidateId}`);
      setResumeInfo(res.data);
    } catch (err) {
      // Resume not uploaded yet
      console.log("No resume found");
    }
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage("Please select a resume file");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      setLoading(true);

      const res = await api.post("/upload/resume", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setMessage(res.data.message);
      setResumeInfo(res.data.resume);
      setFile(null);

    } catch (error) {
      console.error(error);
      setMessage(error.response?.data?.message || "Upload failed");
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    if (!resumeInfo) return;

    const confirmDelete = window.confirm(
      "Are you sure you want to delete your resume?"
    );

    if (!confirmDelete) return;

    try {
      await api.delete(`/resume/${resumeInfo.id}`);

      setResumeInfo(null);
      setMessage("Resume deleted successfully");

    } catch (error) {
      console.error(error);
      setMessage("Failed to delete resume");
    }
  };

  return (
    <div className="container py-5">
      <div className="card shadow border-0 mx-auto" style={{ maxWidth: "700px" }}>
        <div className="card-body p-4">

          <div className="text-center mb-4">
            <h2 className="fw-bold">Resume Management</h2>
            <p className="text-muted">
              Upload your resume to apply for jobs quickly
            </p>
          </div>

          {/* Upload Form */}
          <form onSubmit={handleUpload}>
            <div className="mb-3">
              <label className="form-label fw-semibold">
                Select Resume (PDF / DOC / DOCX)
              </label>

              <input
                type="file"
                className="form-control"
                accept=".pdf,.doc,.docx"
                onChange={(e) => setFile(e.target.files[0])}
              />
            </div>

            <button
              type="submit"
              className="btn btn-primary w-100"
              disabled={loading}
            >
              {loading
                ? "Uploading..."
                : resumeInfo
                ? "Update Resume"
                : "Upload Resume"}
            </button>
          </form>

          {/* Message */}
          {message && (
            <div
              className={`alert mt-3 ${
                message.toLowerCase().includes("success")
                  ? "alert-success"
                  : message.toLowerCase().includes("updated")
                  ? "alert-success"
                  : "alert-info"
              }`}
            >
              {message}
            </div>
          )}

          {/* Resume Info */}
          {resumeInfo && (
            <div className="mt-4 border rounded p-3 bg-light">
              <h5 className="fw-bold mb-3">Current Resume</h5>

              <p className="mb-2">
                <strong>File Name:</strong> {resumeInfo.file_name}
              </p>

              <p className="mb-3">
                <strong>Uploaded At:</strong>{" "}
                {new Date(resumeInfo.created_at).toLocaleString()}
              </p>

              <div className="d-flex gap-2 flex-wrap">
                <a
                  href={`https://jobportal-aver.onrender.com/resume/download/${resumeInfo.candidate_id}`}
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-success"
                >
                  Download Resume
                </a>

                <button
                  className="btn btn-outline-danger"
                  onClick={handleDelete}
                >
                  Delete Resume
                </button>
              </div>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}

export default ResumeUpload;