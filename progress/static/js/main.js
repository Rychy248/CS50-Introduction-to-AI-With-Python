
function loadYear() {
  document.getElementById('year').innerHTML = (new Date()).getFullYear();
};

function main() {
  loadYear();
};


window.addEventListener("DOMContentLoaded", function() {
  main();
}, false);