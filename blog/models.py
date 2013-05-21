#!/usr/bin/env python
# −*− coding: UTF−8 −*−
#
# Author:   Jove Yu <yushijun110@gmail.com>

from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink

class Image(models.Model):
    '''图片'''
    UPLOAD_ROOT = '%Y/%m'
    title = models.CharField(max_length=100, unique=True, verbose_name=u'名称')
    image = models.ImageField(upload_to=UPLOAD_ROOT, verbose_name=u'图片')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = u'图片'

class Category(models.Model):
    '''分类'''
    name = models.CharField(max_length=100, unique=True, verbose_name=u'名称')

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return('blog_category',None,{'categoryname':self.name})

    class Meta:
        verbose_name_plural = verbose_name = u'分类'

class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=100, unique=True, verbose_name=u'名称')
    count_post = models.IntegerField(default=0, editable=False, verbose_name=u'文章数')
    posts = models.ManyToManyField('Post', through='PostTag', verbose_name="文章")

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return('blog_tag',None,{'tagname':self.name})

    class Meta:
        verbose_name_plural = verbose_name = u'标签'

class Page(models.Model):
    '''单页'''
    title = models.CharField(max_length=100, verbose_name=u'标题')
    slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Slug', help_text=u'页面URL名称')
    author = models.ForeignKey(User, editable=False, verbose_name=u'作者')
    markdown = models.TextField(verbose_name=u'内容')
    content = models.TextField(blank=True, editable=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'发布日期')
    allow_comment = models.BooleanField(default=False, verbose_name=u'允许评论')
    seq = models.IntegerField(default=0, db_index=True, verbose_name=u'排序')

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return('blog_page',None,{'pagename':self.slug})

    class Meta:
        ordering = ['seq']
        verbose_name_plural = verbose_name = u'页面'


class Post(models.Model):
    '''文章'''
    title = models.CharField(max_length=100, verbose_name=u'标题')
    slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Slug', help_text=u'页面URL名称')
    author = models.ForeignKey(User, editable=False , verbose_name=u'作者')
    markdown = models.TextField(verbose_name=u'内容')
    content = models.TextField(blank=True, editable=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'发布日期')
    allow_comment = models.BooleanField(default=False, verbose_name=u'允许评论')
    counts = models.IntegerField(default=0, editable=False, verbose_name=u'点击数')
    category= models.ForeignKey(Category ,  verbose_name=u'分类')
    tags = models.ManyToManyField(Tag, blank=True, through="PostTag", verbose_name=u'标签')
    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return('blog_post',None,{'postid':self.id,
                'postname':self.slug})

    class Meta:
        get_latest_by = 'creat_time'
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'文章'


class Link(models.Model):
    '''链接'''
    name = models.CharField(max_length=100, verbose_name=u'名称')
    url = models.URLField(verbose_name=u'链接')
    seq = models.IntegerField(default=0, db_index=True, verbose_name=u'排序')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering=['seq']
        verbose_name_plural=verbose_name=u'链接'

class PostTag(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = "文章标签"

    def __unicode__(self):
        return unicode(self.tag)
