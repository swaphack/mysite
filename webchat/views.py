# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from webchat.context import validates
from utility.response import response_error_result


##########################################################
from webchat.config import WEBCHAT_VALIDATE

#验证是否通过app
def validate(request):
	#服务器识别
	if WEBCHAT_VALIDATE != True:
		return response_error_result(request)

	valid = validates.SignatureValidate(request)
	if valid.valid() == True:
		result = valid.getEchostr()
		return HttpResponse(result)
		
	return response_error_result(request)

##########################################################
from utility.globals import get_center_server
# 派发操作
def index(request):
	return get_center_server(request).dispatchOperator(request)

##########################################################