$(document).ready(function(){
    
     setTimeout(function() {$("._slider_block ._slider ._sl_block .VjCarouselLite").jCarouselLite({
        btnNext: "._slider_block ._slider ._sl_block ._sl_next",
        btnPrev: "._slider_block ._slider ._sl_block ._sl_prev",
        visible: 3,
        speed: 700
     });},400 );

    $('.right ul li').click(function() {
        $('.right ul li').removeClass('active').css('border-right','1px solid #fff');
        $(this).addClass('active');
        $(this).prev().css('border-right','none');
        $(this).css('border-right','1px solid #d5d5d5');
        var id = $(this).attr('id');
        $('.s1, .s2, .s3, .s4, .s5').css('display','none');
        $('.right .form div.'+id).css('display','block');
    });
    
    $('.nav .pages li').click(function() {
        $('.nav .pages li').removeClass('active').css('border-right','1px solid #fff');
        $(this).addClass('active');
        $(this).prev().css('border-right','none');
        $(this).css('border-right','1px solid #d5d5d5');
        var id = $(this).attr('id');
        $('.list').css('display','none');
        $('.list.'+id).css('display','block');
    });
});