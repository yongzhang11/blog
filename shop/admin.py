# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):

    list_display = ('id','username','email','last_name', 'status', )
    list_display_links = ('id', )
    fieldsets = (
        (None, {
            'fields': ('last_name','first_name', 'status', )
        }),
    )

# Register your models here.
class FenleiAdmin(admin.ModelAdmin):

    list_display = ('id', 'title','desc', )
    list_display_links = ('id', 'title','desc', )

    fieldsets = (

    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )



# Register your models here.
class ProductsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title','price','stock','time' )
    list_display_links = ('id', 'title' )

#     fieldsets = (

#     )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
        

class CommentAdmin(admin.ModelAdmin):

    list_display = ('id','name','text','publish_time' )
    list_display_links = ('id','name','text', )

class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', )
#     list_display_links = ('id',  )

#     fieldsets = (

#     )

#     class Media:
#         js = (
#             '/static/js/kindeditor-4.1.10/kindeditor-min.js',
#             '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
#             '/static/js/kindeditor-4.1.10/config.js',
#         )
admin.site.register(User,UserAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Fenlei,FenleiAdmin)
admin.site.register(Products,ProductsAdmin)
