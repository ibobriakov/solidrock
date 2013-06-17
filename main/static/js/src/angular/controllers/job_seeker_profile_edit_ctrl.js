/**
 * User: jackdevil
 */

var AplInfoCtrl = {};

AplInfoCtrl.AplInfoData = function ($scope, aplInfoShare) {
    $scope.set_data = function (data) {
        aplInfoShare.personal_information = data.personal_information;
        aplInfoShare.current_employment = data.current_employment;
        aplInfoShare.previous_employments = data.previous_employments;
        aplInfoShare.educations = data.educations;
        aplInfoShare.referees = data.referees;
    };
};

AplInfoCtrl.AplInfoCtrl = function ($scope, $rootScope, $http, $location, aplInfoShare) {
    $scope.data = {};
    $scope.data.personal_information = aplInfoShare.personal_information;
    $scope.data.current_employment = aplInfoShare.current_employment;
    $scope.data.previous_employments = aplInfoShare.previous_employments;
    $scope.data.educations = aplInfoShare.educations;
    $scope.data.referees = aplInfoShare.referees;

    $scope.has_error = function (dict) {
        if (!dict) return false;
        for (var key in dict) {
            if (dict.hasOwnProperty(key)) {
                return true;
            }
        }
        return false;
    };

    $scope.get_current_data = function (current) {
        switch (current) {
            case 1:
                return $scope.data.personal_information;
            case 2:
                return $scope.data.current_employment;
            case 3:
                return $scope.data.previous_employments;
            case 4:
                return $scope.data.educations;
            case 5:
                return $scope.data.referees
        }
        return false;
    };

    $scope.get_api_uri = function (section) {
        switch (section) {
            case 1:
                return '/api/v1/job_seeker_information/';
            case 2:
                return '/api/v1/job_seeker_current_employment/';
            case 3:
                return '/api/v1/job_seeker_previous_employment/';
            case 4:
                return '/api/v1/job_seeker_education/';
            case 5:
                return '/api/v1/job_seeker_referee/';
        }
        return false;
    };

    $scope.append = function (container, append_data) {
        container.push(append_data || {});
    };

    $scope.remove = function (item, container) {
        if (item.resource_uri) {
            $http.delete(item.resource_uri);
            container.splice(container.indexOf(item), 1);
        }
    };

    $scope.save = function (section, list, exit, next) {
        exit = exit || false;
        next = next || 1;
        var url = $scope.get_api_uri(parseInt(section));
        var no_valid = list.length;
        _.each(list, function (item) {
            $('.preloader').show();
            var error_callback = function (data, status, headers, config) {
                $('.preloader').hide();
                $('.error, .error_top').fadeIn();
                _.each(data, function (value, key) {
                    item.error = value;
                });
            };
            var success_callback = function (data, status, headers, config) {
                no_valid--;
                item.error = {};
                if (!no_valid) {
                    $('.preloader').hide();
                    $('.section' + $scope.current).addClass('checked');
                    $scope.current = parseInt(next);
                    $location.path('/section/' + parseInt(next) + '/');
                }
            };
            var success_exit_callback = function (data, status, headers, config) {
                no_valid--;
                item.error = {};
                if (!no_valid) {
                    $('.preloader').hide();
                    window.location.href = "/job_seeker/";
                }
            };
            $('.error, .error_top').fadeOut();
            if (item.resource_uri) {
                $http.put(item.resource_uri, item)
                    .error(error_callback).success(exit ? success_exit_callback : success_callback);
            } else {
                $http.post(url, item)
                    .error(error_callback).success(exit ? success_exit_callback : success_callback);
            }
        });
    }
};

MainApp.controller(AplInfoCtrl);