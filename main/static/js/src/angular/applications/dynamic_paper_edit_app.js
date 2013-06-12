/**
 * User: jackdevil
 */

var DynamicPaperApp = angular.module('DynamicPaperApp', ['ui',]);

DynamicPaperApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

DynamicPaperApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});