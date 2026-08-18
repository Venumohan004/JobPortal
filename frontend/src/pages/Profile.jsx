import { useEffect, useState } from "react";
import api from "../api";

function Profile() {
  const role = localStorage.getItem("role");

  const [profile, setProfile] = useState({
    full_name: "",
    email: "",
    phone: "",
    location: "",
    skills: "",
    bio: "",
    role: "",
  });

  const [editing, setEditing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");

  // =========================
  // Get Profile
  // =========================
  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {
      setLoading(true);

      const res = await api.get("/profile");

      console.log("Profile response:", res.data);

      setProfile({
        full_name: res.data.full_name || "",
        email: res.data.email || "",
        phone: res.data.phone || "",
        location: res.data.location || "",
        skills: res.data.skills || "",
        bio: res.data.bio || "",
        role: res.data.role || role || "",
      });

    } catch (err) {
      console.error(
        "Profile error:",
        err.response?.data || err.message
      );

      setMessage(
        err.response?.data?.message ||
        "Failed to load profile"
      );
    } finally {
      setLoading(false);
    }
  };

  // =========================
  // Handle Input
  // =========================
  const handleChange = (e) => {
    setProfile({
      ...profile,
      [e.target.name]: e.target.value,
    });
  };

  // =========================
  // Update Profile
  // =========================
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await api.put("/profile", {
        full_name: profile.full_name,
        phone: profile.phone,
        location: profile.location,
        skills: profile.skills,
        bio: profile.bio,
      });

      console.log("Update response:", res.data);

      setMessage("Profile updated successfully!");

      setEditing(false);

      // Refresh latest profile
      await fetchProfile();

    } catch (err) {
      console.error(
        "Update profile error:",
        err.response?.data || err.message
      );

      setMessage(
        err.response?.data?.message ||
        "Failed to update profile"
      );
    }
  };

  // =========================
  // Loading
  // =========================
  if (loading) {
    return (
      <div className="container py-5 text-center">
        <h4>Loading profile...</h4>
      </div>
    );
  }

  return (
    <div
      className="container py-5"
      style={{ maxWidth: "700px" }}
    >
      <div className="card shadow border-0">

        {/* Header */}
        <div className="card-header bg-dark text-white p-4">
          <h2 className="mb-1">My Profile</h2>
          <p className="mb-0">
            View and manage your account details
          </p>
        </div>

        <div className="card-body p-4">

          {/* Message */}
          {message && (
            <div className="alert alert-info">
              {message}
            </div>
          )}

          {!editing ? (
            <>
              {/* Full Name */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Full Name
                </label>

                <div className="form-control bg-light">
                  {profile.full_name || "-"}
                </div>
              </div>

              {/* Email */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Email
                </label>

                <div className="form-control bg-light">
                  {profile.email || "-"}
                </div>
              </div>

              {/* Phone */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Contact Number
                </label>

                <div className="form-control bg-light">
                  {profile.phone || "Not added"}
                </div>
              </div>

              {/* Role */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Role
                </label>

                <div>
                  <span className="badge bg-primary text-capitalize px-3 py-2">
                    {profile.role}
                  </span>
                </div>
              </div>

              {/* Location */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Location
                </label>

                <div className="form-control bg-light">
                  {profile.location || "Not added"}
                </div>
              </div>

              {/* Skills - Candidate */}
              {role === "candidate" && (
                <>
                  <div className="mb-3">
                    <label className="form-label fw-bold">
                      Skills
                    </label>

                    <div className="form-control bg-light">
                      {profile.skills || "Not added"}
                    </div>
                  </div>

                  <div className="mb-3">
                    <label className="form-label fw-bold">
                      Bio
                    </label>

                    <div className="form-control bg-light">
                      {profile.bio || "Not added"}
                    </div>
                  </div>
                </>
              )}

              {/* Edit Button */}
              <button
                className="btn btn-primary mt-3"
                onClick={() => {
                  setMessage("");
                  setEditing(true);
                }}
              >
                Edit Profile
              </button>
            </>
          ) : (
            <form onSubmit={handleSubmit}>

              {/* Full Name */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Full Name
                </label>

                <input
                  type="text"
                  name="full_name"
                  className="form-control"
                  value={profile.full_name}
                  onChange={handleChange}
                  required
                />
              </div>

              {/* Email */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Email
                </label>

                <input
                  type="email"
                  className="form-control"
                  value={profile.email}
                  disabled
                />

                <small className="text-muted">
                  Email cannot be changed.
                </small>
              </div>

              {/* Phone */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Contact Number
                </label>

                <input
                  type="text"
                  name="phone"
                  className="form-control"
                  value={profile.phone}
                  onChange={handleChange}
                  placeholder="Enter contact number"
                />
              </div>

              {/* Role */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Role
                </label>

                <input
                  type="text"
                  className="form-control text-capitalize"
                  value={profile.role}
                  disabled
                />

                <small className="text-muted">
                  Role cannot be changed.
                </small>
              </div>

              {/* Location */}
              <div className="mb-3">
                <label className="form-label fw-bold">
                  Location
                </label>

                <input
                  type="text"
                  name="location"
                  className="form-control"
                  value={profile.location}
                  onChange={handleChange}
                  placeholder="Enter your location"
                />
              </div>

              {/* Candidate Fields */}
              {role === "candidate" && (
                <>
                  {/* Skills */}
                  <div className="mb-3">
                    <label className="form-label fw-bold">
                      Skills
                    </label>

                    <input
                      type="text"
                      name="skills"
                      className="form-control"
                      value={profile.skills}
                      onChange={handleChange}
                      placeholder="Python, React, SQL..."
                    />
                  </div>

                  {/* Bio */}
                  <div className="mb-3">
                    <label className="form-label fw-bold">
                      Bio
                    </label>

                    <textarea
                      name="bio"
                      className="form-control"
                      rows="4"
                      value={profile.bio}
                      onChange={handleChange}
                      placeholder="Tell us about yourself..."
                    />
                  </div>
                </>
              )}

              {/* Buttons */}
              <div className="d-flex gap-2 mt-4">

                <button
                  type="submit"
                  className="btn btn-success"
                >
                  Save Changes
                </button>

                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => {
                    setEditing(false);
                    setMessage("");
                    fetchProfile();
                  }}
                >
                  Cancel
                </button>

              </div>

            </form>
          )}

        </div>
      </div>
    </div>
  );
}

export default Profile;