import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import React from 'react';
import HomePage from './components/HomePage/Home';
import Result from './components/Dashboard/Result';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/result" element={<Result />} />
      </Routes>
    </Router>
  );
}

export default App;
