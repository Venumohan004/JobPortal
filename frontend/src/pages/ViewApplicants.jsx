import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

function ViewApplicants() {
  const { id } = useParams();

  const [applicants, setApplicants] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchApplicants();
  }, []);

  const fetchApplicants = async () => {
    try {
      const res = await api.get(`/jobs/${id}/applicants`);
      setApplicants(res.data || []);
    } catch (err) {
      console.error(
        "Applicants fetch error:",
        err.response?.data || err.message
      );

      // Show empty list if request fails
      setApplicants([]);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container py-5">
        <p>Loading applicants...</p>
      </div>
    );
  }

  return (
    <div className="container py-5">
      <h2 className="mb-4">Applicants</h2>

      {applicants.length === 0 ? (
        <div className="alert alert-info">
          No applicants yet for this job.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-bordered align-middle">
            <thead className="table-dark">
              <tr>
                <th>Candidate</th>
                <th>Applied At</th>
                <th>Status</th>
              </tr>
            </thead>

            <tbody>
              {applicants.map((applicant) => (
                <tr key={applicant.id}>
                  <td>Candidate #{applicant.candidate_id}</td>

                    <td>
                        {applicant.applied_at
                        ? new Date(applicant.applied_at).toLocaleString()
                        : "Recently applied"}
                    </td>

                  <td>
                    <span className="badge bg-success">
                      Application received
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default ViewApplicants;