from django.db import models
from board.models import Board
from post.models import PostStudy,PostAlbum,PostFree,PostJokbo
import time


def makefilename(instance, filename):
    return str(time.time()) + '_' + filename


# File Field 참고 URL : https://cjh5414.github.io/django-file-upload/
class FileFree(models.Model):
    boardId = models.ForeignKey(Board, on_delete=models.CASCADE)
    postIdx = models.ForeignKey(PostFree, on_delete=models.CASCADE)
    file = models.FileField(upload_to=makefilename)


class FileAlbum(models.Model):
    boardId = models.ForeignKey(Board, on_delete=models.CASCADE)
    postIdx = models.ForeignKey(PostAlbum, on_delete=models.CASCADE)
    file = models.FileField(upload_to=makefilename)


class FileJokbo(models.Model):
    boardId = models.ForeignKey(Board, on_delete=models.CASCADE)
    postIdx = models.ForeignKey(PostJokbo, on_delete=models.CASCADE)
    file = models.FileField(upload_to=makefilename)


class FileStudy(models.Model):
    boardId = models.ForeignKey(Board, on_delete=models.CASCADE)
    postIdx = models.ForeignKey(PostStudy, on_delete=models.CASCADE)
    file = models.FileField(upload_to=makefilename)
