'''
from django.http import HttpResponse
#create your views here
def welcome_view(request):
	print('This line added by view function names welcome_view...!!!')
	return HttpResponse('<h1>Custom Middleware Demo</h1> <hr />')

from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
	return HttpResponse('<h1> Hello This is from home page view </h1><hr />')
'''
from django.http import HttpResponse
# Create your views here.
def home_page_view2(request):
	print(10/0)
	return HttpResponse('<h1>Hello This is from home page view</h1><hr />')

def process_exception(self, request, exception):
	print("Server is printing exception")
	return HttpResponse('<h1> Currently we are facing some technical problems..(Exception) plz try after some time !!!</h1><hr /><h2>Raised Exception:{}</h2><h3>Exception Message : {}</h3>'.format(
			exception.__class__.__name__, exception));


def home_page_view3(request):
	print('This line printed by home_page_view3 function...')
	return HttpResponse('<h1>Hello this is from home page view3 </h1><hr />')