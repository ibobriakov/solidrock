/**
 * Created with PyCharm.
 * User: jackdevil
 * Date: 17.03.13
 * Time: 12:47
 * To change this template use File | Settings | File Templates.
 */

var login_view = new (form_view_fabric('login'))({el:$('#login_form')});
login_view.render();

var job_seeker_registration_view = new (form_view_fabric('job_seeker_registration'))({el:$('#register_job_seeker_form')});
job_seeker_registration_view.render();

var employer_registration_view = new (form_view_fabric('employer_registration'))({el:$('#register_employer_form')});
employer_registration_view.render();