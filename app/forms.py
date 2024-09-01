# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.db.models import Q

import re


class MsgsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "输入昵称", "required": "required", }),
                           max_length=150, error_messages={"required": "昵称不能为空", })
    text = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "输入留言", "required": "required", }),
                           max_length=500, error_messages={"required": "留言不能为空", })


class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30)
    age = forms.CharField(max_length=30)
# class CommentForm(forms.Form):
#     '''
#     评论表单
#     '''
#     author = forms.CharField(widget=forms.TextInput(attrs={"id": "author", "class": "comment_input",
#                                                            "required": "required","size": "25", "tabindex": "1"}),
#                               max_length=50,error_messages={"required":"username不能为空",})
#     email = forms.EmailField(widget=forms.TextInput(attrs={"id":"email","type":"email","class": "comment_input",
#                                                            "required":"required","size":"25", "tabindex":"2"}),
#                                  max_length=50, error_messages={"required":"email不能为空",})
#     url = forms.URLField(widget=forms.TextInput(attrs={"id":"url","type":"url","class": "comment_input",
#                                                        "size":"25", "tabindex":"3"}),
#                               max_length=100, required=False)
#     comment = forms.CharField(widget=forms.Textarea(attrs={"id":"comment","class": "message_input",
#                                                            "required": "required", "cols": "25",
#                                                            "rows": "5", "tabindex": "4"}),
#                                                     error_messages={"required":"评论不能为空",})
#     article = forms.CharField(widget=forms.HiddenInput())
