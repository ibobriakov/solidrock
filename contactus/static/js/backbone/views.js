/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 06.04.13
 * Time: 9:47
 * To change this template use File | Settings | File Templates.
 */

var ContactView = Backbone.View.extend ({
    model: ContactModel,
    errors: [],
    initialize: function(){
        this.model.view = this;
    },
    render: function() {
        var object = {};
        this.rivets = rivets;
        this.rivets.bind(this.el, {'contactus':this.model});
        $('.error_list').fadeIn();
        return this;
    }
});