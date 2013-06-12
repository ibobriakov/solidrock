/**
 * User: jackdevil
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

directives.section = function ($location) {
    return {
        transclude: true,
        scope: {
            num: '@'
        },
        template: '<a href="#/section/{[{num}]}/" ng-transclude></a>',
        link: function ($scope, element, attr) {
            element.bind('click', function (event) {
                $location.path('/section/' + parseInt($scope.num) + '/');
            });
        }
    }
};

AplInfoPublicApp.directive(directives);