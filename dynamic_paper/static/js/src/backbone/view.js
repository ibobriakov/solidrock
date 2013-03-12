/**
 * User: jackdevil
 */

function paper_view_factory(paper_type,paper){
    return Backbone.View.extend({
        collection: new (paper_collection_factory(paper_type,paper))(),
        paper_body: '#paper',
        paper_item: '.paper',
        paper_add: '.add-btn',
        paper_remove: '.remove-btn',
        url: url_resolver[paper_type],
        initialize: function() {
            _.bindAll(this, 'render');
            this.collection.view = this;
            this.collection.model.view = this;
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
        bind_event: function(){
            var that = this;
            $(this.paper_item).blur(function(){
                that.collection.get_model($(this).attr('data-id')).set('value',$(this).html());
            });
            $(this.paper_add).on('click',function(){
                var model = that.collection.get_model($(this).attr('data-id'));
                var value = model.get('type').split('_')[0];
                if (!model.get('children')) model.set('children',new (paper_collection_factory(paper_type,paper))());
                model.get('children').create(
                    {'paper':model.get('paper'),'type':'container','parent':model.get('id'),'value':value},
                    {'wait':true}
                );
            });
            $(this.paper_remove).on('click',function(){
                var model = that.collection.get_model($(this).attr('data-id'));
                model.destroy({'wait':true});
                model.collection.remove(model);
                that.render();
            });
            update_view.on('update_view',function(msg){
                that.render();
            })
        },
        render: function(){
            $(this.paper_body).html(this.collection.html());
            this.bind_event();
            return this;
        }
    })
}
