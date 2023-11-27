from __future__ import absolute_import, print_function
import os
import sys
import time

from celery import Celery
from celery._state import _set_current_app

result_backend = 'rpc://'
#task_time_limit = 600
worker_max_memory_per_child = 2048000  #2GB

USER='rb_user'
PASSWD='rb_passwd'
VHOST='rb_vhost'

broker_url = [f'pyamqp://{USER}:{PASSWD}@localhost/{VHOST}']

app = Celery('test_celery',backend='amqp',broker=broker_url,include=['test_celery.tasks'])


