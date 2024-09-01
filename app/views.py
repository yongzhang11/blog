# coding=utf8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from shop.models import User
from django.shortcuts import render, redirect
from django.conf import settings
# 分页器相关的类
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
# from news_publish.forms import CommentForm, LoginForm, RegForm
from app.models import *
from app.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
# import json,cStringIO
from datetime import datetime


def index(request):
    article_list = Article.objects.all().order_by('-browse_count')
    hot = article_list.all()[:5]
    # 分页
    paginator = Paginator(article_list, 6)
    try:
        # 当前页页码page
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        # 发生异常，默认跳转1页
        article_list = paginator.page(1)
    # 把结果映射到字典，传到模板
    return render(request, 'index.html', locals())


def catg(request, id):
    cat = Cate.objects.get(id=id)
    article_list = Article.objects.filter(cate=cat)
    paginator = Paginator(article_list, 20)
    try:
        # 当前页页码page
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        # 发生异常，默认跳转1页
        article_list = paginator.page(1)
    return render(request, 'alist.html', locals())


def alist(request):
    article_list = Article.objects.all()
    # 分页
    paginator = Paginator(article_list, 20)
    try:
        # 当前页页码page
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        # 发生异常，默认跳转1页
        article_list = paginator.page(1)
    return render(request, 'alist.html', locals())


def article(request, id):
    article = Article.objects.get(pk=id)
    article.browse_count = article.browse_count + 1
    article.save()
    cms = Comment.objects.filter(a_id=id)
    return render(request, 'page.html', locals())


def listpic(request):
    album = Album.objects.all()
    return render(request, 'listpic.html', locals())


def message(request):
    if request.method == 'POST':
        if request.POST.get('msg') != u' ' and request.POST.get('name'):
            # print request.POST.get('msg')
            m = Msgs.objects.create(name=request.POST["name"], text=request.POST["msg"])
            m.save()
            info = u'留言成功！'
        else:
            info = u'没有填写昵称或内容！'
        msgs = Msgs.objects.all()
        return render(request, 'message.html', locals())
    else:
        msgs = Msgs.objects.all()
        return render(request, 'message.html', locals())


def about(request):
    return render(request, 'about.html')


def comment(request):
    if request.is_ajax() and request.method == 'POST':
        if request.POST.get('name') != u'' and request.POST.get('comment') != u'':
            info = {'info': u'评论成功！'}
            cm = Comment.objects.create(name=request.POST.get('name'), text=request.POST.get('comment'),
                                        a_id=request.POST.get('a_id'))
            cm.save()
        else:
            info = {'info': u'没有填写昵称或内容！'}
        return HttpResponse(json.dumps(info), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'info': 'syntax error'}), content_type="application/json")


def tj(request):
    from collections import Counter
    us = User.objects.all()
    s = Counter([int(i.last_name) if i.last_name != "" else 0 for i in us])
    s = dict(s)
    x = str(list(s.keys()))
    y = str(list(s.values()))
    return render(request, 'ages.html', locals())


def grade(request):
    gd = Marks.objects.all()
    return render(request, 'grade.html', locals())


def dologout(request):
    try:
        logout(request)
    except Exception as e:
        print(e)
    return redirect('/')


def checkin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
            login(request, user)
            request.session["username"] = user.username
            if user.is_superuser == 1:
                return redirect('/admin/')
            else:
                return redirect('/')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误！'})
    else:
        return render(request, 'login.html')


def reg(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            age = uf.cleaned_data['age']
            u = User.objects.create(username=username, last_name=age, password=make_password(password))
            return redirect('/login/')
        else:
            return render(request, 'reg.html', {'error': '已经被注册！'})
    else:
        uf = UserForm()
        return render(request, 'reg.html', locals())


def search(request):
    article_list = Article.objects.filter(title__contains=request.POST['keys'])
    return render(request, 'alist.html', locals())


def down(request):  # 文件下载功能
    fid = request.GET['id']
    fn = Cloud.objects.get(id=fid)
    file_name = fn.file

    response = HttpResponse(file_name)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name.name[2:])
    return response


def readFile(fn, buf_size=262144):
    f = open(fn, "rb")
    while True:
        c = f.read(buf_size)
        if c:
            yield c
        else:
            break
    f.close()
