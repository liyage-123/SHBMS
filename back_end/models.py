from django.db import models
from django.utils import timezone


class Account(models.Model):
    user_name = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")
    business_account = models.BooleanField(default=False)
# 用户表


class Administrators(models.Model):
    user_name = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")
# 管理员表


class Limit(models.Model):
    content_type_id = models.IntegerField()
    permission = models.CharField(max_length=255)
# 用户权限表


class Prohibition(models.Model):
    user_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    blocked_permission = models.ForeignKey('Limit', on_delete=models.CASCADE)
    block_time = models.DateTimeField(auto_now_add=True)
    block_end_time = models.DateTimeField(auto_now=True)
# 用户封禁表


class UpShelfExamine(models.Model):
    goods_id = models.ForeignKey('Goods', on_delete=models.CASCADE)
# 上架审核表


class ComplaintExamine(models.Model):
    complain_id = models.ForeignKey('Account', on_delete=models.CASCADE)
# 待投诉处理表


class MyChar(models.Field):
    def __init__(self, max_length, unique, *args, **kwargs):
        self.max_length = max_length
        super(MyChar, self).__init__(max_length=max_length, unique=unique, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length
# 自定义数据（char）


class Book(models.Model):
    full_title = models.CharField(max_length=255)
    ISBN_num = MyChar(max_length=13, unique=True)
    publisher = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    edition = models.IntegerField()
    original_price = models.DecimalField(max_digits=19, decimal_places=4)
# 书籍信息表


class Goods(models.Model):
    type = ((1, "上架中"), (2, "待处理"), (3, "已下架") )
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
    merchant_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=4)
    description = models.TextField()
    status = models.IntegerField(choices=type)
# 商品表


class PersonalInfo(models.Model):
    user_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True)
    mobile = models.DecimalField(max_digits=19, decimal_places=0)
    email = models.EmailField()
# 个人信息表


class TransRecord(models.Model):
    costumer_id = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='costumer')
    merchant_id = models.ForeignKey('Account', on_delete=models.SET_DEFAULT, default=' ', related_name='merchant')
    good_id = models.ForeignKey('Goods', on_delete=models.DO_NOTHING)
    order_time = models.DateTimeField(auto_now_add=True)
# 交易记录表


class MessageRecord (models.Model):
    from_id = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='from_id')
    to_id = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='to_id')
    content = models.TextField()

# Create your models here.