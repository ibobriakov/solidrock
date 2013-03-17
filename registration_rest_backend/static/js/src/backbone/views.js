/**
 * Create user: jackdevil
 */

function form_view_fabric(type) {
    return Backbone.View.extend ({
        model: form_model_fabric(type),
        template: _.template($("#form-template").html()),
        errors: [],
        initialize: function(){
            this.model.view = this;
        },
        render: function() {
            this.$el.html(this.template({
                'fields':this.model.toJSON(),
                'model':this.model,
                'errors':this.errors,
                'type':type
            }));
            var object = {};
            object[type] = this.model;
            this.rivets = rivets;
            this.rivets.bind(this.el, object);
            return this;
        }
    });
}
