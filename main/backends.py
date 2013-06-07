from email_auth.backends import EmailBackend

__author__ = 'ir4y'


class EmailWithPermissionBackend(EmailBackend):
    def has_perm(self, user, perm, obj=None):
        if obj is None:
            return False
        if perm == 'userprofile.change_employer':
            return obj.user == user
        elif perm in ('userprofile.change_jobseekerinformation',
                      'userprofile.change_jobseekercurrentemployment',):
            return obj.job_seeker == user.profile
        elif perm in ('userprofile.change_jobseekerpreviousemployment',
                      'userprofile.change_jobseekereducation',
                      'userprofile.change_jobseekerreferee',):
            return obj.job_seeker == user.profile
        elif perm in ('userprofile.add_jobseekerpreviousemployment',
                      'userprofile.add_jobseekereducation',
                      'userprofile.add_jobseekerreferee',):
            return True
        elif perm in ('resume.change_resumeitem', 'cover_letter.change_coverletteritem',):
            return obj.paper.owner == user
        elif perm in ('resume.change_resume', 'cover_letter.change_coverletter',):
            return obj.owner == user
        elif perm in ('resume.add_resumeitem', 'cover_letter.add_coverletteritem'):
            return True
        elif perm in ('resume.delete_resumeitem', 'cover_letter.delete_coverletteritem'):
            return True
        elif perm in ('employer.change_job',):
            return obj.owner == user
        elif perm in ('employer.add_job',):
            return True
        elif perm in ('employer.change_desireable', 'employer.change_essential', 'employer.delete_jobuploaddocument',
                      'employer.change_jobselectedcategory', 'employer.change_jobselectedsubcategory',
                      'employer.add_jobselectedcategory', 'employer.add_jobselectedsubcategory',
                      'employer.delete_jobselectedcategory', 'employer.delete_jobselectedsubcategory',
                      'employer.delete_desireable', 'employer.delete_essential' ):
            return obj.job.owner == user
        elif perm in ('employer.add_desireable', 'employer.add_essential',):
            return True
        elif perm == 'contactus.add_feedback':
            return True
        elif perm == 'job_seeker.change_applytojob':
            return obj.paper.owner == user
        elif perm == 'job_seeker.add_applytojob':
            return True
        return False
