const BASE_URL = "http://127.0.0.1:5000/api";

export async function uploadCSV(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BASE_URL}/upload`, {
    method: "POST",
    body: formData
  });

  return res.json();
}

export async function getSites() {
  const res = await fetch(`${BASE_URL}/sites`);
  return res.json();
}

export async function verifySite(siteId) {
  const res = await fetch(`${BASE_URL}/verify/${siteId}`, {
    method: "POST"
  });
  return res.json();
}
