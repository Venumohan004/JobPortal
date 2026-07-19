import axios from "axios";

const api = axios.create({
  baseURL: "https://jobportal-aver.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 30000,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  // Only attach token for protected routes
  const protectedRoutes = [
    "/profile",
    "/applications",
    "/apply",
    "/recruiter",
    "/admin",
  ];

  const shouldAttachToken = protectedRoutes.some((route) =>
    config.url.includes(route)
  );

  if (token && shouldAttachToken) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

export default api;