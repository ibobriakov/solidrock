/**
 * User: jackdevil
 */

PostJobApp.factory ('share',function() {
    var job = [];
    return { job: job };
});

PostJobApp.factory ('sharePayment', function(){
    var subscriptions = [],
        packages = [],
        current_package = false,
        current_subscription = false,
        select = false;

    return {
        subscriptions: subscriptions,
        packages: packages,
        current_package: current_package,
        current_subscription: current_subscription,
        select: select
    };
});