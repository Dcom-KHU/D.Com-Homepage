from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.Form):
    content = forms.CharField(widget=CKEditorUploadingWidget, label='')

