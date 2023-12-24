import React from "react";
import PrivateRoute from "./PrivateRoute";
import { Routes, Route } from 'react-router-dom';
import NotFound from "../pages/notfound/NotFound";
import MainPage from "../pages/main/Main";
import Links from "../pages/links/Links";
import Create from "../pages/create/Create";
import New from "../pages/create/New";

//роуты
export default function MembersRouter() {
  return (
      <Routes>
        <Route path="*" element={<NotFound />} />
        <Route path="/" element={<MainPage />} />
        <Route path="links/:code" element={<Links />} />
        <Route path="create/:code" element={<PrivateRoute><Create /></PrivateRoute>} />
        <Route path="new" element={<PrivateRoute><New /></PrivateRoute>} />
      </Routes>
  );
}