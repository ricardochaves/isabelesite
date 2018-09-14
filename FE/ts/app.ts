function scrollMe(element: Element) {
    let target = element.getAttribute("data-move-to-id") || "header";

    let elementTarget = document.getElementById(target);
    if (!elementTarget) {
        return
    }
    myMoveTo(elementTarget);

    let menu = document.getElementById("nav-list");
    if (menu) {
        menu.style.display = "";
    }

}

function initMoveTo() {
    document.querySelectorAll('[data-move-to-id]').forEach(function (currentValue) {
        currentValue.addEventListener("click", function () { scrollMe(currentValue) }, false);
    });
}

function verifyScrollTo() {
    if (window.location.hash) {
        var hash = window.location.hash.substring(1); //Puts hash in variable, and removes the # character

        let elementTarget = document.getElementById(hash);
        if (!elementTarget) {
            return
        }
        myMoveTo(elementTarget);
    }
}

function myMoveTo(element: HTMLElement) {

    let offsetTop = element.offsetTop;

    window.scroll({
        top: offsetTop,
        behavior: "smooth"
    });
}