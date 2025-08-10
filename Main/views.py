from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'Main/index.html')

def services(req):
    return render(req, 'Main/service.html')

