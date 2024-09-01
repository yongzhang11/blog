# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Count
from shop.models import *
from shop.forms import *
import json, datetime
from django.core import serializers
import time

logger = logging.getLogger('shop.views')


# Create your views here.
def global_setting(request):
    # 站点基本信息
    SITE_URL = settings.SITE_URL
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    carnum = range(1, 50)

    return locals()


def index(request):
    goods = Products.objects.all()[:14]
    aa = goods[:5]
    return render(request, 'shop/index.html', locals())


def products(request):
    goods = Products.objects.all()
    return render(request, 'shop/product_list.html', locals())


def plist(request):
    goods = Products.objects.all()[:10]

    # return HttpResponse(json.dumps(g), content_type="application/json")
    return render(request, 'shop/product_list.html', locals())


def plook(request):
    id = request.GET['id']
    product = Products.objects.get(id=id)
    try:
        user = User.objects.get(username=request.user.username)
        cms = Comment.objects.filter(pid=id)
        code = 200
    except:
        cms = Comment.objects.filter(pid=id)
        code = 100
    return render(request, 'shop/productLook.html', locals())


def pj(request):
    user = User.objects.get(id=request.POST['uid'])
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    cm = Comment.objects.create(name=user, text=request.POST['pj'], pid=request.POST['id'], publish_time=time)
    cm.save()
    res = render(request, 'shop/success.html', {'reason': '提交成功！'})
    return res


def addtocar(request):
    id = request.GET['id']
    amount = int(request.GET['amount'])
    res = render(request, 'shop/success.html', {'reason': '添加购物车成功！'})
    try:
        ck = eval(request.COOKIES.get('mycart'))
        if id in ck:
            ck[id] += amount
        else:
            ck[id] = amount
        res.set_cookie("mycart", str(ck))
    except:
        res.set_cookie("mycart", {id: amount})
    return res


def removeProduct(request):
    info = eval(request.COOKIES.get('mycart'))
    if request.GET['id'] in info:
        del info[request.GET['id']]
    res = render(request, 'shop/success.html', {'reason': '删除商品成功！', 'url': ('/shop/shopcar', '返回购物车')})
    res.set_cookie("mycart", str(info))
    return res


def modifyProduct(request):
    info = eval(request.COOKIES.get('mycart'))
    if request.GET['id'] in info:
        info[request.GET['id']] = int(request.GET['amount'])
    res = render(request, 'shop/success.html', {'reason': '修改数量成功！', 'url': ('/shop/shopcar', '返回购物车')})
    res.set_cookie("mycart", str(info))
    return res


def shopcar(request):
    try:
        info = eval(request.COOKIES.get('mycart'))
        cart = []
        totalPrice = 0
        try:
            for k, v in info.items():
                p = Products.objects.get(id=k)
                car = (p, v)
                cart.append(car)
                totalPrice += float(p.price) * v
        except:
            pass
    except:
        code = 400
    return render(request, 'shop/cart.html', locals())


def checkresult(request):
    od = Order.objects.get(id=request.GET['id'])
    user = User.objects.get(username=request.user.username)
    fee = request.GET['fee']
    user.balance = user.balance - float(fee)
    user.save()
    od.delete()
    return render(request, 'shop/success.html', {'reason': '结账成功！'})


@login_required
def checknow(request):
    pid = request.GET.get('id')
    num = request.GET.get('amount')
    p = Products.objects.get(id=pid)
    totalPrice = float(p.price) * int(num)
    receiver = User.objects.get(username=request.user.username)
    buynow = 1
    return render(request, 'shop/check.html', locals())


@login_required
def check(request):
    user = User.objects.get(username=request.user.username)
    info = eval(request.COOKIES.get('mycart'))
    cart = []
    totalPrice = 0
    try:
        for k, v in info.items():
            p = Products.objects.get(id=k)
            car = (p, v)
            cart.append(car)
            totalPrice += float(p.price) * v
    except:
        pass

    receiver = User.objects.get(username=request.user.username)
    return render(request, 'shop/check.html', locals())


def deleteOrder(request):
    id = request.GET['id']
    od = Order.objects.get(id=id)
    od.delete()
    return HttpResponse(json.dumps({'data': 'success'}), content_type="application/json")


def order(request):
    user = User.objects.get(username=request.user.username)
    ods = Order.objects.filter(user_id=user.id)
    orders = []
    for item in ods:
        p = Products.objects.get(id=item.product)
        orders.append((item.id, p, item.money, item.time))
    return render(request, 'shop/order_list.html', {'orders': orders})


def usercenter(request):
    try:
        user = User.objects.get(username=request.user.username)
    except:
        return redirect('/login')
    return render(request, 'shop/usercenter.html', locals())


def updatePerson(request):
    # 根据请求中的id获取对应的用户对象
    user = User.objects.get(id=request.GET['id'])
    # 打印用户信息到日志中
    # 更新用户的手机号码
    user.mobile = request.GET['user.mobile']
    # 更新用户的名字
    user.first_name = request.GET['user.name']
    # 更新用户的邮箱
    user.email = request.GET['user.email']
    # 更新用户的地址
    user.address = request.GET['user.address']
    # 保存用户信息的更改
    try:
        user.save()
    except Exception as e:
        print(e)
    # 返回一个JSON格式的响应，表示更新成功
    return HttpResponse(json.dumps({'data': 'success'}), content_type="application/json")


def saveOrder(request):
    total = request.GET.get('total')
    pid = request.GET.get('pid')
    if total and pid:
        uorder = Order.objects.create(user_id=request.GET['id'], product=pid, money=float(total))
        uorder.save()
        return render(request, 'shop/success.html', {'reason': '订单提交成功！', 'url':
            '<script type="text/javascript"> alert("即将跳转支付页面..."); window.location.href="https://www.alipay.com"; </script>'})
    else:
        info = eval(request.COOKIES.get('mycart'))
        cart = []
        totalPrice = 0
        try:
            for k, v in info.items():
                p = Products.objects.get(id=k)
                car = (p, v)
                cart.append(car)
                totalPrice += float(p.price) * v
                uorder = Order.objects.create(user_id=request.GET['id'], product=p.id, money=float(p.price) * v)
                uorder.save()
        except Exception as e:
            print(e)
        res = render(request, 'shop/success.html', {'reason': '订单提交成功！', 'url':
            '<script type="text/javascript"> alert("即将跳转支付页面..."); window.location.href="https://www.alipay.com"; </script>'})
        res.set_cookie("mycart", "")
        return res


# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        print(e)
        logger.error(e)
    return redirect('/shop/')


# 注册
def do_reg(request):
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


# 登录
def do_login(request):
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


def search(request):
    goods = Products.objects.filter(title__contains=request.POST['kw'])
    return render(request, 'shop/product_list.html', locals())
