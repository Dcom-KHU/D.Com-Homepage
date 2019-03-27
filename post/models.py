from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from user.models import User
# Create your models here.


class PostFree(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.CharField(max_length=20, default=None)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.CharField(max_length=20)
    link = models.CharField(max_length=50)


class PostAlbum(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.CharField(max_length=20, default=None)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.CharField(max_length=20)
    link = models.CharField(max_length=50)


class PostJokbo(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.CharField(max_length=20, default=None)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.CharField(max_length=20)
    link = models.CharField(max_length=50)


class PostStudy(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.CharField(max_length=20, default=None)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    startDate = models.DateField('date study started')
    endDate = models.DateField('date study ended')


class PostStudyMember(models.Model):
    studyIdx = models.ForeignKey(PostStudy, on_delete=models.CASCADE)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)


class PostNotice(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.CharField(max_length=20, default=None)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    tag = models.CharField(max_length=10)
