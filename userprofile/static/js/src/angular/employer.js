/**
 * User: jackdevil
 */

var app = angular.module('PostJobApp', []);

function get_cookie (name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

app.config( function ($routeProvider) {
    $routeProvider
        .when('/section/:section/', { controller: 'JobInfoCtrl', templateUrl: 'post-job.html' }  )
        .otherwise({ redirectTo: '/section/1/' })
});

app.config(["$httpProvider", function (provider) {
    provider.defaults.headers.common['X-CSRFToken'] = get_cookie('csrftoken');
}]);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

var directives = {};

directives.activated = function() {
    return {
        restrict: "A",
        link: function($scope, element, attr) {
            element.children().each(function(index,item) {
                if (attr.activated == "block") {
                   if (parseInt($scope.section) == parseInt(index+1)) {
                        $(item).show();
                    } else {
                       $(item).hide();
                   }
                } else {
                    if (parseInt($scope.section) == parseInt(index+1)) {
                        $(item).addClass('active');
                    }
                }
            })
        }
    }
}


app.directive(directives);

app.controller('JobInfoCtrl', function ($scope, $http, $route, $routeParams) {
    $scope.job = [];
    $scope.error = [];
    $scope.section = $routeParams.section

    $scope.checkActive = function(section) {
        return true ? parseInt(section) === parseInt($scope.section) : false;
    };

    var success_callback = function (data, status, headers, config) {
    };

    var error_callback = function (data, status, headers, config) {
        $scope.error = data.job;
    };

    $scope.save = function () {
        $http.put($scope.job.resource_uri, $scope.job)
            .success(success_callback)
            .error(error_callback);
    };

    $scope.append = function (container) {
        container.push({"job": $scope.job.resource_uri});
    };

    $scope.remove = function (container, index) {
        if (container[index].resource_uri) $http.delete(container[index].resource_uri);
        container.splice(index, 1);
    };
});
