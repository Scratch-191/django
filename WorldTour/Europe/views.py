from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Main Europe Trips page,<br> This page is a standalone one</br>")

    