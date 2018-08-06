from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.models import GoodsInfo, Cart, OrderModel, OrderGoodsModel
from utils.functions import get_order_num




def usercenterinfo(request):
    if request.method == 'GET':
        return render(request,'user_center_info.html')

def usercenterorder(request):
    if request.method == 'GET':
        return render(request,'user_center_order.html')


def usercentersite(request):
    if request.method == 'GET':
        return render(request,'user_center_site.html')

def list(request):
    if request.method == 'GET':
        return render(request, 'list.html')

def placeorder(request):
    if request.method == 'GET':
        return render(request, 'place_order.html')

def index(request):
    if request.method == 'GET':
        goods = GoodsInfo.objects.all()
        data={'goods':goods}
        return  render(request,'index.html',data)

def addtogood(request):
    if request.method =='POST':
        user = request.user
        data={}
        if user.id:
            good_id = request.POST.get('good_id')
            cart = Cart.objects.filter(user=user,goods_id=good_id).first()
            if cart:
                cart.c_num += 1
                cart.save()
                data['c_num'] = cart.c_num
            else:
                Cart.objects.create(user=user, goods_id=good_id)
                data['c_num'] = 1
            data['price'] = cart.goods.gprice * cart.c_num
            data['code'] = '200'
            data['msg'] = '请求成功!'
            return JsonResponse(data)
        return JsonResponse(data)


def subtogood(request):
    if request.method =='POST':
        user = request.user
        data = {}
        if user.id:
            good_id = request.POST.get('good_id')
            cart = Cart.objects.filter(goods_id=good_id,user=user).first()
            if cart:
                if cart.c_num == 1:
                    cart.delete()
                    data['c_num']=0
                else:
                    cart.c_num -=1
                    cart.save()
                    data['c_num']= cart.c_num
                data['price']=cart.goods.gprice*cart.c_num
                data['code'] = '200'
                data['msg'] = '请求成功!'
                return JsonResponse(data)
            else:
                data['msg']='请先添加商品'
                return JsonResponse(data)
        else:
            return JsonResponse(data)

def detail(request):
    if request.method == 'GET':
        good_id = request.GET.get('good_id')
        good = GoodsInfo.objects.filter(id=good_id).first()
        data = {'good':good}
        return render(request,'detail.html',data)

def re_detail(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            good_id = request.GET.get('good_id')
            cart = Cart.objects.filter(user=user,goods_id=good_id).first()
            price = cart.goods.gprice * cart.c_num
            data = {'cart':cart.c_num,'code':200,'price':price}
            return JsonResponse(data)

# 总价
def goodscount(request):
    if request.method == 'GET':
        user = request.user
        carts = Cart.objects.filter(user=user)
        count_gprice = 0
        for cart in carts:
            if cart.c_num > 0:
                count_gprice = cart.goods.gprice*cart.c_num
            else:
                count_gprice = 0
        count_gprice = round(count_gprice)
        return  JsonResponse({'count':count_gprice,'code':200})

def addtocart(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            good_id = request.GET.get('good_id')
            cart = Cart.objects.filter(user=user,goods_id=good_id).first()
            cart.is_select = 0
            cart.save()
            data={'code':200}
            return JsonResponse(data)
        else:
            data={'code':1001}
            return JsonResponse(data)


def cart(request):
    if request.method == 'GET':
        user = request.user
        cart =Cart.objects.filter(user=user,is_select=0)
        data={'carts':cart}
        return render(request,'cart.html',data )

def is_delete(request):
    if request.method == 'GET':
        user = request.user
        cart_id = request.GET.get('cart_id')
        Cart.objects.filter(user=user,id=cart_id).delete()
        return HttpResponseRedirect(reverse('app:cart'))

