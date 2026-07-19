import axios from "axios";

const api = axios.create({
  baseURL: "https://jobportal-aver.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;