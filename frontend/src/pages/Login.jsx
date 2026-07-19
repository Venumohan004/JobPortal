import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        "https://jobportal-aver.onrender.com/login",
        {
          email,
          password,
        }
      );

      // Check backend response
      console.log("Login response:", res.data);

      // Get token from either access_token or token
      const token = res.data.access_token || res.data.token;

      // Save token in localStorage
      localStorage.setItem("token", token);

      alert("Login successful");

      // Redirect to home page
      navigate("/profile");
    } catch (error) {
      console.error(error);

      const msg =
        error.response?.data?.message || "Login failed";

      alert(msg);
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "50px auto" }}>
      <h2>Login</h2>

      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <br /><br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <br /><br />

        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;