import React, { useEffect, useState } from "react";
import { getSites } from "../services/api";
import StatusBadge from "../components/StatusBadge";

export default function Credits() {
  const [credits, setCredits] = useState([]);

  useEffect(() => {
    getSites().then((sites) => {
      const verified = sites.filter(s => s.mrv_status === "Verified");

      // Simple credit logic for UI (1 credit = 1 ton CO₂)
      const generated = verified.map(site => ({
        site_id: site.site_id,
        credits: Math.round(site.total_carbon_stock),
        status: "Available"
      }));

      setCredits(generated);
    });
  }, []);

  return (
    <div>
      <h2>Carbon Credits</h2>
      <p>Credits generated from verified blue carbon restoration projects.</p>

      {credits.length === 0 ? (
        <p>No credits available yet. Verify MRV records first.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Site ID</th>
              <th>Credits (tCO₂e)</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {credits.map((c, i) => (
              <tr key={i}>
                <td>{c.site_id}</td>
                <td>{c.credits}</td>
                <td><StatusBadge status={c.status} /></td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

