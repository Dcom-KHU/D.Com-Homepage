from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=CKEditorUploadingWidget)

