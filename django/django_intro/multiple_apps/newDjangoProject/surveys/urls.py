from django.urls import path
from . import views


urlpatterns = [
    path('', views.survey),
    path('new', views.new)
]