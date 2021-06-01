from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_wall),
    path('new_message', views.new_message),
    path('new_comment/<int:id>', views.new_comment),
    path('edit/<int:id>', views.edit_comment),
    path('delete/<int:id>', views.delete_comment),
]