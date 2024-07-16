"""
URL configuration for samplesitebackend project.

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.contrib import admin
from django.urls import path
from simplebackend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receive/', views.receive_message, name='receive'),
    path('send/', views.send_message, name="send" ),
]
