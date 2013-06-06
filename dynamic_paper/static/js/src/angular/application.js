/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 05.06.13
 * Time: 14:36
 * To change this template use File | Settings | File Templates.
 */

var DynamicPaperApp = angular.module('DynamicPaperApp', ['ui',]);

DynamicPaperApp.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

DynamicPaperApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});