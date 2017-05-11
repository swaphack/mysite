# -*- coding: utf-8 -*-

from django.shortcuts import render
from utility.response import response_msg_result, response_error_result
from utility.globals import init_server
from utility.tool import get_request_method

from shop.config import SHOP_OPERATOR_MARK, SHOP_URL, WEBCHAT_OPERATOR
from shop.models import Mommodity

from mysite.settings import STATIC_URL
from mysite.config import HTTP_URL

# Create your views here.

#请求物品列表
def response_item_list(request):
	items = Mommodity.objects.all()

	varList = []
	for item in items:
		var = {}
		var['href'] = '%s?%s=%s&id=%d' % (SHOP_URL, SHOP_OPERATOR_MARK, WEBCHAT_OPERATOR[1], item.id)
		var['url'] = ('%s%s') % (STATIC_URL,item.piture)

		varList.append(var)

	content = {'items' : varList}
	url = 'shop/mommodity_list.html'
	return render(request, url, content)

#显示物品信息
def response_item_info(request, method):
	itemId = method.get('id', None)
	if itemId == None:
		return response_error_result(request)

	items = Mommodity.objects.filter(id=itemId)
	if items == None or items.count() == 0:
		return response_error_result(request)

	content = {'item' : items[0]}
	url = 'shop/mommodity_info.html'
	return render(request, url, content)

# 显示主页
def response_home_page(request):
	url = 'shop/index.html'
	content = {
		'title' : 'Home'
	}
	return render(request, url, content)

# 处理
def index(request):
	init_server(request)

	method = get_request_method(request)
	mark = method.get(SHOP_OPERATOR_MARK, None)
	if mark != None:
		if mark == WEBCHAT_OPERATOR[0]:
			return response_item_list(request)
		elif mark == WEBCHAT_OPERATOR[1]:
			return response_item_info(request, method)
		else:
			return response_home_page(request)
	else:
		return response_home_page(request)


	




