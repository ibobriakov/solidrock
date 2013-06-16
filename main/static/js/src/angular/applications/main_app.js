/**
 * User: jackdevil
 */

var MainApp = angular.module('MainApp', ['ui.state']);

var show_auth_modal = function () {
    var id = $('.window.login .window_block');
    $('#register_employer_tab_fieldset').css('display', 'none');
    $('#register_job_seeker_tab_fieldset').css('display', 'block');
    var maskHeight = $(document).height();
    var maskWidth = $(window).width();
    $('.window.login ._hide').css({'width': maskWidth, 'height': maskHeight});
    $('.window.login ._hide').fadeIn(500);
    $('.window.login ._hide').fadeTo(500);
    var winH = $(window).height();
    var winW = $(window).width();
    $(id).css('top', winH / 2 - $(id).height() / 2);
    $(id).css('left', winW / 2 - $(id).width() / 2);
    $(id).fadeIn(500);
};

var show_terms_modal = function () {
    var id = $('.window.terms .window_block');
    var maskHeight = $(document).height();
    var maskWidth = $(window).width();
    $('.window.terms ._hide').css({'width': maskWidth, 'height': maskHeight});
    $('.window.terms ._hide').fadeIn(500);
    $('.window.terms ._hide').fadeTo(500);
    var winH = $(window).height();
    var winW = $(window).width();
    var hhh = $(document).height();
    $(id).css('top', hhh - $(id).height() / 0.75);
    $(id).css('left', winW / 2 - $(id).width() / 2);
    $(id).fadeIn(500);
};

MainApp.config(function ($stateProvider, $routeProvider) {
    $stateProvider
        .state('login', {
            url: "/login",
            onEnter: function ($stateParams, $state) {
                show_auth_modal();
                $('#register_employer_tab').removeClass('active');
                $('#register_employer_tab_fieldset').css('display', 'none');
                $('#register_job_seeker_tab').addClass('active');
                $('#register_job_seeker_tab_fieldset').css('display', 'block');
            }
        })
        .state('close', {
            url: "/close",
            onEnter: function ($stateParams, $state) {
                $('._hide, .window_block').fadeOut();
                $('.window.terms .window_block').fadeOut();
            }
        })
        .state('register_job_seeker', {
            url: "/register/job_seeker",
            onEnter: function ($stateParams, $state) {
                show_auth_modal();
                $('#register_employer_tab').removeClass('active');
                $('#register_employer_tab_fieldset').css('display', 'none');
                $('#register_job_seeker_tab').addClass('active');
                $('#register_job_seeker_tab_fieldset').css('display', 'block');
            }
        })
        .state('register_employer', {
            url: "/register/employer",
            onEnter: function ($stateParams, $state) {
                show_auth_modal();
                $('#register_job_seeker_tab').removeClass('active');
                $('#register_job_seeker_tab_fieldset').css('display', 'none');
                $('#register_employer_tab').addClass('active');
                $('#register_employer_tab_fieldset').css('display', 'block');
            }
        })
        .state('terms_conditions', {
            url: "/terms_conditions",
            onEnter: function ($stateParams, $state) {
                show_terms_modal();
                $('#privacy_policy_tab').removeClass('active');
                $('#privacy_policy_content').css('display', 'none');
                $('#terms_conditions_tab').addClass('active');
                $('#terms_conditions_content').css('display', 'block');
            }
        })
        .state('privacy_policy', {
            url: "/privacy_policy",
            onEnter: function ($stateParams, $state) {
                show_terms_modal();
                $('#terms_conditions_tab').removeClass('active');
                $('#terms_conditions_content').css('display', 'none');
                $('#privacy_policy_tab').addClass('active');
                $('#privacy_policy_content').css('display', 'block');
            }
        })
});

MainApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

MainApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

MainApp.run(function($rootScope){
    $rootScope.adv = {};
    $rootScope.adv.section = 1;
});