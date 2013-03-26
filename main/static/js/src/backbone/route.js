/**
 * User: jackdevil
 */
var GlobalRoute = Backbone.Router.extend({
    routes: {
        "login": "login",
        "register/job_seeker": "register_job_seeker",
        "register/employer": "register_employer",
        "terms_conditions": "terms_conditions",
        "privacy_policy":"privacy_policy"
    },
    terms_conditions: function(){
        this.show_terms_modal();
        $('#privacy_policy_tab').removeClass('active');
        $('#privacy_policy_content').css('display','none');
        $('#terms_conditions_tab').addClass('active');
        $('#terms_conditions_content').css('display','block');
    },
    privacy_policy: function(){
        this.show_terms_modal();
        $('#terms_conditions_tab').removeClass('active');
        $('#terms_conditions_content').css('display','none');
        $('#privacy_policy_tab').addClass('active');
        $('#privacy_policy_content').css('display','block');
    },
    show_terms_modal: function(){
        var id = $('.window.terms .window_block');
        var maskHeight = $(document).height();
        var maskWidth = $(window).width();
        $('.window.terms ._hide').css({'width':maskWidth,'height':maskHeight});
        $('.window.terms ._hide').fadeIn(500);
        $('.window.terms ._hide').fadeTo(500);
        var winH = $(window).height();
        var winW = $(window).width();
        var hhh = $(document).height();
        $(id).css('top',  hhh-$(id).height()/0.75);
        $(id).css('left', winW/2-$(id).width()/2);
        $(id).fadeIn(500);
    },
    show_auth_modal: function(){
        var id = $('.window.login .window_block');
        $('#register_employer_tab_fieldset').css('display','none');
        $('#register_job_seeker_tab_fieldset').css('display','block');
        var maskHeight = $(document).height();
        var maskWidth = $(window).width();
        $('.window.login ._hide').css({'width':maskWidth,'height':maskHeight});
        $('.window.login ._hide').fadeIn(500);
        $('.window.login ._hide').fadeTo(500);
        var winH = $(window).height();
        var winW = $(window).width();
        $(id).css('top',  winH/2-$(id).height()/2);
        $(id).css('left', winW/2-$(id).width()/2);
        $(id).fadeIn(500);
    },
    login: function() {
        this.show_auth_modal();
        $('#register_employer_tab').removeClass('active');
        $('#register_employer_tab_fieldset').css('display','none');
        $('#register_job_seeker_tab').addClass('active');
        $('#register_job_seeker_tab_fieldset').css('display','block');
    },

    register_job_seeker: function() {
        this.show_auth_modal();
        $('#register_employer_tab').removeClass('active');
        $('#register_employer_tab_fieldset').css('display','none');
        $('#register_job_seeker_tab').addClass('active');
        $('#register_job_seeker_tab_fieldset').css('display','block');
    },

    register_employer: function(){
        this.show_auth_modal();
        $('#register_job_seeker_tab').removeClass('active');
        $('#register_job_seeker_tab_fieldset').css('display','none');
        $('#register_employer_tab').addClass('active');
        $('#register_employer_tab_fieldset').css('display','block');
    }
});

var route = new GlobalRoute();

Backbone.history.start();