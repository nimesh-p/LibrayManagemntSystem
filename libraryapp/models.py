from django.db import models
from django.contrib.auth.models import AbstractUser
from library.managers import UserManager
# Create your models here.

class User(AbstractUser):

    username = None
    name = models.CharField(max_length=50,null=True,blank=True)
    role = models.CharField(max_length=100, default="Admin")
    email = models.EmailField(max_length=50,null=True,blank=True, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, default="John Doe")
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title