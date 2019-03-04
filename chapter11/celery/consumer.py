#!/usr/bin/python3

from producer import task_execution

while True:
    message = input('Enter Message> ')
    task_execution.delay(message)