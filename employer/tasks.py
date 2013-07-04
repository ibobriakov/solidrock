from celery import task
from utils import rotate_jobs as do_rotate_jobs


@task
def rotate_jobs():
    do_rotate_jobs()
