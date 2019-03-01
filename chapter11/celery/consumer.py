#!/usr/bin/python3

from producer import task_execution

while True:
    message = input('Enter Mensaje> ')
    task_execution.delay(message)