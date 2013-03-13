/**
 * Create user: jackdevil
 */

var LoginView = Backbone.View.extend ({
    model: new LoginModel(),
    template: _.template($("#login-template").html()),
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this.rivets = rivets.bind( this.el, { login: this.model } );
        return this;
    }
});

var RegistrationEmployerView = Backbone.View.extend ({
    model: new RegistrationEmployerModel(),
    template: _.template($("#registration-employer-template").html()),
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this.rivets = rivets.bind( this.el, { registration: this.model } );
        return this;
    }
});

var RegistrationJobSeekerView = Backbone.View.extend ({
    model: new RegistrationJobSeekerModel(),
    template: _.template($("#registration-job-seeker-template").html()),
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this.rivets = rivets.bind( this.el, { registration: this.model } );
        return this;
    }
});

login_view = new LoginView({el:$('#login-form')});
login_view.render();

registration_employer_view = new RegistrationEmployerView({el:$('#registration-employer-form')});

registration_job_seeker_view = new RegistrationJobSeekerView({el:$('#registration-job-seeker-form')});
