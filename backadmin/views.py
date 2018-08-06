from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from app.models import GoodsInfo, TypeInfo


def index(request):
    if request.method =='GET':
        return render(request,'backadmin/index.html')

# 分页展示
def productlist(request):
    if request.method == 'GET':
        num = request.GET.get('page_num',1)
        good = GoodsInfo.objects.filter(is_delete=0)
        paginator = Paginator(good,1)
        page = paginator.page(num)
        data={'goods':page}
        return render(request,'backadmin/product_list.html',data)


# 删除
def deletegood(request):
    if request.method == 'GET':
        gid = request.GET.get('gid')
        good = GoodsInfo.objects.filter(id=gid).first()
        good.is_delete = 1
        good.save()
        msg = '删除成功'
        return HttpResponseRedirect(reverse('backadmin:productlist'),{'msg':msg})

# 增加和修改
def productdetail(request):
    gtypes = TypeInfo.objects.all()
    gid = request.GET.get('gid')
    good = GoodsInfo.objects.filter(id=gid).first()
    if request.method == 'GET':
        if gid:
            data={'goods':good, 'gtypes':gtypes}
        else:
            data = {'gtypes': gtypes}
        return render(request,'backadmin/product_detail.html', data )

    if request.method == 'POST':
        gname = request.POST.get('gname')
        gprice = request.POST.get('gprice')
        gpic = request.FILES.get('gpic')
        gstock = request.POST.get('gstock')
        tname = request.POST.get('tname')
        gtype_id = TypeInfo.objects.filter(tname=tname).first().id

        gid = request.POST.get('gid')

        if gid:
            if  all([gname, gprice, gpic ,gstock, gtype_id]):
                good.gname  = gname
                good.gprice = gprice
                good.gpic   = gpic
                good.gstock = gstock
                good.gtype_id = gtype_id
                good.save()
                msg = '修改成功'
                return HttpResponseRedirect(reverse('backadmin:productlist'), {'msg': msg})
            elif all([gname, gprice, gstock, gtype_id]):
                good.gname = gname
                good.gprice = gprice
                good.gstock = gstock
                good.gtype_id = gtype_id
                good.save()
                msg = '修改成功'
                return HttpResponseRedirect(reverse('backadmin:productlist'), {'msg': msg})
            else:
                msg = '请将数据填写完整'
                data = {'gtypes': gtypes, 'msg': msg, 'goods': good}
                return render(request, 'backadmin/product_detail.html', data)


        else:
            if not all([gname, gprice, gpic, gstock, gtype_id]):
                msg = '请将数据填写完整'
                data ={'gtypes':gtypes,'msg': msg}
                return render(request, 'backadmin/product_detail.html', data)
            else:
                GoodsInfo.objects.create(gname=gname,gprice=gprice,gpic=gpic,gstock=gstock,gtype_id=gtype_id)
                msg = '添加成功'
                return HttpResponseRedirect(reverse('backadmin:productlist'),{'msg': msg})


def recyclebin(request):
    if request.method =='GET':
        num = request.GET.get('page_num',1)
        good = GoodsInfo.objects.filter(is_delete=1)
        paginator = Paginator(good,1)
        page = paginator.page(num)
        data={'goods':page}
        return render(request,'backadmin/recycle_bin.html',data)

# 恢复
def recovergood(request):
    if  request.method == 'GET':
        gid = request.GET.get('gid')
        good = GoodsInfo.objects.filter(id=gid).first()
        good.is_delete = 0
        good.save()
        msg = '恢复成功'
        return HttpResponseRedirect(reverse('backadmin:recyclebin'),{'msg':msg})

def login(request):
    if request.method =='GET':
        return render(request,'backadmin/login.html')




