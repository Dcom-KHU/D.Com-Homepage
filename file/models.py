from django.db import models
from board.models import Board
from post.models import PostStudy,PostAlbum,PostFree,PostJokbo

# Create your models here.
class FileFree(models.Model):
    boardId = models.ForeignKey(Board,on_delete=models.CASCADE)
    postIdx = models.ForeignKey(PostFree,on_delete=models.CASCADE)
    fileName = models.CharField(max_length=50)
    url = models.CharField(max_length=100)


class FileAlbum(models.Model):
    boardId = models.ForeignKey(Board,on_delete=models.CASCADE)
    postIdx = models.ForeignKey(PostAlbum,on_delete=models.CASCADE)
    fileName = models.CharField(max_length=50)
    url = models.CharField(max_length=100)


class FileJokbo(models.Model):
    boardId = models.ForeignKey(Board,on_delete=models.CASCADE)
    postIdx = models.ForeignKey(PostJokbo,on_delete=models.CASCADE)
    fileName = models.CharField(max_length=50)
    url = models.CharField(max_length=100)


class FileStudy(models.Model):
    boardId = models.ForeignKey(Board,on_delete=models.CASCADE)
    postIdx = models.ForeignKey(PostStudy,on_delete=models.CASCADE)
    fileName = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
