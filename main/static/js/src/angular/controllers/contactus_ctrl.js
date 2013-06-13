/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 13.06.13
 * Time: 14:46
 * To change this template use File | Settings | File Templates.
 */

var contactUsController = {}; // Dynamic Paper Controllers Dict

contactUsController.ContactUsCtrl = function ($scope, $http) {
    $scope.item = {};

    var success_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        document.location.href="/contact_us/";
    };

    var error_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        $scope.error = data.job;
    };

    $scope.save_exit = function () {
        $('.preloader').show();
        $http.put('', $scope.item)
            .success(success_callback)
            .error(error_callback);
    };
};

ContactUsApp.controller(contactUsController);