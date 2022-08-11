from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('name=<str:name> message=<str:message>', views.test, name='test')
]
