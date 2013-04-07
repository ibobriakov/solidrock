/**
 * User: jackdevil
 */

function get_nested(object, keypath) {
    var nested_list = keypath.split('.');
    for (var i=0; i<nested_list.length-1; i++){
        object = object[nested_list[i]]
    }
    return {object:object, keypath:nested_list[nested_list.length-1]}
}

rivets.configure({
    adapter: {
        subscribe: function(object, keypath, callback) {
            var nested_item = get_nested(object,keypath);
            object = nested_item.object;
            keypath = nested_item.keypath;
            if (object instanceof Backbone.Collection) {
                object.on('add remove reset', function (){ callback(object[keypath]) });
            } else if (object instanceof Backbone.Model) {
                object.on('change:'+keypath, function(m,v){ callback(v) });
            }
        },

        unsubscribe: function(object, keypath, callback) {
            var nested_item = get_nested(object,keypath);
            object = nested_item.object;
            keypath = nested_item.keypath;
            if (object instanceof Backbone.Collection) {
                object.off('add remove reset', function (){ callback(object[keypath]) });
            } else if (object instanceof Backbone.Model) {
                object.off('change:'+keypath, function(m,v){ callback(v) });
            }
        },

        read: function(object, keypath) {
            var nested_item = get_nested(object,keypath);
            object = nested_item.object;
            keypath = nested_item.keypath;
            if (object instanceof Backbone.Collection)  {
                return object[keypath];
            } else if (object instanceof Backbone.Model) {
                return object.get(keypath);
            }
            return object[keypath];
        },

        publish: function(object, keypath, value) {
            var nested_item = get_nested(object,keypath);
            object = nested_item.object;
            keypath = nested_item.keypath;
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