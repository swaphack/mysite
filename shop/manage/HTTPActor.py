# -*- coding: utf-8 -*-

from shop.manage.Actor import ShopActor

from shop.manage.AccountActor import get_account_actor
from shop.manage.MommodityActor import get_mommodity_actor
from shop.manage.OrderActor import get_order_actor


# 商店操作处理
SHOP_OPERATOR_MARK = 'action'
SHOP_OPERATOR_MOMMODITY = 'mommodity'
SHOP_OPERATOR_ACCOUNT = 'account'
SHOP_OPERATOR_ORDER = 'order'

# http管理对象
class HTTPActor(ShopActor):
	"""docstring for HTTPActor"""
	def __init__(self):
		super(HTTPActor, self).__init__()

		self.name = SHOP_OPERATOR_MARK

		self.add_dispacher(SHOP_OPERATOR_MOMMODITY, self.disatch_mommodity)
		self.add_dispacher(SHOP_OPERATOR_ACCOUNT, self.dispatch_account)
		self.add_dispacher(SHOP_OPERATOR_ORDER, self.dispatch_order)

	# 派发商品处理
	def disatch_mommodity(self, request):
		return get_mommodity_actor().hand(request)

	# 派发账号处理
	def dispatch_account(self, request):
		return get_account_actor().hand(request)

	# 派发订单处理
	def dispatch_order(self, request):
		return get_order_actor().hand(request)

########################################################################
global __http_actor
__http_actor = HTTPActor()

def get_http_actor():
	global __http_actor
	return __http_actor


