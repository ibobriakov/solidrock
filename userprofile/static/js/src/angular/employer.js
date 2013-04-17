/**
 * User: jackdevil
 */


var app = angular.module('PostJobApp', []);

app.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = getCookie('csrftoken');
}]);

function $appendClassCtrl($scope, $element, $transclude, $compile){
    $transclude(function(clone) {
        $element.replaceWith(clone.addClass($element.attr('input_class')));
    })
};

var directives = {};

directives.section = function () {
    return {
        restrict: "E",
        replace: true,
        transclude: true,
        template: '<li> <a href="" ng-transclude></a> </li>'
    }
}

//directives.styled = function () {
//    return {
//        restrict: 'E',
//        transclude: true,
//        controller: $appendClassCtrl
//    }
//}

directives.field = function () {
    return {
        restrict: 'E',
        scope: {
            title: '@title'
        },
        replace: true,
        transclude: true,
        template: '' +
            '<div class="field">' +
                '<label>{{title}}</label>' +
                '<div ng-transclude></div>' +
                '<div class="help-tip">' +
                    '<div class="help-tip-title">Helpful Tip</div>' +
                    '<div class="help-tip-text">' +
                        '<div class="help-tip-right"></div>TEXT' +
                    '</div>' +
            '</div>',
    };
}

app.controller('JobInfoCtrl', function ($scope, $http) {
    $scope.job = [];

    $scope.save = function () {
        $http.put($scope.job.resource_uri, $scope.job);
    };

    $scope.append = function (container) {
        container.push({"job": $scope.job.resource_uri});
    };

    $scope.remove = function (container, index) {
        if (container[index].resource_uri) $http.delete(container[index].resource_uri);
        container.splice(index, 1);
    };
});

app.directive(directives);