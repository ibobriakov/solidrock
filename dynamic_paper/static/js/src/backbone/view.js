/**
 * User: jackdevil
 */

function paper_view_factory(paper_type,paper){
    return Backbone.View.extend({
        collection: new (paper_collection_factory(paper_type,paper))(),
        paper_body: '#paper',
        paper_item: '.paper',
        paper_add: '.add-btn',
        url: false,
        initialize: function() {
            _.bindAll(this, 'render');
        },
        papers_to_json: function(collection) {
            var that = this, json=[];
            collection.each(function(model) {
                var children = model.get('children');
                json.push(model.toJSON());
                if (children) {
                    json = json.concat(that.papers_to_json(children));
                }
            });
            return json;
        },
        render: function(){
            var that = this;
            $(this.paper_body).html(this.collection.html());
            $(this.paper_item).blur(function(){
                that.collection.get_model($(this).attr('data-id')).set('value',$(this).html());
            });
            $(this.paper_add).on('click',function(){
                var model = that.collection.get_model($(this).attr('data-id'));
                model.get('children').create({'paper':model.get('paper')});
            });
            return this;
        }
    })
}
