from django.urls import path
from . import views

urlpatterns = [
    path('send_notification_to_one_user/', views.send_notification_to_one_user, name='send_notification_to_one_user'),
]