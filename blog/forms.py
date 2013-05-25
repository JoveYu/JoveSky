# -*- coding: utf-8 -*-
"""
File: forms.py
Author: Jove Yu
Email: yushijun110@gmail.com
Github: https://github.com/JoveYu
Description: forms for blog app
"""

from pagedown.widgets import AdminPagedownWidget
from django import forms
from models import Post,Page

class PostForm(forms.ModelForm):
    markdown = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post

class PageForm(forms.ModelForm):
    markdown = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Page
