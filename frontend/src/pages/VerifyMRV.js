import React, { useState } from "react";
import { verifySite } from "../services/api";

export default function VerifyMRV() {
  const [siteId, setSiteId] = useState("");
  const [result, setResult] = useState(null);

  const handleVerify = async () => {
    const res = await verifySite(siteId);
    setResult(res);
  };

  return (
    <div>
      <h2>Verify MRV</h2>
      <input
        placeholder="Enter Site ID"
        value={siteId}
        onChange={(e) => setSiteId(e.target.value)}
      />
      <button onClick={handleVerify}>Verify</button>

      {result && (
        <div>
          <p>Status: {result.status}</p>
          <p>Blockchain TX: {result.blockchain_tx}</p>
        </div>
      )}
    </div>
  );
}
