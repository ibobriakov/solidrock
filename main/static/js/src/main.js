/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 15.03.13
 * Time: 12:11
 * To change this template use File | Settings | File Templates.
 */

function get_async_json (url) {
    var json = false;
    $.ajax({
        url: url,
        async: false,
        success: function(data) {
            json = data;
        }
    });
    return json;
}

var rest_url = get_async_json('/api/v1/');