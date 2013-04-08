#!/usr/bin/env python
# −*− coding: UTF−8 −*−
#
# Author:   Jove Yu <yushijun110@gmail.com>
import markdown
from django.contrib import admin
from models import Tag,Page,Post,Link,Category,Image ,PostTag
from pagedown.widgets import AdminPagedownWidget
from forms import PostForm,PageForm

class PostTagInline(admin.TabularInline):
    model = PostTag

class ImageAdmin(admin.ModelAdmin):
    list_display=['image']

class TagAdmin(admin.ModelAdmin):
    list_display=['name','count_post']
    inlines = (PostTagInline,)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    
class LinkAdmin(admin.ModelAdmin):
    list_display=['name','url']
    
class PageAdmin(admin.ModelAdmin):
    list_display=['title', 'get_absolute_url', 'author', 'create_time', 'seq']
    prepopulated_fields={"slug":("title",)}    

    form = PageForm  

    def save_model(self, request, obj, form, change):
        '''新建，修改页面'''
        obj.author=request.user
        obj.content = markdown.markdown(obj.markdown,['codehilite'])
        
        return super(PageAdmin,self).save_model(request, obj, form, change)
    
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'create_time']
    list_filter = ['author', 'tags']
    prepopulated_fields={"slug":("title",)}

    form = PostForm  

    inlines = (PostTagInline,)
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.content = markdown.markdown(obj.markdown,['codehilite'])
        return super(PostAdmin, self).save_model( request, obj, form, change)
    
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Image, ImageAdmin)
