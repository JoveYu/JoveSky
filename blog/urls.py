from django.conf.urls import patterns, include, url
from blog.feeds import LatestPostFeed

urlpatterns = patterns('blog.views',
    url(r'^$','index'),
    url(r'^post/(?P<postid>\d+)/', 'show_post'),
    url(r'^tag/(?P<tagname>.+)/$', 'show_tag'),
    url(r'^archives/$', 'archives'),
    url(r'^feed/$', LatestPostFeed()),
    
    url(r'^(?P<pagename>\w+)/', 'show_page'),
)
