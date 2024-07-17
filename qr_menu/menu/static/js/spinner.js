// spinner.js
document.addEventListener("DOMContentLoaded", function() {
    const spinner = document.getElementById("spinner");
  
    function showSpinner() {
      spinner.classList.remove("hidden");
    }
  
    function hideSpinner() {
      spinner.classList.add("hidden");
    }
  
    window.addEventListener("load", hideSpinner);
  });
  