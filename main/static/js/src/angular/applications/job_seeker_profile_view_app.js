/**
 * User: jackdevil
 */

var AplInfoPublicApp = angular.module('AplInfoPublicApp', ['ui']);

AplInfoPublicApp.config( function ( $routeProvider) {
    $routeProvider
        .when('/section/:section/', { controller: 'AplInfoPublicCtrl', templateUrl: 'application-information-public' }  )
        .otherwise({ redirectTo: '/section/1/' })
});

AplInfoPublicApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});