/**
 * User: jackdevil
 **/

var directives = {};

directives.changeSection = function () {
    return {
        link: function (scope, element, attrs) {
            element.on('click', function (event) {
                if (!scope.current) {
                    _.each($('.pages.sections').children(), function (item, index) {
                        if ($(item).is(":visible")) {
                            scope.current = index + 1;
                        }
                    });
                }
                scope.save_exit(scope.current, false, attrs.section);
                return false;
            });
        }
    }
};

directives.supportdocument = function () {
    return {
        restrict: "E",
        template: "" +
            "<div class='document' ng-repeat='document in job.jobuploaddocument_set | filter:{document_type.id:2}'>" +
            "<a class='link' href='{[{ document.document }]}'>{[{ document.file_name }]}</a>" +
            "<a class='remove' href='' ng-click='document_remove(document)'><img src='/static/main/img/icon_remove.png'></a>" +
            "</div>"
    }
};


directives.fullpositiondocument = function () {
    return {
        restrict: "E",
        template: "" +
            "<div class='document' ng-repeat='document in job.jobuploaddocument_set | filter:{document_type.id:1}'>" +
            "<a class='link' href='{[{ document.document }]}'>{[{ document.file_name }]}</a>" +
            "<a class='remove' href='' ng-click='document_remove(document)'><img src='/static/main/img/icon_remove.png'></a></a>" +
            "</div>"
    }
};

directives.upload = function () {
    return {
        restrict: "E",
        link: function ($scope, element, attrs) {
            var text = element.html();
            var htmlText = '<div class="upload_document_block"><input class="_hide" type="file" name="files[]" data-url="' + attrs.url + '">\n';
            htmlText += '<a href="">' + text + '</a></div>';
            var new_element = element.replaceWithPush(htmlText);
            var input = new_element.find('input'), a = new_element.find('a');

            a.bind('click', function (event) {
                event.preventDefault();
                input.bind('fileuploadstart', function (e) {
                    $('.preloader').show();
                });
                input.fileupload({
                    dataType: 'json',
                    done: function (e, data) {
                        $scope.$apply(function () {
                            $scope.job.jobuploaddocument_set.push(data.result);
                            $('.preloader').hide();
                        });
                    },
                    error: function (e, data) {
                        $('.preloader').hide();
                    }
                });

                input.trigger('click');

            });
        }
    }
};

directives.payment = function () {
    return {
        restrict: "E",
        controller: function ($scope, sharePayment, share, $http) {
            $scope.subscriptions = sharePayment.subscriptions;
            $scope.packages = sharePayment.packages;
            $scope.user_subscription = sharePayment.user_subscription;
            $scope.user_package = sharePayment.user_package;
            $scope.default_package = sharePayment.default_package;
            $scope.job = share.job;
            $scope.select_item = sharePayment.select_item;
            $scope.service_cost = sharePayment.service_cost;

            $scope.confirm = function () {
                $http.post('/payment/payment_redirect/', {job: $scope.job.resource_uri, item: $scope.select_item.resource_uri})
                    .success(function (data, status, headers, config) {
                        window.location.href = data.redirect_url;
                    })
                    .error(function (data, status, headers, config) {
                        $scope.payment_error = data.error;
                    });
            };

            if ($scope.user_subscription) {
                var start_date = new Date();
                var finish_date = new Date($scope.user_subscription.finish_date);
                $scope.user_subscription.remaining = parseInt((finish_date - start_date) / (1000 * 60 * 60 * 24));
            }
            var set_active = function (item) {
                _.map($scope.subscriptions, function (value) {
                    value.active = false
                });
                _.map($scope.packages, function (value) {
                    value.active = false
                });
                if ($scope.user_subscription) {
                    $scope.user_subscription.active = false;
                }
                if ($scope.user_package) {
                    $scope.user_package.active = false;
                }
                $scope.default_package.active = false;

                item.active = true;
            };

            $scope.select = function (item) {
                set_active(item);
                $scope.select_item = item;
                if (item.cost) {
                    $scope.service_cost = item.cost;
                }
            }
        },
        templateUrl: "payment-job.html"
    }
};

directives.advpayment = function () {
    return {
        restrict: "E",
        controller: function ($scope, share, sharePayment) {
            $scope.job = share.job;
            $scope.advanced_total = sharePayment.advanced_total;
            $scope.select_item = sharePayment.select_item;

        },
        link: function ($scope, element, attrs) {
            var advanced_total = 0;
            var html = "<div class='advanced_payment'>";
            if ($scope.job.featured_job) {
                html += "<p> Featured Job - $100 </p>";
                advanced_total += 100;
            }
            if ($scope.job.executive_positions) {
                html += "<p> Executive positions - $25 <p>";
                advanced_total += 25;
            }
            if ($scope.job.categories_set.length > 1) {
                var category_total = (parseInt($scope.job.categories_set.length) - 1) * 15;
                html += "<p> Advanced category - $" + category_total + "<p>";
                advanced_total += category_total;
            }
            if ($scope.job.sub_categories_set.length > 1) {
                var sub_category_total = (parseInt($scope.job.sub_categories_set.length) - 1) * 15;
                html += "<p> Advanced sub-category - $" + sub_category_total + "<p>";
                advanced_total += sub_category_total;
            }
            $scope.advanced_total = advanced_total;
            html += "</div>";
            element.replaceWith(html);
        }
    }
};

directives.total = function () {
    return {
        restrict: "E",
        controller: function ($scope, sharePayment) {
            $scope.service_cost = sharePayment.service_cost;

            $scope.select_text = function () {
                if ($scope.service_cost) {
                    return 'Service cost - $' + $scope.service_cost;
                }
            }

        },
        template: "<p>{[{ select_text() }]}</p><br/><p>Total - ${[{service_cost + advanced_total}]}<p>"
    }
};

directives.field = function () {
    return {
        compile: function compile(temaplateElement, templateAttrs) {
            return {
                pre: function (scope, element, attrs) {
                    console.log("preCompile");
                },
                post: function (scope, element, attrs) {
                    console.log("postCompile");
                }
            }
        },
        priority: 0,
        terminal: false,
        template: '<input type="{[{ type }]}" ng-model="model">',
        replace: false,
        transclude: false,
        restrict: 'E',
        scope: {
            type: "@type",
            name: "@"
        },
        controller: function ($scope, $element, $attrs, $transclude) {
            console.log("controller");
        }
    }
};

MainApp.directive(directives);