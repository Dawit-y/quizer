from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
   
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.first_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', "last_name", "username"]

       