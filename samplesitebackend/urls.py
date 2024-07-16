from django.contrib import admin
from django.urls import path
from simplebackend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receive/', views.receive_message, name='receive'),
    path('send/', views.send_message, name="send" ),
]
