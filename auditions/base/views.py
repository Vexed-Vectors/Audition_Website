from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'base/index.html')

def login(request):
    pass

def signup(request):
    pass

def questions(request):
    pass

# Create your views here.
