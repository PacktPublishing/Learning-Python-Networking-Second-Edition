#!/usr/bin/python3

# Celery full example: publisher/subscriber
from celery import Celery

# Redis
app = Celery('demo_celery', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


@app.task
def task_execution(message,count):
	array=[]
	print('Message received: %s' % message)
	for index in range(0,int(count)):
		array.append(message)
	return (array)

def main():
	while True:
		message = input('Enter Message> ')
		count = input('Enter times appears the message> ')
		promise = task_execution.delay(message,count)

if __name__ == '__main__':
    main()