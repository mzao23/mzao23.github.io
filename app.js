document.addEventListener("DOMContentLoaded", function () {
    var currentUrl = window.location.href;

    var navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(function (link) {
        if (link.href === currentUrl) {
            link.classList.add("active");
        }
    });
});
