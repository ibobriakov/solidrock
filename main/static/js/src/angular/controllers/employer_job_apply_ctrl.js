/**
 * User: jackdevil
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
                $('.click-apply-now').replaceWith('<div class="click-apply-now" style="height: auto;"><a>You have been applied for this job.</a></div>')
            }).error(function(data, status, headers, config){
                $scope.error = data.applytojob;
            })
        };
});