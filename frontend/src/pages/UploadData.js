import React, { useState } from "react";
import { uploadCSV } from "../services/api";

export default function UploadData() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const response = await uploadCSV(file);
    setMessage(response.message);
  };

  return (
    <div>
      <h2>Upload MRV Dataset</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files[0])} />
        <button type="submit">Upload</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
