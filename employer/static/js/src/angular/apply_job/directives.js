/**
 * User: jackdevil
**/

var apply_job_directives = {};

apply_job_directives.collapse = function() {
    var collapsed = function(element){
        element.fadeToggle();
    };
    return {
        restrict: "A",
        link: function(scope, element, attrs) {
            var collapseItems = element.children('.collapseItems');
            if (attrs.collapse=="true") {
                collapseItems.hide();
            }
            var collapseAction = element.children('.collapseAction');
            collapseAction.on('click', function() {
                collapsed(collapseItems);
            });
        }
    }
}

ApplyJobApp.directive(apply_job_directives);