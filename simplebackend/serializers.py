from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    user_message = serializers.CharField(source='message', max_length=100) 

    class Meta:
        model = Message
        fields = ['user_message']