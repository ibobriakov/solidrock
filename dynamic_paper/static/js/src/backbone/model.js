/**
 * User: jackdevil
 */

var PaperModel = Backbone.Model.extend({
    defaults: { "type": "text", "value": "", "children": false },
    url: '/',
    initialize: function(){
        this.bind('change',function(){
            this.save();
        });
    }
});