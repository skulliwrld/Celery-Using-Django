from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery_project import settings



from celery import shared_task


@shared_task(bind=True)
def send_mail_fun(self):
    users = get_user_model().objects.all()
    for user in users:
        subject = 'Hi! Celery Testing'
        message ="this is a new projects on celery.and am getting all the concept thereof,as well as learning how to send mail"
        email_to =user.email 
        send_mail(subject=subject,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email_to],
                  fail_silently =True,)
    return "Done"