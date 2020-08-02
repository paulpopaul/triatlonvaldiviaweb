(function ($) {
    $(function () {
        /*
         var window_width = $(window).width();/
         * */
        $('.carousel.carousel-slider').carousel({});
        $('.carousel').carousel({dist: 0, shift: 0, padding: 20});
        $('select').material_select();
        $('.parallax').parallax();

        var mediaquery = window.matchMedia("(max-width: 600px)");
        if (mediaquery.matches) {
            // mediaquery es 600
            $('.slider').slider({height: 600, indicators: false});
        } else {
            $('.slider').slider({height: 750, indicators: false});
        }
        $('ul.tabs').tabs();
        $('.scrollspy').scrollSpy({scrollOffset: 200});
        $('.modal').modal();
        $(".button-collapse").sideNav({
            menuWidth: 250
        });
    });
    $('#datepicker').datepicker();

    var app = function (a, b) {
        "use strict";
        var c = a.documentElement, d = function () {
            c.setAttribute("data-useragent", navigator.userAgent)
        }, e = function () {
            var a = b(window), c = 1, d = a.height() / 2.5;
            a.on("mousewheel DOMMouseScroll", function (b) {
                b.preventDefault();
                var e = b.originalEvent.wheelDelta / 120 || -b.originalEvent.detail / 3, f = a.scrollTop(), g = f - parseInt(e * d);
                TweenMax.to(a, c, {scrollTo: {y: g, autoKill: !1}, ease: Power4.easeOut, overwrite: 5})
            })
        }, f = function () {
            b(a).foundation(), d(), e()
        };
        return {init: f}
    }(document, jQuery);
    !function () {
        "use strict";
        app.init()
    }();
})(jQuery);

