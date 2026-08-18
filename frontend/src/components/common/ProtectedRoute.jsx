import { Navigate } from "react-router-dom";

function ProtectedRoute({ children, allowedRoles }) {
  const token = localStorage.getItem("token");

  // Get role from the separate role key
  let role = localStorage.getItem("role");

  // If role key doesn't exist, try getting it from user object
  if (!role) {
    try {
      const user = JSON.parse(localStorage.getItem("user"));
      role = user?.role || "";
    } catch (error) {
      role = "";
    }
  }

  // Not logged in
  if (!token) {
    return <Navigate to="/login" replace />;
  }

  // Role not allowed
  if (
    allowedRoles &&
    !allowedRoles.includes(role)
  ) {
    return <Navigate to="/" replace />;
  }

  return children;
}

export default ProtectedRoute;