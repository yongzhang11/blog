"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app.views import *
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^shop/', include('shop.urls')),
                  # url(r'^shop/', include(('shop.urls', 'shop'), namespace='shop')),
                  url(r'^$', index, name='index'),
                  url(r'^about/$', about, name='about'),
                  url(r'^alist/$', alist, name='alist'),
                  url(r'^albums$', listpic, name='listpic'),
                  url(r'^search/$', search, name='search'),
                  url(r'^message$', message, name='message'),
                  url(r'^article/(P?\d+)$', article, name='article'),
                  url(r'^comment/$', comment, name='comment'),
                  url(r"^reg/$", reg),
                  url(r"^logout/$", dologout),
                  url(r"^tj/$", tj),
                  url(r"^catg/$", catg),
                  url(r'^grade/$', grade, name='grade'),
                  url(r'^login/$', checkin, name='checkin'),
                  url(r'^down/$', down, name='down'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
