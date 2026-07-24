import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../services/api";
import "../styles/dashboard.css";


function ScheduleInterview() {

  const { applicationId } = useParams();
  const navigate = useNavigate();


  const [formData, setFormData] = useState({

    interview_date: "",
    interview_time: "",
    mode: "Online",
    meeting_link: "",
    location: "",
    notes: ""

  });


  const [message, setMessage] = useState("");
  const [error, setError] = useState("");



  const handleChange = (e) => {

    setFormData({

      ...formData,
      [e.target.name]: e.target.value

    });

  };




  const handleSubmit = async (e) => {

    e.preventDefault();


    try {


      const response = await api.post(

        "/interviews/",

        {

          application_id: Number(applicationId),

          ...formData

        }

      );



      setMessage(

        response.data.message ||

        "Interview scheduled successfully"

      );



      setError("");



      setTimeout(() => {

        navigate(-1);

      }, 2000);



    } catch (err) {


      console.error(

        "Interview scheduling error:",

        err.response?.data || err.message

      );


      setError(

        err.response?.data?.message ||

        "Failed to schedule interview"

      );


      setMessage("");

    }

  };




  return (

    <div className="container py-5">


      <h2 className="mb-4">

        Schedule Interview

      </h2>



      <div className="card p-4">


        <p>

          Application ID:

          <strong> {applicationId}</strong>

        </p>



        {
          message && (

            <div className="alert alert-success">

              {message}

            </div>

          )
        }



        {
          error && (

            <div className="alert alert-danger">

              {error}

            </div>

          )
        }




        <form onSubmit={handleSubmit}>


          <div className="mb-3">


            <label className="form-label">

              Interview Date

            </label>


            <input

              type="date"

              name="interview_date"

              className="form-control"

              value={formData.interview_date}

              onChange={handleChange}

              required

            />


          </div>





          <div className="mb-3">


            <label className="form-label">

              Interview Time

            </label>


            <input

              type="time"

              name="interview_time"

              className="form-control"

              value={formData.interview_time}

              onChange={handleChange}

              required

            />


          </div>





          <div className="mb-3">


            <label className="form-label">

              Interview Mode

            </label>


            <select

              name="mode"

              className="form-control"

              value={formData.mode}

              onChange={handleChange}

            >


              <option value="Online">

                Online

              </option>


              <option value="Offline">

                Offline

              </option>


            </select>


          </div>






          {
            formData.mode === "Online" && (


              <div className="mb-3">


                <label className="form-label">

                  Meeting Link

                </label>


                <input

                  type="text"

                  name="meeting_link"

                  className="form-control"

                  placeholder="Google Meet / Zoom link"

                  value={formData.meeting_link}

                  onChange={handleChange}

                />


              </div>


            )
          }







          {
            formData.mode === "Offline" && (


              <div className="mb-3">


                <label className="form-label">

                  Location

                </label>


                <input

                  type="text"

                  name="location"

                  className="form-control"

                  placeholder="Interview location"

                  value={formData.location}

                  onChange={handleChange}

                />


              </div>


            )
          }







          <div className="mb-3">


            <label className="form-label">

              Notes

            </label>


            <textarea

              name="notes"

              className="form-control"

              rows="3"

              placeholder="Additional instructions"

              value={formData.notes}

              onChange={handleChange}

            />


          </div>





          <button

            type="submit"

            className="btn btn-success"

          >

            Schedule Interview

          </button>
          
        </form>

      </div>

    </div>

  );

}



export default ScheduleInterview;