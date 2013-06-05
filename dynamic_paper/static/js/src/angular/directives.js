/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 05.06.13
 * Time: 14:48
 * To change this template use File | Settings | File Templates.
 */

var dpd = {}; // Dynamic Paper directives Dict

dpd.paper = function(){
    return {
        restrict: "E",
        scope: {
            data: '='
        },
        template: "<div ng-repeat=\'item in data\'>\n    <p>{[{ item }]}</p>\n</div>"
    }
};

DynamicPaperApp.directive(dpd);