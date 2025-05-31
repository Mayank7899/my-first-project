from django.shortcuts import render

# Create your views here.

def start(req):
    return render(req, "home/start.html")
