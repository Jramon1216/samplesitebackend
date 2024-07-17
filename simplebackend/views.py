from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt

from .models import Message



def receive_message(request):
    messages = Message.objects.all().values('message')
    all_messages = [message for message in messages]
    return HttpResponse(all_messages)

@csrf_exempt
@api_view(['POST'])
def send_message(request):
    if request.method == 'POST':
        data = {
            'message': 'this is a message from json'
        }

        message = data.get('message')

        new_message = Message(message)
        new_message.save()
        return Response({'message':'Message sent!'}, status=status.HTTP_201_CREATED)
