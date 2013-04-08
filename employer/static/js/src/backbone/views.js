/**
 * User: jackdevil
 */

var BaseView = Backbone.View.extend({
    api_url: function(){ return rest_url }, // Api url
    resource: false, // Rest api resource
    list_endpoint_key: 'list_endpoint', // List_endpoint key in resource JSON
    schema_key: 'schema', // Schema key in resource JSON

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
            options[bindName] = this;
            this.rivets = rivets;
            this.rivets.bind(this.el, options);
        }
    }
});

var BaseCollectionView = BaseView.extend({
    // Model initialize
    initialize: function(attributes) {
        this.resource = attributes.resource || false; // Get resource name
        this.bindName = attributes.bindName || false; // Get rivets binding name

        this.collection.model.prototype.defaults = _.result(this, 'schema');
        this.collection.model.prototype.urlRoot = this.get_resource_url(this.list_endpoint_key); // Set model urlRoot

        this.binding(this.bindName || this.resource);
    }
});

var BaseItemView = BaseView.extend({
    // Model initialize
    initialize: function(attributes) {
        this.resource = attributes.resource || false; // Get resource name
        this.bindName = attributes.bindName || false; // Get rivets binding name

        this.model.prototype.defaults = _.result(this, 'schema');
        this.model.prototype.urlRoot = this.get_resource_url(this.list_endpoint_key); // Set model urlRoot
        this.model = new this.model();

        this.binding(this.bindName || this.resource);
    }
});


var PostJobView = BaseItemView.extend({
    model: PostJobModel
});

var EssentialView = BaseCollectionView.extend({
    collection: new EssentialCollection
});