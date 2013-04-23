/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 22.04.13
 * Time: 14:36
 * To change this template use File | Settings | File Templates.
 */

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
};

directives.supportdocument = function(){
    return {
        restrict: "E",
        template: "" +
            "<div ng-repeat='document in job.jobuploaddocument_set | filter:{document_type.id:2}'>" +
                "<a href='{[{ document.document }]}'>{[{ document.file_name }]}</a>" +
                "<a href='' ng-click='document_remove(document)'>x</a>" +
            "</div>"
    }
};


directives.fullpositiondocument = function(){
    return {
        restrict: "E",
        template: "" +
            "<div ng-repeat='document in job.jobuploaddocument_set | filter:{document_type.id:1}'>" +
                "<a href='{[{ document.document }]}'>{[{ document.file_name }]}</a>" +
                "<a href='' ng-click='document_remove(document)'>x</a>" +
            "</div>"
    }
};

directives.upload = function(){
    return {
        restrict: "E",
        link: function($scope, element, attrs) {
            var text = element.html();
            var htmlText = '<div><input class="_hide" type="file" name="files[]" data-url="' + attrs.url + '">\n';
            htmlText += '<a href="">' + text + '</a></div>';
            var new_element = element.replaceWithPush(htmlText);
            var input = new_element.find('input'), a = new_element.find('a');

            a.bind('click',function(event) {
                event.preventDefault();
                input.fileupload({
                    dataType: 'json',
                    done: function (e, data) {
                        $scope.$apply( function () {
                            $scope.job.jobuploaddocument_set.push(data.result);
                        });
                    }
                });
                input.trigger('click');
            });
        }
    }
};

PostJobApp.directive(directives);