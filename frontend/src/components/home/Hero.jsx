import { Link } from "react-router-dom";

function Hero() {
  return (
    <section className="bg-primary text-white py-5">
      <div className="container">
        <div className="row align-items-center">

          <div className="col-lg-6">
            <h1 className="display-4 fw-bold">
              Find Your Dream Job Today
            </h1>

            <p className="lead mt-3">
              Explore thousands of job opportunities from top companies.
              Start your career with confidence.
            </p>

            <div className="mt-4">
                <Link to="/jobs" className="btn btn-light btn-lg me-3">
                  Find Jobs
                </Link>

              <button className="btn btn-outline-light btn-lg">
                Post a Job
              </button>
            </div>
          </div>

          <div className="col-lg-6 text-center mt-4 mt-lg-0">
            <img
              src="https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600"
              alt="Job Search"
              className="img-fluid rounded shadow"
            />
          </div>

        </div>
      </div>
    </section>
  );
}

export default Hero;