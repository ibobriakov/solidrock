from celery import task

__author__ = 'ir4y'

@task
def send_activation_email(registration_profile, site):
    registration_profile.send_activation_email(site)
