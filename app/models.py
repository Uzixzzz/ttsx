from django.db import models
from tinymce.models import HTMLField
from user.models import UserModel

class TypeInfo(models.Model):
    tname=models.CharField(u'种类',max_length=20)
    is_delete=models.BooleanField(default=False)
    class Meta:
        db_table= 'ttsx_typeinfo'

class GoodsInfo(models.Model):
    gname=models.CharField(u'名字',max_length=20)
    gpic=models.ImageField(u'图片',upload_to='df_goods')
    gprice=models.DecimalField(u'价钱',max_digits=50,decimal_places=2)
    is_delete=models.BooleanField(default=False)
    gunit=models.CharField(u'单位',max_length=20,default='千克')
    gclick=models.IntegerField(u'点击',default=0)
    gjianjie=models.CharField(max_length=200)
    gstock=models.IntegerField(u'库存')
    gcontent=HTMLField(u'描述')
    gtype=models.ForeignKey(TypeInfo)

    class Meta:
        db_table = 'ttsx_goodsinfo'

class Cart(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    goods = models.ForeignKey(GoodsInfo)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)  #  是否选择商品

    class Meta:
        db_table = 'ttsx_cart'



class OrderModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    o_num = models.CharField(max_length=64)  # 订单号
    # 0 代表已下单，但是未付款， 1 已付款未发货  2 已付款，已发货.....
    o_status = models.IntegerField(default=0)  # 状态
    o_create = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        db_table = 'ttsx_order'


class OrderGoodsModel(models.Model):
    goods = models.ForeignKey(GoodsInfo)  # 关联的商品
    order = models.ForeignKey(OrderModel)  # 关联的订单
    goods_num = models.IntegerField(default=1)  # 商品的个数

    class Meta:
        db_table = 'ttsx_order_goods'