from django import template
from employer.models import Job
from job_seeker.templatetags.job_seeker_information import any_not_None
from main.utils import get_model_values


__author__ = 'ir4y'


register = template.Library()


def all_not_None(l):
    return all(map(lambda u: u is not None and u != '', l))


@register.filter()
def section1_complete(job):
    return all_not_None(get_model_values(job, fileds=Job.REQUIRED_FIELDS))


@register.filter()
def section2_complete(job):
    return any(map(lambda u: any_not_None(get_model_values(u)),
                   job.jobuploaddocument_set.all()))


@register.filter()
def section3_complete(job):
    return False
