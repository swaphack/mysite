# -*- coding: utf-8 -*-

#是否显示print输出
SHOW_PRINT = True

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


