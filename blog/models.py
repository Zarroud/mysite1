from django.db import models
from datetime import datetime 
from django.utils.timezone import now
from django.contrib.auth.models import User

class Post(models.Model) :
    publisher=models.ForeignKey(User, related_name='publisher', verbose_name='Publisher')
    title=models.CharField(max_length=140)
    body=models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self) :
        return self.title
