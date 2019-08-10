from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def greeter(request):
    return HttpResponse("hello shaikh")

