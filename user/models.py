from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    stuNo = models.CharField(max_length=3)
    phoneNum = models.CharField(max_length=20, default='010-0000-0000')
    github = models.URLField()
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}{}'.format(self.stuNo, self.user.first_name, self.user.last_name)




