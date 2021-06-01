from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_wall),
    path('new_message', views.new_message),
    path('new_comment', views.new_comment),
]