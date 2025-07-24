const counter = document.getElementById("visitor-count");

// Replace this URL with your actual backend API endpoint later (e.g., Azure Function URL)
const apiUrl = "https://YOUR-API-ENDPOINT-HERE";

fetch(apiUrl)
  .then((response) => response.json())
  .then((data) => {
    counter.textContent = `👀 Visitors: ${data.visitorCount}`;
  })
  .catch((error) => {
    console.error("Error fetching visitor count:", error);
    counter.textContent = "👀 Visitors: (offline)";
  });
