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
    get_model: function(id, collection){
        var that = this;
        collection = collection || that;
        if (collection.get(id)) return collection.get(id);
        for (var i=0; i < collection.length; i++){
            if (collection.at(i).get('children')) return that.get_model(id, collection.at(i).get('children'));
        }
    }
})
}