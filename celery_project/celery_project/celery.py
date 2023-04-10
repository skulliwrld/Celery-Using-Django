from __future__ import absolute_import,unicode_literals
import os


from celery import Celery
from celery.schedules import crontab
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')


app = Celery('celery_project')
app.conf.enable_utc = False

app.config_from_object(settings,namespace='CELERY')

app.conf.beat_schedule ={
    'send_mail_every_hour':{
    'task':'Email_app.task.send_mail_fun',
    'schedule': crontab(hour=7, minute=4),
    #'args':
    }
    
}

#Celery Beats

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')