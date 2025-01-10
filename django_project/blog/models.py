from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # can use auto_now=True or auto_now_add = True (but cant change time later)
    date_posted = models.DateTimeField(default=timezone.now)
    # if user is delete all its post going to be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #to print particular attribute of post model
    def __str__(self):
        return self.title

