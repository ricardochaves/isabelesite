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

