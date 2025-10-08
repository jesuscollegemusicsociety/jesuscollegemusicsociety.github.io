/*** dev website alert ***/

alert("Looking for the JCMS website? Go to jcms.jesus.cam.ac.uk")

/*** carousel ***/

const defaultOptions = {
    contain: true,
    imagesLoaded: true,
};

var flktys;

htmx.onLoad(function (target) {
    flktys = Array.from(target.querySelectorAll(".main-carousel"))
        .map(elt => new Flickity(elt, { ...defaultOptions, ...JSON.parse(elt.dataset.carousel) }));
});

htmx.on("htmx:beforeHistorySave", function () {
    flktys.forEach(flk => flk.destroy());
});

/*** scroll ***/

htmx.on("htmx:afterSettle", function () {
    if (window.pageYOffset > document.querySelector(".banner").offsetHeight) {
        document.querySelector("main").scrollIntoView();
    }
})
