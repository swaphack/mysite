# -*- coding: utf-8 -*-

from webchat.config import SHOW_PRINT
from django.shortcuts import render


# 获取请求的方法
def get_request_method(request):
	if request.method == 'GET':
		return request.GET
	elif request.method == 'POST':
		return request.POST
	else:
		return None

# 输出日志
def log(msg):
	if SHOW_PRINT == True:
		print(msg)


# 反馈错误结果
def response_error_result(request):
	context = {"error" : "Bad Request"}
	url = "error.html"
	return render(request, url, context)

# 反馈错误结果
def response_list_result(request, data):
	context = {"items" : data}
	url = "list.html"
	return render(request, url, context)