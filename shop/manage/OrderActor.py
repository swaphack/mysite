# -*- coding: utf-8 -*-

from shop.manage.Actor import ShopActor

# 订单
class OrderActor(ShopActor):
	"""docstring for OrderActor"""
	def __init__(self):
		super(OrderActor, self).__init__()

########################################################################
global __order_actor
__order_actor = OrderActor()

def get_order_actor():
	global __order_actor
	return __order_actor
