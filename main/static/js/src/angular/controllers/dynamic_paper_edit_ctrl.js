/**
 * User: jackdevil
 */

var dpc = {}; // Dynamic Paper Controllers Dict

dpc.DynamicPaperCtrl = function ($scope) {
    $scope.paper = {};
    $scope.set_data = function (data) {
        $scope.paper.data = data.data;
        $scope.paper.name = data.name[0];
    };

    $('#id_resume').change(function () {
        window.location.replace(this.value);
    });

    $('#id_cover_letter').change(function () {
        window.location.replace(this.value);
    });
};

DynamicPaperApp.controller(dpc);