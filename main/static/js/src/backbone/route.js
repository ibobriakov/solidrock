/**
 * User: jackdevil
 */
var GlobalRoute = Backbone.Router.extend({
    routes: {
        "login": "login",
        "register/job_seeker": "register_job_seeker",
        "register/employer": "register_employer"
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
    close_auth_modal: function(){
        $('._hide, .window_block').hide();
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