/**
 * User: jackdevil
 **/

var listJobDir = {};

listJobDir.paginate = function(){
    return {
        link: function (scope, element, attr){
            element.on('click', function(){
                console.log(scope);
            });
        }
    }
}

MainApp.directive(listJobDir);
