/**
 * User: jackdevil
 */

var EmployerEditProfileApp = angular.module('EmployerEditProfileApp', []);

EmployerEditProfileApp.config( function ( $routeProvider) {
    $routeProvider
        .when('/section/:section/', { controller: 'EmployerEditProfileCtrl', templateUrl: 'employer-profile-edit' }  )
        .otherwise({ redirectTo: '/section/1/' })
});

EmployerEditProfileApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

EmployerEditProfileApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});