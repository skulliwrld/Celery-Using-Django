from celery import shared_task
name_list = ['joseph','jonathan',"joshua"]
@shared_task(bind=True)
def task_loader(self):
    #Any operation
    for i in name_list:
        return i