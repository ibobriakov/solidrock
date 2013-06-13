/**
 * User: jackdevil
 */

var dpd = {}; // Dynamic Paper directives Dict

dpd.noteditable = function () {
    return {
        require: 'ngModel',
        link: function (scope, element, attrs, ctrl) {
            ctrl.$render = function () {
                element.html(ctrl.$viewValue);
            };
            ctrl.$render();
        }
    }
};

dpd.contenteditable = function ($http) {
    return {
        require: 'ngModel',
        link: function (scope, element, attrs, ctrl) {
            element.bind('blur', function () {
                scope.$apply(function () {
                    ctrl.$setViewValue(element.html());
                    var url = scope.data.resource_uri;
                    $http.put(url, scope.data);
                });
            });
            ctrl.$render = function () {
                element.html(ctrl.$viewValue);
            };
            ctrl.$render();
        }
    }
};

dpd.remove = function ($http) {
    return {
        restrict: 'E',
        scope: {
            container: '=',
            index: '='
        },
        template: '<a href="" ng-click="remove(container, index)"></a>',
        link: function (scope) {
            var success_callback = function () {
                scope.container.children.splice(scope.index, 1);
            };
            scope.remove = function (container, index) {
                var url = container.children[index].resource_uri;
                $http.delete(url).success(success_callback);
            }
        }
    }
};

dpd.append = function ($http) {
    return {
        restrict: 'E',
        scope: {
            container: '='
        },
        template: '<a href="" ng-click="append(container)"></a>',
        link: function (scope) {
            var success_callback = function (data) {
                scope.container.children.push(data);
            };
            scope.append = function (container) {
                var url = container.resource_uri;
                url = url.replace(url.substr((url.substring(0, url.length - 1)).lastIndexOf('/') + 1), '');
                $http.post(url, {
                    'paper': container.paper,
                    'type': 'container',
                    'parent': container.id,
                    'value': container.type.split('_')[0]
                }).success(success_callback);
            }
        }
    }
};

dpd.tree = function () {
    return {
        restrict: 'E',
        scope: {
            all_data: '=data'
        },
        template: '<div ng-repeat="child in all_data">\n    <children data="child" index="$index" container="all_data"></children>\n</div>'
    }
};

dpd.oneline = function () {
    return {
        link: function (scope, element, attrs) {
            element.keypress(function (e) {
                if (e.which == 13) {
                    $(this).blur();
                }
            });
        }
    }
};

dpd.paperName = function ($http) {
    return {
        transclude: true,
        restrict: 'E',
        scope: {
            data: '='
        },
        template: '<div class="title" ng-transclude></div><input type="text" ng-model="data.name"/>',
        link: function (scope, element, attrs) {
            element.find('input').bind('blur', function () {
                var url = scope.data.resource_uri;
                $http.put(url, scope.data);
            })
        }
    }
};

dpd.children = function ($compile) {
    return {
        restrict: 'E',
        scope: {
            data: '=',
            index: '=',
            container: '='
        },
        link: function (scope, element) {
            var template = '';
            var oneline = true ? scope.data.item_class && scope.data.item_class.split(' ').indexOf('oneline') != -1 : false;
            if (scope.data.type.split('_')[1] == 'list') {
                template += '<div>\n    <div noteditable="true" class="paper {[{ data.item_class }]}" ng-model="data.value" data-placeholder="{[{ data.placeholder }]}"></div>\n    <append container="data"></append>\n</div>\n<div class="group {[{ data.item_class }]}">\n    <div ng-repeat="child in data.children">\n        <children data="child" index="$index" container="data"></children>\n    </div>\n</div>'
            } else if (scope.data.type == 'container') {
                if (scope.data.children.length > 2) {
                    template += '<div class="paper container {[{ data.item_class }]} ">\n    <div ng-repeat="child in data.children">\n        <children data="child" index="$index" container="data"></children>\n    </div>\n    <remove container="container" index="index" class="remove_top"></remove>\n</div>'
                } else {
                    template += '<div class="paper container {[{ data.item_class }]} ">\n    <div ng-repeat="child in data.children">\n        <children data="child" index="$index" container="data"></children>\n    </div>\n    <remove container="container" index="index"></remove>\n</div>'
                }
            } else if (scope.data.type == 'text') {
                template += '<div contenteditable="true" ng-class="{outline: data.type == \'text\'}" class="paper {[{ data.type }]} {[{ data.item_class }]}" ng-model="data.value" data-placeholder="{[{ data.placeholder }]}"';
                if (scope.data.value && scope.data.value != "<br>") {
                    template += ' data-div-placeholder-content="true" ';
                }
                if (oneline) {
                    template += ' oneline ';
                }
                template += '></div>';
            } else {
                template += '<div noteditable="true" ng-class="{outline: data.type == \'text\'}" class="paper {[{ data.type }]} {[{ data.item_class }]}" ng-model="data.value" data-placeholder="{[{ data.placeholder }]}"></div>'
            }
            var newElement = angular.element(template);
            $compile(newElement)(scope);
            element.replaceWith(newElement);
        }
    }
};

DynamicPaperApp.directive(dpd);