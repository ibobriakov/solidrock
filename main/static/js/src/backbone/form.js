/**
 * Create user: jackdevil
 */

var User = Backbone.Model.extend({
    url: '/user/form/',
    schema: {
        title:      { type: 'Select', options: ['Mr', 'Mrs', 'Ms'] },
        name:       'Text',
        email:      { validators: ['required', 'email'] },
        birthday:   'Date',
        password:   'Password'
    }
});

var user = new User();

var form = new Backbone.Form({
    model: user
}).render();

//form.bind('change',user.save());