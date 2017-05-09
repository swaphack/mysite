# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

import webchat.views

def index(request):
	return webchat.views.index(request)
