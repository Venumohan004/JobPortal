import { Link, useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();

  const token = localStorage.getItem("token");
  const role = localStorage.getItem("role");

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
    navigate("/login");
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm">
      <div className="container">
        {/* Brand */}
        <Link className="navbar-brand fw-bold" to="/">
          JobPortal
        </Link>

        {/* Mobile Toggle */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarContent"
          aria-controls="navbarContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Navbar Content */}
        <div className="collapse navbar-collapse" id="navbarContent">
          {/* Left Menu */}
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link className="nav-link" to="/">
                Home
              </Link>
            </li>

            <li className="nav-item">
              <Link className="nav-link" to="/jobs">
                Jobs
              </Link>
            </li>

            {/* Candidate Links */}
            {token && role === "candidate" && (
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/saved-jobs">
                    Saved Jobs
                  </Link>
                </li>

                <li className="nav-item">
                  <Link className="nav-link" to="/upload-resume">
                    Upload Resume
                  </Link>
                </li>
              </>
            )}

            {/* Recruiter Dashboard */}
            {token && role === "recruiter" && (
              <li className="nav-item">
                <Link className="nav-link" to="/recruiter/dashboard">
                  Dashboard
                </Link>
              </li>
            )}

            {/* Admin Dashboard */}
            {token && role === "admin" && (
              <li className="nav-item">
                <Link className="nav-link" to="/admin/dashboard">
                  Admin
                </Link>
              </li>
            )}
          </ul>

          {/* Right Menu */}
          <div className="d-flex align-items-center gap-2">
            {token ? (
              <>
                <Link to="/profile" className="btn btn-outline-light">
                  Profile
                </Link>

                <button className="btn btn-danger" onClick={handleLogout}>
                  Logout
                </button>
              </>
            ) : (
              <>
                <Link to="/login" className="btn btn-outline-light">
                  Login
                </Link>

                <Link to="/register" className="btn btn-primary">
                  Register
                </Link>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;