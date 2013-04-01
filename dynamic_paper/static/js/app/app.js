/**
 * User: jackdevil
**/

var App = new Marionette.Application();

App.addRegions({
    "mainRegion": "#main"
});

App.module("SampleModule", function(Mod, App, Backbone, Marionette, $, _){
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

App.start();