/**
 * Created with PyCharm.
 * User: jackdevil
 */

function profile_model_fabric(type) {
    return Backbone.Model.extend({
        errors: {},
        valid: false,
        urlRoot: rest_url[type].list_endpoint,
        initialize: function(){},
        url: function(){
            if (this.id){
                return this.urlRoot + this.id + '/';
            } else {
                return this.urlRoot;
            }
        },
        essential_add: function(){
            var essentials = this.get('essential_set');
            essentials.push({});
            this.set('essential_set',essentials);
            this.view.render();
            return false;
        },
        desireable_add: function(){
            var desireables = this.get('desireable_set');
            desireables.push({});
            this.set('desireable_set',desireables);
            this.view.render();
            return false;
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