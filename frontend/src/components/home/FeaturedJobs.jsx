import { Link } from "react-router-dom";

const featuredJobs = [
  {
    id: 1,
    title: "Python Backend Developer",
    company: "ABC Technologies",
    location: "Bangalore",
    salary: "₹8 LPA",
    type: "Full Time",
  },
  {
    id: 2,
    title: "React Frontend Developer",
    company: "XYZ Solutions",
    location: "Hyderabad",
    salary: "₹7 LPA",
    type: "Full Time",
  },
  {
    id: 3,
    title: "Data Analyst",
    company: "TechSoft",
    location: "Chennai",
    salary: "₹6 LPA",
    type: "Full Time",
  },
];

function FeaturedJobs() {
  return (
    <section className="py-5 bg-light">
      <div className="container">
        <div className="text-center mb-5">
          <h2 className="fw-bold display-6">Featured Jobs</h2>
          <p className="text-muted">
            Handpicked opportunities from top companies
          </p>
        </div>

        <div className="row g-4">
          {featuredJobs.map((job) => (
            <div className="col-md-6 col-lg-4" key={job.id}>
              <div className="card border-0 shadow-sm h-100 rounded-4 p-3">
                <div className="d-flex align-items-center mb-3">
                  <div
                    className="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center me-3"
                    style={{ width: "50px", height: "50px" }}
                  >
                    <strong>{job.company.slice(0, 2)}</strong>
                  </div>

                  <div>
                    <h5 className="fw-bold mb-0">{job.title}</h5>
                    <small className="text-muted">{job.company}</small>
                  </div>
                </div>

                <p className="mb-2">📍 {job.location}</p>
                <p className="mb-2 text-success fw-semibold">💰 {job.salary}</p>
                <span className="badge bg-light text-dark border mb-4 align-self-start">
                  {job.type}
                </span>

                {/* THIS BUTTON NOW WORKS */}
                <Link
                  to={`/jobs/${job.id}`}
                  className="btn btn-primary w-100 rounded-pill"
                >
                  View Details
                </Link>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default FeaturedJobs;