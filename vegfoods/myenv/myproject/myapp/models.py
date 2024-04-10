from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.fname
        