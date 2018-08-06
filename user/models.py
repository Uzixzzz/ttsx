from django.db import models

class UserModel(models.Model):
    username = models.CharField(u'用户名', max_length=20)
    password = models.CharField(u'密码', max_length=255)
    email = models.CharField(u'电子邮箱', max_length=30)
    showname = models.CharField(u'收件人名字', max_length=20, default='')
    showaddress = models.CharField(u'收件地址', max_length=100, default='')
    showpostcode = models.CharField(u'收件邮编', max_length=6, default='')
    showtel = models.CharField(u'收件人电话', max_length=11, default='')

    class Meta:
        db_table= 'ttsx_user'

class UserSession(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    session = models.CharField(max_length=256)   # 密码
    out_time = models.DateTimeField()  # 过期时间

    class Meta:
        db_table = 'ttsx_user_ticket'