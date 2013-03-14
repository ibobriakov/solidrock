/**
 * Create user: jackdevil
 */

function form_view_fabric(type,properties) {
    return Backbone.View.extend ({
        template: _.template($("#form-template").html()),
        collection: new (form_collection_fabric(type))(properties),
        render: function() {
            var view = this;
            this.$el.html(this.template({'fields':this.collection,'type':type}));
            this.collection.each(function(model){
                var object = {};
                object[model.get('name')]=model;
                model.rivets = rivets.bind( view.el, object );
            });
        }
    });
}

var job_seeker_class = form_view_fabric('registration',[
    {'name':'first_name', 'type':'text', 'label':'First Name'},
    {'name':'last_name', 'type':'text', 'label':'Last Name'},
    {'name':'email', 'type':'text', 'label':'Email'},
    {'name':'password', 'type':'password', 'label':'Password'},
    {'name':'re-password', 'type':'password', 'label':'Re-password'},
]);

var job_seeker_view = new job_seeker_class({el:$('#registration-form')});

job_seeker_view.render();