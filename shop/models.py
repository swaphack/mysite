# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

# 商品
class Mommodity(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20, verbose_name="名称")
	price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name="价格")
	num = models.IntegerField(verbose_name="数量", default=0)
	detail = models.TextField(max_length=100, verbose_name="说明", default='')
	piture = models.CharField(max_length=100, verbose_name="图片", default='')

	def __str__(self):
		return ('%d-%s') % (self.id, self.name)

# 订单
class Order(models.Model):
	# 订单状态
	STATUS_CHOICE = (
		('New', '新订单'),
		('Prepare', '准备'),
		('Finish', '完成'),
	)

	id = models.AutoField(primary_key=True)
	custom_id = models.CharField(max_length=20, verbose_name="客户名称")
	custom_address = models.CharField(max_length=100, verbose_name="客户地址")
	mommodity_id = models.IntegerField(verbose_name="商品编号", default=0)	
	mommodity_name = models.CharField(max_length=20, verbose_name="商品名称", default='')
	num = models.IntegerField(verbose_name="数量", default=0)
	timestamp = models.DateTimeField(verbose_name="订单时间")
	status = models.CharField(max_length=20, choices=STATUS_CHOICE, verbose_name="订单状态", default='New')
	mobile = models.CharField(max_length=20, verbose_name="联系电话", default='')
	msg = models.CharField(max_length=100, verbose_name="留言", default='') 

	def __str__(self):
		return ('%d-%s-%d') % (self.id, self.mommodity_name, self.num)

# 账号
class Account(models.Model):
	# 性别
	GENDER_CHOICE = (
		('M', '男'),
		('F', '女'),
	)

	id = models.AutoField(primary_key=True)
	account = models.CharField(max_length=50, verbose_name="账号")
	name = models.CharField(max_length=20, verbose_name="姓名", default='')
	email = models.EmailField(verbose_name="邮箱", default='')
	gender = models.CharField(max_length=2, verbose_name="性别", choices=GENDER_CHOICE, default='M')
	mobile = models.CharField(max_length=20, verbose_name="联系电话", default='')
	balance = models.DecimalField(max_digits=11, decimal_places=2, verbose_name="余额", default=0)
	score = models.IntegerField(verbose_name="积分", default=0)
	vip = models.PositiveSmallIntegerField(verbose_name="VIP等级", default=0)
		

