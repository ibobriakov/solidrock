/**
 * User: jackdevil
 */

var AplInfoApp = angular.module('AplInfoApp', []);

AplInfoApp.config( function ( $routeProvider) {
    $routeProvider
        .when('/section/:section/', { controller: 'AplInfoCtrl', templateUrl: 'application-information' }  )
        .otherwise({ redirectTo: '/section/1/' })
});

AplInfoApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

AplInfoApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});