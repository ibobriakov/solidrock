/**
 * User: jackdevil
 */

var update_view = {};
_.extend(update_view, Backbone.Events);

function paper_model_factory (paper_type,paper,button){
    return Backbone.Model.extend({
        defaults: { "type": "text", "value": "" },
        urlRoot: rest_url[paper_type].list_endpoint,
        url: function(){
            if (this.id){
                return this.urlRoot + this.id + '/';
            } else {
                return this.urlRoot;
            }
        },
        urlParent: rest_url[paper_type].list_endpoint+'?parent=',
        type: paper_type,
        paper: paper,
        template: _.template($("#paper_model").html()),
        html: function(level){
            level = level | 0;
            return this.template({'model':this, 'level':level, 'button':button});
        },
        initialize: function(){
            this.bind('change:pk', function(){
                this.save({},{'wait':true});
            });
            this.bind('change:value', function(){
                this.save({},{'wait':true});
            });
            this.bind('sync', function(){
                if (this.get('type') == 'container' && !this.get('children')) {
                    var container_objects = this.get_objects_list(this.get('id'));
                    var container_tree = this.generate_tree(container_objects);
                    this.set('children',container_tree);
                    update_view.trigger('update_view', 'models_sync')
                }
            });
        },
        get_objects_list: function(id) {
            var objects = false;
            id = id || this.id;
            $.ajax({
                url: this.urlParent+id,
                async: false,
                success: function(data) {
                    objects = data.objects;
                }
            });
            return objects;
        },
        generate_tree: function(objects){
            var collection = new (paper_collection_factory(this.type,this.paper))();
            for (var i=0; i < objects.length; i++) {
                if (objects[i].type.split('_')[1] == 'list' || objects[i].type == 'container'){
                    var model = new (paper_model_factory(this.type,this.paper))(objects[i]);
                    var container_objects = this.get_objects_list(model.get('id'));
                    var container_tree = this.generate_tree(container_objects);
                    model.set('children',container_tree);
                    collection.add(model);
                } else {
                    collection.add(objects[i]);
                }
            }
            return collection;
        }
    });
}