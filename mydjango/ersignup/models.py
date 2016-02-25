
from django.db import models


# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=32, default='', blank=False, null=False)
    last_name = models.CharField(max_length=32, default='', blank=True, null=True)
    pan = models.CharField(blank=False, null=False, max_length=10)
    timestamp = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)


    def __str__(self):
        return self.email
