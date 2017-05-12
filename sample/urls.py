import sample.views
import os

from django.views.static import serve
from django.conf.urls import url

from mysite.settings import DEBUG, STATIC_ROOT, BASE_DIR

if DEBUG == False:
	SAMPLE_STATIC_ROOT = os.path.join(STATIC_ROOT, 'sample')
else:
	SAMPLE_STATIC_ROOT = os.path.join(BASE_DIR, 'sample/static_assets')

print('SAMPLE_STATIC_ROOT %s' % SAMPLE_STATIC_ROOT)

def sample_urlpatterns():
	patterns = [
		url(r'^sample/$', sample.views.index),
    	url(r'^sample/(?P<path>.*)$', serve, {'document_root' : SAMPLE_STATIC_ROOT}, name='sample'),
	]

	return patterns