from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt

from .models import Message
from .serializers import MessageSerializer

import random

@csrf_exempt
@api_view(['GET'])
def receive_message(request):
    if request.method == 'GET':
        try:
            messages = Message.objects.values('message')
            if messages.exists():
                msg_list = [m['message'] for m in messages]
                length = len(msg_list)
                random_message = msg_list[random.randint(0,length-1)]
                return Response({'RECEIVED MESSAGE': f'{random_message}'}, status=status.HTTP_200_OK) 
            else:
                return Response({"EMPTY": "There are no messages to receive"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'ERROR': f'Something went wrong! Please Try again later - {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'ERROR': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['POST'])
def send_message(request):
    if request.method == 'POST':
        try:
            serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'SUCCESS':'Message sent!'}, status=status.HTTP_201_CREATED)
            else:
                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'ERROR': f'Something went wrong! Please Try again later - {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'ERROR': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
