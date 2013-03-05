/**
 * User: jackdevil
 */
var PaperView;

$(document).ready(function () {
    PaperView = Backbone.View.extend({
        collection: new PaperCollection(),
        id: 'paper',
        template: _.template($('#papers_template').html()),
        papers_to_json: function(collection) {
            var that = this, json=[];
            collection.each(function(model) {
                var children = model.get('children');
                model.unset('children');
                json.push(model.toJSON());
                if (children) {
                    json = json.concat(that.papers_to_json(children));
                }
            });
            return json;
        },
        render: function(){
            var json = this.papers_to_json(this.collection);
            $('#paper').html(this.template({'papers':json}));
            return this;
        }
    });
});