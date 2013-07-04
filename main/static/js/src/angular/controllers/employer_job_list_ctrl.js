/**
 * User: jackdevil
 */

// Job payment controller

var listJobCtrl = {};

listJobCtrl.ListJobCtrl = function ($scope, $http, $location) {
    var url = '/api/v1/jobbanner/';
    var limit = 5;
    var offset = 0;
    $scope.current = 0;
    $scope.pages = 1;

    $('.preloader').show();
    $http.get(url+"?limit="+limit).success(function(data, status, headers, config) {
        $scope.data = data;
        $scope.pages = data.meta.total_count/limit + 1;
        $('.preloader').hide();
    })
};

MainApp.controller(listJobCtrl);
