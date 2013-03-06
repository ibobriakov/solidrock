/**
 * User: jackdevil
 */
function paper_model_factory (paper_type,paper){
    return Backbone.Model.extend({
        defaults: { "type": "text", "value": "", "children": false },
        url: url_resolver[paper_type]+paper+'/',
        html: function(){

        },
        initialize: function(){
            this.bind('change',function(){
                this.save();
            });
        }
    });
}
