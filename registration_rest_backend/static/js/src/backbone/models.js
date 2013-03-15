/**
 * Create user: jackdevil
 */

function form_model_fabric(type,attributes) {
    var Model = Backbone.Model.extend({
        urlRoot: rest_url[type].list_endpoint,
        types: attributes.types,
        titles: attributes.titles,
        initialize: function() {
        },
        commit: function(){
            this.save();
        },
        validate: function(){
            return false;
        }
    });
    return new Model(attributes.fields);
}