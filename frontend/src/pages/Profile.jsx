import { useEffect, useState } from "react";
import api from "../api";

function Profile() {
  const role = localStorage.getItem("role");

  const [profile, setProfile] = useState({
    full_name: "",
    email: "",
    role: "",
  });

  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (role === "admin") {
      fetchAdminProfile();
    } else if (role === "recruiter") {
      fetchRecruiterProfile();
    } else {
      setLoading(false);
    }
  }, [role]);

  // =====================================================
  // ADMIN PROFILE
  // =====================================================

  const fetchAdminProfile = async () => {
    try {
      const res = await api.get("/admin/profile");

      console.log("Admin profile:", res.data);

      setProfile({
        full_name: res.data.full_name || "",
        email: res.data.email || "",
        role: res.data.role || "admin",
      });
    } catch (err) {
      console.error(
        "Admin profile error:",
        err.response?.data || err.message
      );

      setMessage(
        err.response?.data?.message ||
        "Failed to load admin profile"
      );
    } finally {
      setLoading(false);
    }
  };

  // =====================================================
  // RECRUITER PROFILE
  // =====================================================

  const fetchRecruiterProfile = async () => {
    try {
      const res = await api.get("/recruiter/profile");

      console.log("Recruiter profile:", res.data);

      setProfile({
        company_name: res.data.company_name || "",
        company_email: res.data.company_email || "",
        location: res.data.company_location || "",
        website: res.data.company_website || "",
      });
    } catch (err) {
      console.log("No recruiter profile found");
    } finally {
      setLoading(false);
    }
  };

  // =====================================================
  // HANDLE INPUT
  // =====================================================

  const handleChange = (e) => {
    setProfile({
      ...profile,
      [e.target.name]: e.target.value,
    });
  };

  // =====================================================
  // SAVE ADMIN PROFILE
  // =====================================================

  const handleAdminSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await api.put("/admin/profile", {
        full_name: profile.full_name,
        email: profile.email,
      });

      console.log("Admin save response:", res.data);

      setMessage("Admin profile updated successfully!");

      await fetchAdminProfile();

    } catch (err) {
      console.error(
        "Admin save error:",
        err.response?.data || err.message
      );

      setMessage(
        err.response?.data?.message ||
        "Failed to update admin profile"
      );
    }
  };

  // =====================================================
  // SAVE RECRUITER PROFILE
  // =====================================================

  const handleRecruiterSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      company_name: profile.company_name,
      company_email: profile.company_email,
      company_location: profile.location,
      company_website: profile.website,
    };

    try {
      const res = await api.put(
        "/recruiter/profile",
        payload
      );

      console.log("Save response:", res.data);

      setMessage(
        "Recruiter profile saved successfully!"
      );

      await fetchRecruiterProfile();

    } catch (err) {
      console.error(
        "Save error:",
        err.response?.data || err.message
      );

      setMessage(
        err.response?.data?.message ||
        "Failed to save profile"
      );
    }
  };

  // =====================================================
  // LOADING
  // =====================================================

  if (loading) {
    return (
      <div className="container py-5 text-center">
        <h4>Loading profile...</h4>
      </div>
    );
  }

  // =====================================================
  // ADMIN PROFILE
  // =====================================================

  if (role === "admin") {
    return (
      <div
        className="container py-5"
        style={{ maxWidth: "700px" }}
      >
        <div className="card shadow p-4">

          <h2 className="mb-4">
            Admin Profile
          </h2>

          {message && (
            <div className="alert alert-info">
              {message}
            </div>
          )}

          <form onSubmit={handleAdminSubmit}>

            {/* Admin Name */}
            <div className="mb-3">
              <label className="form-label">
                Admin Name
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
              <label className="form-label">
                Email
              </label>

              <input
                type="email"
                name="email"
                className="form-control"
                value={profile.email}
                onChange={handleChange}
                required
              />
            </div>

            {/* Role */}
            <div className="mb-4">
              <label className="form-label">
                Role
              </label>

              <input
                type="text"
                className="form-control"
                value="Admin"
                disabled
              />
            </div>

            <button
              type="submit"
              className="btn btn-primary"
            >
              Save Changes
            </button>

          </form>

        </div>
      </div>
    );
  }

  // =====================================================
  // RECRUITER PROFILE
  // =====================================================

  if (role === "recruiter") {
    return (
      <div
        className="container py-5"
        style={{ maxWidth: "700px" }}
      >
        <div className="card shadow p-4">

          <h2 className="mb-4">
            Recruiter Profile
          </h2>

          {message && (
            <div className="alert alert-info">
              {message}
            </div>
          )}

          <form onSubmit={handleRecruiterSubmit}>

            <div className="mb-3">
              <label className="form-label">
                Company Name
              </label>

              <input
                type="text"
                name="company_name"
                className="form-control"
                value={profile.company_name || ""}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label className="form-label">
                Company Email
              </label>

              <input
                type="email"
                name="company_email"
                className="form-control"
                value={profile.company_email || ""}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label className="form-label">
                Location
              </label>

              <input
                type="text"
                name="location"
                className="form-control"
                value={profile.location || ""}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-4">
              <label className="form-label">
                Website
              </label>

              <input
                type="url"
                name="website"
                className="form-control"
                value={profile.website || ""}
                onChange={handleChange}
              />
            </div>

            <button
              type="submit"
              className="btn btn-primary"
            >
              Save Profile
            </button>

          </form>

        </div>
      </div>
    );
  }

  // =====================================================
  // CANDIDATE PROFILE
  // =====================================================

  return (
    <div className="container py-5">
      <div className="card shadow p-4">

        <h2>My Profile</h2>

        <p className="text-muted">
          Welcome! You are logged in.
        </p>

      </div>
    </div>
  );
}

export default Profile;