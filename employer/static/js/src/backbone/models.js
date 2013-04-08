/**
 * User: jackdevil
 */


var BaseError = Backbone.Model.extend({});

var BaseModel = Backbone.Model.extend({
    error: new BaseError(),
    url: function() {
        return  this.id ?  this.urlRoot + this.id + '/' :  this.urlRoot;
    },
    commit: function() {
        this.save([],{
            error: function(model, response) {
                model.error.clear();
                model.error.set(JSON.parse(response.responseText)[model.type]);
                model.trigger('error');
            }
        });
    }
});

var PostJobModel = BaseModel.extend({});

var EssentialModel = BaseModel.extend({});