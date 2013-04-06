/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 29.03.13
 * Time: 22:44
 * To change this template use File | Settings | File Templates.
 */
rivets.configure({
    adapter: {
        subscribe: function(object, keypath, callback) {
            if (object instanceof Backbone.Collection) {
                object.on('add remove reset', function (){ callback(object[keypath]) });
            } else if (object instanceof Backbone.Model) {
                object.on('change:'+keypath, function(m,v){ callback(v) });
            }
        },

        unsubscribe: function(object, keypath, callback) {
            if (object instanceof Backbone.Collection) {
                object.off('add remove reset', function (){ callback(object[keypath]) });
            } else if (object instanceof Backbone.Model) {
                object.off('change:'+keypath, function(m,v){ callback(v) });
            }
        },

        read: function(object, keypath) {
            if (object instanceof Backbone.Collection)  {
                return object[keypath];
            } else if (object instanceof Backbone.Model) {
                return object.get(keypath);
            }
            return object[keypath];
        },

        publish: function(object, keypath, value) {
            if (object instanceof Backbone.Collection) {
                object[keypath] = value;
            } else if (object instanceof Backbone.Model) {
                object.set(keypath, value);
            } else {
                object[keypath] = value;
            }
        }
    }
});

rivets.binders.error = function(el, value) {
    if (value){
        $(el).fadeOut(function(){
            $(el).html(value);
            $(el).fadeIn();
        });
    } else {
        $(el).fadeOut();
    }
};