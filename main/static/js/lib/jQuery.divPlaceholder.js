/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 07.06.13
 * Time: 10:09
 * To change this template use File | Settings | File Templates.
 */
(function ($) {
	$(document).on('change keydown keypress input', '*[data-placeholder]', function() {
		if (this.textContent) {
			this.setAttribute('data-div-placeholder-content', 'true');
		}
		else {
			this.removeAttribute('data-div-placeholder-content');
		}
	});
})(jQuery);