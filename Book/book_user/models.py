from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Book_user(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "图书用户"
        db_table = 'Book_user'