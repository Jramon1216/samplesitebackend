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
            messages = Message.objects.values('message') # Get all messages (specifically the message value from the db)
            if messages.exists(): 
                msg_list = [m['message'] for m in messages] 
                length = len(msg_list)
                random_message = msg_list[random.randint(0,length-1)] # Get a random message from the list of messages
                return Response({'RECEIVED MESSAGE': f'{random_message}'}, status=status.HTTP_200_OK)  # Return message response
            else:
                return Response({"EMPTY": "There are no messages to receive"}, status=status.HTTP_204_NO_CONTENT) 
        except Exception as e:
            return Response({'ERROR': f'Something went wrong! Please Try again later - {str(e)}'}, status=status.HTTP_400_BAD_REQUEST) # Something is wrong, raise exception
    return Response({'ERROR': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@csrf_exempt
@api_view(['POST'])
def send_message(request):
    if request.method == 'POST':
        try:
            serializer = MessageSerializer(data=request.data) # Serialize data (parse data)
            if serializer.is_valid():
                serializer.save() # Save record into DB
                return Response({'SUCCESS':'Message sent!'}, status=status.HTTP_201_CREATED) # Success message
            else:
                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Bad data, respond with serialzier error
        except Exception as e:
            return Response({'ERROR': f'Something went wrong! Please Try again later - {str(e)}'}, status=status.HTTP_400_BAD_REQUEST) # Something is wrong, raise exception
    return Response({'ERROR': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
