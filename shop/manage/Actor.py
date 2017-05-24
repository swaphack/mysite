# -*- coding: utf-8 -*-

# 表演者
class Actor(object):
	"""docstring for DispatchActor"""
	dispatchers = {}

	def __init__(self):
		super(Actor, self).__init__()

	# 添加派发处理
	def add_dispacher(self, name, handler):
		if name == None or handler == None:
			return
		self.dispatchers[name] = handler

	# 派发事件
	def dispatch(self, name, arg):
		if name == None or arg == None:
			return None 

		handler = self.dispatchers.get(name, None)
		if handler == None:
			return None

		return handler(arg)

	# 处理事件
	def hand(self, request):
		pass	


############################################################
from django.shortcuts import render
from utility.tool import get_request_method, log
from utility.response import response_error_result

# 商店表演者
class ShopActor(Actor):
	"""docstring for ShopActor"""
	name = None
	
	def __init__(self):
		super(ShopActor, self).__init__()

	# 返回主界面
	def response_home_html(self, request):
		url = 'index.html'
		content = {
			'title' : 'Home'
		}
		return render(request, url, content)

	# 返回错误代码
	def response_error_html(self, request):
		return response_error_result(request)

	#获取方法
	def get_method(self, request):
		return get_request_method(request);

	# 处理
	def hand(self, request):
		if self.name == None or request == None:
			return self.response_error_html(request)

		method = self.get_method(request)
		mark = method.get(self.name, None)
		log("request name %s, mark %s" % (self.name, mark))
		result = self.dispatch(mark, request)
		if result != None:
			log("Dispatch %s" % mark)
			return result
		else:
			log("Not register dispatcher by %s" % self.name)
			return self.response_home_html(request)

	# 刷新页面
	def flush_html(self, request, url, content):
		return render(request, url, content)
		

		