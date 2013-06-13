/**
 * User: jackdevil
 */

var aplInfoDir = {};

aplInfoDir.upload = function () {
    return {
        restrict: 'E',
        scope: {
            uploadUrl: '@',
            removeUrl: '@',
            photo: '='
        },
        template: '<div>Profile Picture (optional)</div>\n<div class="img">\n    <img id="avatar_img" ng-src="{[{photo}]}">\n\n    <div class="links">\n        <a id="link_upload_file" href="">Upload Photo</a>|\n        <a id="link_remove_file" url="" href="">Delete Picture</a>\n    </div>\n</div>\n<input class="_hide" id="fileupload" type="file" name="files[]" data-url="/upload/job_seeker_photo/">',
        link: function (scope, element, attr) {
            element.find('#fileupload').fileupload({
                singleFileUploads: true,
                dataType: 'json',
                done: function (e, data) {
                    element.find('#avatar_img').attr('src', data.result.url);
                }
            });
            element.find('#link_upload_file').on('click', function () {
                element.find('#fileupload').trigger('click');
                return false;
            });
            element.find('#link_remove_file').on('click', function () {
                $.ajax({
                    url: '/remove/job_seeker_photo/'
                }).done(function (data) {
                        $('#avatar_img').attr('src', data.url);
                    });
                return false;
            })
        }
    }
};

aplInfoDir.activated = function () {
    return {
        restrict: "A",
        link: function ($scope, element, attr) {
            element.children().each(function (index, item) {
                if (attr.activated == "block") {
                    if (parseInt($scope.section) == parseInt(index + 1)) {
                        $(item).show();
                    } else {
                        $(item).hide();
                    }
                } else {
                    if (parseInt($scope.section) == parseInt(index + 1)) {
                        $(item).addClass('active');
                    }
                }
            })
        }
    }
};

aplInfoDir.section = function ($location, $http) {
    return {
        transclude: true,
        scope: {
            num: '@',
            current: '='
        },
        template: '<a href="#/section/{[{num}]}/" ng-transclude></a>',
        link: function ($scope, element, attr) {
            element.bind('click', function (event) {
                $scope.list = $scope.current();
                var no_valid = $scope.list.length;
                _.each($scope.list, function (item) {
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
                            $location.path('/section/' + parseInt($scope.num) + '/');
                        }
                    };
                    $http.put(item.resource_uri, item).error(error_callback).success(success_callback);
                });
                return false;
            });
        }
    }
};

AplInfoApp.directive(aplInfoDir);