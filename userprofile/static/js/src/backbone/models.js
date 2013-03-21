/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 20.03.13
 * Time: 20:49
 * To change this template use File | Settings | File Templates.
 */

function profile_model_fabric(type) {
    return Backbone.Model.extend({
        errors: {},
        commit: function() {
            var error = false;
            this.save([],{ wait: true,
                error: function(model,response){
                    error = true;
                    model.errors = JSON.parse(response.responseText)[type];
                    model.view.render();
                },
                success: function(model){
                    error = false;
                    model.errors = [];
                    section_route.next_section();
                    model.view.render();
                }
            });
            return error;
        }
    });
}