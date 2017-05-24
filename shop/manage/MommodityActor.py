# -*- coding: utf-8 -*-

from shop.manage.Actor import ShopActor
from mysite.settings import STATIC_URL
from shop.models import Mommodity

# 商品操作处理
MOMMODITY_OPERATOR_MARK = 'mommodity'
MOMMODITY_OPERATOR_ITEM_LIST = 'item_list'
MOMMODITY_OPERATOR_ITEM_INFO = 'item_info'

# 商品管理对象
class MommodityActor(ShopActor):
	"""docstring for MommodityActor"""
	def __init__(self):
		super(MommodityActor, self).__init__()

		self.name = MOMMODITY_OPERATOR_MARK

		self.add_dispacher(MOMMODITY_OPERATOR_ITEM_LIST, self.response_item_list)
		self.add_dispacher(MOMMODITY_OPERATOR_ITEM_INFO, self.response_item_info)


	#请求物品列表
	def response_item_list(self, request):
		items = Mommodity.objects.all()

		varList = []
		for item in items:
			var = {}
			var['id'] = item.id
			var['piture'] = item.piture
			var['name'] = item.name
			var['price'] = item.price
			var['detail'] = item.detail
			varList.append(var)

		context = {
			'items' : varList,
		}
		url = 'mommodity/mommodity_list.html'
		return self.flush_html(request, url, context)

	#显示物品信息
	def response_item_info(self, request):
		method = get_request_method(request)
		itemId = method.get('id', None)
		if itemId == None:
			return None

		items = Mommodity.objects.filter(id=itemId)
		if items == None or items.count() == 0:
			return None

		context = {'item' : items[0]}
		url = 'mommodity/mommodity_info.html'
		return self.flush_html(request, url, context)

########################################################################
global __mommodity_actor
__mommodity_actor = MommodityActor()

def get_mommodity_actor():
	global __mommodity_actor
	return __mommodity_actor


