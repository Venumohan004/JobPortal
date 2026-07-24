import { useState } from "react";
import { useNavigate } from "react-router-dom";

function SearchSection() {
  const navigate = useNavigate();
  const [search, setSearch] = useState("");

  const handleSearch = () => {
    if (search.trim()) {
      navigate(`/jobs?search=${encodeURIComponent(search)}`);
    } else {
      navigate("/jobs");
    }
  };

  return (
    <section className="py-4" style={{ marginTop: "-40px" }}>
      <div className="container">
        <div className="bg-white rounded-4 shadow-lg p-4">
          <h3 className="text-center fw-bold mb-4">Quick Job Search</h3>

          <div className="row g-3 align-items-center">
            <div className="col-md-9">
              <input
                type="text"
                className="form-control form-control-lg"
                placeholder="🔍 Search jobs, companies, or skills"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </div>

            <div className="col-md-3">
              <button
                className="btn btn-primary btn-lg w-100"
                onClick={handleSearch}
              >
                Search Jobs
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default SearchSection;