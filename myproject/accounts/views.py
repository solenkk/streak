from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home page')

def product(request):
    return HttpResponse('Product page')

def coustomer(request):
    return HttpResponse('this coustumer service')
# Create your views here.
