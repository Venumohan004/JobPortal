function Stats() {
  return (
    <section className="container my-5">
      <div className="row text-center">

        <div className="col-md-3 mb-3">
          <div className="card shadow p-4">
            <h2 className="text-primary">1000+</h2>
            <p>Jobs Posted</p>
          </div>
        </div>

        <div className="col-md-3 mb-3">
          <div className="card shadow p-4">
            <h2 className="text-success">500+</h2>
            <p>Companies</p>
          </div>
        </div>

        <div className="col-md-3 mb-3">
          <div className="card shadow p-4">
            <h2 className="text-danger">10K+</h2>
            <p>Candidates</p>
          </div>
        </div>

        <div className="col-md-3 mb-3">
          <div className="card shadow p-4">
            <h2 className="text-warning">95%</h2>
            <p>Success Rate</p>
          </div>
        </div>

      </div>
    </section>
  );
}

export default Stats;