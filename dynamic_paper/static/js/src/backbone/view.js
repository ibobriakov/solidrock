/**
 * User: jackdevil
 */

PaperView = Backbone.View.extend({
    collection: new PaperCollection(),
    template: _.template($('#papers_template').html()),
    paper_body: '#paper',
    paper_item: '.paper',
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
        $(this.paper_body).html(this.template({'papers':this.papers_to_json(this.collection)}));
        $(this.paper_item).on('click',function(){$(this).attr('contenteditable','true')});
        $(this.paper_item).blur(function(){that.collection.get_model($(this).attr('id')).set('value',$(this).html());});
        return this;
    }
});

var paper_view = new PaperView();