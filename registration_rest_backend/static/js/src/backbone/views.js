/**
 * Create user: jackdevil
 */

function form_view_fabric(type) {
    return Backbone.View.extend ({
        model: form_model_fabric(type),
        template: _.template($("#form-template").html()),
        render: function() {
            this.$el.html(this.template({
                'fields':this.model.toJSON(),
                'model':this.model,
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

var job_seeker_view = new (form_view_fabric('job_seeker_registration'))({el:$('#registration-form')});1

job_seeker_view.render();