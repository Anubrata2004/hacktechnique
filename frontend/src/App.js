import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import UploadData from "./pages/UploadData";
import MRVRecords from "./pages/MRVRecords";
import VerifyMRV from "./pages/VerifyMRV";
import Credits from "./pages/Credits";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/upload" element={<UploadData />} />
          <Route path="/records" element={<MRVRecords />} />
          <Route path="/verify" element={<VerifyMRV />} />
          <Route path="/credits" element={<Credits />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
