// Função para pegar a query string
function getQueryString() {
  // Obtém a URL atual
  const url = window.location.href;

  // Obtém a query string
  const queryString = url.split("?")[1];

  // Retorna a query string
  return queryString;
}

// Adiciona o código ao evento DOMContentLoaded
document.addEventListener("DOMContentLoaded", function() {
  // Obtém a query string
  const href = getQueryString();
  if (typeof href === "undefined") {return}

  // Adiciona a query string ao href
  const link = document.querySelector("#whats-link");
  link.href = link +"?"+ href;


});