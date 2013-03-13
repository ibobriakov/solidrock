/**
 * Create user: jackdevil
 */

var LoginModel = Backbone.Model.extend({
   url: '/login/',
   initialize: function(){
       this.on('change:email change:password',function(){
           this.save(this.changed);
       });
   }
});

var RegistrationJobSeekerModel = Backbone.Model.extend({
    default: {'type':'job_seeker'},
    url: '/registration/',
    initialize: function(){
        this.on('change:first_name change:last_name change:email change:password change:re_password',function(){
            this.save(this.changed);
        });
    }
});

var RegistrationEmployerModel = Backbone.Model.extend({
    default: {'type':'employer'},
    url: '/registration/',
    initialize: function(){
        this.on('change:company_name change:email change:phone_number change:password change:re_password',function(){
            this.save(this.changed);
        });
    }
});