# -*- coding: utf-8 -*-
import requests

from webchat.config import APPID, AppSecret, TOKEN, WEBCHAT_URL,WEBCHAT_OPERATOR
from utility.tool import log
from utility.classes import Info

####################################################################
#获取凭证
class AccessToken(Info):
	"""docstring for AccessToken"""
	def __init__(self):
		super(AccessToken, self).__init__()

		self.requestBody['url'] = WEBCHAT_URL[WEBCHAT_OPERATOR[0]]
		self.requestBody['params'] = {
			'grant_type' : 'client_credential',
			'appid' : APPID,
			'secret' : AppSecret,
		}

		self.response['successKeys'] = ['access_token', 'expires_in']

	# 获取凭证
	def getAccessToken(self):
		return self.getSuccessParam(self.response['successKeys'][0])

	# 获取有效时间
	def getExpiresIn(self):
		return self.getSuccessParam(self.response['successKeys'][1]) - 10

####################################################################
#获取服务器列表
class AccessServerList(Info):
	"""docstring for AccessServerList"""
	def __init__(self, access_token):
		super(AccessServerList, self).__init__()

		self.requestBody['url'] = WEBCHAT_URL[WEBCHAT_OPERATOR[1]]
		self.requestBody['params'] = {
			'access_token' : access_token, 
		}

		self.response['successKeys'] = ['ip_list']

	# 获取凭证
	def getServerList(self):
		return self.getSuccessParam(self.response['successKeys'][0])
		