/**
 * User: jackdevil
 */
var current_section = 1;
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
            }
        });
});