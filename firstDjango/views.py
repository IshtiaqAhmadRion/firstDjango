from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    return_data = "<h1>First Django project</h1>"
    return HttpResponse(return_data)

def FirstPage(request):
    return render(request,'index.html')