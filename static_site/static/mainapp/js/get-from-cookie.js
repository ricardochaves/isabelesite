function getCookie(name) {
  let cookie = {};

  document.cookie.split(';').forEach(function(el) {
    let [k,v] = el.split('=');
    cookie[k.trim()] = el.replace("gclid=","");
  })
  return cookie[name];

}
function addQueryString(id, queryString){
  // Adiciona a query string ao href
  const link = document.querySelector(id);
  if (typeof link !== "undefined")
  {
    link.href = link +"?"+ queryString;
  }
}


document.addEventListener("DOMContentLoaded", function() {
  const gclidCookie = getCookie("gclid")
  if (typeof gclidCookie === "undefined") {return}
  addQueryString("#link_1", gclidCookie);
  addQueryString("#link_2", gclidCookie);

});

