/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 14.03.13
 * Time: 14:54
 * To change this template use File | Settings | File Templates.
 */


function form_collection_fabric(type){
    return Backbone.Collection.extend({
        model: form_model_fabric(type)
    });
}