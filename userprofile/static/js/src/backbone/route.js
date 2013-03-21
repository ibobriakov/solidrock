/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 20.03.13
 * Time: 22:59
 * To change this template use File | Settings | File Templates.
 */
var SectionRoute = Backbone.Router.extend({
    routes: {
        "section/:query": "change_section",
        "section":"change_section"
    },
    show_section: function(section) {
        $('.sections_text li').removeClass('active');
        $('.sections_tab li').removeClass('active');
        $('.sections_form .page').attr('style','display:none');
        $('.sections_text .section'+section).addClass('active');
        $('.sections_tab .section'+section).addClass('active');
        $('.sections_form .section'+section).attr('style','display:block');
    },
    change_section: function(section){
        section = section || 1;
        this.show_section(section);
        window.scrollTo(0,$('#section_top').offset().top);
    }


});

var section_route = new SectionRoute();