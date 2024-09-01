from django.conf.urls import url
from shop.views import *

app_name = 'shop'
urlpatterns = [
    url(r'^$', index, name='shopindex'),
    url(r'productList/$', plist, name='shopplist'),
    url(r'check/$', check, name='shopcheck'),
    url(r'pj/$', pj, name='shoppj'),
    url(r'checknow/$', checknow, name='shopchecknow'),
    url(r'order/$', order, name='shoporder'),
    url(r'products/$', products, name='shopproducts'),
    url(r'removeProduct/$', removeProduct, name='shopremoveProduct'),
    url(r'modifyProduct/$', modifyProduct, name='shopmodifyProduct'),
    url(r'logout$', do_logout, name='shoplogout'),
    url(r'reg/$', do_reg, name='shopreg'),
    url(r'loggin/$',do_login, name='shoploggin'),
    url(r'productLook/$', plook, name='shopplook'),
    url(r'addProductCar/$', addtocar, name='shopaddtocar'),
    url(r'shopcar/$', shopcar, name='shopshopcar'),
    url(r'search/$', search, name='shopsearch'),
    url(r'deleteOrder/$', deleteOrder, name='shopdeleteOrder'),
    url(r'usercenter/$', usercenter, name='shopusercenter'),
    url(r'saveOrder/$', saveOrder, name='shopsaveOrder'),
    url(r'updatePerson/$', updatePerson, name='shopupdatePerson'),

   
]
