import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const API = "https://jobportal-aver.onrender.com";

function Login() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // Decode JWT token
  const decodeToken = (token) => {
    try {
      const payload = JSON.parse(atob(token.split(".")[1]));
      return payload;
    } catch (err) {
      console.error("Token decode error:", err);
      return null;
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      // 1. Login request
      const loginRes = await axios.post(`${API}/login`, formData);

      const token = loginRes.data.token;

      // 2. Decode token to get role
      const decoded = decodeToken(token);
      const role = decoded?.role;

      // 3. Get profile data using token
      const profileRes = await axios.get(`${API}/profile`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const user = profileRes.data;

      // 4. Save data in localStorage
      localStorage.clear();

      localStorage.setItem("token", token);
      localStorage.setItem("role", role);
      localStorage.setItem("user_id", user.id);
      localStorage.setItem("full_name", user.full_name);

      alert("Login successful!");

      // 5. Redirect based on role
      if (role === "recruiter") {
        navigate("/recruiter-dashboard");
      } else if (role === "admin") {
        navigate("/admin-dashboard");
      } else {
        navigate("/candidate-dashboard");
      }

    } catch (err) {
      console.error(err);
      setError(err.response?.data?.message || "Login failed");
    }
  };

  return (
    <div className="container py-5" style={{ maxWidth: "450px" }}>
      <div className="card shadow p-4">
        <h2 className="text-center mb-4">Login</h2>

        {error && (
          <div className="alert alert-danger">{error}</div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              type="email"
              name="email"
              className="form-control"
              placeholder="Enter email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>

          <div className="mb-4">
            <label className="form-label">Password</label>
            <input
              type="password"
              name="password"
              className="form-control"
              placeholder="Enter password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>

          <button type="submit" className="btn btn-primary w-100">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;