/**
 * Create user: jackdevil
 */

function form_model_fabric(type,attributes) {
    var Model = Backbone.Model.extend({
        urlRoot: url_resolver[type],
        types: attributes.types,
        titles: attributes.titles,
        initialize: function() {
            this.bind('change',function(){
                console.log(this);
            })
        },
        validate: function(){
//            var attr = this.attributes, keys = _.keys(attr);
//            for (var i = 0; i < keys.length; i++){
//                switch (this.types[keys[i]]) {
//                    case 'email':
//                        var mail = new RegExp('^\S+\@\S+\.\S+$', 'i');
//                        mail.exec(attr[keys[i]]);
//                        if (!mail.lastIndex) {
//                            console.log('Incorrect email ' + attr[keys[i]]);
//                            return true;
//                        }
//                        break;
//                    case 'hidden':
//                        continue;
//                    default :
//                        if (!attr[keys[i]]) {
//                            console.log('Blank filed '+keys[i]);
//                            return true;
//                        }
//                }
//            }
            return false;
        }
    });
    return new Model(attributes.fields);
}