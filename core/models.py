from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USER_TYPES = [
        ('T' , 'Teacher'),
        ('S', 'Student')
    ]
    email = models.EmailField()
    phone = models.CharField(max_length=12)  # 251 9 55 35  64 43
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    
    def __str__(self):
        return self.username
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"