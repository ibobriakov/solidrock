/**
 * User: jackdevil
 */

var BaseCollection = Backbone.Collection.extend({
    append: function(event){
        event.preventDefault();
        this.add();
    },
    updateAll: function() {
        var collection = this;
        var options = {
            success: function(model, resp, xhr) {
                collection.reset(model);
            }
        };
        return Backbone.sync('update', this, options);
    }
});

var EssentialCollection = BaseCollection.extend({
    model: EssentialModel
});

var DesireableCollection = BaseCollection.extend({
    model: DesireableModel
});