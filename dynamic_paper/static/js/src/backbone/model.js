/**
 * User: jackdevil
 */
function paper_model_factory (paper_type,paper){
    return Backbone.Model.extend({
        defaults: { "type": "text", "value": "", "children": false },
        urlRoot: url_resolver[paper_type],
        html: function(){

        },
        initialize: function(){
            this.bind('change',function(){
                this.save();
            });
        }
    });
}
