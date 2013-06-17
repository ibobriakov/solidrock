/**
 * User: jackdevil
 */

MainApp.config(function ($stateProvider, $routeProvider, $urlRouterProvider) {
    $urlRouterProvider
        .otherwise('/section/1/');
    $stateProvider
        .state('section', {
            url: "/section/:section/",
            onEnter: function ($stateParams) {
                var section = $stateParams.section;
                $('.sections').children().removeClass('active');
                $('.pages.sections').children().hide();
                $('.pages.sections .section'+section).show();
                $('.section'+section).addClass('active');
                $('body,html').animate({scrollTop:0},200);
            }
        });
});