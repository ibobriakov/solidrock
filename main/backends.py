__author__ = 'ir4y'


class PermissionBackend(object):
    def has_perm(self, user, perm, obj):
        if perm == 'userprofile.change_employer':
            return obj.user == user
        elif perm == 'userprofile.change_jobseekerinformation':
            return obj.job_seeker == user.profile
        return False