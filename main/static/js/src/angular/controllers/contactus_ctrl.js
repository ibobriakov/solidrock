/**
 * User: jackdevil
 */

var contactUsCtrl = {}; // Dynamic Paper Controllers Dict

contactUsCtrl.ContactUsCtrl = function ($scope, $http) {
    $scope.item = {
        priority: 0
    };

    var success_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        document.location.href="/contact_us/";
    };

    var error_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        $scope.item.error = data.contactus;
    };

    $scope.save = function () {
        $('.preloader').show();
        $http.post('/api/v1/contactus/', $scope.item)
            .success(success_callback)
            .error(error_callback);
    };
};

MainApp.controller(contactUsCtrl);
