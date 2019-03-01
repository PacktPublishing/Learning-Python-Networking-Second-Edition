#!/usr/bin/python3

from celery import Celery
from time import sleep

app = Celery('celery_tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')
			 
@app.task
def task_execution(message):
    sleep(5)
    print('Message received: %s' % message)