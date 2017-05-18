# -*- coding: utf-8 -*-

import threading

from utility.tool import get_request_method, log
from utility.response import response_error_result, response_list_result, response_msg_result

from webchat.settings import WEBCHAT_OPERATOR_MARK, WEBCHAT_OPERATOR
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

	# 请求凭证
	def request_access_token(self):
		log('================Access Token================')
		handler = AccessToken()
		if handler.access() == False:
			return

		access_token = handler.getAccessToken()
		expiresIn = handler.getExpiresIn()
		log ("access_token %s" % access_token)
		log ("left time %d" % expiresIn)

		self.access_token = access_token

		return (access_token, expiresIn)

	# 获取凭证
	def getAccessToken(self, request):
		access_token, expiresIn = self.request_access_token()

		if access_token != None:
			timer = threading.Timer(expiresIn, self.request_access_token)
			timer.start()

		return response_msg_result(request, self.access_token)

	#获取服务器列表
	def getServerList(self, request):
		log('================Get Server List================')
		handler = AccessServerList(self.access_token)
		if handler.access() == False:
			return

		serverList = handler.getServerList()

		return response_list_result(request, serverList)


	#派发操作消息
	def dispatchOperator(self, request):
		method = get_request_method(request)
		mark = method.get(WEBCHAT_OPERATOR_MARK, None)
		if mark != None:
			if mark in self.dispatchers.keys():
				return self.dispatchers[mark](request)
		else:
			return response_error_result(request)


