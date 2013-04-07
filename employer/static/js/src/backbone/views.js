/**
 * User: jackdevil
 */


var BaseItemView = Backbone.View.extend({
    type: false,
    bind_name: false,
    model_init: function(Model){
        return new Model({type:this.type});
    },
    initialize: function(attributes) {
        console.assert(attributes, 'Attributes not set');
        this.type = attributes.type || false;
        this.bind_name = attributes.bind_name || false;
        console.assert(this.model, 'Model not set');
        this.model = this.model_init(this.model);  // dirty and unclean logic
        this.model.view = this;
        this.data_binding();
    },
    data_binding: function() {
        var bind_name = this.bind_name || this.type;
        console.assert(this.model, 'Model not init');
        console.assert(this.el, 'Element not init');
        if (bind_name) {
            var options = {};
            options[bind_name] = this.model;
            this.rivets = rivets;
            this.rivets.bind(this.el, options);
        }
    }
});

var PostJobView = BaseItemView.extend({
    model: PostJobModel
});