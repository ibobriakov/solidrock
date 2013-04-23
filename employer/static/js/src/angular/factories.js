/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 22.04.13
 * Time: 15:13
 * To change this template use File | Settings | File Templates.
 */

PostJobApp.factory ('share',function() {
    var job = [];
    return { job: job };
});

PostJobApp.factory ('sharePayment', function(){
    var subscriptions = [], packages = [];
    return { subscriptions: subscriptions, packages: packages };
});