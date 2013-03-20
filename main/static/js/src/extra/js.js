$(document).ready(function(){
    
     setTimeout(function() {$("._slider_block ._slider ._sl_block .VjCarouselLite").jCarouselLite({
        btnNext: "._slider_block ._slider ._sl_block ._sl_next",
        btnPrev: "._slider_block ._slider ._sl_block ._sl_prev",
        visible: 3,
        speed: 700
     });},400 );

    // Сроки и политика
    $('._footer_nav li a').click(function(e) {
		e.preventDefault();
		var id = $('.window.terms .window_block');
		var maskHeight = $(document).height();
		var maskWidth = $(window).width();
		$('.window.terms ._hide').css({'width':maskWidth,'height':maskHeight});
		$('.window.terms ._hide').fadeIn(500);
		$('.window.terms ._hide').fadeTo(500);
		var winH = $(window).height();
		var winW = $(window).width();
        var hhh = $(document).height();
		$(id).css('top',  hhh-$(id).height()/0.75);
		$(id).css('left', winW/2-$(id).width()/2);
		$(id).fadeIn(500);
	});
	$('.window .close').click(function (e) {
		e.preventDefault();
		$('._hide, .window_block').hide();
	});
	$('.window.terms ._hide').click(function () {
		$(this).hide();
		$('.window.terms .window_block').hide();
	});
    
    $('.window.terms .window_block .top ul li').click(function() {
        $('.window.terms .window_block .top ul li').removeClass('active');
        $(this).addClass('active');
        
    });

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
    
    $('#canvas div').hover(function() {
        //var a = $(this).attr('id');
        //if (a != 'paper') alert($('#'+a+' h2').text());
    });
    
});