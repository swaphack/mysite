# -*- coding: utf-8 -*-
# 全局变量

#中心服务器
global g_CenterServer
g_CenterServer = None

from utility.center import CenterServer

# 初始化服务器
def init_server(request):
	global g_CenterServer
	if g_CenterServer == None:
		g_CenterServer = CenterServer()
		g_CenterServer.getAccessToken(request)

# 获取中心服务器
def get_center_server(request):
	global g_CenterServer
	
	init_server(request)
	
	return g_CenterServer

# 获取凭证
def get_access_token():
	global g_CenterServer
	return g_CenterServer.access_token
