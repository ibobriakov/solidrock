$(document).ready(function(){

    // Radio button
    $('input.styled').radio();
    $('#add').click(function() {
    	var inputs = '';
    	for (i = 1; i <= 5; i++) {
    		inputs += '<br /><label><input type="radio" name="radio" class="styled" /> radio ' + i + '</label>';
    	}
    	$('form').append(inputs);
    	$('input.styled').radio();
    	return false;
    })
    $('#toggle').click(function() {
    	(function($) {
    		$.fn.toggleDisabled = function() {
    			return this.each(function() {
    				this.disabled = !this.disabled;
    			});
    		};
    	})(jQuery);
    	$('input.styled').toggleDisabled().trigger('refresh');
    	return false;
    })
    
});