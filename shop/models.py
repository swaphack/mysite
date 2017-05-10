# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

# 商品
class Mommodity(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20, verbose_name="名称")
	price = models.FloatField(max_length=10, verbose_name="价格")
	num = models.IntegerField(verbose_name="数量", default=0)
	detail = models.TextField(max_length=100, verbose_name="说明", default='')
	piture = models.CharField(max_length=100, verbose_name="图片", default='')

	def __str__(self):
		return ('%d-%s') % (self.id, self.name)

#订单
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

