/**
 * Created with PyCharm.
 * User: jackdevil
 */

function profile_model_fabric(type) {
    return Backbone.Model.extend({
        errors: {},
        valid: false,
        urlRoot: rest_url[type].list_endpoint,
        url: function(){
            if (this.id){
                return this.urlRoot + this.id + '/';
            } else {
                return this.urlRoot;
            }
        },
        commit: function() {
            this.valid = false;
            this.save([],{ wait: true,
                error: function(model,response) {
                    model.valid = false;
                    model.errors = JSON.parse(response.responseText)[type];
                    model.view.render();
                },
                success: function(model){
                    model.errors = [];
                    model.valid = true;
                }
            });
        }
    });
}