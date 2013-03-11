/**
 * Create user: jackdevil
 */

Handlebars.registerHelper('each', function(context, options) {
    var ret = "";
    context.each(function(item){
        ret = ret + options.fn(item);
    });
    return new Handlebars.SafeString(ret);
});

Handlebars.registerHelper('noop', function(options) {
    return new Handlebars.SafeString(options.fn(this));
});

Handlebars.registerHelper('if', function(conditional, options) {
    if(conditional) {
        return new Handlebars.SafeString(options.fn(this));
    }
});