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
        categories_add: function(){
            var categories = this.get('categories');
            categories.push({});
            this.set('categories',categories);
            this.view.render();
            return false;
        },
        sub_categories_add: function(){
            var sub_categories = this.get('sub_categories');
            sub_categories.push({});
            this.set('sub_categories',sub_categories);
            this.view.render();
            return false;
        },
        essential_del: function(e){
            console.log(e);
            return false;
        },
        desireable_del: function(e){
            console.log(e);
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