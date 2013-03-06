/**
 * User: jackdevil
 */

function paper_collection_factory(paper_type,paper) {
    return Backbone.Collection.extend({
    model: paper_model_factory(paper_type,paper),
    url_suffix: 'paper',
    initialize: function(){
        this.model.collection = this;
    },
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
})
}