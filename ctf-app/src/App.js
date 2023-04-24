import React from 'react';
import Login from './components/login';
import Dashboard from './components/dashboard';
import RouteGuard from './helpers/RouteGuard';
import { useRoutes } from "react-router-dom";

const App = () => {
  const routes = useRoutes([
    {
      path: '/',
      element: <Login />
    },
    {
      path: 'dashboard',
      element: <RouteGuard><Dashboard /></RouteGuard>
    }
  ]);
  return routes;
}

export default App;