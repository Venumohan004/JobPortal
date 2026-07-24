import { Link } from "react-router-dom";

function Hero() {
  return (
    <section
      style={{
        background: "linear-gradient(135deg, #0f172a 0%, #2563eb 100%)",
        color: "white",
        padding: "80px 0",
      }}
    >
      <div className="container">
        <div className="row align-items-center g-5">
          {/* Left */}
          <div className="col-lg-6">
            <span className="badge bg-light text-primary px-3 py-2 rounded-pill mb-3">
              🚀 Smart Career Platform
            </span>

            <h1
              className="fw-bold mb-4"
              style={{ fontSize: "3.8rem", lineHeight: "1.1" }}
            >
              Find Your Dream Job <br />
              <span style={{ color: "#93c5fd" }}>Today</span>
            </h1>

            <p
              className="lead mb-4"
              style={{ color: "#dbeafe", maxWidth: "540px" }}
            >
              Explore thousands of job opportunities from top companies across
              India. Apply faster, track applications, and build a successful
              career.
            </p>

            <div className="d-flex gap-3 flex-wrap">
              <Link to="/jobs" className="btn btn-light btn-lg px-4">
                🔍 Find Jobs
              </Link>

              <Link
                to="/create-job"
                className="btn btn-outline-light btn-lg px-4"
              >
                💼 Post a Job
              </Link>
            </div>
          </div>

          {/* Right */}
          <div className="col-lg-6">
            <div className="position-relative">
              <img
                src="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1200&q=80"
                alt="Job Search"
                className="img-fluid rounded-4 shadow-lg"
              />

              {/* Floating Card */}
              <div
                className="position-absolute bg-white text-dark p-3 rounded-4 shadow"
                style={{
                  bottom: "20px",
                  left: "20px",
                  width: "260px",
                }}
              >
                <h6 className="fw-bold mb-1">Python Backend Developer</h6>
                <p className="mb-1 text-muted">ABC Technologies</p>
                <p className="mb-2 text-muted small">Bangalore • ₹8–12 LPA</p>

                <span className="badge bg-success">Actively Hiring</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;