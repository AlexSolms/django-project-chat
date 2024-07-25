from django.db import models
from datetime import date
from django.conf import settings

# Create your models here.

class Chat(models.Model):
    created_at = models.DateField(default=date.today)
    
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
    author = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)