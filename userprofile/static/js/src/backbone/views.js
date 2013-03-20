/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 20.03.13
 * Time: 20:49
 * To change this template use File | Settings | File Templates.
 */

function profile_view_fabric(type, template_selector) {
    template_selector = template_selector || '#form-template';
    return Backbone.View.extend ({
        model: profile_model_fabric(type),
        initialize: function(){
            this.model.view = this;
            var object = {};
            object[type] = this.model;
            this.rivets = rivets;
            this.rivets.bind(this.el, object);
        }
    });
}
