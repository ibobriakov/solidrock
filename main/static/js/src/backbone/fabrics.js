/**
 * Create user: jackdevil
 */

function form_model_fabric(type) {
    var data = get_async_json(rest_url[type].schema);
    var defaults = {}, labels = {}, types = {};
//    TODO return fields list.

    var fields = [];
    _.each(data.fields,function(value,key){
        if (key!='resource_uri'){
            fields[value.order_index] = key;
        }
    });

    _.each(fields,function(key){
        defaults[key] = data.fields[key].default;
        labels[key] = data.fields[key].label;
        types[key] = data.fields[key].type;
    });
    var Model = Backbone.Model.extend({
        urlRoot: rest_url[type].list_endpoint,
        defaults: defaults,
        labels: labels,
        types: types,
        initialize: function(){
        },
        commit: function(event){
            var that = this;
            var parent = event.toElement.parentElement;
            var next = $(parent).attr('data-next-url');
            this.save({},{ wait: true,
                error: function(model,response) {
                    that.view.errors = JSON.parse(response.responseText)[type];
                    that.view.render();
                },
                success: function(){
                    that.view.errors = [];
                    that.view.render();
                    if (next) {
                        window.location.replace(next);
                    } else {
                        window.location.replace('/');
                    }
                }
            });
        },
        get_errors: function(){
            return this.error;
        }
    });
    return new Model();
}

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
