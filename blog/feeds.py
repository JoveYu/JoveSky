# -*- coding: utf-8 -*-
"""
File: feeds.py
Author: Jove Yu
Email: yushijun110@gmail.com
Github: https://github.com/JoveYu
Description: feed for blog app
"""

from models import Post
from django.conf import settings
from django.contrib.syndication.views import Feed

class LatestPostFeed(Feed):
    title = getattr(settings,'SITE_TITLE','JoveSky')
    description  = getattr(settings,'SITE_DESC','Blog for Jove')
    link = '/'

    def items(self):
        return Post.objects.all()[:settings.FEED_COUNT]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
