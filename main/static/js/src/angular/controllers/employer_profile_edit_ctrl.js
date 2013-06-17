/**
 * User: jackdevil
 */

var employerProfileCtrl = {};

employerProfileCtrl.EmployerEditProfileData = function ($scope, employerEditProfileShare) {
    $scope.set_data = function (data) {
        employerEditProfileShare.personal_information = data.personal_information;
    };
};

employerProfileCtrl.EmployerEditProfileCtrl = function ($scope, $http, $route, $routeParams, $location, employerEditProfileShare) {
    $scope.data = {};
    $scope.data.personal_information = employerEditProfileShare.personal_information;

    $scope.has_error = function (dict) {
        if (!dict) return false;
        for (var key in dict) {
            if (dict.hasOwnProperty(key)) {
                return true;
            }
        }
        return false;
    };

    $scope.save = function (list) {
        var no_valid = list.length;
        _.each(list, function (item) {
            $('.preloader').show();
            var error_callback = function (data, status, headers, config) {
                $('.preloader').hide();
                $('.error').fadeIn();
                _.each(data, function (value, key) {
                    item.error = value;
                });
            };
            var success_callback = function (data, status, headers, config) {
                no_valid--;
                item.error = {};
                if (!no_valid) {
                    $('.preloader').hide();
                    window.location.href = "/employer/";
                }
            };
            $('.error').fadeOut();
            $http.put(item.resource_uri, item)
                .error(error_callback).success(success_callback);
        });
    }
};

MainApp.controller(employerProfileCtrl);