#!/usr/bin/env python
# −*− coding: UTF−8 −*−
#
# Author:   Jove Yu <yushijun110@gmail.com>
import re
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def get_page(objs, page):
	'''分页'''
	paginator = Paginator(objs, settings.PER_PAGE)

	try:
		ret = paginator.page(page)
	except (EmptyPage, InvalidPage):
		ret = paginator.page(paginator.num_pages)

	return ret

def recent_post(Post, num=settings.RECENT_COUNT, quick=True):
	'''获取最近的num条文章'''
	if quick:
		return [Post(**i) for i in Post.objects.values('id', 'title', 'slug')[:num]]
	return Post.objects.all()[:num]

def is_slug(slug):
	'''slug check'''
	return re.match(r'^[a-z0-9A-Z_\-]+$', slug)
