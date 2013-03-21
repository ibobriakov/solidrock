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
        commit: function() {
            this.collection.each(function(element,index){
               element.commit();
            });
        },
        create: function() {
            this.collection.add({});
            this.render();
            return false;
        },
        render: function() {
            this.$el.html(this.template({'collection':this.collection.models,'type':type}));

            var view_object = {};
            view_object[type+'_view'] = this;
            this.rivets = rivets;
            this.rivets.bind(this.el, view_object);

            var that = this;
            this.collection.each(function(element, index, list){
                var model_object = {};
                model_object[type+'_'+index] = element;
                element.rivets = rivets;
                element.rivets.bind(that.el, model_object);
                element.view = that;
            });
        }
    });
}
