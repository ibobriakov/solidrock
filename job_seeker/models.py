from django.core.exceptions import ValidationError
from django.db import models


class ApplyToJob(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    job_seek = models.ForeignKey('auth.User')
    job = models.ForeignKey('employer.Job')

    def __unicode__(self):
        return "User {0} applied for job {1}".format(self.job_seek, self.job)

    def save(self, **kwargs):
        if self.job_seek.user_type != 0:  # Job Seeker
            raise ValidationError("User should be Job Seeker")
        return super(ApplyToJob, self).save(**kwargs)

    class Meta:
        unique_together = ('job_seek', 'job',)