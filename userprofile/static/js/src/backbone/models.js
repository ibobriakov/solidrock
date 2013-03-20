/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 20.03.13
 * Time: 20:49
 * To change this template use File | Settings | File Templates.
 */

function profile_model_fabric(type) {
    var data = get_async_json(rest_url[type].list_endpoint);
    var Model = Backbone.Model.extend({
        urlRoot: rest_url[type].list_endpoint,
        initialize: function(){
        },
        commit: function() {
            var that = this;
            this.save({},{ wait: true,
                error: function(model,response) {
                    that.view.errors = JSON.parse(response.responseText)[type];
                    that.view.render();
                },
                success: function(){
                    that.view.errors = [];
                    that.view.render();
                }
            });
        }
    });
    var values = {};
    _.each(data.objects[0],function(value,key){
        if (typeof (value) == 'boolean') {
            values[key] = value.toString();
        } else {
            values[key] = value;
        }
    });
    return new Model(values);
}