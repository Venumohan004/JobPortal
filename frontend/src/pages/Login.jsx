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

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await axios.post(`${API}/login`, formData);

      console.log("Login response:", res.data);

      // Save token
      localStorage.setItem("token", res.data.token);

      // Save role if backend sends it
      localStorage.setItem("role", res.data.role || "candidate");

      alert("Login successful!");

      // Redirect based on role
      if (res.data.role === "recruiter") {
        navigate("/recruiter/dashboard");
      } else {
        navigate("/");
      }

    } catch (err) {
      console.error(err);
      setError(err.response?.data?.message || "Login failed");
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <form onSubmit={handleSubmit}>
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />

        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;