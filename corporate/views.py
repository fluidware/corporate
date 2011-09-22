from django import http
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('chide/base.html')

def frontpage(request):
	return render_to_response('chide/index.html')

def about(request):
	return render_to_response('chide/about.html')

def contact(request):
	return render_to_response('chide/contact.html')