from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path('process', views.process_form, name='process'),
    path('delete', views.remove, name='delete')
]
