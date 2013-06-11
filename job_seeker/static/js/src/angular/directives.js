/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 10.06.13
 * Time: 10:14
 * To change this template use File | Settings | File Templates.
 */
var directives = {};

directives.activated = function () {
    return {
        restrict: "A",
        link: function ($scope, element, attr) {
            element.children().each(function (index, item) {
                if (attr.activated == "block") {
                    if (parseInt($scope.section) == parseInt(index + 1)) {
                        $(item).show();
                    } else {
                        $(item).hide();
                    }
                } else {
                    if (parseInt($scope.section) == parseInt(index + 1)) {
                        $(item).addClass('active');
                    }
                }
            })
        }
    }
};

directives.section = function ($location, $http) {
    return {
        transclude: true,
        scope: {
            num: '@',
            error: '='
        },
        template: '<a href="#/section/{[{num}]}/" ng-transclude></a>',
        controller: function($scope) {
//            $scope.job = share.job;
        },
        link: function ($scope, element, attr) {
//            var success_callback = function (data, status, headers, config) {
//                $('.preloader').hide();
//                $location.path('/section/' + parseInt($scope.num) + '/');
//            };
//            var error_callback = function (data, status, headers, config) {
//                $('.preloader').hide();
//                $scope.error = data.job;
//            };
            element.bind('click', function (event) {
                $location.path('/section/' + parseInt($scope.num) + '/');
//                $('.preloader').show();
//                $http.put($scope.job.resource_uri, $scope.job)
//                    .success(success_callback)
//                    .error(error_callback);
//                return false;
            });
        }
    }
};

directives.inputField = function() {
    return {
        restrict: 'E',
        scope: {
            data: '=',
            'name': '@name',
            'label': '@'
        },
        compile: function(scope, element, attr){

        }

    }
};

directives.save = function($http) {
    return {
        restrict: 'E'
    }
};

AplInfoApp.directive(directives);