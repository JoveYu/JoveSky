from pagedown.widgets import AdminPagedownWidget
from django import forms
from blog.models import Post,Page

class PostForm(forms.ModelForm):
    markdown = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post

class PageForm(forms.ModelForm):
    markdown = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Page
