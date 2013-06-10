/**
 * User: jackdevil
 */

var dpc = {}; // Dynamic Paper Controllers Dict

dpc.DynamicPaperCtrl = function($scope) {
    $scope.paper = {};
    $scope.set_data = function(data){
        $scope.paper.data = data.data;
        $scope.paper.name = data.name[0];
    };
};

DynamicPaperApp.controller(dpc);