/**
 * User: jackdevil
 */

// Job payment controller

var postJobCtrl = {};

postJobCtrl.JobPaymentData = function ($scope, sharePayment) {
    $scope.set_data = function (data) {
        _.each(data, function (value, key) {
            $scope[key] = value;
        });
        sharePayment.subscriptions = $scope.subscriptions;
        sharePayment.packages = $scope.packages;

        sharePayment.user_subscription = $scope.user_subscription ? $scope.user_subscription : false;
        sharePayment.user_package = $scope.user_package ? $scope.user_package : false;

        sharePayment.default_package = $scope.default_package;
    }
};

postJobCtrl.JobPayment = function ($scope, sharePayment, share) {
    $scope.subscriptions = sharePayment.subscriptions;
    $scope.packages = sharePayment.packages;

    $scope.user_subscription = sharePayment.user_subscription;
    $scope.user_package = sharePayment.user_package;

    $scope.default_package = sharePayment.default_package;

    $scope.job = share.job;
};

// Main post job controller

postJobCtrl.JobData = function ($scope, share) {
    $scope.set_data = function (data) {
        $scope.job = data;
        share.job = $scope.job;
    };
};

postJobCtrl.JobInfoCtrl = function ($scope, $http, $route, $routeParams, $location, share) {
    $scope.job = share.job;

    $scope.error = share.error;

    $scope.save_exit = function (section, exit, next) {
        exit = typeof (exit) == 'boolean' ? exit : true;
        next = parseInt(next) || parseInt(section)+1;

        var success_callback = function (data, status, headers, config) {
            $('.preloader').hide();
            $('.section'+section).addClass('checked');
            $location.path('/section/' + parseInt(next) + '/');
            $scope.current = parseInt(next);
        };

        var success_exit_callback = function (data, status, headers, config) {
            $('.preloader').hide();
            document.location.href = "/employer/";
        };

        var error_callback = function (data, status, headers, config) {
            $('.preloader').hide();
            $('.error').fadeIn();
            $scope.error = data.job;
        };

        $('.preloader').show();
        $('.error').fadeOut();
        _.each($scope.job, function(v,k) {
            if (v === "") {
                console.log(k, v);
                $scope.job[k] = null;
            }
        });
        if (exit) $scope.job['no_validate']=true
        $http.put($scope.job.resource_uri, $scope.job)
            .success(exit ? success_exit_callback : success_callback)
            .error(error_callback);
    };

    $scope.append = function (container) {
        if (!container) container=[];
        container.push({"job": $scope.job.resource_uri});
    };

    $scope.remove = function (container, index) {
        if (container[index].resource_uri) $http.delete(container[index].resource_uri);
        container.splice(index, 1);
    };

    $scope.document_remove = function (document) {
        _.each($scope.job.jobuploaddocument_set, function (item, index) {
            if (item.resource_uri == document.resource_uri) {
                if ($scope.job.jobuploaddocument_set[index].resource_uri)
                    $http.delete($scope.job.jobuploaddocument_set[index].resource_uri);
                $scope.job.jobuploaddocument_set.splice(index, 1);
            }
        });
    };

    $scope.upload_add_btn_hide = function (container) {
        if (container)
            return container.length > 5 ? true : false;
        return false;
    };
};

MainApp.controller(postJobCtrl);
