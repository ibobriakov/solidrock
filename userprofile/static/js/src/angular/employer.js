/**
 * User: jackdevil
 */

var app = angular.module('PostJobApp', []);

app.config(["$httpProvider", function(provider) {
    provider.defaults.headers.common['X-CSRFToken'] = getCookie('csrftoken');
}]);

var directives = {}

directives.section = function() {
    return {
        restrict: "E",
        replace: true,
        transclude: true,
        template: '<li><a href="" ng-transclude></a></li>'
    }
}

directives.field = function() {
        return {
        restrict: "E",
        replace: true,
        transclude: true,
        scope: {
            title: "@"
        },
        template: '<div class="field"><label>{{title}}</label><div ng-transclude></div></div>',
        link: function(scope, element){
            scope.addClass('it3');
        }

    }
}

//app.directive('field', function() {
//    return {
//        restrict: "E",
////        replace: true,
//        transclude: true,
//        scope: {
//            title: "@"
//        }
//        template: '' +
//            '<div class="field">' +
//                '<label>{{title}}</label>' +
//                '<div ng-transclude></div>' +
//            '</div>'
//    }
//});


app.controller('JobInfoCtrl',function($scope, $http){
    $scope.job = [];

    $scope.save = function () {
        $http.put($scope.job.resource_uri, $scope.job);
    };

    $scope.append = function (container) {
        container.push({"job": $scope.job.resource_uri});
    };

    $scope.remove = function (container, index) {
        if (container[index].resource_uri) $http.delete(container[index].resource_uri);
        container.splice(index,1);
    };
});

app.directive(directives);