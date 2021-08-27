from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Conversation(models.Model):
    title = models.CharField(max_length=100 , null=True)
    member = models.ManyToManyField(User)
    def __str__(self):
        return self.title

    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null = True)
    message_text = models.TextField()
    
class UserStatus(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField()
    
    

    
    
    
    