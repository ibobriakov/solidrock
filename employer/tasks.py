import datetime
from celery import task
from models import Job

@task
def rotate_jobs():
    Job.objects.approved().filter(end_date__lte=datetime.datetime.now().date)\
                          .update(approved=False,archived=True)
