# -*- coding: utf-8 -*-

from django.shortcuts import render

# 反馈错误结果
def response_error_result(request):
	context = {"error" : "Bad Request"}
	url = "error.html"
	return render(request, url, context, None, 400)
	
# 反馈信息
def response_msg_result(request, data):
	context = {"msg" : data}
	url = "msg.html"
	return render(request, url, context)

# 反馈错误结果
def response_list_result(request, data):
	context = {"items" : data}
	url = "list.html"
	return render(request, url, context)