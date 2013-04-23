/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 22.04.13
 * Time: 14:35
 * To change this template use File | Settings | File Templates.
 */

var PostJobApp = angular.module('PostJobApp', ['ui']);

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