// Runs after the page loads
document.addEventListener("DOMContentLoaded", function () {
  console.log("Farm Management System loaded.");

  // Automatically dismiss flash alerts after 3 seconds
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach((alert) => {
    setTimeout(() => {
      alert.style.display = 'none';
    }, 3000);
  });
});