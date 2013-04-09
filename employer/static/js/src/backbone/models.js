/**
 * User: jackdevil
 */


var BaseError = Backbone.Model.extend({});

var BaseModel = Backbone.Model.extend({
    error: new BaseError(),
    initialize: function(){
        this.bind('sync', this.save_success);
    },
    save_success: function(model, result, options){
        console.log('Success');
    },
    url: function() {
        return  this.id ?  this.urlRoot + this.id + '/' :  this.urlRoot;
    },
    remove: function(event){
        event.preventDefault();
        this.destroy();
    },
    commit: function() {
        this.save([],{ wait: true,
            error: function(model, response) {
                model.error.clear();
                model.error.set(JSON.parse(response.responseText)[model.resource]);
                model.trigger('error');
            }
        });
    }
});

var PostJobModel = BaseModel.extend({});

var EssentialModel = BaseModel.extend({});

var DesireableModel = BaseModel.extend({});