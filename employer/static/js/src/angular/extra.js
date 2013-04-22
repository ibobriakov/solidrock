/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 22.04.13
 * Time: 14:36
 * To change this template use File | Settings | File Templates.
 */

$.fn.replaceWithPush = function(a) {
    var $a = $(a);
    this.replaceWith($a);
    return $a;
};

function get_cookie (name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}