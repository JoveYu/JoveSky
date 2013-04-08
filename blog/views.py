#!/usr/bin/env python
# −*− coding: UTF−8 −*−
#
# Author:   Jove Yu <yushijun110@gmail.com>
from django.http import Http404, HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from blog.models import Post, Page ,Link ,Tag, Category
from django.db.models import Q, Count, Max, Min

import utils

THEME=settings.THEME
MAX_FONT_SIZE = 30
MIN_FONT_SIZE = 12
MINUS_FONT_SIZE = MAX_FONT_SIZE - MIN_FONT_SIZE

global_settings={
    'SITE_TITLE':settings.SITE_TITLE,
    'SITE_AUTHOR':settings.SITE_AUTHOR,
    'SITE_DESC':settings.SITE_DESC,
    'SITE_SUBTITLE':settings.SITE_SUBTITLE,
    'SITE_URL':settings.SITE_URL,
}

def common_response(request):
    tags = Tag.objects.annotate(n_posts=Count("posts"))[:25]
    if tags:
        tag_max_posts = tags.aggregate(Max("n_posts"))['n_posts__max']
        tag_min_posts = tags.aggregate(Min("n_posts"))['n_posts__min']
        for tag in tags:
            if tag_max_posts - tag_min_posts > 0:
                tag.font_size = MIN_FONT_SIZE \
                + MINUS_FONT_SIZE*(tag.n_posts-tag_min_posts)/(tag_max_posts-tag_min_posts)
            else:
                tag.font_size = MINUS_FONT_SIZE

    global_sidebar={
        'recposts':utils.recent_post(Post),
        'links':Link.objects.all(),
        'pages':Page.objects.all(),
        'categorys':Category.objects.all(),
        'tags':tags,
    }
    return global_sidebar


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
    c.update(common_response(request))
    
    return render_to_response('%s/index.html'%THEME,c,
                context_instance=RequestContext(request))

def show_post(request, postid , postname):
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
    c.update(common_response(request))
    return render_to_response('%s/page.html'%THEME, c
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
    c.update(common_response(request))
    return render_to_response('%s/page.html'%THEME, c
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
    c.update(common_response(request))
    return render_to_response('%s/index.html'%THEME, c
                , context_instance=RequestContext(request))

def show_category(request, categoryname):
    '''按分类查看'''
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    c={
       'settings':global_settings,
       'title': tagname + ' - Category',
       'no_sidebar':False,
       'posts': utils.get_page(Post.objects.filter(category__name=categoryname), page),
    }
    c.update(common_response(request))
    return render_to_response('%s/index.html'%THEME, c
                , context_instance=RequestContext(request))
    
def archives(request):
    '''归档页面'''
    posts = [Post(**i) for i in Post.objects.values('id', 'title', 'create_time', 'slug')]
    page = {
        'title': '文章归档',
    }

    c= {
        'settings':global_settings,
        'posts': posts,
        'page': page,
        'no_sidebar':False,
    }
    c.update(common_response(request))
    return render_to_response('%s/archives.html'%THEME,c
                , context_instance=RequestContext(request))
    
