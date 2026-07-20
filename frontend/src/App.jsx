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

import ProtectedRoute from "./components/common/ProtectedRoute";
import Navbar from "./components/common/Navbar";

function App() {
  return (
    <>
      <Navbar />

      <Routes>
        {/* Public Routes */}
        <Route path="/" element={<Home />} />
        <Route path="/jobs" element={<Jobs />} />
        <Route path="/jobs/:id" element={<JobDetails />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/recruiter/dashboard" element={<RecruiterDashboard />} />
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
        <Route path="/saved-jobs" element={<SavedJobs />} />
        <Route path="/upload-resume" element={<ResumeUpload />} />
        
        {/* Protected Route */}
        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />
      </Routes>
    </>
  );
}

export default App;