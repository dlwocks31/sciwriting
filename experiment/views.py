from random import randint

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'experiment/index.html')

def main(request):
    mode = randint(1, 2)
    return render(request, 'experiment/main%d.html' % mode)

def end(request):
    return render(request, 'experiment/end.html')
