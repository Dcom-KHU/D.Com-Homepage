from django.db import models

# Create your models here.


class Board(models.Model):
    boardId = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    skin = models.CharField(max_length=10)

    def __str__(self):
        return self.name

