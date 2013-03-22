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
            var next_section = parseInt(section_route.section)+1;
            this.collection.each(function(element){
               element.commit(next_section);
            });
        },
        commit_and_exit: function(){
            this.collection.each(function(element){
                element.commit(false);
            });
        },
        remove: function(event){
            var model = this.collection.get($(event.toElement).attr('data-cid'));
            model.destroy();
            this.render();
            return false;
        },
        create: function() {
            this.collection.add({});
            this.render();
            return false;
        },
        create_by_type: function(){
            var type_object = {};
            type_object[$(event.toElement).attr('data-type-name')] = $(event.toElement).attr('data-type');
            this.collection.add(type_object);
            this.render();
            return false;
        },
        render: function() {
            this.$el.html(this.template({'collection':this.collection,'type':type}));

            var view_object = {};
            view_object[type+'_view'] = this;
            this.rivets = rivets;
            this.rivets.bind(this.el, view_object);

            var that = this;
            this.collection.each(function(element, index, list){
                var model_object = {};
                model_object[type+'_'+element.cid] = element;
                element.rivets = rivets;
                element.rivets.bind(that.el, model_object);
                element.view = that;
            });
        }
    });
}
