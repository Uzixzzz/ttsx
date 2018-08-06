from django.conf.urls import url

from backadmin import views

urlpatterns =[
    url(r'^index/',views.index,name='index'),
    url(r'^productlist/',views.productlist,name='productlist'),
    url(r'^productdetail/',views.productdetail,name='productdetail'),
    url(r'^recyclebin/',views.recyclebin,name='recyclebin'),
    url(r'^login/',views.login,name='login'),
    url(r'^deletegood/', views.deletegood, name='deletegood'),
    url(r'^recovergood/', views.recovergood, name='recovergood')


]