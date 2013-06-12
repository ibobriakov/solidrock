/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 10.06.13
 * Time: 10:14
 * To change this template use File | Settings | File Templates.
 */

var AplInfoApp = angular.module('AplInfoApp', ['ui']);

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