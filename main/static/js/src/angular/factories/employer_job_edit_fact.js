/**
 * User: jackdevil
 */

PostJobApp.factory ('share',function() {
    var job = [],
        error = [];
    return {
        job: job ,
        error: error
    };
});

PostJobApp.factory ('sharePayment', function(){
    var subscriptions = [],
        packages = [],
        user_package = false,
        user_subscription = false,
        default_package = false,
        select_item = false,
        service_cost = 0,
        advanced_total = 0;

    return {
        subscriptions: subscriptions,
        packages: packages,
        user_package: user_package,
        user_subscription: user_subscription,
        default_package: default_package,
        select_item: select_item,
        service_cost:service_cost,
        advanced_total:advanced_total
    };
});