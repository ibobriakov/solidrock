/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 05.06.13
 * Time: 14:48
 * To change this template use File | Settings | File Templates.
 */

var dpd = {}; // Dynamic Paper directives Dict

dpd.contenteditable = function () {
    return {
        require: 'ngModel',
        link: function (scope, element, attrs, ctrl) {
            // view -> model
            element.bind('blur', function () {
                scope.$apply(function () {
                    ctrl.$setViewValue(element.html());
                });
            });

            // model -> view
            ctrl.$render = function () {
                element.html(ctrl.$viewValue);
            };

            // load init value from DOM
            ctrl.$setViewValue(element.html());
        }
    }
}

DynamicPaperApp.directive(dpd);