/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 05.06.13
 * Time: 14:48
 * To change this template use File | Settings | File Templates.
 */

var dpc = {}; // Dynamic Paper Controllers Dict

dpc.DynamicPaperCtrl = function($scope) {
    $scope.paper_data = {};
    $scope.set_data = function(data){
        console.log(data)
    };
};

DynamicPaperApp.controller(dpc);