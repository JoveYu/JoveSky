#!/usr/bin/env python
# −*− coding: UTF−8 −*−
#
# Author:   Jove Yu <yushijun110@gmail.com>

from django.conf.urls import patterns, include, url
from feeds import LatestPostFeed
from sitemap import PostSitemap

urlpatterns = patterns('blog.views',
    url(r'^$','index' ,name='blog_index'),
    url(r'^post/(?P<postid>\d+)/(?P<postname>[-\w\./\s]+)/$', 'show_post', name='blog_post'),
    url(r'^tag/(?P<tagname>.+)/$', 'show_tag', name='blog_tag'),
    url(r'^category/(?P<categoryname>.+)/$', 'show_category', name='blog_category'),
    url(r'^archives/$', 'archives', name='blog_archives'),
    url(r'^feed/$', LatestPostFeed(), name='blog_feed'),

)

sitemaps = {
    'Post': PostSitemap,
}
urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

)
urlpatterns += patterns('blog.views',
    url(r'^(?P<pagename>[-\w\./\s]*)/$', 'show_page', name='blog_page'),
)

