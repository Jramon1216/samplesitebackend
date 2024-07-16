from django.shortcuts import render
from django.http import HttpResponse

from .models import Message

def receive_message(request):
    msg = Message.objects.first()
    return HttpResponse(msg)

def send_message(request):
    return HttpResponse("This endpoint also works!")

