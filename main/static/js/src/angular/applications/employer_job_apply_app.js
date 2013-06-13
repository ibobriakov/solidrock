/**
 * User: jackdevil
**/


var ApplyJobApp = angular.module('ApplyJobApp', []);


ApplyJobApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);


ApplyJobApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});