function SearchSection() {
  return (
    <section className="container my-5">
      <div className="card shadow p-4">
        <h2 className="text-center mb-4">Search Jobs</h2>

        <div className="row g-3">
          <div className="col-md-4">
            <input
              type="text"
              className="form-control"
              placeholder="Job Title"
            />
          </div>

          <div className="col-md-4">
            <input
              type="text"
              className="form-control"
              placeholder="Location"
            />
          </div>

          <div className="col-md-4">
            <button className="btn btn-primary w-100">
              Search
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

export default SearchSection;