from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to John Hassler's Web Development Portfolio!")
