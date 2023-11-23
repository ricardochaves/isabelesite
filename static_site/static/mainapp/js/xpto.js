// Função para pegar a query string
function getQueryString() {
  // Obtém a URL atual
  const url = window.location.href;

  // Obtém a query string
  const queryString = url.split("?")[1];

  // Retorna a query string
  return queryString;
}

function addQueryString(id, queryString){
  // Adiciona a query string ao href
  const link = document.querySelector(id);
  if (typeof link !== "undefined")
  {
    link.href = link +"?"+ queryString;
  }
}

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

// Adiciona o código ao evento DOMContentLoaded
document.addEventListener("DOMContentLoaded", function() {
  // Obtém a query string
  const href = getQueryString();
  if (typeof href === "undefined") {return}

  // Adiciona a query string ao href
  addQueryString("#whats-link", href);
  addQueryString("#link_1", href);
  setCookie("gclid", href, 1)

});