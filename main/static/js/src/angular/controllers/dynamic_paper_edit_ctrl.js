/**
 * User: jackdevil
 */

var dynamicPaperCtrl = {}; // Dynamic Paper Controllers Dict

dynamicPaperCtrl.DynamicPaperCtrl = function ($scope) {
    $scope.paper = {};
    $scope.set_data = function (data) {
        $scope.paper.data = data.data;
        $scope.paper.name = data.name[0];
        $scope.paper.select = data.select;
    };
    $scope.select2Options = {
        allowClear: true,
        width: 'off'
    };

    $('#select_cover_letter, #select_resume').change(function () {
        if (this.value) {
            window.location.replace(this.value);
        }
    });
};

MainApp.controller(dynamicPaperCtrl);