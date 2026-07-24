import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Jobs from "./pages/Jobs";
import JobDetails from "./pages/JobDetails";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Profile from "./pages/Profile";

import RecruiterDashboard from "./pages/RecruiterDashboard";
import AdminDashboard from "./pages/AdminDashboard";

import SavedJobs from "./pages/SavedJobs";
import ResumeUpload from "./pages/ResumeUpload";
import CreateJob from "./pages/CreateJob";
import EditJob from "./pages/EditJob";
import ViewApplicants from "./pages/ViewApplicants";

import CandidateDashboard from "./pages/CandidateDashboard";
import AppliedJobs from "./pages/AppliedJobs";

import ProtectedRoute from "./components/common/ProtectedRoute";
import Navbar from "./components/common/Navbar";
import ScheduleInterview from "./pages/ScheduleInterview";

function App() {
  return (
    <>
      <Navbar />

      <Routes>
        {/* =========================
            Public Routes
        ========================== */}
        <Route path="/" element={<Home />} />
        <Route path="/jobs" element={<Jobs />} />
        <Route path="/jobs/:id" element={<JobDetails />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/schedule-interview/:applicationId" element={<ScheduleInterview />} />
        
        {/* =========================
            Candidate Protected Routes
        ========================== */}
        <Route
          path="/candidate-dashboard"
          element={
            <ProtectedRoute allowedRoles={["candidate"]}>
              <CandidateDashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/profile"
          element={
            <ProtectedRoute allowedRoles={["candidate", "recruiter"]}>
              <Profile />
            </ProtectedRoute>
          }
        />

        <Route
          path="/saved-jobs"
          element={
            <ProtectedRoute allowedRoles={["candidate"]}>
              <SavedJobs />
            </ProtectedRoute>
          }
        />

        <Route
          path="/applied-jobs"
          element={
            <ProtectedRoute allowedRoles={["candidate"]}>
              <AppliedJobs />
            </ProtectedRoute>
          }
        />

        <Route
          path="/upload-resume"
          element={
            <ProtectedRoute allowedRoles={["candidate"]}>
              <ResumeUpload />
            </ProtectedRoute>
          }
        />

        {/* =========================
            Recruiter Protected Routes
        ========================== */}
        <Route
          path="/recruiter-dashboard"
          element={
            <ProtectedRoute allowedRoles={["recruiter"]}>
              <RecruiterDashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/create-job"
          element={
            <ProtectedRoute allowedRoles={["recruiter"]}>
              <CreateJob />
            </ProtectedRoute>
          }
        />

        <Route
          path="/edit-job/:id"
          element={
            <ProtectedRoute allowedRoles={["recruiter"]}>
              <EditJob />
            </ProtectedRoute>
          }
        />

        <Route
          path="/job/:id/applicants"
          element={
            <ProtectedRoute allowedRoles={["recruiter"]}>
              <ViewApplicants />
            </ProtectedRoute>
          }
        />

        {/* =========================
            Admin Protected Routes
        ========================== */}
        <Route
          path="/admin-dashboard"
          element={
            <ProtectedRoute allowedRoles={["admin"]}>
              <AdminDashboard />
            </ProtectedRoute>
          }
        />

        {/* =========================
            404 Route
        ========================== */}
        <Route
          path="*"
          element={
            <div className="container py-5 text-center">
              <h2>404 - Page Not Found</h2>
              <p className="text-muted">
                The page you are looking for does not exist.
              </p>
            </div>
          }
        />
      </Routes>
    </>
  );
}

export default App;