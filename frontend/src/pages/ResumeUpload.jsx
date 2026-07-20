import { useState } from "react";
import axios from "axios";
import "../styles/dashboard.css";

const API = "https://jobportal-aver.onrender.com";

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [resumeInfo, setResumeInfo] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage("Please select a resume file");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const token = localStorage.getItem("token");

      const res = await axios.post(
        `${API}/upload/resume`,
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setMessage(res.data.message);
      setResumeInfo(res.data.resume);

    } catch (error) {
      console.error(error);
      setMessage(error.response?.data?.message || "Upload failed");
    }
  };

  return (
    <div className="dashboard-container">
      <h1>Upload Resume</h1>

      <form onSubmit={handleUpload}>
        <input
          type="file"
          accept=".pdf,.doc,.docx"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button type="submit">Upload Resume</button>
      </form>

      {message && <p><strong>{message}</strong></p>}

      {resumeInfo && (
        <div className="profile-card">
            <h3>Uploaded Resume</h3>

            <p><strong>File:</strong> {resumeInfo.file_name}</p>

            <p>
            <strong>Uploaded:</strong>{" "}
            {new Date(resumeInfo.created_at).toLocaleString()}
            </p>

            <a
            href={`${API}/resume/download/${resumeInfo.candidate_id}`}
            target="_blank"
            rel="noreferrer"
            >
            <button type="button">Download Resume</button>
            </a>
        </div>
        )}
    </div>
  );
}

export default ResumeUpload;