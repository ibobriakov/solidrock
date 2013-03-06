/**
 * User: jackdevil
 */

function paper_sync_fabric(csrf_token){
    return Backbone.sync = function(method, model, options){
        var old_sync = Backbone.sync;
        options.beforeSend = function(xhr){
            xhr.setRequestHeader('X-CSRFToken', csrf_token);
        };
        return old_sync(method, model, options);
    };
}