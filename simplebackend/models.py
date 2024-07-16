from django.db import models

class Message(models.Model):
    messageid = models.IntegerField(primary_key=True, null=False)
    message = models.CharField(max_length=100, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)