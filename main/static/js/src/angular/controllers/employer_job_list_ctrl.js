/**
 * User: jackdevil
 */

// Job payment controller

var listJobCtrl = {};

listJobCtrl.ListJobCtrl = function ($scope, $http, $location) {
    $scope.url = '/api/v1/jobbanner/';
    $scope.limit = 9;
    $scope.offset = 0;
    $scope.current = 0;
    $scope.pages = 1;
    $scope.archived = false;
    
    $scope.get_url = function(item){
        return $scope.url + '?limit=' + $scope.limit + '&offset=' + $scope.limit*item + '&archived=' + $scope.archived;
    };
   
    $scope.set_archived = function(archived){
        $scope.archived = archived;
        $scope.get_data($scope.get_url(0),0);
    }

    $scope.get_data = function(url,page) {
        if (!url) return;
        $('.preloader').show();
        $http.get(url).success(function(data, status, headers, config) {
            $scope.data = data;
            $scope.current = page;
            $scope.pages = parseInt(data.meta.total_count/$scope.limit)
            $('.preloader').hide();
        });
    };

    $scope.get_data($scope.get_url(0),0);

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
