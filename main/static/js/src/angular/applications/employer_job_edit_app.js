/**
 * User: jackdevil
 */

var PostJobApp = angular.module('PostJobApp', ['ui.select2']);

PostJobApp.config( function ( $routeProvider) {
    $routeProvider
        .when('/section/:section/', { controller: 'JobInfoCtrl', templateUrl: 'post-job.html' }  )
        .otherwise({ redirectTo: '/section/1/' })
});

PostJobApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

PostJobApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});