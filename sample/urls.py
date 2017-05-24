# -*- coding: utf-8 -*-

import sample.views
import os

from django.views.static import serve
from django.conf.urls import url

from mysite.settings import STATIC_ROOT, BASE_DIR

# 例子app资源路径
SAMPLE_STATIC_ROOT = os.path.join(BASE_DIR, 'sample/static_assets')

def sample_urlpatterns():
	patterns = [
		url(r'^sample/?$', sample.views.index),
		url(r'^sample/(?P<path>.*)$', serve, {'document_root' : SAMPLE_STATIC_ROOT}),
	]

	return patterns