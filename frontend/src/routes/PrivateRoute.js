import React, { useState, useEffect } from "react";
import { Navigate } from "react-router-dom";

// обработка роутов страниц для юзеров
export default function PrivateRoute({ children }) {
  const [auth, setAuth] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = () => {
      const refreshToken = localStorage.getItem('authtoken');
      if (refreshToken) {
        setAuth(true);
      } else {
        setAuth(false);
      }
      setLoading(false);
    }
    checkAuth();
  }, []);

  if (loading) {
    return null;
  }
  if (!auth) {
    return <Navigate to="/" />;
  }

  return children;
}
