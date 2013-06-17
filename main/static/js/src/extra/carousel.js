$(document).ready(function() {
    setTimeout(function() {
        $("._slider_block ._slider ._sl_block .VjCarouselLite").jCarouselLite({
            btnNext: "._slider_block ._slider ._sl_block ._sl_next",
            btnPrev: "._slider_block ._slider ._sl_block ._sl_prev",
            visible: 3,
            speed: 700
        });
    },400 );
});