/**
 * User: jackdevil
 */

var PaperModel = Backbone.Model.extend({
    defaults: { "type": "text", "value": "", "children": false },
    initialize: function(){
        this.bind('change',function(){
            console.log(this.changed);
        });
    }
});