import shop.views

from django.views.static import serve
from django.conf.urls import url

def shop_urlpatterns():
	patterns = [
		url(r'^shop/', shop.views.index, name='shop'),
	]

	return patterns