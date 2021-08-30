from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey

class Conversation(models.Model):
    title = models.CharField(max_length=100 , null=True)
    member = models.ManyToManyField(User)
    def __str__(self):
        return self.title
    
    def get_last_message(self):
        return self.message_set.last().message_text
    
class Reaction(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')  
    name = models.CharField(max_length=100)
    text =  models.TextField()
    reactor = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    def __str__(self):
        return self.name
    @property
    def source(self):
        return self.content_object

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null = True)
    message_text = models.TextField()
    reaction = GenericRelation(Reaction, related_query_name='message')
    
class UserStatus(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField()
   
class Reply(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    reply_text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    reaction = GenericRelation(Reaction, related_query_name='reply')
    