# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from webchat.context import validates
from webchat.context.tool import response_error_result


##########################################################
#验证是否通过app
def validate(request):
	#服务器识别
	valid = validates.SignatureValidate(request)
	if valid.valid() == True:
		result = valid.getEchostr()
		return HttpResponse(result)
		
	return response_error_result(request)

##########################################################
from webchat.context.center import CenterServer

global g_CenterServer
g_CenterServer = None

# 开启服务器
def run(request):
	global g_CenterServer
	if g_CenterServer == None:
		g_CenterServer = CenterServer()
		g_CenterServer.getAccessToken(request)

	return g_CenterServer.dispatch(request)

##########################################################

#微信功能验证
WEBCHAT_VALIDATE = False


def index(request):
	if WEBCHAT_VALIDATE == True:
		return validate(request)
	else:
		return run(request)