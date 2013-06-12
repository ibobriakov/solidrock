/**
 * User: jackdevil
 */

var EditProfileApp = angular.module('EditProfileApp', []);

EditProfileApp.config( function ( $routeProvider) {
    $routeProvider
        .when('/section/:section/', { controller: 'JobInfoCtrl', templateUrl: 'post-job.html' }  )
        .otherwise({ redirectTo: '/section/1/' })
});

EditProfileApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

EditProfileApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});