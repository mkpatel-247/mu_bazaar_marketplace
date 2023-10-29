from django.db import models
from datetime import datetime
import uuid
from django.db import models
from accounts.models import User
from listings.models import ads

# Create your models here.
class Conversation(models.Model):
    ads = models.ForeignKey(ads, related_name='conversations', on_delete=models.CASCADE)
    user_members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

class ConversationsMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)