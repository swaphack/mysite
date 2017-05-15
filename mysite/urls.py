"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url
from django.views.static import serve
from django.contrib import admin


import mysite.view
from mysite.settings import STATIC_ROOT

from sample.urls import sample_urlpatterns
from shop.urls import shop_urlpatterns
from webchat.urls import webchat_urlpatterns

urlpatterns = [
	url(r'^static/(?P<path>.*)$', serve, {'document_root' : STATIC_ROOT}),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$',  mysite.view.index, name='index'),
]

urlpatterns += webchat_urlpatterns()
urlpatterns += sample_urlpatterns()
urlpatterns += shop_urlpatterns()

urlpatterns += staticfiles_urlpatterns()

