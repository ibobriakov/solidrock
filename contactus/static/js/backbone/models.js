/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 06.04.13
 * Time: 9:44
 * To change this template use File | Settings | File Templates.
 */

var ContactModel = Backbone.Model.extend({
    urlRoot: rest_url['contactus'].list_endpoint,
    url: function(){
        if (this.id){
            return this.urlRoot + this.id + '/';
        } else {
            return this.urlRoot;
        }
    },
    keyup: function(event) {
        if (event.keyCode == 13){
            this.commit(event);
        }
    },
    commit: function(event) {
        var that = this;
        this.save({},{ wait: true,
            error: function(model,response) {
                that.view.errors.clear();
                that.view.errors.set(JSON.parse(response.responseText)['contactus']);
                that.view.render();
            },
            success: function(){
                that.view.errors.clear();
                    window.location.replace('/success/contacts');
            }
        });
    }
});

var ContactErrorModel = Backbone.Model.extend({});
