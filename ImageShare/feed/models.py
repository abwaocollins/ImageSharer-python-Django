from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.base import Model
from sorl.thumbnail import ImageField
from django.conf import settings


# Create your models here.

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, null='True', on_delete=models.SET_NULL)
    title = models.CharField(max_length=140, null="False", blank="False")
    author = models.CharField(max_length=100, null="False", blank="False")
    description = models.CharField(max_length=250, blank="False")
    image = ImageField()
    date_created = models.TimeField(auto_now_add="True")

    def __str__(self):
        return self.title
