/**
 * Created with PyCharm.
 * User: jackdevil
 */

function profile_model_fabric(type) {
    return Backbone.Model.extend({
        errors: {},
        valid: false,
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