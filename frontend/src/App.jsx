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
import CreateJob from "./pages/CreateJob"; // Create this file if not available

import ProtectedRoute from "./components/common/ProtectedRoute";
import Navbar from "./components/common/Navbar";

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

        {/* =========================
            Candidate Protected Routes
        ========================== */}
        <Route
          path="/profile"
          element={
            <ProtectedRoute allowedRoles={["candidate"]}>
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
          path="/recruiter/dashboard"
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

        {/* =========================
            Admin Protected Routes
        ========================== */}
        <Route
          path="/admin/dashboard"
          element={
            <ProtectedRoute allowedRoles={["admin"]}>
              <AdminDashboard />
            </ProtectedRoute>
          }
        />

        {/* =========================
            Fallback Route
        ========================== */}
        <Route
          path="*"
          element={
            <div className="container py-5 text-center">
              <h2>404 - Page Not Found</h2>
            </div>
          }
        />
      </Routes>
    </>
  );
}

export default App;