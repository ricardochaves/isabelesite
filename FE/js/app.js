function scrollMe(element) {
    let target = element.getAttribute("data-move-to-id") || "header";
    let elementTarget = document.getElementById(target);
    if (!elementTarget) {
        return;
    }
    let offsetTop = elementTarget.offsetTop;
    window.scroll({
        top: offsetTop,
        behavior: "smooth"
    });
    let menu = document.getElementById("nav-list");
    if (menu) {
        menu.style.display = "";
    }
}
function initMoveTo() {
    document.querySelectorAll('[data-move-to-id]').forEach(function (currentValue) {
        currentValue.addEventListener("click", function () { scrollMe(currentValue); }, false);
    });
}
