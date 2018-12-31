from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length= 100)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100);
    contact_no = models.CharField(max_length = 20);

    def __str__(self):
        return self.email
    

# Create your models here.
