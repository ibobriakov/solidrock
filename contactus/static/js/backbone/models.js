/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 06.04.13
 * Time: 9:44
 * To change this template use File | Settings | File Templates.
 */

var ContactModel = Backbone.Model.extend({
    urlRoot: rest_url[type].list_endpoint,
    keyup: function(event) {
        if (event.keyCode == 13){
            this.commit(event);
        }
    },
    commit: function(event){
        var that = this;
        var parent = event.target.parentElement;
        var next = $(parent).attr('data-next-url');
        this.save({},{ wait: true,
            error: function(model,response) {
                that.view.errors = JSON.parse(response.responseText)[type];
                that.view.render();
            },
            success: function(){
                that.view.errors = [];
                that.view.render();
                if (next) {
                    window.location.replace(next);
                } else {
                    window.location.replace('/');
                }
            }
        });
    },
    get_errors: function(){
        return this.error;
    }
});