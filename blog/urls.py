from django.conf.urls import patterns, include, url
from blog.feeds import LatestPostFeed

urlpatterns = patterns('blog.views',
    url(r'^$','index' ,name='blog_index'),
    url(r'^post/(?P<postid>\d+)/(?P<postname>[-\w]+)/', 'show_post', name='blog_post'),
    url(r'^tag/(?P<tagname>.+)/$', 'show_tag', name='blog_tag'),
    url(r'^archives/$', 'archives', name='blog_archives'),
    url(r'^feed/$', LatestPostFeed(), name='blog_feed'),
    
    url(r'^(?P<pagename>\w+)/', 'show_page', name='blog_page'),
)
