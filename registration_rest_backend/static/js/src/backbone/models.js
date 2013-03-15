/**
 * Create user: jackdevil
 */

function form_model_fabric(type) {
    var data = get_async_json(rest_url[type].schema);
    var defaults = {}, labels = {}, types = {};
    _.each(data.fields,function(value,key){
        if (key!='resource_uri'){
            defaults[key] = value.default;
            labels[key] = value.label;
            types[key] = value.type;
        }
    });
    var Model = Backbone.Model.extend({
        urlRoot: rest_url[type].list_endpoint,
        defaults: defaults,
        labels: labels,
        types: types,
        commit: function(){
            this.save();
        },
        get_errors: function(){
            return this.error;
        }
    });
    return new Model();
}