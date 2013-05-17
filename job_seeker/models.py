from django.core.exceptions import ValidationError
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.template import loader, Context
from django.conf import settings


class ApplyToJob(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    job_seeker = models.ForeignKey('auth.User')
    job = models.ForeignKey('employer.Job')
    resume = models.ForeignKey('resume.Resume', verbose_name="Select resume", blank=True, null=True)
    cover_letter = models.ForeignKey('cover_letter.CoverLetter',
                                     verbose_name="Select cover letter", blank=True, null=True)

    def __unicode__(self):
        return "User {0} applied for job {1}".format(self.job_seeker, self.job)

    def save(self, **kwargs):
        if self.job_seeker.user_type != 0:  # Job Seeker
            raise ValidationError("User should be Job Seeker")
        return super(ApplyToJob, self).save(**kwargs)

    class Meta:
        unique_together = ('job_seeker', 'job',)


def email_notify(instance, created, **kwargs):
    if created:
        template = loader.get_template("email/apply_to_job.txt")
        site = Site.objects.get_current()
        email_text = template.render(Context({'protocol': 'http',
                                              'domain': site.domain,
                                              'employer': instance.job.owner,
                                              'job': instance.job}))
        send_mail('Solid Rock - Some one applied to your job!',
                  email_text, settings.EMAIL_HOST_USER, [instance.job.owner.email])

post_save.connect(email_notify,ApplyToJob)