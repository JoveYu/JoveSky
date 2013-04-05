#!/usr/bin/env python
# −*− coding: UTF−8 −*−
#
# Author:   Jove Yu <yushijun110@gmail.com>
from django.http import Http404, HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from blog.models import Post, Page ,Link

import utils

global_settings={
    'SITE_TITLE':settings.SITE_TITLE,
    'SITE_AUTHOR':settings.SITE_AUTHOR,
    'SITE_DESC':settings.SITE_DESC,
    'SITE_SUBTITLE':settings.SITE_SUBTITLE,
    'SITE_URL':settings.SITE_URL,
}
global_sidebar={
    'recposts':utils.recent_post(Post),
    'links':Link.objects.all(),
    'pages':Page.objects.all(),
}
def index(request):
    '''首页及分页'''
    try:
        page =int(request.GET.get('page','1'))
    except ValueError:
        page=1

    c={
        'posts':utils.get_page(Post.objects.all(),page),
        'settings':global_settings,
        'no_sidebar':False,
    }
    c.update(global_sidebar)
    
    return render_to_response('index.html',c,
                context_instance=RequestContext(request))

def show_post(request, postid):
    '''查看文章'''
    try:
        post = Post.objects.select_related().get(id=int(postid))
    except:
        raise Http404

    post.counts += 1
    post.save()
    tags = post.tags.all()
    
    c={
        'settings':global_settings,
        'page': post,
        'footer': True,
        'sharing': True,
        'comments': True,
        'tags': tags,
        'keywords': ','.join([i.name for i in tags]),
    }
    c.update(global_sidebar)
    return render_to_response('page.html', c
                , context_instance=RequestContext(request))

def show_page(request, pagename):
    '''查看文章'''
    try:
        post = Page.objects.select_related().get(slug=pagename)
    except:
        raise Http404

    c={
        'settings':global_settings,
        'page': post,
        'footer': True,
        'sharing': False,
        'comments': True,
    }
    c.update(global_sidebar)
    return render_to_response('page.html', c
                , context_instance=RequestContext(request))

def show_tag(request, tagname):
    '''按标签查看'''
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    c={
       'settings':global_settings,
       'title': tagname + ' - Tag',
       'no_sidebar':False,
       'posts': utils.get_page(Post.objects.filter(tags__name=tagname), page),
    }
    c.update(global_sidebar)
    return render_to_response('index.html', c
                , context_instance=RequestContext(request))
    
def archives(request):
    '''归档页面'''
    posts = [Post(**i) for i in Post.objects.values('id', 'title', 'create_time', 'slug')]
    page = {
        'title': 'Blog Archive',
    }

    c= {
        'settings':global_settings,
        'posts': posts,
        'page': page,
        'no_sidebar':False,
    }
    c.update(global_sidebar)
    return render_to_response('archives.html',c
                , context_instance=RequestContext(request))
    
