from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt

from .models import Message
from .serializers import MessageSerializer


@csrf_exempt
@api_view(['GET'])
def receive_message(request):
    return Response({'this method': 'works'}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def send_message(request):
    if request.method == 'POST':
        try:
            serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success':'Message sent!'}, status=status.HTTP_201_CREATED)
            else:
                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'ERROR': 'Something went wrong! Please Try again later'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
