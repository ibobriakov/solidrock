/**
 * User: jackdevil
 */


var BaseError = Backbone.Model.extend({

});

var BaseModel = Backbone.Model.extend({
    error: new BaseError(),
    type: false,
    endpoint_item: 'list_endpoint',
    schema_item: 'schema',
    constructor: function(attributes, options) {
        this.type = attributes.type || false;
        this.defaults = this.get_default_items();
        this.urlRoot = this.type_api_url()[this.endpoint_item];
        Backbone.Model.prototype.constructor.call(this, attributes, options);
    },
    get_default_items: function(){
        var schema_url =  this.type_api_url()[this.schema_item];
        var schema_json = get_async_json(schema_url);
        var defaults = {};
        if (schema_json){
            _.each(schema_json.fields, function(value, key){
                defaults[key] = value.default;
            });
        }
        return defaults;
    },
    type_api_url: function(){
        console.assert(this.type, 'Type not set');
        return rest_url[this.type];
    },
    url: function() {
        return  this.id ?  this.urlRoot + this.id + '/' :  this.urlRoot;
    },
    commit: function() {
        this.save([],{
            error: function(model, response) {
                model.error.clear();
                model.error.set(JSON.parse(response.responseText)[model.type]);
                model.trigger('error');
            }
        });
    }
});

var PostJobModel = BaseModel.extend({

});