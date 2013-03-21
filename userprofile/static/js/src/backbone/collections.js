/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 21.03.13
 * Time: 16:27
 * To change this template use File | Settings | File Templates.
 */

function profile_collection_fabric(type) {
    return Backbone.Collection.extend({
        url: rest_url[type].list_endpoint,
        model: profile_model_fabric(type),
        parse: function(response){
            return response.objects;
        }
    });
}