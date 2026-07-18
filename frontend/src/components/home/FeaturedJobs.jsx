function FeaturedJobs() {
  const jobs = [
    {
      id: 1,
      title: "Python Backend Developer",
      company: "ABC Technologies",
      location: "Bangalore",
      salary: "₹8 LPA",
    },
    {
      id: 2,
      title: "React Frontend Developer",
      company: "XYZ Solutions",
      location: "Hyderabad",
      salary: "₹7 LPA",
    },
    {
      id: 3,
      title: "Data Analyst",
      company: "TechSoft",
      location: "Chennai",
      salary: "₹6 LPA",
    },
  ];

  return (
    <section className="container my-5">
      <h2 className="text-center fw-bold mb-4">Featured Jobs</h2>

      <div className="row">
        {jobs.map((job) => (
          <div className="col-md-4 mb-4" key={job.id}>
            <div className="card shadow-sm h-100">
              <div className="card-body">
                <h5>{job.title}</h5>

                <p className="text-muted">{job.company}</p>

                <p>📍 {job.location}</p>

                <p className="fw-bold text-success">
                  {job.salary}
                </p>

                <button className="btn btn-primary w-100">
                  View Details
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default FeaturedJobs;