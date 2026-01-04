import React, { useEffect, useState } from "react";
import { getSites } from "../services/api";
import StatusBadge from "../components/StatusBadge";

export default function MRVRecords() {
  const [sites, setSites] = useState([]);

  useEffect(() => {
    getSites().then(setSites);
  }, []);

  return (
    <div>
      <h2>MRV Records</h2>
      <table>
        <thead>
          <tr>
            <th>Site ID</th>
            <th>Area (ha)</th>
            <th>Carbon</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {sites.map((s) => (
            <tr key={s.site_id}>
              <td>{s.site_id}</td>
              <td>{s.area_ha}</td>
              <td>{s.total_carbon_stock}</td>
              <td><StatusBadge status={s.mrv_status} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
