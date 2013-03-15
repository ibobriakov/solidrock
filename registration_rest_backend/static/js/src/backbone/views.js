/**
 * Create user: jackdevil
 */

function form_view_fabric(type,attributes) {
    return Backbone.View.extend ({
        model: form_model_fabric(type,attributes),
        template: _.template($("#form-template").html()),
        render: function() {
            this.$el.html(this.template({
                'fields':this.model.toJSON(),
                'model':this.model,
                'type':type
            }));
            var object = {};
            object[type] = this.model;
            this.rivets = rivets.bind(this.el, object);
            return this;
        }
    });
}

var job_seeker_view = new (form_view_fabric('registration',{
    'fields':{'first_name':'','last_name':'','email_address':'','password':'','re_password':'','user_type':'job_seeker'},
    'types':{'first_name':'text','last_name':'text','email_address':'email','password':'password','re_password':'password','user_type':'hidden'},
    'titles':{'first_name':'First Name','last_name':'Last Name','email_address':'Email','password':'Password','re_password':'Re-Password','user_type':''}
}))({el:$('#registration-form')});

job_seeker_view.render();