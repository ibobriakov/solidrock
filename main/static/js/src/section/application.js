/**
 * User: jackdevil
 */

var Section = new Marionette.Application();

App.module("Default", function(Mod, App, Backbone, Marionette, $, _){
    var SectionModel = Backbone.Model.extend({
        url: function() {
            if (!this.urlRoot) return false;
            if (this.id) {
                return this.urlRoot + this.id + '/';
            } else {
                return this.urlRoot;
            }
        },
        commit: function() {
            this.save();
        }
    });
});

App.module("Multi", function(Mod, App, Backbone, Marionette, $, _){
    var MainView = Marionette.ItemView.extend({
        template: "#sample-template"
    });
    var Controller = Marionette.Controller.extend({
        initialize: function(options){
            this.region = options.region
        },
        show: function(){
            var model = new Backbone.Model({
                contentPlacement: "here"
            });
            var view = new MainView({
                model: model
            });
            this.region.show(view);
        }
    });
    Mod.addInitializer(function(){
        Mod.controller = new Controller({
            region: App.mainRegion
        });
        Mod.controller.show();
    });
});