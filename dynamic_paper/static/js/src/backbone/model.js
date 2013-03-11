/**
 * User: jackdevil
 */
function paper_model_factory (paper_type,paper){
    return Backbone.Model.extend({
        defaults: { "type": "text", "value": "", "children": false },
        urlRoot: url_resolver[paper_type],
        template: _.template($("#paper_model").html()),
        html: function(level){
            level = level+1 | 0;
            return this.template({'model':this, 'level':level});
        },
        initialize: function(){
            this.bind('change',function(){
                this.save();
            });
        }
    });
}
