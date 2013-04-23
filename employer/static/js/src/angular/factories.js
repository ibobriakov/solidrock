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
        user_package = false,
        user_subscription = false,
        default_package = false,
        select = false;

    return {
        subscriptions: subscriptions,
        packages: packages,
        user_package: user_package,
        user_subscription: user_subscription,
        default_package: default_package,
        select: select
    };
});