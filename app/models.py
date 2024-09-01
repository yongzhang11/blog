# -*-coding:utf-8-*-
""" 数据库的数据模型 """
from __future__ import unicode_literals
from django.db import models
from django.db.models.query import QuerySet
from django.core.serializers import serialize
# from django.utils.timezone import now
# import time
# import datetime

import json


# import sys


# reload(sys)
# sys.setdefaultencoding('utf-8')


class Cate(models.Model):
    name = models.CharField('标题', max_length=50)  # 字段的最大数量

    def __str__(self):
        return self.name

    class Meta:  # 按照时间显示
        verbose_name = u'分类'
        verbose_name_plural = u'分类'


class Article(models.Model):
    cate = models.ForeignKey(Cate, verbose_name='类型', on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=50)  # 字段的最大数量
    text = models.TextField('正文')
    publish_time = models.DateTimeField('发布时间', auto_now_add=True)
    header_img = models.ImageField(upload_to="header/", verbose_name=u'焦点图')
    browse_count = models.PositiveIntegerField('浏览数', default=0)

    def __str__(self):
        return self.title

    class Meta:  # 按照时间显示
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
        ordering = ['-publish_time']


class Marks(models.Model):
    title = models.CharField('课程名称', max_length=150)
    year = models.CharField('学年', max_length=50)
    term = models.PositiveIntegerField('学期', default=1)
    point = models.FloatField('学分', default=0)
    gpa = models.FloatField('绩点', default=0)
    mark = models.PositiveIntegerField('分数', default=0)

    publish_time = models.DateTimeField('更新时间', auto_now_add=True)

    class Meta:
        verbose_name = u'成绩'
        verbose_name_plural = u'成绩'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']


class Msgs(models.Model):
    name = models.CharField('名称', max_length=150, default="File")
    text = models.TextField('留言')
    publish_time = models.DateTimeField('发布时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'留言'
        verbose_name_plural = u'留言'
        ordering = ['-publish_time']


class Comment(models.Model):
    name = models.CharField('昵称', max_length=50)
    text = models.TextField('评论')
    publish_time = models.DateTimeField('发布时间', auto_now_add=True)
    a_id = models.PositiveIntegerField('文章id', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'
        ordering = ['-publish_time']


class Album(models.Model):
    title = models.CharField('标题', max_length=250, unique=True)
    path = models.ImageField(upload_to="", verbose_name=u'图片')
    upload_time = models.DateTimeField('上传时间', auto_now_add=True)

    class Meta:
        verbose_name = u'相册'
        verbose_name_plural = u'相册'


class Cloud(models.Model):
    name = models.CharField('文件名', max_length=250, unique=True)
    file = models.FileField(upload_to="", verbose_name=u'文件')
    upload_time = models.DateTimeField('上传时间', auto_now_add=True)

    class Meta:
        verbose_name = u'文件'
        verbose_name_plural = u'文件'


def getObject(obj):
    if isinstance(obj, QuerySet):
        fields = []
        for data in obj:
            json_data = serialize('json', [data])[1:-1]
            dic_data = json.loads(json_data)['fields']
            dic_data['id'] = data.id
            fields.append(dic_data)
        return fields
    if isinstance(obj, models.Model):
        json_data = serialize('json', [obj])[1:-1]
        dic_data = json.loads(json_data)['fields']
        dic_data['id'] = obj.id
        return dic_data
