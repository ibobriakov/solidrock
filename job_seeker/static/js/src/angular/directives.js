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
            current: '='
        },
        template: '<a href="#/section/{[{num}]}/" ng-transclude></a>',
        link: function ($scope, element, attr) {
            element.bind('click', function (event) {
                $scope.list = $scope.current();
                var no_valid = $scope.list.length;
                _.each($scope.list, function (item) {
                    $('.preloader').show();
                    var error_callback = function (data, status, headers, config) {
                        $('.preloader').hide();
                        _.each(data, function (value, key) {
                            item.error = value;
                        });
                    };
                    var success_callback = function (data, status, headers, config) {
                        no_valid--;
                        item.error = {};
                        if (!no_valid) {
                            $('.preloader').hide();
                            $location.path('/section/' + parseInt($scope.num) + '/');
                        }
                    };
                    $http.put(item.resource_uri, item).error(error_callback).success(success_callback);
                });
                return false;
            });
        }
    }
};

AplInfoApp.directive(directives);