var employerProfileDir = {};

employerProfileDir.upload = function () {
    return {
        restrict: 'E',
        scope: {
            logo: '='
        },
        template: '<div>Company Logo (optional)</div>\n<div class="img">\n    <img id="avatar_img" ng-src="{[{ logo }]}">\n\n    <div class="links">\n        <a id="link_upload_file" href="">Upload Photo</a>|\n        <a id="link_remove_file" href="">Delete Picture</a>\n    </div>\n</div>\n<input class="_hide" id="fileupload" type="file" name="files[]" data-url="/upload/employer_company_logo/">',
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
                    url: '/remove/employer_company_logo/'
                }).done(function (data) {
                        $('#avatar_img').attr('src', data.url);
                    });
                return false;
            })
        }
    }
};

MainApp.directive(employerProfileDir);