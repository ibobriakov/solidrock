/**
 * User: jackdevil
 */

// Job payment controller

var listJobCtrl = {};

listJobCtrl.ListJobCtrl = function ($scope, $http, $location) {
    $scope.url = '/api/v1/jobbanner/';
    $scope.limit = 5;
    $scope.offset = 0;
    $scope.current = 0;
    $scope.pages = 1;
    $scope.archived = false;
    $scope.get_url = function(item){
        if ($scope.archived) {
            return $scope.url + '?limit=' + $scope.limit + '&offset=' + $scope.limit*item + '&archived=true';
        } else {
            return $scope.url + '?limit=' + $scope.limit + '&offset=' + $scope.limit*item; 
        }
    };
    $('.preloader').show();
    $http.get($scope.url+"?limit="+$scope.limit).success(function(data, status, headers, config) {
        $scope.data = data;
        $scope.pages = parseInt(data.meta.total_count/$scope.limit)
        $('.preloader').hide();
    });
};

MainApp.filter('makeRange', function() {
    return function(input) {
        var result = [];
        for (var i = 0; i <= input; i++) {
            result.push(i);
        }
        return result;
    }
});

MainApp.controller(listJobCtrl);
