__author__ = 'ir4y'


class PermissionBackend(object):
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
        return False

    def authenticate(self):
        return False