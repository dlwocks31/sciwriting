from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('파기글주거')
# Create your views here.
