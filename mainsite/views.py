# Create your views here.
from django.shortcuts import render, redirect

#首頁
def index(request):
	return render(request, "index.html", locals())

#登入
def sign_on(request):
    return render(request, 'login.html')

#副木呈現
def content_on(request):
    return render(request, 'content.html')