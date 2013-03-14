/**
 * Create user: jackdevil
 */

function form_model_fabric(type) {
    return Backbone.Model.extend({
        urlRoot: url_resolver[type],
        initialize: function() {
            this.set('name',type+'#'+this.get('name'));
            this.bind('change',function(){
                console.log(this);
            })
        }
    });
}