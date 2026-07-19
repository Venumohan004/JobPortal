import { useState } from "react";
import { useNavigate, useLocation, Link } from "react-router-dom";
import api from "../services/api";

function Login() {
  const navigate = useNavigate();
  const location = useLocation();

  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  // Redirect back to the page user came from
  const from = location.state?.from || "/jobs";

  // ✅ Missing function
  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      const response = await api.post("/login", form);

      console.log("Login response:", response.data);

      // Get token from backend response
      const token =
        response.data.access_token ||
        response.data.token;

      if (!token) {
        setMessage("Token not received from server");
        return;
      }

      // Save token
      localStorage.setItem("token", token);

      setMessage("Login successful!");

      // Redirect after login
      setTimeout(() => {
        navigate(from, { replace: true });
      }, 1000);

    } catch (err) {
      console.error(err);

      setMessage(
        err.response?.data?.message ||
        err.response?.data?.error ||
        "Invalid email or password"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container py-5" style={{ maxWidth: "450px" }}>
      <div className="card shadow-sm border-0">
        <div className="card-body p-4">
          <h2 className="text-center mb-4">Welcome Back</h2>

          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">Email</label>

              <input
                type="email"
                name="email"
                className="form-control"
                placeholder="Enter your email"
                value={form.email}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label className="form-label">Password</label>

              <input
                type="password"
                name="password"
                className="form-control"
                placeholder="Enter your password"
                value={form.password}
                onChange={handleChange}
                required
              />
            </div>

            <button
              type="submit"
              className="btn btn-primary w-100"
              disabled={loading}
            >
              {loading ? "Logging in..." : "Login"}
            </button>
          </form>

          {message && (
            <div
              className={`alert mt-3 ${
                message.includes("successful")
                  ? "alert-success"
                  : "alert-danger"
              }`}
            >
              {message}
            </div>
          )}

          <div className="text-center mt-3">
            <span>Don’t have an account? </span>

            <Link to="/register">Register here</Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;