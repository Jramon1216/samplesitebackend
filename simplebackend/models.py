from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=100, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)