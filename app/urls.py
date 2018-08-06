from django.conf.urls import url

from app import views

urlpatterns =[
    url(r'^index/',views.index,name='index'),
    url(r'^usercenterinfo/',views.usercenterinfo,name='usercenterinfo'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^usercenterorder/',views.usercenterorder,name='usercenterorder'),
    url(r'^usercentersite/',views.usercentersite,name='usercentersite'),
    url(r'^detail/',views.detail,name='detail'),
    url(r'^list/',views.list,name='list'),
    url(r'^placeorder/',views.placeorder,name='placeorder'),
    url(r'^addtogood/',views.addtogood,name='addtogood'),
    url(r'^subtogood/',views.subtogood,name='subtogood'),
    url(r'^goodscount/',views.goodscount,name='goodscount'),
    url(r'^re_detail/',views.re_detail,name='re_detail'),
    url(r'^addtocart/',views.addtocart,name='addtocart'),
    url(r'^is_delete/',views.is_delete,name='is_delete')
    # url(r'^placeorder/',views.placeorder,name='placeorder'),

]