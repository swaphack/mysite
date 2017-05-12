import webchat.views

from django.views.static import serve
from django.conf.urls import url

def webchat_urlpatterns():
	patterns = [
		url(r'^webchat/', webchat.views.index, name='webchat'),
	]

	return patterns