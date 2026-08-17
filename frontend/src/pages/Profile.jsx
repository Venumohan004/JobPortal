import { useEffect, useState } from "react";
import api from "../api";

function Profile() {
  const role = localStorage.getItem("role");

  const [profile, setProfile] = useState({
    company_name: "",
    company_email: "",
    location: "",
    website: "",
  });

  const [message, setMessage] = useState("");

  useEffect(() => {
    if (role === "recruiter") {
      fetchRecruiterProfile();
    }
  }, [role]);

  const fetchRecruiterProfile = async () => {
    try {
      const res = await api.get("/recruiter/profile");

      setProfile({
        company_name: res.data.company_name || "",
        company_email: res.data.company_email || "",
        location: res.data.company_location || "",
        website: res.data.company_website || "",
      });
    } catch (err) {
      console.log("No recruiter profile found");
    }
  };

  const handleChange = (e) => {
    setProfile({
      ...profile,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
  e.preventDefault();

  // Send exact field names expected by backend
  const payload = {
    company_name: profile.company_name,
    company_email: profile.company_email,
    company_location: profile.location,
    company_website: profile.website,
  };

  console.log("Sending payload:", payload);

  try {
    const res = await api.put("/recruiter/profile", payload);

    console.log("Save response:", res.data);

    setMessage("Recruiter profile saved successfully!");

    // Refresh profile after save
    fetchRecruiterProfile();
  } catch (err) {
    console.error("Save error:", err.response?.data || err.message);

    // Show backend error message if available
    setMessage(
      err.response?.data?.message ||
      err.response?.data?.error ||
      "Failed to save profile"
    );
  }
};

  // =========================
  // Recruiter Profile
  // =========================
  if (role === "recruiter") {
    return (
      <div className="container py-5" style={{ maxWidth: "700px" }}>
        <div className="card shadow p-4">
          <h2 className="mb-4">Recruiter Profile</h2>

          {message && (
            <div className="alert alert-info">{message}</div>
          )}

          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">Company Name</label>
              <input
                type="text"
                name="company_name"
                className="form-control"
                value={profile.company_name}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label className="form-label">Company Email</label>
              <input
                type="email"
                name="company_email"
                className="form-control"
                value={profile.company_email}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label className="form-label">Location</label>
              <input
                type="text"
                name="location"
                className="form-control"
                value={profile.location}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-4">
              <label className="form-label">Website</label>
              <input
                type="url"
                name="website"
                className="form-control"
                value={profile.website}
                onChange={handleChange}
              />
            </div>

            <button type="submit" className="btn btn-primary">
              Save Profile
            </button>
          </form>
        </div>
      </div>
    );
  }

  // =========================
  // Candidate Profile
  // =========================
  return (
    <div className="container py-5">
      <div className="card shadow p-4">
        <h2>My Profile</h2>
        <p className="text-muted">Welcome! You are logged in.</p>
      </div>
    </div>
  );
}

export default Profile;