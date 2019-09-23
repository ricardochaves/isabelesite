function scrollMe(element) {
    let target = element.getAttribute("data-move-to-id") || "header";
    let elementTarget = document.getElementById(target);
    if (!elementTarget) {
        return;
    }
    myMoveTo(elementTarget);
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
function verifyScrollTo() {
    if (window.location.hash) {
        var hash = window.location.hash.substring(1); //Puts hash in variable, and removes the # character
        let elementTarget = document.getElementById(hash);
        if (!elementTarget) {
            return;
        }
        myMoveTo(elementTarget);
    }
}
function myMoveTo(element) {
    let offsetTop = element.offsetTop;
    window.scroll({
        top: offsetTop,
        behavior: "smooth"
    });
}

// Test via a getter in the options object to see if the passive property is accessed
var supportsPassive = true;


function fn() {
    document.getElementById("header").style.backgroundPosition = "50%" + (document.body.scrollTop) * -1.3;
}
function initMoveBackGround() {
    // Use our detect's results. passive applied if supported, capture will be false either way.
    document.addEventListener('scroll', fn, { capture: false, passive: true });
}

function mobileMenu() {
    if (document.getElementById("nav-list").style.display == "") {
        document.getElementById("nav-list").style.display = "initial";
        return;
    };

    document.getElementById("nav-list").style.display = "";
}

function initMenu() {
    document.getElementById("nav-toggle").addEventListener("click", mobileMenu)
}


document.addEventListener("DOMContentLoaded", function (event) {
    initMoveTo();
    initMenu();
    initMoveBackGround();
    verifyScrollTo();
});

