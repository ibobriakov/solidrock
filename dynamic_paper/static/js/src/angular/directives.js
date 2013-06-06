/**
 * User: jackdevil
 */

var dpd = {}; // Dynamic Paper directives Dict

dpd.contenteditable = function () {
    return {
        require: 'ngModel',
        link: function (scope, element, attrs, ctrl) {
            element.bind('blur', function () {
                scope.$apply(function () {
                    ctrl.$setViewValue(element.html());
                });
            });
            ctrl.$render = function () {
                element.html(ctrl.$viewValue);
            };
            ctrl.$render();
        }
    }
};

dpd.append = function () {
    return {
        restrict: 'E',
        scope: {
            container: '='
        },
        template: '<a href="#">Add</a>',
        link: function (scope, element, attr) {

        }
    }
};

dpd.repeat = function ($parse) {
    return {
        link: function (scope, element, attr) {
            var data = $parse(attr.repeat)(scope);
            if (data) {
                for (var i = 0; i < data.length; i++) {
                    element.append(data[i]);
                }
            }
            console.log(data);
        }
    }
};

dpd.tree = function () {
    return {
        restrict: 'E',
        scope: {
            all_data: '=data'
        },
        template: '<div ng-repeat="data in all_data"><children data="data"></children></div>'
    }
};

dpd.children = function ($compile) {
    return {
        restrict: 'E',
        scope: {
            data: '='
        },
        link: function (scope, element) {
            var template = '';
            if (scope.data.type.split('_')[1] == 'list') {
                template += '<div>\n    <div contenteditable="true" class="paper {[{ data.item_class }]}" ng-model="data.value"></div>\n    <append container="data"></append>\n</div>\n<div class="group">\n    <div ng-repeat="data in data.children">\n        <children data="data"></children>\n    </div>\n</div>'
            } else if (scope.data.type == 'container') {
                template += '<div ng-class="data.type" class="paper container {[{ data.item_class }]}">\n    <div ng-repeat="data in data.children">\n        <children data="data"></children>\n    </div>\n    <a class="del span">del</a>\n</div>'
            } else {
                template += '<div contenteditable="true" ng-class="{outline: data.type == \'text\'}" class="paper {[{ data.type }]} {[{ data.item_class }]}" ng-model="data.value"></div>'
            }
            var newElement = angular.element(template);
            $compile(newElement)(scope);
            element.replaceWith(newElement);
        }
    }
};

DynamicPaperApp.directive(dpd);