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
        commit: function(next_section) {
            this.save([],{ wait: true,
                error: function(model,response){
                    model.errors = JSON.parse(response.responseText)[type];
                    model.view.render();
                },
                success: function(model){
                    model.errors = [];
                    if (next_section) {
                        section_route.next_section(next_section);
                        model.view.render();
                    }
                }
            });
        }
    });
}