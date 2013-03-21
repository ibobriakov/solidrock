/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 20.03.13
 * Time: 20:49
 * To change this template use File | Settings | File Templates.
 */

function profile_model_fabric(type) {
    return Backbone.Model.extend({
        commit: function() {
            this.save({},{ wait: true });
        }
    });
}