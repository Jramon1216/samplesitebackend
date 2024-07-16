from django.shortcuts import render
from django.http import HttpResponse

from.models import Message

def receive_message(request):
    return HttpResponse("this endpoint works!")

def send_message(request):
    return HttpResponse("This endpoint also works!")

