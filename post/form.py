from django import forms
from post.models import PostNotice, PostShare, PostFree, PostJokbo, PostStudy
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostNoticeForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = PostNotice
        fields = ['tag', 'title', 'content']


class PostShareForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = PostShare
        fields = ['tag', 'title', 'content']


class PostFreeForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = PostFree
        fields = ['title', 'content']


class PostJokboForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = PostJokbo
        fields = ['tag', 'title', 'content']


class PostStudyForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = PostStudy
        fields = ['tag', 'title', 'content']


class CommentForm(forms.Form):
    comment = forms.CharField(widget=CKEditorUploadingWidget)

