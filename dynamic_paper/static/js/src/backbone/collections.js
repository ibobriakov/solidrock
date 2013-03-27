/**
 * User: jackdevil
 */

function paper_collection_factory(paper_type,paper,button) {
    var collection_factory = this;
    return Backbone.Collection.extend({
    model: paper_model_factory(paper_type,paper,button),
    url_suffix: 'paper',
    template: _.template($("#paper_collection").html()),
    html: function(level){
        level = level | 0;
        return this.template({'collection':this, 'level':level});
    },
    initialize: function(){
        this.model.collection = this;
        this.model.collection_factory = collection_factory;
    },
    get_model: function(id, collection){
        var that = this;
        collection = collection || that;
        if (collection.get(id)) return collection.get(id);
        for (var i=0; i < collection.length; i++) {
            if (collection.at(i).get('children'))
                var model = that.get_model(id, collection.at(i).get('children'));
                if (model) return model;
        }
        return false;
    }
})
}