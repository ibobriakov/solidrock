/**
 * User: jackdevil
 */

var contactUsCtrl = {}; // Dynamic Paper Controllers Dict
    
contactUsCtrl.ContactUsCtrl = function ($scope, $http) {
    $scope.item = {
        priority: 0
    };

    var show_contactus_success = function (){
        var id = $('.window.contactus_success .window_block');
        var contactus_hide = $('.window.contactus_success ._hide'); 
        contactus_hide.css({'width': maskWidth, 'height': maskHeight});
        var maskHeight = $(document).height();
        var maskWidth = $(window).width();
        contactus_hide.css({'width': maskWidth, 'height': maskHeight});
        contactus_hide.fadeIn(500);
        contactus_hide.fadeTo(500);
        var winH = $(window).height();
        var winW = $(window).width();
        $(id).css('top', winH / 2 - $(id).height() / 2);
        $(id).css('left', winW / 2 - $(id).width() / 2);
        $(id).fadeIn(500);
    };

    var success_callback = function (data, status, headers, config) {
        $('.preloader').hide();
        show_contactus_success();
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
