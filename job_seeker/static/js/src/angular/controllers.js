/**
 * User: jackdevil
 */

AplInfoApp.controller('AplInfoData', function ($scope, aplInfoShare) {
    $scope.set_data = function (data) {
        aplInfoShare.personal_information = data.personal_information;
        aplInfoShare.current_employment = data.current_employment;
        aplInfoShare.previous_employments = data.previous_employments;
        aplInfoShare.educations = data.educations;
        aplInfoShare.referees = data.referees;
    };
});

AplInfoApp.controller('AplInfoCtrl', function ($scope, $http, $route, $routeParams, $location, aplInfoShare) {
    $scope.data = {};
    $scope.data.personal_information = aplInfoShare.personal_information;
    $scope.data.current_employment = aplInfoShare.current_employment;
    $scope.data.previous_employments = aplInfoShare.previous_employments;
    $scope.data.educations = aplInfoShare.educations;
    $scope.data.referees = aplInfoShare.referees;
    $scope.section = parseInt($routeParams.section);

    $scope.current = function() {
        switch ($scope.section) {
            case 1:
                return $scope.data.personal_information
            case 2:
                return $scope.data.current_employment
            case 3:
                return $scope.data.previous_employments
            case 4:
                return $scope.data.educations
            case 5:
                return $scope.data.referees
        }
        return false;
    };

    $scope.append = function (container, url, append_data) {
        append_data = append_data || {};
        var success_callback = function (data, status, headers, config) {
            container.push(data);
        };
        $http.post(url, append_data).success(success_callback);
    };

    $scope.remove = function (item, container) {
        if (item.resource_uri) {
            $http.delete(item.resource_uri);
            container.splice(container.indexOf(item), 1);
        }
    };

    $scope.save = function (list, exit) {
        exit = typeof (exit) == 'boolean' ? exit : true;
        var no_valid = list.length;
        _.each(list, function (item) {
            $('.preloader').show();
            var error_callback = function (data, status, headers, config) {
                $('.preloader').hide();
                _.each(data, function (value, key) {
                    item.error = value;
                });
            };
            var success_callback = function (data, status, headers, config) {
                no_valid--;
                item.error = {};
                if (!no_valid) {
                    $('.preloader').hide();
                    $location.path('/section/' + parseInt($scope.section + 1) + '/');
                }
            };
            var success_exit_callback = function (data, status, headers, config) {
                no_valid--;
                item.error = {};
                if (!no_valid) {
                    $('.preloader').hide();
                    $location.path('/section/' + parseInt($scope.section + 1) + '/');
                }
            };
            $http.put(item.resource_uri, item)
                .error(error_callback).success(exit ? success_exit_callback : success_callback);
        });
    }
});