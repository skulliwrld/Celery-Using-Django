from django.shortcuts import render,HttpResponse
from .task import task_loader
from Email_app.task import send_mail_fun
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json
# Create your views here.

def test(request):
    task_loader.delay()
    return HttpResponse('Done')


def send_mail_to_all(request):
    send_mail_fun.delay()
    return HttpResponse('sent')

#Creating a dynamic scheduler for celery
def schedule_mail(request):
    schedule, created= CrontabSchedule.objects.get_or_create(hour=11,minute=2)
    task = PeriodicTask.objects.create(crontab=schedule, name='shedule_mail_task'+ '3',task='Email_app.task.send_mail_fun')
    return HttpResponse('Done')


