
var BaseError = Backbone.Model.extend({});

var BaseModel = Backbone.Model.extend({});

var BaseRESTModel = Backbone.Model.extend({
    errors: new BaseError(),
    type: false,
    urlRoot: function(){
        if (this.type) {
            return rest_url[this.type]['list_endpoint'];
        } else {
            console.log('Type not set', this);
            return false;
        }
    },
    url: function() {
        if (this.id) { return this.urlRoot + this.id + '/';}
        else { return this.urlRoot; }
    },
    commit: function() {
        if (this.type) {
            this.save([],{
                error: function(model, response) {
                    model.errors.clear();
                    model.errors.set(JSON.parse(response.responseText)[model.type]);
                    model.trigger('error');
                }
            })
        } else {
            console.log('Type not set', this);
        }
    }
});

var BaseCollection = Backbone.Collection.extend({
    append_first_item: true,
    initialize: function() {
        if (this.append_first_item && !this.models) this.add({});
    }
});


var BaseCollectionView = Marionette.CollectionView.extend({

});