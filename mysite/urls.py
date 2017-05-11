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
from django.conf.urls import url, include
from django.contrib import admin

from django.views.static import serve
from mysite.settings import STATIC_ROOT

import shop.views
import webchat.views
import mysite.view

urlpatterns = [
    #url(r'^static/', serve, {'document_root': STATIC_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', shop.views.index),
    url(r'^webchat/', webchat.views.index),
    url(r'^$',  mysite.view.index),
]

urlpatterns += staticfiles_urlpatterns()

