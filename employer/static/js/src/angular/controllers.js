/**
 * User: jackdevil
 */

PostJobApp.controller ('JobData', function($scope, share) {
    $scope.set_data = function(data){
        $scope.job = data;
        share.job = $scope.job;
    };
});

PostJobApp.controller('JobInfoCtrl', function ($scope, $http, $route, $routeParams, $location, share) {
    $scope.job = share.job;

    $scope.error = [];
    $scope.section = parseInt($routeParams.section);

    $scope.checkActive = function(section) {
        return parseInt(section) == parseInt($scope.section) ? true : false
    };

    $scope.save_exit = function (exit) {
        exit = typeof (exit) == 'boolean' ? exit : true;
        $('.footer_loader').show();
        $http.put($scope.job.resource_uri, $scope.job)
            .success(exit ? success_exit_callback : success_callback)
            .error(error_callback);
    };

    $scope.append = function (container) {
        container.push({"job": $scope.job.resource_uri});
    };

    $scope.remove = function (container, index) {
        if (container[index].resource_uri) $http.delete(container[index].resource_uri);
        container.splice(index, 1);
    };

    $scope.document_remove = function(document){
        _.each($scope.job.jobuploaddocument_set, function(item,index){
            if (item.resource_uri == document.resource_uri) {
                if ($scope.job.jobuploaddocument_set[index].resource_uri)
                    $http.delete($scope.job.jobuploaddocument_set[index].resource_uri);
                $scope.job.jobuploaddocument_set.splice(index, 1);
            }
        });
    };

    var success_callback = function (data, status, headers, config) {
        $('.footer_loader').hide();
        $location.path('/section/'+parseInt($scope.section+1)+'/');
    };

    var success_exit_callback = function (data, status, headers, config) {
        $('.footer_loader').hide();
        document.location.href="/employer/";
    };

    var error_callback = function (data, status, headers, config) {
        $('.footer_loader').hide();
        $scope.error = data.job;
    };

    $('select').select2();
});
