from django.urls import path
from . import views


urlpatterns = [
    path('',views.test,name='test'),
    path('send_mail',views.send_mail_to_all,name='send_mail'),
    path('schedule_mail',views.schedule_mail,name='schedule_mail')
]