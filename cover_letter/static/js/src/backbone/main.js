/**
 * User: jackdevil
 */
var paper_view;

$(document).ready(function () {
    paper_view = new PaperView();
    paper_view.collection.reset([
        {'id':1,'type':'text','value':'First Name'},
        {'id':2,'type':'text','value':'Second Name'},
        {'id':3,'type':'text','value':'Work',
            'children': new PaperCollection().reset([
                {'id':4,'type':'text','value':'Work name'},
                {'id':5,'type':'text','value':'Work about'},
                {'id':6,'type':'text','value':'Work phone', 'children':new PaperCollection().reset([
                    {'id':7,'type':'phone','value':'+0 000 000 00 00'},
                    {'id':8,'type':'phone','value':'+0 000 000 00 00'}
                ])}
            ])},
        {'id':9,'type':'text','value':'About'},
    ]);
});