/**
 * User: jackdevil
 */

function profile_view_fabric(type,redirect_url, template) {
    template = template || $('#'+type+'_form_template');
    return Backbone.View.extend ({
        template: _.template(template.html()),
        action: {},
        initialize: function() {
            this.collection.view = this;
            this.action['section'] = false;
            this.action['url'] = false;
            this.render();
        },

        commit: function() {
            this.action['section'] = parseInt(section_route.section)+1;
            this.collection.each(function(element){
               element.commit();
            });
        },
        
        commit_and_exit: function(){
            this.action['url'] = redirect_url;
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

        check_model_valid: function() {
            for (var i=0; i < this.collection.models.length; i++){
                if (!this.collection.models[i].valid) {
                    return true;
                }
            }
            if (this.view.action['section']) {
                section_route.next_section(this.view.action['section']);
                this.view.render();
                this.view.action['section'] = false;
            } else if (this.view.action['url']) {
                document.location.href = this.view.action['url'];
                this.view.action['url'] = false;
            }
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
                element.on('sync',that.check_model_valid);
            });
        }
    });
}
