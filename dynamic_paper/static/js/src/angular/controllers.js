/**
 * User: jackdevil
 */

var dpc = {}; // Dynamic Paper Controllers Dict

dpc.DynamicPaperCtrl = function($scope, $http) {
    $scope.paper_data = {};
    $scope.set_data = function(data){
        $scope.paper_data = data;
    };
};

DynamicPaperApp.controller(dpc);