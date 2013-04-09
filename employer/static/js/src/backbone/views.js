/**
 * User: jackdevil
 */

var BaseView = Backbone.View.extend({
    api_url: function(){ return rest_url }, // Api url
    resource: false, // Rest api resource
    list_endpoint_key: 'list_endpoint', // List_endpoint key in resource JSON
    schema_key: 'schema', // Schema key in resource JSON
    data_prototype: false,

    bind_item: function() { return this.collection ? this.collection : this.model },

    append_variables_to_prototype: function(prototype) {
        prototype = prototype || _.result(this, 'bind_item');
        prototype.view = this;
        prototype.defaults = _.result(this, 'schema');
        prototype.resource = this.resource;
        prototype.urlRoot = this.get_resource_url(this.list_endpoint_key);
    },

    custom_data_initialize: function(){},

    // Get resource url by resource name and key name
    get_resource_url: function(key) {
        return _.result(this, 'api_url')[this.resource][key];
    },

    // Get schema as JSON
    schema: function() {
        var schema_resource_url = this.get_resource_url(this.schema_key);
        var schema_json = get_async_json(schema_resource_url);
        var defaults = {};
        if (schema_json){
            _.each(schema_json.fields, function(value, key){
                defaults[key] = value.default;
            });
        }
        return defaults;
    },
    // Binding rivets to collection data
    binding: function(bindName) {
        if (bindName) {
            var options = {};
            options[bindName] = _.result(this, 'bind_item');
            this.rivets = rivets;
            this.rivets.bind(this.el, options);
        }
    },
    initialize: function(attributes) {
        this.resource = attributes.resource || false; // Get resource name
        this.bindName = attributes.bindName || false; // Get rivets binding name
        this.append_variables_to_prototype();
        this.custom_data_initialize();
        this.binding(this.bindName || this.resource);
    }
});

var BaseCollectionView = BaseView.extend({
    custom_data_initialize: function(){
        this.collection.url = this.get_resource_url(this.list_endpoint_key);
    }
});

var BaseItemView = BaseView.extend({
    custom_data_initialize: function(){
        this.model = new this.model();
    }
});


var PostJobView = BaseItemView.extend({
    model: PostJobModel
});

var EssentialView = BaseCollectionView.extend({
    collection: new EssentialCollection
});

var DesireableView = BaseCollectionView.extend({
    collection: new DesireableCollection
});