from epiceditor.widgets import AdminEpicEditorWidget
from django import forms
from models import Post,Page

class PostForm(forms.ModelForm):
    markdown = forms.CharField(widget=AdminEpicEditorWidget())

    class Meta:
        model = Post

class PageForm(forms.ModelForm):
    markdown = forms.CharField(widget=AdminEpicEditorWidget())

    class Meta:
        model = Page
