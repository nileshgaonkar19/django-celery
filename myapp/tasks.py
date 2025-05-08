# myapp/tasks.py
from celery import shared_task
import time

@shared_task
def add(x, y):
    time.sleep(5)  # Simulate a long process
    return x + y
