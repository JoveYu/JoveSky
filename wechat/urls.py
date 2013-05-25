# -*- coding: utf-8 -*-
"""
File: urls.py
Author: Jove Yu
Email: yushijun110@gmail.com
Github: https://github.com/JoveYu
Description: url for wechat app
"""
from django.conf.urls import patterns, include, url

urlpatterns=patterns('',
    url(r'^$','wechat.views.index'),

)


