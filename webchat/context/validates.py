# -*- coding: utf-8 -*-
import hashlib
from django.http import HttpResponse

from webchat import config
from utility.classes import Validate

#http验证
class HttpValidate(Validate):
	"""docstring for HttpValidate"""
	def __init__(self, request):
		super(HttpValidate, self).__init__()
		self.request = request
		self.method = get_request_method(request)

	#验证传入参数
	def validRequestParams(self, validKeys):
		if self.method == None or validKeys == None:
			return True

		if self.method == None:
			return False

		for key in validKeys:
			if self.method.get(key, None) == None:
				return False

		return True

	# 验证
	def valid(self):
		pass

	# 验证通过时处理
	def work(self):
		pass

####################################################################
#服务器识别
class SignatureValidate(HttpValidate):
	"""docstring for SignatureValidate"""
	validKeys = {'signature', 'timestamp', 'nonce', 'echostr'}

	def __init__(self, request):
		super(SignatureValidate, self).__init__(request)

	def valid(self):
		if super(SignatureValidate, self).validRequestParams(self.validKeys) == False:
			return False

		signature = self.method.get('signature', None)
		timestamp = self.method.get('timestamp', None)
		nonce = self.method.get('nonce', None)
		token = TOKEN

		if signature == None \
			or timestamp == None \
			or nonce == None:
			return False

		tempAry = (token, timestamp, nonce)
		tempAry = sorted(tempAry)
		tempStr = "".join(tempAry)
		tempStr = hashlib.sha1(tempStr)

		if tempStr != signature:
			return False

		return True

	def work(self):
		echostr = self.method.get('echostr', None)
		return HttpResponse(echostr)

####################################################################
