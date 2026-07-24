function Stats() {
  return (
    <section className="pb-5">
      <div className="container">
        <div className="bg-white rounded-4 shadow-sm p-4">
          <div className="row text-center g-4">
            <div className="col-md-3">
              <div style={{ fontSize: "2rem" }}>💼</div>
              <h2 className="fw-bold text-primary mb-0">1000+</h2>
              <p className="text-muted mb-0">Jobs Posted</p>
            </div>

            <div className="col-md-3">
              <div style={{ fontSize: "2rem" }}>🏢</div>
              <h2 className="fw-bold text-success mb-0">500+</h2>
              <p className="text-muted mb-0">Companies</p>
            </div>

            <div className="col-md-3">
              <div style={{ fontSize: "2rem" }}>👥</div>
              <h2 className="fw-bold text-warning mb-0">10K+</h2>
              <p className="text-muted mb-0">Candidates</p>
            </div>

            <div className="col-md-3">
              <div style={{ fontSize: "2rem" }}>📈</div>
              <h2 className="fw-bold text-danger mb-0">95%</h2>
              <p className="text-muted mb-0">Success Rate</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Stats;