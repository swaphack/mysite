# -*- coding: utf-8 -*-

from utility.globals import init_server
from shop.manage.HTTPActor import get_http_actor

# 处理
def index(request):
	init_server(request)
	return get_http_actor().hand(request)




	




