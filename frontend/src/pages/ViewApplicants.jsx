import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api";

function ViewApplicants() {

  const { id } = useParams();

  const [applicants, setApplicants] = useState([]);
  const [loading, setLoading] = useState(true);



  useEffect(() => {

    fetchApplicants();

  }, [id]);



  const fetchApplicants = async () => {

    try {

      const res = await api.get(`/jobs/${id}/applicants`);

      console.log("Applicants Response:", res.data);


      // Supports both response formats
      if (Array.isArray(res.data)) {

        setApplicants(res.data);

      } else {

        setApplicants(
          res.data.applications || []
        );

      }


    } catch (err) {

      console.error(
        "Applicants fetch error:",
        err.response?.data || err.message
      );

      setApplicants([]);

    } finally {

      setLoading(false);

    }

  };



  if (loading) {

    return (

      <div className="container py-5">

        <p>
          Loading applicants...
        </p>

      </div>

    );

  }



  return (

    <div className="container py-5">


      <h2 className="mb-4">
        Applicants
      </h2>



      {
        applicants.length === 0 ? (

          <div className="alert alert-info">

            No applicants yet for this job.

          </div>


        ) : (


          <div className="table-responsive">


            <table className="table table-bordered align-middle">


              <thead className="table-dark">

                <tr>

                  <th>
                    Application ID
                  </th>

                  <th>
                    Candidate
                  </th>

                  <th>
                    Status
                  </th>

                  <th>
                    Applied At
                  </th>

                  <th>
                    Action
                  </th>


                </tr>

              </thead>



              <tbody>


                {
                  applicants.map((applicant) => (


                    <tr key={applicant.id}>


                      <td>
                        {applicant.id}
                      </td>



                      <td>

                        Candidate #{applicant.candidate_id}

                      </td>




                      <td>


                        <span className="badge bg-primary">

                          {applicant.status || "Applied"}

                        </span>


                      </td>




                      <td>


                        {
                          applicant.created_at

                          ?

                          new Date(
                            applicant.created_at
                          ).toLocaleString()

                          :

                          "Recently applied"

                        }


                      </td>




                      <td>


                        <Link

                          to={`/schedule-interview/${applicant.id}`}

                          className="btn btn-success"

                        >

                          Schedule Interview


                        </Link>


                      </td>



                    </tr>


                  ))

                }


              </tbody>


            </table>


          </div>


        )
      }


    </div>

  );

}


export default ViewApplicants;