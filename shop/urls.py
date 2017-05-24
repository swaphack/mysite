# -*- coding: utf-8 -*-

import shop.views
import os

from django.views.static import serve
from django.conf.urls import url

from mysite.settings import STATIC_ROOT, BASE_DIR

# 例子app资源路径
SHOP_STATIC_ROOT = os.path.join(BASE_DIR, 'shop/static_assets')

def shop_urlpatterns():
	patterns = [
		url(r'^shop/?$', shop.views.index, name='shop'),
		url(r'^shop/static/(?P<path>.*)$', serve, {'document_root' : STATIC_ROOT}),
		url(r'^shop/(?P<path>.*)$', serve, {'document_root' : SHOP_STATIC_ROOT}),
	]

	return patterns