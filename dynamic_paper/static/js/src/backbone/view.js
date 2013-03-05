/**
 * User: jackdevil
 */
var PaperView;

$(document).ready(function () {
    PaperView = Backbone.View.extend({
        collection: new PaperCollection(),
        template: _.template($('#papers_template').html()),
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
            $('#paper').html(this.template({'papers':this.papers_to_json(this.collection)}));
            var paper = $('.paper');
            paper.on('click',function(){$(this).attr('contenteditable','true')});
            paper.blur(function(){
                var model = that.collection.get_model($(this).attr('id'));
                model.set('value',$(this).html());
            });
            return this;
        }
    });
});