import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Register() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    full_name: "",
    email: "",
    password: "",
    role: "candidate",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post("/register", form);

      setMessage(response.data.message || "Registered successfully!");

      setTimeout(() => {
        navigate("/login");
      }, 1500);
    } catch (err) {
      setMessage(err.response?.data?.message || "Registration failed");
    }
  };

  return (
    <div className="container py-5" style={{ maxWidth: "500px" }}>
      <div className="card shadow-sm">
        <div className="card-body">
          <h3 className="mb-4 text-center">Create Account</h3>

          <form onSubmit={handleSubmit}>
            <input
              type="text"
              name="full_name"
              className="form-control mb-3"
              placeholder="Full Name"
              value={form.full_name}
              onChange={handleChange}
              required
            />

            <input
              type="email"
              name="email"
              className="form-control mb-3"
              placeholder="Email"
              value={form.email}
              onChange={handleChange}
              required
            />

            <input
              type="password"
              name="password"
              className="form-control mb-3"
              placeholder="Password"
              value={form.password}
              onChange={handleChange}
              required
            />

            <select
              name="role"
              className="form-select mb-3"
              value={form.role}
              onChange={handleChange}
            >
              <option value="candidate">Candidate</option>
              <option value="recruiter">Recruiter</option>
            </select>

            <button type="submit" className="btn btn-primary w-100">
              Register
            </button>
          </form>

          {message && (
            <div className="alert alert-info mt-3">{message}</div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Register;