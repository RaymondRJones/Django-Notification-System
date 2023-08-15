from django.urls import path
from . import views

urlpatterns = [
    path('send_notification_to_one_user/', views.send_notification_to_one_user, name='send_notification_to_one_user'),
    path('create_new_user/', views.create_new_user, name='create_new_user'),
    path('add_loyalty_points/', views.add_loyalty_points, name='add_loyalty_points'),
]