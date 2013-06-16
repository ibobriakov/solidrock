/**
 * User: jackdevil
 */

var mainController = {}; // Dynamic Paper Controllers Dict

mainController.LoginCtrl = function ($scope, $http) {
    $scope.login = {'username': '', password: ''};
    $scope.error = {};
    $scope.next_url = $('#login_form').attr('data-next-url') || '/';
    var success_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        window.location.href = $scope.next_url;
    };
    var error_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        $('.error').fadeIn();
        $scope.error = data.login;
        $scope.login.password = '';
    };
    $scope.submit = function () {
        $('.preloader').show();
        $('.error').fadeOut();
        $http.post('/api/v1/login/', $scope.login)
            .error(error_callback)
            .success(success_callback)
    }
};

mainController.RegisterJobSeekerCtrl = function ($scope, $http) {
    $scope.reg = {
        "email_address": '',
        "first_name": '',
        "last_name": '',
        "password": '',
        "re_password": ''
    };
    $scope.error = {};
    $scope.next_url = $('#register_job_seeker_form').attr('data-next-url') || '/';
    var success_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        window.location.href = $scope.next_url;
    };
    var error_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        $('.error').fadeIn();
        $scope.error = data.job_seeker_registration;
    };
    $scope.submit = function () {
        $('.preloader').show();
        $('.error').fadeOut();
        $http.post('/api/v1/job_seeker_registration/', $scope.reg)
            .error(error_callback)
            .success(success_callback)
    }
};

mainController.RegisterEmployerCtrl = function ($scope, $http) {
    $scope.reg = {
        "company_name": '',
        "email_address": '',
        "password": '',
        "phone_number": '',
        "re_password": ''
    };
    $scope.error = {};
    $scope.next_url = $('#register_employer_form').attr('data-next-url') || '/';
    var success_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        window.location.href = $scope.next_url;
    };
    var error_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        $('.error').fadeIn();
        $scope.error = data.employer_registration;
    };
    $scope.submit = function () {
        $('.preloader').show();
        $('.error').fadeOut();
        $http.post('/api/v1/employer_registration/', $scope.reg)
            .error(error_callback)
            .success(success_callback)
    }
};

MainApp.controller(mainController);