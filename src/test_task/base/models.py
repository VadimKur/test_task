from django.db import models

# Create your models here.
class Message(models.Model):
    author_email = models.CharField(max_length=30, default='user@email.ru', name='емэйл автора сообщения')
    text = models.TextField(null=True, blank=True, name='текст сообщения')