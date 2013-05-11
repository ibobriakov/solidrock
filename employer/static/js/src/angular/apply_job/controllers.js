/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 11.05.13
 * Time: 12:24
 * To change this template use File | Settings | File Templates.
 */

ApplyJobApp.controller('ApplyJobCtrl',function($scope, $http) {
    $scope.applyToJob = {};
    $scope.confirm = function() {
        $http.post('/api/v1/applytojob/', {
                cover_letter: $scope.applyToJob.cover_letter,
                resume: $scope.applyToJob.resume,
                job: $scope.applyToJob.job
            })
            .success(function(data, status, headers, config) {
            })
        };
});