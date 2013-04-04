from celery import task
from haystack.management.commands import update_index as update_index_commant

__author__ = 'ir4y'

@task
def update_index():
    update_index_commant.Command().handle()
