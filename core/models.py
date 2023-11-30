from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
   
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)  # 251 9 55 35  64 43
    
    def __str__(self):
        return self.username
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

       