from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from user.models import User
from dcomhomepage.utils import extractImage, extractText
# Create your models here.


class PostFree(models.Model):
    title = models.CharField(max_length=50, blank=True, default='Comments')
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    depth = models.IntegerField(default=0)


class PostAlbum(models.Model):
    title = models.CharField(max_length=50, blank=True, default='Comments')
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    depth = models.IntegerField(default=0)


class PostJokbo(models.Model):
    title = models.CharField(max_length=50, blank=True, default='Comments')
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    depth = models.IntegerField(default=0)


class PostStudy(models.Model):
    TAGS = (
        ('교과', '교과'),
        ('데이터', '데이터'),
        ('프론트', '프론트'),
        ('백', '백'),
        ('기타', '기타')
    )

    title = models.CharField(max_length=50, blank=True, default='Comments')
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    startDate = models.DateField('date study started')
    endDate = models.DateField('date study ended')
    tag = models.CharField(max_length=10, choices=TAGS, default='공지')
    depth = models.IntegerField(default=0)

    def __str__(self):
        return self.writer + ': ' + self.title


class PostStudyMember(models.Model):
    studyIdx = models.ForeignKey(PostStudy, on_delete=models.CASCADE)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)


class PostNotice(models.Model):
    TAGS = (
        ('공지', '공지'),
        ('행사', '행사'),
        ('대회', '대회'),
        ('프젝', '프젝'),
        ('기타', '기타'),
    )

    # blank=True : Form 사용 시 입력 안해도 오류 X
    # null=True : Foreign Key가 null 값을 가져도 되게 함
    title = models.CharField(max_length=50, blank=True, default='Comments')
    content = RichTextUploadingField()
    writer = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    tag = models.CharField(max_length=10, choices=TAGS, default='공지')
    depth = models.IntegerField(default=0)
    imageLink = models.CharField(max_length=200, default='', blank=True)
    summary = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.writer + ': ' + self.title

    def save(self, *args, **kwargs):
        exImage = extractImage(self.content)
        if exImage is not None:
            self.imageLink = exImage
        self.summary = extractText(self.content)
        super().save(*args, **kwargs)

