from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    stuNo = models.IntegerField(default=0)
    phoneNo = models.IntegerField(default=0)
    lastVisited = models.DateTimeField('date last visited')
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.name



