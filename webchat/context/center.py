# -*- coding: utf-8 -*-

import threading

from webchat.context.tool import log, \
	get_request_method, \
	response_error_result, \
	response_list_result

from webchat.config import WEBCHAT_OPERATOR_MARK, WEBCHAT_OPERATOR
from webchat.context.infos import AccessToken, AccessServerList


# 中心服务器
class CenterServer(object):
	"""docstring for CenterServer"""

	access_token = None
	def __init__(self):
		super(CenterServer, self).__init__()
		#派发处理
		self.dispatchers = {
			WEBCHAT_OPERATOR[0] : self.getAccessToken,
			WEBCHAT_OPERATOR[1] : self.getServerList,
		}

	# 获取凭证
	def getAccessToken(self, request):
		log('================Access Token================')
		handler = AccessToken()
		if handler.access() == False:
			return

		self.access_token = handler.getAccessToken()
		log ("access_token %s" % self.access_token)
		if self.access_token != None:
			timer = threading.Timer(handler.getExpiresIn(), self.getAccessToken)
			timer.start()

	#获取服务器列表
	def getServerList(self, request):
		log('================Get Server List================')
		handler = AccessServerList(self.access_token)
		if handler.access() == False:
			return

		serverList = handler.getServerList()

		return response_list_result(request, serverList)


	#派发消息
	def dispatch(self, request):
		method = get_request_method(request)
		mark = method.get(WEBCHAT_OPERATOR_MARK, None)
		if mark != None:
			if mark in self.dispatchers.keys():
				return self.dispatchers[mark](request)
		else:
			return response_error_result(request)


