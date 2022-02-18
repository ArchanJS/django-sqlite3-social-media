from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=14)

class Post(models.Model):
    postedBy=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    postTitle=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    def __str__(self):
        return self.postTitle
    