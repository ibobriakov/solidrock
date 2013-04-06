/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 06.04.13
 * Time: 9:47
 * To change this template use File | Settings | File Templates.
 */

var ContactView = Backbone.View.extend ({
    model: new ContactModel(),
    errors: new ContactErrorModel(),
    initialize: function() {
        this.model.view = this;
        this.rivets = rivets;
        this.rivets.bind(this.el, {'contactus': this.model, 'contactus_errors': this.errors});
    }
});

var contact_view = new ContactView({el: $('#contact-form')});