/**
 * User: jackdevil
 */

var ContactUsApp = angular.module('ContactUsApp', ['ui.select2']);

ContactUsApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

ContactUsApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});