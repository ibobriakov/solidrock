/**
 * User: jackdevil
 */
var PaperView = Backbone.View.extend({
    collection: new PaperCollection(),
    id: 'paper',
    render: function(){
        $(this.el).html();
    }
});

var paper_view = new PaperView();