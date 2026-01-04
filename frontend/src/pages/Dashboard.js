import React from "react";
import Card from "../components/Card";

export default function Dashboard() {
  return (
    <div>
      <h2>Dashboard</h2>
      <div className="grid">
        <Card title="Total Sites" value="--" />
        <Card title="Verified MRV" value="--" />
        <Card title="Blockchain Enabled" value="Yes" />
      </div>
    </div>
  );
}
