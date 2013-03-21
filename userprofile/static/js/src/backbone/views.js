/**
 * User: jackdevil
 */

function profile_view_fabric(type, template) {
    template = template || $('#'+type+'_form_template');
    return Backbone.View.extend ({
        template: _.template(template.html()),
        initialize: function() {
            this.collection.view = this;
            this.render();
        },
        render: function() {
            var that = this;
            this.$el.html(this.template({'collection':this.collection.toJSON(),'type':type}));
            this.collection.each(function(element, index, list){
                var object = {};
                object[type+'_'+index] = element;
                element.rivets = rivets;
                element.rivets.bind(that.el, object);
            });
        }
    });
}
