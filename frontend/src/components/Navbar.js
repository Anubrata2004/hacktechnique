import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar">
      <h1>Blue Carbon MRV</h1>
      <div>
        <Link to="/">Dashboard</Link>
        <Link to="/upload">Upload</Link>
        <Link to="/records">Records</Link>
        <Link to="/verify">Verify</Link>
        <Link to="/credits">Credits</Link>
      </div>
    </nav>
  );
}
