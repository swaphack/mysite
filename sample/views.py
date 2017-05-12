from django.http import HttpResponseRedirect

from mysite.config import HTTP_URL

# Create your views here.
def index(request):
	return HttpResponseRedirect("/sample/index.html")
	