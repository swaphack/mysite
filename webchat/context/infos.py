# -*- coding: utf-8 -*-
import requests

from webchat.config import APPID, AppSecret, TOKEN, WEBCHAT_URL,WEBCHAT_OPERATOR
from webchat.context.tool import log

class Info(object):
	"""docstring for Info"""
	def __init__(self):
		super(Info, self).__init__()
		# 成功参数
		self.successParams = {}
		# 失败参数
		self.failureParams = {}

		#请求主体
		self.requestBody = {'url' : None, 'params' : None}

		#反馈主体
		self.response = {'successKeys' : None, 'failureKeys' : None}

		# 通用失败接口，如果要特殊定义，需重写
		self.response['failureKeys'] = ['errcode', 'errmsg']

	def makeInfo(self, data, keys):
		if data == None or keys == None:
			return False

		container = {}
		for key in keys:
			val = data.get(key, None)
			if val == None:
				return False
			else:
				container[key] = val
		return True		

	# 生成成功信息
	def makeSuccessInfo(self, data):
		if data == None:
			return False

		self.successParams = {}
		for key in self.response['successKeys']:
			val = data.get(key, None)
			if val != None:
				self.successParams[key] = val

		return True


	# 生成失败信息
	def makeFailureInfo(self, data):
		if data == None:
			return False

		self.failureParams = {}
		for key in self.response['failureKeys']:
			val = data.get(key, None)
			if val != None:
				self.failureParams[key] = val

		return True

	# 获取数据值
	def getSuccessParam(self, name):
		return self.successParams.get(name, None)

	# 获取数据值
	def getFailureParam(self, name):
		return self.failureParams.get(name, None)

	# 获取信息
	def access(self):
		if self.requestBody['url'] == None \
			or self.requestBody['params'] == None:
			return False

		res = requests.get(url = self.requestBody['url'], params = self.requestBody['params'])
		json = res.json()

		if json == None:
			return False

		result = False
		if res.status_code == requests.codes.ok:
			result = self.makeSuccessInfo(json)
		else:
			result = self.makeFailureInfo(json)

		return result

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
		