/**
 * User: jackdevil
 */

var PaperCollection = Backbone.Collection.extend({
    model: PaperModel,
    get_model: function(id, collection) {
        var that = this,model;
        collection = collection || that;
        model = collection.get(id);
        if (model) {
            return model;
        } else {
            collection.each(function(item) {
                if (item.get('children')) {
                    model = that.get_model(id,item.get('children'));
                    if (model) {
                        return model;
                    }
                }
            });
            return model;
        }
    }
});