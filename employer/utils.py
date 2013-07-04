import datetime
from models import Job

def rotate_jobs():
    Job.objects.approved().filter(end_date__lte=datetime.datetime.now().date)\
                          .update(approved=False,archived=True)
