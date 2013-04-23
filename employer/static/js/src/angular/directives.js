/**
 * User: jackdevil
**/

var directives = {};

directives.activated = function() {
    return {
        restrict: "A",
        link: function($scope, element, attr) {
            element.children().each(function(index,item) {
                if (attr.activated == "block") {
                   if (parseInt($scope.section) == parseInt(index+1)) {
                        $(item).show();
                    } else {
                       $(item).hide();
                   }
                } else {
                    if (parseInt($scope.section) == parseInt(index+1)) {
                        $(item).addClass('active');
                    }
                }
            })
        }
    }
};

directives.supportdocument = function(){
    return {
        restrict: "E",
        template: "" +
            "<div class='document' ng-repeat='document in job.jobuploaddocument_set | filter:{document_type.id:2}'>" +
                "<a class='link' href='{[{ document.document }]}'>{[{ document.file_name }]}</a>" +
                "<a class='remove' href='' ng-click='document_remove(document)'><img src='/static/main/img/icon_remove.png'></a>" +
            "</div>"
    }
};


directives.fullpositiondocument = function(){
    return {
        restrict: "E",
        template: "" +
            "<div class='document' ng-repeat='document in job.jobuploaddocument_set | filter:{document_type.id:1}'>" +
                "<a class='link' href='{[{ document.document }]}'>{[{ document.file_name }]}</a>" +
                "<a class='remove' href='' ng-click='document_remove(document)'><img src='/static/main/img/icon_remove.png'></a></a>" +
            "</div>"
    }
};

directives.upload = function(){
    return {
        restrict: "E",
        link: function($scope, element, attrs) {
            var text = element.html();
            var htmlText = '<div class="upload_document_block"><input class="_hide" type="file" name="files[]" data-url="' + attrs.url + '">\n';
            htmlText += '<a href="">' + text + '</a></div>';
            var new_element = element.replaceWithPush(htmlText);
            var input = new_element.find('input'), a = new_element.find('a');

            a.bind('click',function(event) {
                event.preventDefault();
                input.fileupload({
                    dataType: 'json',
                    done: function (e, data) {
                        $scope.$apply( function () {
                            $scope.job.jobuploaddocument_set.push(data.result);
                        });
                    }
                });
                input.trigger('click');
            });
        }
    }
};

directives.payment = function() {
    return {
        restrict: "E",
        controller: function($scope, sharePayment, share, $http){
            $scope.subscriptions = sharePayment.subscriptions;
            $scope.packages = sharePayment.packages;
            $scope.user_subscription = sharePayment.user_subscription;
            $scope.user_package = sharePayment.user_package;
            $scope.default_package = sharePayment.default_package;
            $scope.job = share.job;
            $scope.select_item = sharePayment.select_item;

            $scope.confirm = function() {
                $http.post('/payment/payment_redirect/', {job: $scope.job.resource_uri, item: $scope.select_item.resource_uri})
                    .success(function(){})
                    .error(function(){});
            };

            if ($scope.user_subscription) {
                var start_date = new Date();
                var finish_date = new Date($scope.user_subscription.finish_date);
                $scope.user_subscription.remaining = parseInt((finish_date-start_date)/(1000*60*60*24));
            }
            var set_active = function(item) {
                _.map($scope.subscriptions,function(value){ value.active=false });
                _.map($scope.packages,function(value){ value.active=false });
                if ($scope.user_subscription) {
                    $scope.user_subscription.active = false;
                }
                if ($scope.user_package) {
                    $scope.user_package.active = false;
                }
                $scope.default_package.active = false;

                item.active = true;
            };

            $scope.select = function(item){
                set_active(item);
                $scope.select_item = item;
            }
        },
        templateUrl: "payment-job.html"
    }
};

directives.advpayment = function(){
    return {
        restrict: "E",
        controller: function($scope, share){
            $scope.job = share.job;
        },
        link: function($scope, element, attrs){
            var html = "<div class='advanced_payment'>";
            if ($scope.job.featured_job) {
                html += "<p> Featured Job - $100 </p>";
            }
            if ($scope.job.executive_positions) {
                html += "<p> Executive positions - $25 <p>";
            }
            if ($scope.job.categories_set.length > 1) {
                html += "<p> Advanced category - $15 <p>";
            }
            if ($scope.job.sub_categories_set.length > 1) {
                html += "<p> Advanced sub-category - $15 <p>";
            }
            html+="</div>";
            element.replaceWith(html);
        }
    }
};

PostJobApp.directive(directives);