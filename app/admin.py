# -*-coding:utf-8-*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


# from .models import BlogArticles
# admin.site.register(BlogArticles)


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'header_img', 'cate', 'text')
    list_display = ('title', 'publish_time', 'browse_count',)
    list_display_links = ('title',)


class MarksAdmin(admin.ModelAdmin):
    fields = ('title', 'year', 'term', 'point', 'gpa', 'mark',)
    list_display = ('title', 'year', 'term', 'point', 'gpa', 'mark', 'publish_time')


class AlbumAdmin(admin.ModelAdmin):
    change_list_template = 'admin/model_list.html'  # C:\Python27\Lib\site-packages\django\contrib\admin\templates\admin
    fields = ('title', 'path')
    list_display = ('title', 'get_size', 'getwh', 'upload_time', 'image_img')

    def image_img(self, obj):
        if obj.path:
            return u'<img src="%s" width="60px" height="60px"/>' % obj.path.url
        else:
            return u'no image'

    image_img.short_description = u'预览图'
    image_img.allow_tags = False

    def getwh(self, obj):
        # print dir(obj.path)
        return "%sx%s" % (obj.path.width, obj.path.height)

    getwh.short_description = u'分辨率'

    def get_size(self, obj):
        return obj.path.size / 1024

    get_size.short_description = u'大小(KB)'


class CloudAdmin(admin.ModelAdmin):
    change_list_template = 'admin/file.html'  # C:\Python27\Lib\site-packages\django\contrib\admin\templates\admin
    fields = ('name', 'file')
    list_display = ('name', 'get_type', 'get_size', 'upload_time', 'download')

    def download(self, obj):
        return '<a href="/down?id=%s">下载</a>' % obj.id

    download.short_description = u'下载'
    download.allow_tags = True

    def get_size(self, obj):
        return obj.file.size / 1024

    get_size.short_description = u'大小(KB)'

    def get_type(self, obj):
        return obj.file.name.split('.')[-1]

    get_type.short_description = u'类型'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Cloud, CloudAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Msgs)
admin.site.register(Cate)
