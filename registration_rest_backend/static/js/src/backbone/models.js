/**
 * Create user: jackdevil
 */

function form_model_fabric(type,attributes) {
    var Model = Backbone.Model.extend({
        urlRoot: url_resolver[type],
        types: attributes.types,
        titles: attributes.titles,
        initialize: function() {
            this.bind('change',function(){
                console.log(this);
            })
        }
    });
    return new Model(attributes.fields);
}